# DER · LM04 — Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 7 |
| **Prerequisites** | QM LM4 (cash flow additivity and no-arbitrage), LM2. |
| **Where it shows up** | 2 questions. The conceptual foundation for LM5-LM10 — do not skip it. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain how the concepts of arbitrage and replication are used in pricing derivatives
- explain the difference between the spot and expected future price of an underlying and the cost of carry associated with holding the underlying asset

---

## Core concepts

### The single most important idea in Derivatives

> **You never need a forecast to price a derivative. You need a replicating portfolio and the
> assertion that riskless profits do not persist.**

Everything in LM5 through LM10 is an application of this.

### Arbitrage

**An arbitrage opportunity exists when two assets or portfolios with identical future cash flows
trade at different prices.** The arbitrageur buys the cheap one, sells the expensive one, and
locks in a riskless profit with **zero net investment**.

The two conditions that define arbitrage:

1. **No initial net investment** — the proceeds of the short position fund the long position
2. **No risk** — the future cash flows offset exactly, in every state of the world

**The law of one price:** two assets producing identical future cash flows must have the same price
today. If they do not, arbitrage forces convergence.

> **The role of arbitrageurs** is not to make money (though they do) but to **enforce pricing
> relationships**. Their trading is the mechanism by which the no-arbitrage price becomes the actual
> price. The relationships in LM5–LM10 hold because someone is watching for violations.

**Limits to arbitrage** — why mispricings can persist:

- **Transaction costs** — bid-ask spreads, commissions, and market impact can exceed the discrepancy
- **Short-selling constraints** — the required security may be unavailable to borrow, or expensive
- **Capital constraints** — the arbitrageur may lack funding, or face margin requirements
- **Execution risk** — the two legs may not fill simultaneously at the observed prices
- **Model risk** — the "mispricing" may be an error in the model identifying it
- **The mispricing can widen before it corrects**, forcing liquidation at a loss

### Replication

**Replication constructs a portfolio of simpler instruments that reproduces a derivative's payoffs
exactly.** By the law of one price, the derivative must cost what the replicating portfolio costs.

**The canonical examples:**

```
Long forward  =  Long the underlying, financed by borrowing
                 (buy the asset now with borrowed money; at maturity you own the asset and owe the loan
                  — exactly the forward's position)

Long asset    =  Long forward + lending the present value of the forward price
Risk-free asset = Long asset + short forward       (a fully hedged position earns the risk-free rate)
```

And for options (LM9 develops this fully):

```
Put-call parity:  c0 + X/(1+r)^T  =  p0 + S0

  A call plus a risk-free bond = a put plus the stock. Identical payoffs at expiry,
  so identical value today.
```

> **Why replication matters:** it converts an unfamiliar instrument into a combination of familiar
> ones. A derivative you cannot price directly becomes a portfolio you **can** price. The binomial
> model (LM10) is replication applied one step at a time.

### Spot price versus expected future price

A persistent source of confusion, and a favourite exam point.

| | Meaning |
| --- | --- |
| **Spot price (S0)** | The price for **immediate** delivery, observable now |
| **Expected future spot price E(ST)** | The market's **expectation** of the price at time T — unobservable |
| **Forward price (F0)** | The price agreed **today** for delivery at T — observable, and set by **no-arbitrage** |

> **The forward price is NOT the expected future spot price.** It is determined by the **cost of
> carry**, not by anyone's forecast. Two markets with wildly different expectations about a
> commodity's future price will still have the same forward price if their spot prices and carrying
> costs are the same — because the forward price is enforced by arbitrage, and arbitrage does not
> care about opinions.
>
> The difference between `F0` and `E(ST)` reflects a **risk premium**, and it is the reason futures
> markets can be in **backwardation** (F0 < E(ST)) or **contango**.

### Cost of carry

**The forward price is the spot price compounded forward, adjusted for the costs and benefits of
holding the asset until delivery.**

```
F0 = S0 × (1 + r)^T  +  FV(costs)  −  FV(benefits)
```

Or in continuous-compounding form, which is often cleaner:

```
F0 = S0 × e^((r + c − i) × T)

where  r = risk-free rate
       c = carrying costs (storage, insurance) as a rate
       i = income or convenience yield as a rate
```

| Component | Effect on the forward price | Examples |
| --- | --- | --- |
| **Risk-free rate (r)** | **Raises** it — you forgo interest by holding the asset | |
| **Storage and insurance costs (c)** | **Raises** it — holding is costly | Commodities |
| **Income or yield (i)** | **Lowers** it — holding pays you | Dividends on a stock, coupons on a bond, foreign interest on a currency |
| **Convenience yield** | **Lowers** it — non-monetary benefit of physical possession | Commodities: holding inventory lets you meet unexpected demand or avoid a production stoppage |

**Why the signs work that way.** Consider the replicating trade: to deliver the asset at T, buy it
now and hold it. That costs the **purchase price plus interest forgone plus storage**, less any
**income received** while holding. The forward price must equal that total cost, or arbitrage
follows.

