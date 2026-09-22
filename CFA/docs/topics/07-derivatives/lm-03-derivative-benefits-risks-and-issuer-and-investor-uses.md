# DER · LM03 — Derivative Benefits, Risks, and Issuer and Investor Uses

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | LM1–LM2. |
| **Where it shows up** | 1 question. Descriptive. Short module. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe benefits and risks of derivative instruments
- compare the use of derivatives among issuers and investors

---

## Core concepts

### Benefits

| Benefit | How it works |
| --- | --- |
| **Risk transfer (hedging)** | An unwanted exposure is transferred to someone willing to bear it. The primary economic purpose |
| **Price discovery** | Derivative prices reveal the market's expectations about future prices, rates, and volatility. Futures curves and implied volatility are widely used as forecasting inputs |
| **Operational advantages** | **Lower transaction costs**, greater liquidity, and the ability to take **short positions easily** — shorting a bond directly is difficult and expensive; buying CDS protection or selling a future is not |
| **Market efficiency** | Arbitrage across derivatives and cash markets keeps prices aligned and speeds the incorporation of information |
| **Capital efficiency** | Exposure with **little or no initial outlay**, freeing capital for other uses |
| **Customisation** | An OTC contract can match an exposure exactly in size, maturity, and underlying |

### Risks

| Risk | Detail |
| --- | --- |
| **Leverage** | Small outlay, large exposure. **Amplifies losses as much as gains** — and a position that would be survivable unlevered can be fatal levered |
| **Counterparty credit risk** | The other side may not perform. Central to OTC; mitigated by clearing, collateral, and netting |
| **Liquidity risk** | Some contracts are thinly traded; exiting in stress can be costly or impossible |
| **Basis risk** | The hedge instrument does not move exactly with the exposure being hedged — the residual is unhedged |
| **Model risk** | Complex derivatives are valued with models; if the model or its inputs are wrong, so is the price (QM LM9) |
| **Operational risk** | Errors in execution, settlement, documentation, and collateral management |
| **Complexity and opacity** | Positions can be difficult to understand and to aggregate, both for management and for outside analysts |
| **Systemic risk** | Interconnected exposures can transmit a single failure across the system |

> **Leverage is the risk that turns the others lethal.** Counterparty failure, basis risk, or a model
> error on an unlevered position is a bad outcome; on a 20× levered position it is insolvency. Every
> major derivatives loss in financial history — Barings, LTCM, Amaranth, and others — combined
> leverage with one of the other risks on this list.

### Use by issuers (corporations)

Corporations use derivatives almost entirely for **hedging operational and financial exposures**
arising from the business, not for taking positions.

| Exposure | Instrument | Purpose |
| --- | --- | --- |
| **Interest rate risk** on floating-rate debt | **Interest rate swap** (pay fixed, receive floating) | Convert floating-rate debt to fixed, locking in the cost |
| **Currency risk** on receivables, payables, or foreign operations | Forwards, currency swaps, options | Lock in an exchange rate |
| **Commodity input costs** | Futures, forwards, swaps | Lock in the cost of fuel, metals, or agricultural inputs |
| **Commodity output prices** | Futures, forwards | Lock in revenue (miners, farmers, energy producers) |
| **Anticipated debt issuance** | Forward-starting swaps, rate locks | Fix the rate before the issue comes to market |
| **Share-based compensation exposure** | Equity derivatives | Hedge the cost of employee options |

**Hedge accounting.** Under IFRS and US GAAP, a derivative designated as an effective hedge may have
its gains and losses recognised in the **same period as the hedged item**, rather than immediately in
profit or loss. Three categories:

| Hedge type | Hedges |
| --- | --- |
| **Fair value hedge** | Changes in the fair value of a recognised asset or liability |
| **Cash flow hedge** | Variability in future cash flows from a forecast transaction |
| **Net investment hedge** | The currency exposure of a net investment in a foreign operation |

> **Why hedge accounting matters:** without it, the derivative is marked to market through earnings
> while the hedged item is not, producing **earnings volatility from a position that reduces
> economic risk**. Companies go to considerable lengths to qualify, because reporting volatility has
> a real cost in how the company is perceived.

### Use by investors

Investors use derivatives for a wider range of purposes:

| Purpose | Example |
| --- | --- |
| **Hedging** | Buying index puts to protect an equity portfolio; using futures to hedge duration |
| **Directional exposure** | Taking a view on a price, rate, or credit without owning the underlying |
| **Efficient portfolio adjustment** | Changing asset allocation or portfolio duration with futures, far faster and cheaper than trading the underlying securities |
| **Yield enhancement** | **Covered call writing** — collecting premiums, at the cost of capping upside |
| **Arbitrage** | Exploiting pricing discrepancies between the derivative and the cash market |
| **Access** | Gaining exposure to markets or asset classes that are restricted or costly to access directly |
| **Volatility trading** | Taking positions on volatility itself rather than on direction |
| **Shorting** | Expressing a negative view where direct shorting is difficult (credit, in particular) |

