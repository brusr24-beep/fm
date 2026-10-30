// Candy Riot game logic, a direct port of math/engine.py.
// Both read the same config.json, so the demo plays with the tuned maths.
// Math.random is fine for a demo; on Stake Engine outcomes come from their RGS.

class Game {
  constructor(cfg) {
    this.cfg = cfg;
    this.reels = cfg.reels;
    this.minRows = cfg.min_rows;
    this.maxRows = cfg.max_rows;
    this.wildReels = new Set(cfg.wild_reels);
    this.paying = Object.keys(cfg.symbols).filter(s => ["low", "high"].includes(cfg.symbols[s].kind));
    this.multValues = Object.keys(cfg.wild_multipliers).map(Number);
    this.multWeights = Object.values(cfg.wild_multipliers);
    this.tables = {};
    for (const [mode, weights] of Object.entries(cfg.weights)) {
      this.tables[mode] = [];
      for (let r = 0; r < this.reels; r++) {
        const syms = Object.keys(weights).filter(s => s !== "wild" || this.wildReels.has(r));
        this.tables[mode].push([syms, syms.map(s => weights[s])]);
      }
    }
  }

  choice(items, weights) {
    const total = weights.reduce((a, b) => a + b, 0);
    let x = Math.random() * total;
    for (let i = 0; i < items.length; i++) {
      x -= weights[i];
      if (x < 0) return items[i];
    }
    return items[items.length - 1];
  }

  draw(mode, reel, n) {
    const [syms, weights] = this.tables[mode][reel];
    return Array.from({ length: n }, () => this.choice(syms, weights));
  }

  drawGrid(mode, heights) {
    return heights.map((h, r) => this.draw(mode, r, h));
  }

  evaluate(grid, wildMult) {
    const wins = [];
    for (const s of this.paying) {
      let ways = 1, mult = 0, length = 0;
      for (let r = 0; r < this.reels; r++) {
        let count;
        if (r in wildMult) {
          count = grid[r].length;
          mult += wildMult[r];
        } else {
          count = grid[r].filter(x => x === s).length;
        }
        if (count === 0) break;
        ways *= count;
        length++;
      }
      if (length >= 3) {
        mult = Math.max(mult, 1);
        wins.push({ symbol: s, length, ways, mult, amount: this.cfg.paytable[s][length] * ways * mult });
      }
    }
    return wins;
  }

  shoveWilds(grid, wildMult, events) {
    for (const r of this.wildReels) {
      if (!(r in wildMult) && grid[r].includes("wild")) {
        wildMult[r] = this.choice(this.multValues, this.multWeights);
        grid[r] = grid[r].map(() => "wild");
        events.push({ type: "shove", reel: r, mult: wildMult[r] });
      }
    }
  }

  tumble(mode, grid, heights, events) {
    const wildMult = {};
    let total = 0;
    while (true) {
      this.shoveWilds(grid, wildMult, events);
      const wins = this.evaluate(grid, wildMult);
      if (!wins.length) break;
      total += wins.reduce((a, w) => a + w.amount, 0);
      const burst = grid.map(() => new Set());
      for (const w of wins) {
        for (let r = 0; r < w.length; r++) {
          grid[r].forEach((x, i) => {
            if (r in wildMult || x === w.symbol) burst[r].add(i);
          });
        }
      }
      for (const r of Object.keys(wildMult)) if (burst[r].size) delete wildMult[r];
      events.push({ type: "win", wins, burst: burst.map(b => [...b].sort((a, b) => a - b)) });
      const added = grid.map(() => 0);
      for (let r = 0; r < this.reels; r++) {
        if (!burst[r].size) continue;
        const kept = grid[r].filter((_, i) => !burst[r].has(i));
        heights[r] = Math.min(heights[r] + 1, this.maxRows);
        added[r] = heights[r] - kept.length;
        grid[r] = this.draw(mode, r, added[r]).concat(kept);
      }
      events.push({ type: "refill", grid: grid.map(c => [...c]), heights: [...heights], added });
    }
    const scatters = grid.reduce((a, c) => a + c.filter(x => x === "ticket").length, 0);
    return [total, scatters];
  }

  freeSpins(spins, events) {
    const heights = Array(this.reels).fill(this.minRows);
    let total = 0, played = 0;
    while (played < spins) {
      played++;
      const grid = this.drawGrid("free", heights);
      events.push({ type: "spin", free: played, of: spins, grid: grid.map(c => [...c]), heights: [...heights] });
      const [win, scatters] = this.tumble("free", grid, heights, events);
      total += win;
      if (scatters >= 3) {
        const extra = this.cfg.free_spins_retrigger[Math.min(scatters, 6)];
        spins += extra;
        events.push({ type: "retrigger", extra });
      }
      if (total >= this.cfg.max_win) break;
    }
    return total;
  }

  // Returns { total, events }; total is a multiple of the base bet.
  play(mode = "base") {
    const events = [];
    let total = 0;
    if (mode === "base") {
      const heights = Array(this.reels).fill(this.minRows);
      const grid = this.drawGrid("base", heights);
      events.push({ type: "spin", grid: grid.map(c => [...c]), heights: [...heights] });
      let scatters;
      [total, scatters] = this.tumble("base", grid, heights, events);
      if (scatters >= 3) {
        const spins = this.cfg.free_spins_award[Math.min(scatters, 6)];
        events.push({ type: "trigger", spins });
        total += this.freeSpins(spins, events);
      }
    } else {
      const spins = this.cfg.free_spins_award["3"];
      events.push({ type: "trigger", spins });
      total = this.freeSpins(spins, events);
    }
    return { total: Math.min(total, this.cfg.max_win), events };
  }
}

if (typeof module !== "undefined") module.exports = { Game };