**Contango and backwardation:**

| | Condition | Typical cause |
| --- | --- | --- |
| **Contango** | Forward price **above** spot | Storage costs dominate; low convenience yield |
| **Backwardation** | Forward price **below** spot | **High convenience yield** — physical scarcity, or an immediate need for the commodity |

> Backwardation in a commodity is informative: it means the market values **having the physical
> commodity now** more than holding a claim on it later, which typically signals a supply shortage.

### The no-arbitrage forward price, derived

**If `F0` is too high:** sell the forward, borrow `S0` at `r`, buy the asset. At maturity, deliver
the asset, receive `F0`, repay `S0(1+r)^T`. Profit = `F0 − S0(1+r)^T` > 0, with no capital and no
risk. This is **cash-and-carry arbitrage**.

**If `F0` is too low:** buy the forward, short the asset, invest the proceeds. **Reverse
cash-and-carry.**

Arbitrage in either direction forces:

```
F0 = S0 × (1 + r)^T   (for an asset with no costs or benefits)
```

> **This derivation is the template for everything that follows.** Forwards, futures, swaps, and
> options are all priced by constructing a replicating portfolio and asserting that riskless profits
> do not persist. If you understand the cash-and-carry argument, you understand the topic.

---

## Formulas to know cold

```
THE CENTRAL PRINCIPLE
  Two portfolios with IDENTICAL future cash flows must have the SAME price today.
  Violations are arbitraged away. NO FORECAST IS REQUIRED.

ARBITRAGE — two defining conditions
  (1) NO initial net investment    (2) NO risk

REPLICATION
  Long forward  = Long the underlying, financed by BORROWING
  Risk-free position = Long asset + Short forward
  Put-call parity:  c0 + X/(1+r)^T = p0 + S0

FORWARD PRICE / COST OF CARRY
  F0 = S0 × (1 + r)^T + FV(costs) − FV(benefits)
  F0 = S0 × e^((r + c − i) × T)        [continuous form]

    r = risk-free rate        → RAISES F0
    c = storage/insurance     → RAISES F0
    i = income / convenience  → LOWERS F0
          (dividends, coupons, foreign interest, convenience yield)

  CONTANGO:      F0 > S0   (storage costs dominate)
  BACKWARDATION: F0 < S0   (high convenience yield — physical scarcity)

CASH-AND-CARRY ARBITRAGE (the template for the whole topic)
  F0 too HIGH → sell the forward, BORROW S0, buy the asset, deliver at T
  F0 too LOW  → buy the forward, SHORT the asset, invest the proceeds

FORWARD PRICE ≠ EXPECTED FUTURE SPOT PRICE
  F0 is set by the COST OF CARRY and enforced by ARBITRAGE.
  E(ST) is a forecast. The difference is a RISK PREMIUM.
```

---

## Exam traps

> **Trap 1 — Believing the forward price is a forecast.** It is **not** the expected future spot
> price. It is the spot price adjusted for **cost of carry**, enforced by arbitrage. The difference
> between them is a risk premium.

> **Trap 2 — Getting the cost-of-carry signs wrong.** **Costs raise** the forward price; **benefits
> (income, convenience yield) lower** it. Derive them from the replicating trade rather than
> memorising.

> **Trap 3 — Contango vs backwardation.** **Contango: F0 > S0.** **Backwardation: F0 < S0**, caused
> by a high convenience yield.

> **Trap 4 — Forgetting arbitrage requires zero net investment AND zero risk.** A profitable trade
> with capital at risk is not arbitrage.

> **Trap 5 — Thinking arbitrage is always available.** **Limits to arbitrage** — transaction costs,
> short-sale constraints, capital limits, execution risk, and the possibility that the mispricing
> widens — let discrepancies persist.

> **Trap 6 — Missing that replication is the whole method.** Every pricing result in LM5–LM10 is a
> replicating portfolio plus the law of one price.

> **Trap 7 — Omitting the convenience yield for commodities.** It is the reason commodity forward
> curves can be downward sloping despite positive storage costs.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** An asset trades at 100. The one-year risk-free rate is 5%. The one-year forward is quoted at 108. Construct the arbitrage.

<details><summary>Answer</summary>

**The no-arbitrage forward price** is F0 = 100 × 1.05 = **105**. The quoted 108 is **too high**, so execute a **cash-and-carry**:

**Today:**
1. **Sell** the forward at 108 (agreeing to deliver the asset in one year)
2. **Borrow** 100 at 5%
3. **Buy** the asset for 100

Net cash flow today: **zero** (the borrowing funds the purchase).

**At maturity:**
4. **Deliver** the asset under the forward, receive **108**
5. **Repay** the loan: 100 × 1.05 = **105**

**Profit = 108 − 105 = 3**, with **no capital committed and no risk** — the asset was owned throughout, so delivery is certain regardless of where the spot price ends.