> **The most common institutional use is not speculation but portfolio adjustment.** A pension fund
> that wants to reduce equity exposure by 5% can sell index futures in minutes at a few basis points
> of cost, versus selling hundreds of individual holdings over days with substantial market impact.
> The derivative is an **overlay** that leaves the underlying portfolio intact.

### Hedging versus speculation — the judgement

The instruments are identical; the **purpose** differs:

| | **Hedging** | **Speculation** |
| --- | --- | --- |
| Starting point | An **existing exposure** | No existing exposure |
| Effect | **Reduces** total risk | **Creates** risk |
| Success measured by | Reduced variability of the combined position | Profit on the derivative itself |

> **The distinction is genuinely blurry in practice**, and that is an important professional point
> rather than a technicality. A company that hedges 100% of its fuel cost is hedging. A company that
> hedges 300% because it expects prices to rise is **speculating** with a hedging instrument — and
> it has replaced a commercial exposure with a financial bet. Several large corporate derivatives
> losses have arisen exactly this way, from treasury functions that drifted from hedging to
> position-taking.
>
> The governance answer (Corporate Issuers LM3) is a **derivatives policy** specifying what may be
> hedged, in what proportion, with what instruments, and with what oversight — and the board
> actually enforcing it.

---

## Formulas to know cold

```
BENEFITS
  Risk transfer (hedging) · Price discovery · Operational advantages (cost, liquidity, easy shorting)
  · Market efficiency · Capital efficiency · Customisation

RISKS
  LEVERAGE (the one that makes the others lethal) · Counterparty credit · Liquidity
  · BASIS RISK · Model risk · Operational · Complexity · Systemic

ISSUER (corporate) USE — almost entirely HEDGING operational and financial exposures
  Interest rate swaps (floating → fixed debt) · FX forwards and swaps
  · Commodity futures (inputs and outputs) · Rate locks on planned issuance

HEDGE ACCOUNTING — three categories
  FAIR VALUE hedge      — a recognised asset or liability's fair value
  CASH FLOW hedge       — variability in future cash flows from a forecast transaction
  NET INVESTMENT hedge  — currency exposure of a net investment in a foreign operation

INVESTOR USE
  Hedging · Directional exposure · Efficient portfolio adjustment (overlays)
  · Yield enhancement (covered calls) · Arbitrage · Access · Volatility trading · Shorting

HEDGING vs SPECULATION: same instruments, different PURPOSE
  Hedging REDUCES an existing exposure.  Speculation CREATES one.
  Hedging MORE than 100% of an exposure is speculation.
```

---

## Exam traps

> **Trap 1 — Assuming derivatives increase risk.** Used to **hedge**, they **reduce** it. The
> instrument is neutral; the **use** determines the effect.

> **Trap 2 — Confusing basis risk with counterparty risk.** **Basis risk** is the hedge not moving
> exactly with the exposure. **Counterparty risk** is the other side failing to perform.

> **Trap 3 — Thinking hedge accounting changes the economics.** It changes **when gains and losses
> are recognised**, not the cash flows. It exists to avoid reporting volatility from a position that
> reduces economic risk.

> **Trap 4 — Missing that over-hedging is speculation.** Hedging **more than 100%** of an exposure
> converts a commercial position into a financial bet.

> **Trap 5 — Underestimating leverage.** It is what turns a manageable loss into insolvency, and it
> features in essentially every historical derivatives disaster.

> **Trap 6 — Assuming corporates use derivatives to speculate.** They use them overwhelmingly to
> **hedge operational exposures**. Investors have the wider range of uses.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** An airline hedges 120% of its expected fuel consumption for next year. Is this hedging?

<details><summary>Answer</summary>

**No — the excess 20% is speculation.**

Hedging **reduces an existing exposure**. Hedging 100% of expected consumption neutralises the fuel price exposure entirely: whatever fuel costs, the airline's effective cost is locked.

The additional 20% has **no underlying exposure to offset**. It is a pure long position in fuel, taken because someone expects prices to rise. If prices fall, the airline loses on that 20% with nothing on the operational side to compensate — it has **created** a risk that did not exist.

**Why this matters practically:**
- The board and shareholders believe they own an airline, not a commodity trading operation
- **Hedge accounting** will not apply to the unhedged portion, so it marks to market through earnings
- Several large corporate derivatives losses arose exactly this way — a treasury function that drifted from hedging into position-taking, often after a period when the view happened to be right

**The governance answer** (Corporate Issuers LM3): a **derivatives policy** specifying what may be hedged, in what proportion, with which instruments, and with what board oversight — and actually enforced.

</details>

