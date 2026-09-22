# AI · LM05 — Natural Resources

## At a glance

| | |
| --- | --- |
| **Topic** | Alternative Investments (7-10% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM1–LM2, Derivatives LM4 (cost of carry, contango and backwardation). |
| **Where it shows up** | 2 questions. The commodity futures return decomposition is the reliable calculation. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain features of raw land, timberland, and farmland and their investment characteristics
- describe features of commodities and their investment characteristics
- analyze sources of risk, return, and diversification among natural resource investments

---

## Core concepts

### Land-based natural resources

| | **Raw land** | **Timberland** | **Farmland** |
| --- | --- | --- | --- |
| **Income** | **None** — pure appreciation play | **Timber sales**, plus the biological growth of the trees | **Crop or lease income**, annually |
| **Key feature** | Value from development potential and location | **Flexibility of harvest timing** — you can wait | Annual production cycle, weather-dependent |
| **Inflation hedge** | Moderate | **Good** | **Good** |
| **Holding costs** | Taxes, maintenance; no offsetting income | Management, fire and disease risk | Management, inputs, weather |
| **Main risks** | Zoning and planning changes, illiquidity, no income | Fire, disease, pests, timber price cycles | Weather, crop prices, water access, input costs |

> **Timberland's distinctive feature is the harvest option.** Trees continue to **grow** if not
> harvested, increasing both volume and value per unit. If timber prices are low, the owner can
> simply **wait** — and the asset appreciates biologically while they do. This makes timberland
> returns notably less dependent on the price cycle than most commodity exposures, and it is the
> main reason institutional investors hold it.
>
> **The three return components of timberland:** biological growth, timber price change, and land
> value change.

**Farmland** has two sub-types: **row crops** (annual — corn, wheat, soybeans), where income is
volatile and weather-dependent, and **permanent crops** (orchards, vineyards), which require years
of investment before producing but then generate income for decades.

Farmland ownership can be **owner-operated** (full exposure to crop and price risk) or **leased** to
a farmer (stable rental income, lower risk and lower return).

### Commodities

**Physical goods:** energy (crude, natural gas, refined products), base metals (copper, aluminium),
precious metals (gold, silver), and agriculture (grains, softs, livestock).

**Investors almost never hold the physical commodity.** Storage, insurance, transport, and spoilage
make it impractical. Exposure is taken through:

| Route | Detail |
| --- | --- |
| **Futures contracts** | The dominant route. Rolled forward as they approach expiry |
| **Exchange-traded products** | Futures-based ETFs and ETNs |
| **Commodity equities** | Shares in producers — but these carry **equity** risk and company-specific risk, not pure commodity exposure |
| **Managed futures funds** | Actively traded futures strategies |
| **Physical** | Practical only for precious metals |

### The commodity futures return decomposition

**This is the most examinable content in the module.**

```
Total return = Spot return + Roll return + Collateral return
```

| Component | Source |
| --- | --- |
| **Spot (price) return** | The change in the commodity's spot price |
| **Roll return (roll yield)** | The gain or loss from **rolling** an expiring futures contract into the next one |
| **Collateral return** | Interest earned on the cash backing the futures position — futures require only margin, so the remainder earns the risk-free rate |

**The roll return depends entirely on the shape of the futures curve** (Derivatives LM4):

| Curve shape | Condition | Roll return |
| --- | --- | --- |
| **Contango** | Futures price **above** spot; the curve slopes **up** | **NEGATIVE** — you sell the cheap expiring contract and buy a more expensive one |
| **Backwardation** | Futures price **below** spot; the curve slopes **down** | **POSITIVE** — you sell the expiring contract and buy a cheaper one |

> **The roll return can dominate the total return, and it is the single most misunderstood feature
> of commodity investing.** An investor can be **right about the direction of the spot price and
> still lose money**, if the curve is in steep contango and the roll cost exceeds the price gain.
>
> Persistent contango in some markets — natural gas is the classic example, where storage is
> expensive and seasonal — has produced long-run negative returns for passive futures investors even
> when spot prices were flat or rising.

**Contango and backwardation, restated:** contango arises when **storage costs dominate** —
carrying the commodity is expensive, so the future costs more than the spot. Backwardation arises
when the **convenience yield is high** — physical possession is valuable, typically because of
scarcity.

### Investment characteristics of commodities

| Characteristic | Detail |
| --- | --- |
| **No income** | Commodities generate **no cash flow** — no dividends, no coupons, no rent. The entire return is price change plus roll plus collateral |
| **Inflation hedge** | Generally **good**, particularly energy, since commodity prices are an **input** to inflation rather than a lagging response to it |
| **Low correlation** with equities and bonds over long horizons — but correlations **rise in inflationary shocks and in crises** |
| **High volatility** | Substantially more volatile than equities |
| **Storage and carry costs** | Real, and they show up as negative roll return |
| **Supply and demand driven** | Weather, geopolitics, production decisions, inventories |
| **Valuation is difficult** | With no cash flows, discounted cash flow valuation is impossible. Analysis is fundamentally about **supply and demand balance** |

> **The absence of cash flow is the fundamental analytical fact about commodities.** An equity can be
> valued by discounting its cash flows; a bond by discounting its coupons. A commodity has neither.
> Its price is determined purely by the balance of physical supply and demand, plus the financial
> demand of investors holding it as an asset. This is why commodity "valuation" is really supply and
> demand forecasting, and why there is no equivalent of a P/E ratio.

### Risk, return, and diversification across natural resources

**Common sources of return:**

- **Price appreciation** of the underlying resource
- **Income**, where it exists (timber harvest, farmland crops or lease)
- **Biological growth** — unique to timberland and farmland
- **Roll return**, for futures-based commodity exposure
- **Collateral return**, for futures positions

**Common risks:**

| Risk | Detail |
| --- | --- |
| **Price volatility** | Commodity cycles are severe |
| **Weather and natural disaster** | Drought, flood, fire, disease |
| **Geopolitical** | Production is often concentrated in politically unstable regions |
| **Regulatory and environmental** | Emissions rules, water rights, land use restrictions |
| **Storage and transport** | Physical constraints and costs |
| **Illiquidity** | Land-based assets especially |
| **Obsolescence / transition risk** | Energy transition materially affects fossil fuel assets |

**Diversification benefits:**

- **Low long-run correlation** with equities and bonds
- **Inflation protection** — among the best available, because commodity prices are an input to
  inflation
- **Different return drivers** — weather, geology, and supply decisions rather than corporate
  earnings
- Timberland in particular has a **biological growth** component that is genuinely uncorrelated with
  financial markets

> **The honest caveat, again:** land-based natural resources are **appraisal-valued**, so their
> reported volatility and correlation are **understated** (LM2). And commodity correlations with
> equities **rise in crises** and in inflationary shocks — which is when diversification is most
> needed. The inflation hedge is real and valuable; the crisis diversification is less reliable than
> the historical correlation suggests.

---

## Formulas to know cold

```
COMMODITY FUTURES TOTAL RETURN — the key decomposition
  Total return = SPOT return + ROLL return + COLLATERAL return

  SPOT       = change in the commodity's spot price
  ROLL       = gain/loss from rolling the expiring contract into the next
  COLLATERAL = interest on the cash backing the futures position (only margin is required)

ROLL RETURN AND CURVE SHAPE
  CONTANGO        (futures ABOVE spot, curve slopes UP)   → roll return NEGATIVE
                   caused by storage costs dominating
  BACKWARDATION   (futures BELOW spot, curve slopes DOWN) → roll return POSITIVE
                   caused by a high CONVENIENCE YIELD (physical scarcity)

  The roll return CAN DOMINATE. An investor can be right on the spot price and STILL LOSE.

TIMBERLAND — three return components
  Biological GROWTH + timber PRICE change + LAND value change
  Distinctive feature: the HARVEST OPTION — trees keep growing if you wait

FARMLAND
  Row crops (annual, volatile) vs permanent crops (orchards/vineyards, long payback)
  Owner-operated (full risk) vs leased (stable rent, lower return)

COMMODITIES: NO CASH FLOW → no DCF valuation possible → analysis is SUPPLY AND DEMAND
```

---

## Exam traps

> **Trap 1 — Roll return direction.** **Contango → NEGATIVE roll return.** **Backwardation →
> POSITIVE roll return.** Reversing this is the most common error in the module.

> **Trap 2 — Ignoring roll return entirely.** It can **dominate** the total return. Being right
> about the spot price does not guarantee a profit.

> **Trap 3 — Forgetting the collateral return.** Futures require only margin, so the remaining cash
> earns the risk-free rate. It is a genuine component of total return.

> **Trap 4 — Treating commodity equities as commodity exposure.** Producer shares carry **equity
> risk, company-specific risk, and hedging policy** effects. They are correlated with commodities
> but are not a clean proxy.

> **Trap 5 — Assuming commodities generate income.** They generate **none**. The entire return is
> price, roll, and collateral.

> **Trap 6 — Missing timberland's harvest option.** If prices are low, the owner can **wait** while
> the trees keep growing. This is what distinguishes timberland from a commodity price bet.

> **Trap 7 — Trusting reported correlations for land-based assets.** They are appraisal-valued and
> therefore **smoothed** (LM2).

> **Trap 8 — Assuming the diversification holds in a crisis.** Commodity correlations with equities
> **rise** in crises and inflationary shocks — exactly when the diversification is wanted.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A commodity futures position earns a spot return of +8%, a roll return of −6%, and a collateral return of +4%. What is the total return, and what does this illustrate?

<details><summary>Answer</summary>

**Total return = 8% − 6% + 4% = +6%**

**What it illustrates:** the investor was **right about the direction of the spot price** — it rose 8% — and yet the roll return consumed three-quarters of that gain. Without the 4% collateral return, the position would have returned only 2% on an 8% spot move.

**The roll cost arises from contango.** Each time the expiring contract is rolled, the investor sells the cheap near contract and buys a more expensive further-dated one. With a curve in steady contango, that happens every month, and the losses compound.

**The practical significance:** passive long commodity futures exposure in a persistently contangoed market — natural gas is the classic case, where storage is expensive and seasonal — has produced **long-run negative returns even when spot prices were flat or rising**. Investors who bought a commodity ETF expecting spot exposure have repeatedly been surprised by this.

**What to do about it:** examine the **shape of the futures curve** before taking commodity exposure, not just the spot price view. Some strategies deliberately roll into longer-dated contracts where the curve is flatter, or hold only commodities in backwardation.

</details>

**2.** Explain the harvest option in timberland and why it changes the investment's risk profile.

<details><summary>Answer</summary>

**The option:** timber does not have to be harvested on a schedule. If timber prices are unattractive, the owner can simply **wait** — and while they wait, the trees **keep growing**.

**Why that matters:** growth adds value in two ways. The trees add **volume** (more cubic metres of wood per hectare), and they also **move into higher-value product classes** — a tree that is pulpwood today becomes sawtimber in a decade, commanding a substantially higher price per unit. So deferring the harvest is not merely delaying income; it is **accumulating value**.

**The effect on risk:** most commodity exposures force the holder to realise at whatever price prevails. A timberland owner has a genuine **option to defer**, and like any option, it has value that **rises with price volatility**.

**The three return components** become:
1. **Biological growth** — largely independent of financial markets, and the most genuinely uncorrelated return source in the entire alternatives universe
2. **Timber price change** — cyclical, but its impact is buffered by the harvest option
3. **Land value change** — a separate, longer-horizon component

**The practical consequence:** timberland returns are **less dependent on the timber price cycle** than a pure commodity position would be. This is the main reason institutional investors — pension funds and endowments in particular — hold it.

**The limits:** the option is not free. Holding costs continue (management, taxes, fire protection), growth rates slow as stands mature, and the risks of **fire, disease, and pests** all increase with time. The option to wait is real, but it is not indefinite.

</details>

**3.** Why can't commodities be valued with a discounted cash flow model, and what does that imply for analysis?

<details><summary>Answer</summary>

**Because commodities generate no cash flows.** A barrel of oil pays no dividend, no coupon, and no rent. There is nothing to discount.

Every valuation model in the curriculum — DDM, FCFE, FCFF, residual income (Equity LM6) — depends on projecting future cash flows and discounting them. With no cash flows, none applies. There is no equivalent of a P/E ratio, no intrinsic value in the usual sense.

**What determines the price instead:**

**(1) Physical supply and demand.** Production capacity, inventories, consumption, and the **elasticity** of each. Short-run supply is usually highly inelastic (you cannot open a mine quickly), which is why commodity prices are so volatile.

**(2) The cost curve.** In the long run, prices tend toward the marginal cost of the highest-cost producer needed to meet demand. This provides a soft anchor that nothing else does.

**(3) Financial demand.** Investors holding commodities as an asset class add demand unrelated to physical consumption, and this can move prices independently of fundamentals.

**(4) The convenience yield and storage costs**, which set the shape of the futures curve (Derivatives LM4).

**What analysis actually consists of:**
- **Inventory levels** relative to historical norms — the single most useful indicator
- **Supply response** — what new capacity is coming, and when
- **Cost curve position** — where does the marginal producer sit?
- **Demand drivers** — industrial production, seasonality, substitution
- **The futures curve shape**, which tells you both the market's carry economics and something about physical tightness

This is fundamentally **different work** from equity or credit analysis, which is why commodity specialists are a distinct discipline.

</details>

**4.** Compare gaining commodity exposure through futures versus through shares in producers.

<details><summary>Answer</summary>

**Futures:**
- **Clean exposure** to the commodity price itself
- Return = **spot + roll + collateral** — and the roll can be materially positive or negative
- Requires only **margin**, so the remaining cash earns the risk-free rate
- Must be **rolled** at each expiry, incurring transaction costs and roll risk
- **No equity risk**, no company-specific risk, no management risk
- High volatility, no income

**Producer shares:**
- **Operational leverage** to the commodity price — a miner with costs of 80 and a price of 100 sees its margin **double** if the price rises to 120. Equity returns amplify commodity moves
- But they carry **equity market risk** — in a general sell-off they fall with everything else regardless of commodity prices
- **Company-specific risk**: operational failures, cost overruns, mine accidents, governance, balance sheet stress
- **Management hedging** can neutralise the exposure entirely — a producer that has hedged its output forward has no commodity exposure left, which is often exactly the opposite of what the investor wanted
- **Pay dividends**, unlike the commodity itself
- Exposure to **reserve life and replacement** — a miner with declining reserves is a wasting asset

**The key point:** producer shares are **correlated with** commodities but are **not a clean proxy**. Empirically their correlation with the underlying commodity is often well below 1, and in equity market stress it can approach the correlation with equities instead.

**Which to choose:** futures for **pure commodity exposure** and inflation hedging; producer equities if you want **operational leverage** and are willing to take equity and company risk alongside it. They are different investments, not two routes to the same one.

</details>

---

## Done when

- [ ] I can compare raw land, timberland, and farmland on income, risk, and key features
- [ ] I can decompose commodity futures total return into spot, roll, and collateral
- [ ] I can state the roll return's direction in contango and backwardation and explain why
- [ ] I can explain the harvest option and timberland's three return components
- [ ] I can explain why commodities cannot be valued by DCF and what analysis replaces it
- [ ] I can contrast futures and producer equities as routes to commodity exposure
- [ ] I can state the honest position on natural resource diversification and its limits
- [ ] I answered the self-check cold, several days after first study

---

← [LM04 Real Estate and Infrastructure](lm-04-real-estate-and-infrastructure.md)  ·  [Topic index](README.md)  ·  [LM06 Hedge Funds](lm-06-hedge-funds.md) →