Arbitrageurs executing this trade sell forwards (pushing F0 down) and buy the asset (pushing S0 up) until F0 = S0(1+r)^T and the profit disappears. That process is what makes the no-arbitrage price the actual price.

</details>

**2.** Why is the forward price not the expected future spot price?

<details><summary>Answer</summary>

Because the forward price is determined by **arbitrage**, and arbitrage does not depend on anyone's expectations.

**The forward price is enforced mechanically:** if F0 differs from S0 adjusted for cost of carry, a riskless profit is available (as in the previous question). Arbitrageurs execute it, and the price moves back. This works **regardless of what anyone expects** the future spot price to be.

**A concrete demonstration:** suppose everyone in the market is certain a stock will be at 150 in a year. It trades at 100 today and the risk-free rate is 5%. The one-year forward is still **105**, not 150 — because at any other price the cash-and-carry arbitrage is available, and executing it does not require sharing the market's view. (The expectation is already in the spot price of 100; if the market really believed 150 with certainty, the spot would not be 100.)

**The difference between F0 and E(ST) is a risk premium.** In commodity markets this shows up as **normal backwardation** (F0 below E(ST), because hedgers pay speculators to bear price risk) or the reverse.

**The practical implication:** you cannot read the futures curve as a market forecast. An upward-sloping oil futures curve reflects **storage costs and interest**, not a prediction that oil will rise. This is the same error as reading forward interest rates as rate forecasts (Fixed Income LM9).

</details>

**3.** A commodity trades at 80 with annual storage costs of 3% and a convenience yield of 7%. The risk-free rate is 4%. Compute the one-year forward price and describe the curve shape.

<details><summary>Answer</summary>

Using the continuous-compounding form:

F0 = S0 × e^((r + c − i) × T)
   = 80 × e^((0.04 + 0.03 − 0.07) × 1)
   = 80 × e^(0.00)
   = **80.00**

The forward price equals the spot price — the curve is **flat**, because the convenience yield (7%) exactly offsets the combined interest and storage costs (4% + 3% = 7%).

**If the convenience yield were higher — say 12%:**
F0 = 80 × e^(0.04 + 0.03 − 0.12) = 80 × e^(−0.05) = **76.10**

The forward price is now **below** spot: the market is in **backwardation**. Economically, holders of the physical commodity value having it **now** — to meet unexpected demand or avoid a production stoppage — by more than the cost of carrying it. That typically signals **physical scarcity**.

**If the convenience yield were zero:**
F0 = 80 × e^(0.07) = **85.80** — **contango**, the normal shape when storage costs dominate.

</details>

**4.** Explain how a long forward position can be replicated, and why that determines its price.

<details><summary>Answer</summary>

**The replication:** a long forward at price F0 obliges you to pay F0 at time T and receive the asset. You can reproduce that position exactly by:

1. **Buying the asset today** for S0
2. **Financing the purchase by borrowing** S0 at the risk-free rate

**At time T** you hold the asset (as the forward would deliver) and owe `S0 × (1+r)^T` (which the forward would have you pay as F0). The two positions have **identical outcomes in every state of the world** — you end up owning the asset and having paid a known amount.

**Why that determines the price:** by the **law of one price**, two portfolios with identical future cash flows must cost the same today. The replicating portfolio costs nothing today (the loan funds the purchase), and the forward costs nothing today. For the two to be genuinely equivalent, the amounts owed at T must match:

```
F0 = S0 × (1 + r)^T
```

If they did not match, the cash-and-carry arbitrage of the first question would be available.

**Why this method matters beyond forwards:** replication is the general technique. Futures, swaps, and options are all priced by constructing a portfolio of simpler instruments that reproduces the payoffs, then asserting that riskless profits do not persist. The binomial model (LM10) is replication applied one period at a time, and put-call parity (LM9) is replication applied to options.

**And note what is absent: any forecast.** The replication argument never asks where the asset price will go.

</details>

---

## Done when

- [ ] I can state the law of one price and the two conditions defining arbitrage
- [ ] I can construct the cash-and-carry arbitrage in both directions
- [ ] I can replicate a long forward and derive F0 = S0(1+r)^T from it
- [ ] I can state the full cost-of-carry formula and get every sign right from the replicating trade
- [ ] I can explain why the forward price is not a forecast of the future spot price
- [ ] I can define contango and backwardation and explain what backwardation signals
- [ ] I can name four limits to arbitrage
- [ ] I answered the self-check cold, several days after first study

---

← [LM03 Derivative Benefits, Risks, and Issuer and Investor Uses](lm-03-derivative-benefits-risks-and-issuer-and-investor-uses.md)  ·  [Topic index](README.md)  ·  [LM05 Pricing and Valuation of Forward Contracts and for an Underlying with Varying Maturities](lm-05-pricing-and-valuation-of-forward-contracts-and-for-an-underl.md) →