**2.** Why would a pension fund use index futures to reduce equity exposure rather than selling stocks?

<details><summary>Answer</summary>

**Speed, cost, and market impact.**

**Selling the underlying portfolio:** reducing equity exposure by 5% means selling hundreds of individual positions. This takes days, incurs bid-ask spreads and commissions on every trade, and generates **market impact** — the act of selling pushes prices down, worsening the execution. It may also realise **capital gains** with tax consequences, and it destroys carefully constructed positions that will have to be rebuilt.

**Selling index futures:** a single trade in a highly liquid contract, executable in minutes at a few basis points of cost. The underlying portfolio is **untouched** — no positions sold, no gains realised, no relationships with managers disturbed.

**The concept is an overlay:** the futures position sits on top of the portfolio, adjusting the net exposure without disturbing the holdings. Reversing it is equally quick.

**The trade-offs:**
- **Basis risk** — index futures hedge market exposure, not the portfolio's specific holdings. If the portfolio has a beta of 1.2 or a sector tilt, the hedge is imperfect
- **Margin** must be posted and **variation margin** funded daily, which requires a cash buffer
- The position must be **rolled** at each expiry, incurring cost and roll risk

This is the most common institutional derivatives use, and it is neither speculation nor pure hedging — it is **efficient implementation of an allocation decision**.

</details>

**3.** Explain the three categories of hedge accounting and why companies bother qualifying for them.

<details><summary>Answer</summary>

**Fair value hedge** — hedges changes in the **fair value** of a recognised asset or liability (for example, using a swap to hedge the fair value of fixed-rate debt against rate changes). Both the derivative **and the hedged item** are marked to market through profit or loss, so the two offset.

**Cash flow hedge** — hedges variability in **future cash flows** from a forecast transaction (for example, hedging the cost of an anticipated fuel purchase). The effective portion of the derivative's gain or loss goes to **other comprehensive income** and is recycled to profit or loss when the hedged transaction occurs.

**Net investment hedge** — hedges the **currency exposure** of a net investment in a foreign operation. Treated similarly to a cash flow hedge, with gains and losses in OCI.

**Why companies bother:** without hedge accounting, the **derivative is marked to market through earnings immediately** while the **hedged item is not**. A perfectly effective economic hedge then produces large swings in reported profit — volatility created by an activity that **reduces** economic risk.

That reported volatility has a real cost: it affects how analysts and lenders perceive the business, can breach earnings-based covenants, and invites questions management would rather not answer. Companies therefore accept substantial documentation and effectiveness-testing burdens to qualify.

**The key point for an analyst:** hedge accounting changes **when** gains and losses are recognised, not the **cash flows**. The economics are identical either way.

</details>

**4.** Why is leverage described as the risk that makes the other derivative risks lethal?

<details><summary>Answer</summary>

Because leverage **scales the consequence** of every other risk.

A derivative typically requires **little or no initial outlay** relative to the notional exposure it creates. A futures position controlling 10m of underlying may require 500,000 of margin — 20× leverage.

Now apply each of the other risks to that position:

- **Basis risk** — a 2% mismatch between the hedge and the exposure is a rounding error unlevered; at 20× it is 40% of the capital committed
- **Model risk** — a valuation model that is 3% wrong is a mild embarrassment on an unlevered book; on a levered one it can exceed the equity
- **Liquidity risk** — being unable to exit is inconvenient unlevered; levered, it means meeting **variation margin calls** on a position you cannot close, which is how solvent institutions fail
- **Counterparty risk** — a defaulting counterparty on a small position is a loss; on a levered book it can cascade

**The historical record makes the point.** Barings, LTCM, Amaranth, and the 2008 monoline and AIG failures all combined **leverage** with one of the other risks. In none of them was the underlying view catastrophically wrong in isolation — leverage converted a survivable loss into an unsurvivable one, usually via margin calls that forced liquidation at the worst possible moment.

**The practical lesson:** size positions by the **exposure** created, not by the capital outlay required.

</details>

---

## Done when

- [ ] I can name six benefits and eight risks of derivatives
- [ ] I can explain why leverage amplifies every other derivative risk
- [ ] I can distinguish basis risk from counterparty risk
- [ ] I can list the main corporate hedging applications and the instruments used
- [ ] I can name the three hedge accounting categories and explain why companies qualify for them
- [ ] I can list eight investor uses and explain the overlay concept
- [ ] I can identify when hedging becomes speculation
- [ ] I answered the self-check cold, several days after first study

---

← [LM02 Forward Commitment and Contingent Claim Features and Instruments](lm-02-forward-commitment-and-contingent-claim-features-and-instrum.md)  ·  [Topic index](README.md)  ·  [LM04 Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives](lm-04-arbitrage-replication-and-the-cost-of-carry-in-pricing-deriv.md) →
