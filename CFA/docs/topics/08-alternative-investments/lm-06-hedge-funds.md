# AI · LM06 — Hedge Funds

## At a glance

| | |
| --- | --- |
| **Topic** | Alternative Investments (7-10% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM1–LM2, Derivatives LM2 (options and short positions). |
| **Where it shows up** | 2 questions. The strategy categories and the fee/leverage characteristics are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain investment features of hedge funds and contrast them with other asset classes
- describe investment forms and vehicles used in hedge fund investments
- analyze sources of risk, return, and diversification among hedge fund investments

---

## Core concepts

### What defines a hedge fund

> **A hedge fund is a structure, not an asset class.** What distinguishes it is the **vehicle** —
> a private partnership with performance fees, the freedom to use leverage and short selling, and
> restricted investor access — not what it holds.

| Feature | Detail |
| --- | --- |
| **Private partnership** | Limited to **qualified/accredited** investors, so lightly regulated |
| **Absolute return objective** | Targets positive returns in all market conditions, not a benchmark-relative return |
| **Ability to short** | The defining operational freedom — unavailable to most traditional long-only funds |
| **Leverage** | Used extensively, through borrowing, derivatives, and margin |
| **Derivatives** | Central to most strategies |
| **Performance fees** | Typically **2 and 20**, with high water marks (LM1) |
| **Lock-ups and gates** | Restricted redemption: initial lock-up periods, notice requirements, and **gates** limiting the proportion redeemable in a period |
| **Limited transparency** | Positions are usually not disclosed, to protect the strategy |
| **Concentrated** | Often far less diversified than traditional funds |

> **"Hedge" is a historical misnomer.** The original hedge funds were long/short equity and genuinely
> hedged market exposure. Most modern hedge funds do not hedge in any meaningful sense — they take
> directional, levered, concentrated positions. The name describes the 1949 origin, not the 2020s
> reality.

### The strategy categories

| Category | Strategies | What drives returns |
| --- | --- | --- |
| **Equity hedge** | Long/short equity, market neutral, short bias, sector specialists | Stock selection, with varying net market exposure |
| **Event driven** | **Merger arbitrage**, distressed, activist, special situations | Corporate events completing as expected |
| **Relative value** | Convertible arbitrage, fixed income arbitrage, volatility arbitrage | Pricing discrepancies between related securities converging |
| **Macro and CTA** | Global macro, managed futures, trend following | Directional views on rates, currencies, commodities, and indices |
| **Multi-strategy** | Allocating across several of the above | Diversification across strategies, with capital reallocated dynamically |

**Strategies worth understanding in more detail:**

**Long/short equity** — long undervalued stocks, short overvalued ones. **Net exposure** = long −
short, as a percentage of capital. **Market neutral** targets zero net exposure, aiming to profit
purely from stock selection.

**Merger arbitrage** — buy the target of an announced acquisition, short the acquirer (in a
stock deal). Profit is the spread between the current price and the deal price, earned when the deal
**closes**. The risk is **deal break** — regulatory rejection, financing failure, or a shareholder
vote. The payoff is **small, steady gains punctuated by large losses**: economically, it is **short
an option** on the deal failing.

**Convertible arbitrage** — buy the convertible bond, short the underlying equity. Profits from the
convertible's cheapness and from delta-hedging the embedded option. Requires **leverage** because
individual spreads are small, and it is highly exposed to **liquidity** conditions.

**Global macro** — directional positions on interest rates, currencies, commodities, and equity
indices based on macroeconomic views. Typically high volatility and low correlation to equities.

**Managed futures / CTAs** — systematic, usually **trend-following**, across futures markets. These
have historically provided **crisis alpha**: trend followers tend to perform well in sustained
drawdowns, because prolonged declines are trends. This is one of the few genuine crisis
diversifiers.

### Investment vehicles

| Vehicle | Detail |
| --- | --- |
| **Direct fund investment** | Invest in a single hedge fund as an LP |
| **Fund of hedge funds** | Diversifies across managers; provides due diligence and access to closed funds — at a **second layer of fees**, which has become hard to justify |
| **Managed account** | The investor owns the assets directly, with the manager trading them. **Better transparency, control, and liquidity**, and it removes co-mingling risk — but requires scale |
| **Liquid alternatives** | Regulated funds (UCITS, '40 Act) running hedge-fund-like strategies with **daily liquidity** and leverage limits. More accessible, but constrained — and the constraints can materially change the strategy's return profile |

**Master-feeder structure:** a common arrangement where onshore and offshore **feeder** funds both
invest into a single **master** fund, allowing investors in different tax jurisdictions to access
the same strategy efficiently.

### Sources of risk, return, and diversification

**Return sources:**

| Source | Detail |
| --- | --- |
| **Manager skill (alpha)** | The claimed source — though much apparent alpha is factor exposure (Equity LM12) |
| **Factor exposures (beta)** | Equity, credit, momentum, carry, volatility — often the real driver |
| **Illiquidity premium** | Many strategies hold less liquid instruments |
| **Leverage** | Amplifies whatever return the underlying strategy generates |
| **Short rebate** | Interest earned on the proceeds of short sales |

**Risk sources:**

| Risk | Detail |
| --- | --- |
| **Leverage** | The dominant risk. Margin calls force liquidation at the worst moment |
| **Liquidity mismatch** | Holding illiquid assets while offering periodic redemption. **Gates** exist precisely because this mismatch is real |
| **Concentration** | Positions can be very large relative to the fund |
| **Counterparty and prime broker risk** | Exposed to the broker's solvency and to changes in financing terms |
| **Model risk** | Especially in relative value and quantitative strategies |
| **Tail risk** | Many strategies have **option-like payoffs** — steady gains, occasional large losses |
| **Manager and operational risk** | Key person departure, fraud, valuation of illiquid positions |
| **Transparency** | The investor often cannot see what they own |

> **The tail risk point is the important one.** Merger arbitrage, convertible arbitrage, carry
> trades, credit strategies, and volatility selling all produce **negatively skewed** return
> distributions (QM LM5): a high Sharpe ratio built on steady small gains, punctuated by an
> occasional loss that erases years of them.
>
> **Standard deviation cannot see this.** A strategy that is short an option looks excellent on a
> Sharpe ratio right up until the option is exercised against it. This is why **downside measures**
> — Sortino, maximum drawdown, conditional VaR — are essential for hedge funds (LM2).

**Diversification:**

- **Low reported correlation** with equities and bonds — subject to the biases and smoothing of LM2
- **Genuine diversification** from strategies with **structurally different** return drivers: macro,
  managed futures, and market-neutral strategies
- **But correlations rise in crises** — leveraged strategies deleverage simultaneously, and
  liquidity evaporates across the board. 2008 demonstrated this comprehensively
- **Managed futures / trend following** is the notable exception, with genuine **crisis alpha** —
  it tends to perform well in sustained drawdowns because those are trends

> **The honest summary:** hedge funds as a group have **not** delivered the returns their fees
> implied, and much of what looked like alpha has been shown by factor analysis to be replicable
> beta (Equity LM12). The **dispersion between managers is enormous**, so the asset class average is
> nearly meaningless — as with venture capital (LM3), the question is not whether to allocate but
> whether you can identify and access the managers who justify the fees.

---

## Formulas to know cold

```
DEFINING FEATURES — a STRUCTURE, not an asset class
  Private partnership · qualified investors only · absolute return objective
  · SHORT SELLING · LEVERAGE · derivatives · 2-and-20 fees with high water marks
  · LOCK-UPS AND GATES · limited transparency · concentrated

THE FIVE STRATEGY CATEGORIES
  EQUITY HEDGE    — long/short, market neutral, short bias, sector
  EVENT DRIVEN    — merger arbitrage, distressed, activist, special situations
  RELATIVE VALUE  — convertible arb, fixed income arb, volatility arb
  MACRO AND CTA   — global macro, managed futures, trend following
  MULTI-STRATEGY  — dynamic allocation across the above

  Net exposure = (Long − Short) / Capital.  Market neutral targets ZERO net exposure.

VEHICLES
  Direct fund · Fund of hedge funds (SECOND fee layer) · Managed account (transparency + control)
  · Liquid alternatives (daily liquidity, leverage limits, constrained strategy)
  Master-feeder: onshore and offshore feeders into one master fund

THE TAIL RISK POINT
  Merger arb, convertible arb, carry, credit, and volatility selling are all
  economically SHORT AN OPTION → NEGATIVELY SKEWED returns
  → steady small gains, occasional large losses
  → the SHARPE RATIO CANNOT SEE THIS. Use Sortino, max drawdown, CVaR.

CRISIS DIVERSIFICATION
  Most hedge fund correlations RISE in crises (simultaneous deleveraging).
  MANAGED FUTURES / TREND FOLLOWING is the notable exception — genuine "crisis alpha".
```

---

## Exam traps

> **Trap 1 — Treating hedge funds as an asset class.** They are a **structure**. The strategies
> within them have almost nothing in common.

> **Trap 2 — Assuming hedge funds hedge.** Most do not. The name is a historical artefact of the
> 1949 original, not a description of modern practice.

> **Trap 3 — Relying on the Sharpe ratio.** Many strategies are economically **short an option**,
> producing negatively skewed returns that standard deviation cannot capture.

> **Trap 4 — Assuming diversification holds in a crisis.** Leveraged strategies **deleverage
> together**, and correlations converge. 2008 demonstrated this across nearly every category.

> **Trap 5 — Missing managed futures as the exception.** **Trend following** has genuine crisis
> alpha, because sustained drawdowns are trends.

> **Trap 6 — Overlooking the liquidity mismatch.** Holding illiquid assets while offering periodic
> redemption is the structural fragility. **Gates** exist because the mismatch is real.

> **Trap 7 — Treating apparent alpha as skill.** Much of it is **replicable factor exposure**
> (Equity LM12), available far more cheaply.

> **Trap 8 — Using the asset class average.** Manager dispersion is enormous. The average is nearly
> meaningless; access to the top managers is the binding constraint.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Why does merger arbitrage produce a negatively skewed return distribution, and what does that mean for its Sharpe ratio?

<details><summary>Answer</summary>

**The strategy:** after an acquisition is announced, buy the target (trading below the offer price) and, in a stock deal, short the acquirer. The spread between the current price and the deal price is earned **when the deal closes**.

**The payoff shape:**
- **If the deal closes** (the large majority of cases): a **small, predictable** gain — typically a few percent annualised
- **If the deal breaks**: the target's price collapses back toward its pre-announcement level, producing a **large, sudden loss** — often 20-30% on that position

So the distribution is many small gains and occasional large losses: **negatively skewed** (QM LM5).

**Economically, the arbitrageur is SHORT AN OPTION** on the deal failing. They collect a premium (the spread) and bear a large contingent liability. The structure is identical to selling insurance.

**What it means for the Sharpe ratio:** in a period with no deal breaks, the return series is **remarkably smooth** — steady small gains, very low standard deviation — producing an **outstanding Sharpe ratio**. That ratio is **measuring the absence of the risk, not its absence**.

When a deal breaks, or when several break together in a regulatory crackdown or a financing freeze, the loss arrives all at once. The historical Sharpe ratio gave no warning, because standard deviation treats upside and downside dispersion identically and cannot distinguish a smooth series from a safe one.

**The remedy:** use **downside measures** — Sortino ratio, **maximum drawdown**, conditional VaR — and examine **skewness and kurtosis** explicitly (LM2).

</details>

**2.** Why do hedge fund correlations with equities tend to rise during crises?

<details><summary>Answer</summary>

**Four mechanisms, reinforcing each other:**

**(1) Simultaneous deleveraging.** Most hedge fund strategies use leverage. When markets fall, **margin calls and prime broker haircut increases** force funds to reduce positions. Everyone deleverages at once, selling whatever is liquid — which transmits selling pressure across unrelated assets and makes them move together.

**(2) Liquidity evaporation.** Bid-ask spreads widen, market depth disappears, and funds cannot exit the positions they want to exit. They sell what they **can** sell, not what they should — again correlating unrelated positions.

**(3) Investor redemptions.** Crises trigger redemption requests. Funds must liquidate to meet them, in the same direction and at the same time as everyone else. This is why **gates** exist — and a gate imposed by one fund pushes redemptions onto others.

**(4) Common factor exposure revealed.** Much of what appears to be diverse, idiosyncratic strategy alpha is in fact shared exposure to **liquidity, credit, and volatility** factors. In normal conditions those factors are quiet and the strategies look independent. In a crisis the common factor dominates, and the apparent independence disappears.

**The statistical framing** (QM LM6): **conditional correlations rise toward 1 in stress**. The unconditional correlation computed over a full sample systematically understates the correlation in the states that matter.

**The exception: managed futures / trend following.** Sustained drawdowns are **trends**, and trend followers position short into them. This has produced genuine **crisis alpha** in 2008 and other extended declines — though not in sharp, sudden reversals where trends have no time to establish.

</details>

**3.** Contrast a fund of hedge funds with a managed account.

<details><summary>Answer</summary>

**Fund of hedge funds:**
- **Diversification across managers** — typically 15-30 underlying funds
- **Professional due diligence** and manager selection, which is genuinely valuable given the dispersion
- **Access** to funds that are closed to new direct investors
- **Lower minimum investment** than investing in each fund directly
- **A SECOND LAYER OF FEES** — commonly 1% and 10% on top of the underlying 2 and 20. Combined with the underlying fees, the investor may keep only around **65% of the gross return** (LM2)
- **No transparency** into underlying positions — you are two layers removed
- **Compounded liquidity restrictions** — the FoF's redemption terms sit on top of the underlying funds'
- **Assets are co-mingled** with other investors'

**Managed account:**
- **The investor owns the assets directly**; the manager has trading authority but not custody
- **Full transparency** — every position is visible in real time
- **Control**: the investor can impose risk limits, leverage caps, and instrument restrictions, and can terminate the manager and retain the assets
- **Better liquidity** — no gates or lock-ups imposed by the manager
- **No co-mingling risk** — the assets cannot be caught in another investor's redemption or in the manager's own difficulties
- **Requires substantial scale** — managers accept separate accounts only above a meaningful minimum
- **Operational burden** on the investor: custody, reporting, valuation, and oversight
- **Single-manager concentration** — no diversification unless several accounts are run

**The trade-off:** a fund of funds buys **diversification and manager selection** at a heavy fee cost with no transparency. A managed account buys **transparency, control, and liquidity** but requires scale and internal capability.

The trend has been strongly toward managed accounts and direct investment for large institutions, and fund-of-funds assets have contracted as fee pressure has grown.

</details>

**4.** A hedge fund reports a Sharpe ratio of 2.1 over five years with a maximum drawdown of 3%. What should you investigate?

<details><summary>Answer</summary>

**A Sharpe ratio of 2.1 with a 3% maximum drawdown is extraordinary** — better than almost any documented long-run record. The base rate strongly favours an explanation other than exceptional skill.

**What to investigate:**

**(1) Is the strategy short an option?** Merger arbitrage, volatility selling, carry trades, and credit strategies all produce exactly this signature: steady small gains, very low volatility, **until the event arrives**. A 2.1 Sharpe with no drawdown may simply mean the tail has not yet occurred. Examine **skewness and kurtosis** directly.

**(2) How are illiquid positions valued?** If the fund holds hard-to-price assets marked by the manager, the return series is **smoothed** (LM2) — understating volatility and manufacturing a high Sharpe ratio. Check who prices the book: an independent administrator, or the manager?

**(3) Does the period contain a genuine stress event?** Five years may span only benign conditions. A strategy untested by a crisis has an unknown risk profile, not a low one.

**(4) Is there leverage?** High leverage on a low-volatility strategy produces a high Sharpe ratio until a small adverse move is amplified into a large one. LTCM reported a superb Sharpe ratio immediately before failing.

**(5) Serial correlation in the returns.** Positive autocorrelation in monthly returns is a **statistical fingerprint of smoothing or stale pricing**. It is directly testable and is one of the standard due diligence checks.

**(6) Operational and fraud risk.** Implausibly smooth returns have historically been a **fraud indicator**. Verify the administrator, the auditor, and the custodian independently.

**The general principle: a Sharpe ratio that looks too good usually means the risk measure is not capturing the risk**, not that the risk is absent.

</details>

---

## Done when

- [ ] I can explain why hedge funds are a structure rather than an asset class
- [ ] I can name the five strategy categories with examples of each
- [ ] I can explain net exposure and what market neutral means
- [ ] I can explain why merger and convertible arbitrage are economically short an option
- [ ] I can compare direct funds, funds of funds, managed accounts, and liquid alternatives
- [ ] I can explain why correlations rise in crises and why managed futures is the exception
- [ ] I can list what to investigate behind an implausibly high Sharpe ratio
- [ ] I answered the self-check cold, several days after first study

---

← [LM05 Natural Resources](lm-05-natural-resources.md)  ·  [Topic index](README.md)  ·  [LM07 Introduction to Digital Assets](lm-07-introduction-to-digital-assets.md) →
