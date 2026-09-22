# DER · LM02 — Forward Commitment and Contingent Claim Features and Instruments

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 7 |
| **Prerequisites** | LM1. |
| **Where it shows up** | 2 questions. Option payoff and profit calculations are certainties. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- define forward contracts, futures contracts, swaps, options (calls and puts), and credit derivatives and compare their basic characteristics
- determine the value at expiration and profit from a long or a short position in a call or put option
- contrast forward commitments with contingent claims

---

## Core concepts

### Forward commitments

**Forward contract.** An agreement to buy or sell an asset at a **specified price on a specified
future date**. OTC, customised, no upfront payment.

```
Payoff to the LONG at expiration  = ST − F0        (spot at expiry minus the forward price)
Payoff to the SHORT at expiration = F0 − ST
```

Both are **linear and symmetric**. The long gains when the spot ends above the forward price; the
short gains when it ends below. Each party's gain is the other's loss — a **zero-sum** contract.

**Futures contract.** Economically the same as a forward, but:

- **Exchange-traded and standardised**
- **Cleared** through a clearinghouse with **daily mark-to-market** and margin
- **Minimal counterparty risk**
- Positions closed by an **offsetting trade** rather than by agreement

**Swap.** An agreement to exchange a **series of cash flows** on specified dates.

A swap is economically equivalent to a **series of forward contracts**, all priced off a single
fixed rate rather than each having its own forward price. The **plain vanilla interest rate swap**
exchanges a **fixed rate** for a **floating rate** on a notional principal that is never exchanged.

Other types: currency swaps (where principal *is* exchanged), equity swaps, commodity swaps, and
credit default swaps.

### Contingent claims: options

| | **Call option** | **Put option** |
| --- | --- | --- |
| Gives the buyer | The **right to BUY** the underlying at the exercise price | The **right to SELL** at the exercise price |
| Buyer profits when | The price **RISES** above the exercise price | The price **FALLS** below the exercise price |
| Buyer's maximum loss | **The premium** | **The premium** |
| Buyer's maximum gain | **Unlimited** | Exercise price **minus the premium** (the price can only fall to zero) |
| Seller's maximum gain | **The premium** | **The premium** |
| Seller's maximum loss | **Unlimited** | Exercise price minus the premium |

**Exercise style:** **European** options may be exercised **only at expiration**; **American**
options may be exercised **at any time** up to expiration. American options are therefore worth at
least as much as otherwise identical European options.

### Payoffs and profits — the four positions

Let `ST` = the spot price at expiration, `X` = the exercise price, `c0`/`p0` = the premiums paid.

| Position | Payoff at expiration | Profit |
| --- | --- | --- |
| **Long call** | `max(0, ST − X)` | `max(0, ST − X) − c0` |
| **Short call** | `−max(0, ST − X)` | `c0 − max(0, ST − X)` |
| **Long put** | `max(0, X − ST)` | `max(0, X − ST) − p0` |
| **Short put** | `−max(0, X − ST)` | `p0 − max(0, X − ST)` |

**Breakeven points:**

```
Long/short call:  ST = X + c0
Long/short put:   ST = X − p0
```

**Payoff diagrams:**

```
LONG CALL                          LONG PUT
Profit                             Profit
  │        ╱                         │╲
  │       ╱                          │ ╲
──┼──────╱───── ST                 ──┼──╲────────── ST
  │  X  ╱                            │   ╲  X
  │────╱  ← loss capped at c0        │    ╲────  ← loss capped at p0
  │                                  │
Max loss = premium                 Max loss = premium
Max gain = UNLIMITED               Max gain = X − p0
```

> **The asymmetry is the whole point.** An option buyer has a **limited, known loss** (the premium)
> and a **large or unlimited gain**. The option seller has the mirror image: a **limited, known
> gain** (the premium) and a **large or unlimited loss**. This is why selling options is often
> compared to selling insurance — steady small premiums, occasional very large losses, with a
> strongly **negatively skewed** return distribution (QM LM5).

**Moneyness:**

| | **Call** | **Put** |
| --- | --- | --- |
| **In the money (ITM)** | `S > X` | `S < X` |
| **At the money (ATM)** | `S = X` | `S = X` |
| **Out of the money (OTM)** | `S < X` | `S > X` |

### Credit derivatives

**Credit default swap (CDS)** — the dominant credit derivative, and a **contingent claim**.

| Party | Position |
| --- | --- |
| **Protection buyer** | Pays a **periodic premium** (the CDS spread). Receives a payment if a **credit event** occurs. Economically **short** the credit — like buying insurance |
| **Protection seller** | Receives the premium. Pays out on a credit event. Economically **long** the credit — like selling insurance |

**Credit events** are defined in the contract: bankruptcy, failure to pay, and (for some contracts)
restructuring.

```
Payout on a credit event ≈ Notional × (1 − Recovery rate)
```

A CDS lets an investor take credit exposure **without owning the bond**, or hedge credit exposure
**without selling** the bond. Other credit derivatives include total return swaps, credit spread
options, and collateralised debt obligations (Fixed Income LM18).

> **The insurance analogy is exact but incomplete.** Unlike insurance, a CDS buyer need not own the
> underlying bond — a "naked" CDS is a pure directional bet on the credit, which is why the
> instrument attracted regulatory attention after 2008.

### The comparison table

| | **Forward** | **Future** | **Swap** | **Option** |
| --- | --- | --- | --- | --- |
| **Family** | Forward commitment | Forward commitment | Forward commitment | Contingent claim |
| **Obligation** | Both parties | Both parties | Both parties | **Buyer has a right** |
| **Payoff** | Symmetric | Symmetric | Symmetric | **Asymmetric** |
| **Upfront payment** | None | None (margin only) | None | **Premium** |
| **Traded** | OTC | **Exchange** | OTC (often cleared) | Both |
| **Settlement** | At maturity | **Daily** | Periodic | At exercise |
| **Counterparty risk** | Yes | Minimal | Yes (reduced by clearing) | Seller's risk to the buyer |

---

## Formulas to know cold

```
FORWARD PAYOFFS (symmetric, linear, zero-sum)
  Long  = ST − F0          Short = F0 − ST

OPTION PAYOFFS AND PROFITS
  Long call   payoff = max(0, ST − X)      profit = max(0, ST − X) − c0
  Short call  payoff = −max(0, ST − X)     profit = c0 − max(0, ST − X)
  Long put    payoff = max(0, X − ST)      profit = max(0, X − ST) − p0
  Short put   payoff = −max(0, X − ST)     profit = p0 − max(0, X − ST)

  Breakeven, call: ST = X + c0        Breakeven, put: ST = X − p0

  Long call:  max loss = premium, max gain = UNLIMITED
  Long put:   max loss = premium, max gain = X − p0
  Short call: max gain = premium, max loss = UNLIMITED
  Short put:  max gain = premium, max loss = X − p0

MONEYNESS
  Call ITM: S > X    Put ITM: S < X    (ATM: S = X)

EXERCISE STYLE
  European — exercisable ONLY at expiration
  American — exercisable ANY time → worth AT LEAST as much as European

CREDIT DEFAULT SWAP
  Protection BUYER  → pays the premium, receives on a credit event → SHORT the credit
  Protection SELLER → receives the premium, pays on a credit event → LONG the credit
  Payout ≈ Notional × (1 − Recovery rate)
```

---

## Exam traps

> **Trap 1 — Payoff vs profit.** **Payoff** ignores the premium; **profit** subtracts it (for the
> buyer) or adds it (for the seller). Read which the question asks for.

> **Trap 2 — Maximum gain on a long put.** It is **X − p0**, not unlimited — the underlying price
> cannot fall below zero. Only a **long call** has unlimited upside.

> **Trap 3 — Breakeven points.** Call: `X + premium`. Put: `X − premium`. Reversing the sign is a
> standard error.

> **Trap 4 — Moneyness for puts.** A put is **in the money when S < X**. Applying the call condition
> to a put inverts the answer.

> **Trap 5 — CDS direction.** The **protection buyer is SHORT the credit** (they gain when it
> deteriorates); the **protection seller is LONG the credit**. The buyer "buys insurance".

> **Trap 6 — Treating a swap as unrelated to forwards.** A swap is economically a **series of
> forward contracts**. Recognising this makes swap valuation (LM7) far easier.

> **Trap 7 — Assuming American options are always exercised early.** They are worth **at least** as
> much as European, but early exercise is rarely optimal for a call on a non-dividend-paying stock.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A call option with exercise price 50 costs 3.40. Compute the payoff and profit at expiration if the stock ends at (a) 45, (b) 53, (c) 62. What is the breakeven?

<details><summary>Answer</summary>

**(a) ST = 45:**
Payoff = max(0, 45 − 50) = **0** (the option expires worthless)
Profit = 0 − 3.40 = **−3.40** (the premium is lost)

**(b) ST = 53:**
Payoff = max(0, 53 − 50) = **3.00**
Profit = 3.00 − 3.40 = **−0.40** (in the money, but not enough to recover the premium)

**(c) ST = 62:**
Payoff = max(0, 62 − 50) = **12.00**
Profit = 12.00 − 3.40 = **+8.60**

**Breakeven** = X + c0 = 50 + 3.40 = **53.40**

Note case (b): the option is **in the money** yet the position is at a **loss**. In-the-money and profitable are different conditions, separated by the premium — a distinction the exam tests directly.

</details>

**2.** Compare the maximum gain and maximum loss for all four basic option positions.

<details><summary>Answer</summary>

| Position | Maximum gain | Maximum loss |
| --- | --- | --- |
| **Long call** | **Unlimited** — the price can rise without bound | The **premium** paid |
| **Short call** | The **premium** received | **Unlimited** — the mirror image |
| **Long put** | **X − p0** — the price can only fall to zero | The **premium** paid |
| **Short put** | The **premium** received | **X − p0** |

**The two things most often got wrong:**

**(1) A long put's gain is NOT unlimited.** The best case is the underlying going to zero, giving a payoff of X and a profit of X − p0. Only the **long call** has genuinely unlimited upside.

**(2) Option sellers face the asymmetry in reverse.** A short call has **unlimited** loss potential against a capped premium gain. This is why naked call writing is heavily margined and generally restricted.

The pattern: **buyers have limited loss and large gain; sellers have limited gain and large loss.** Sellers are compensated by receiving the premium up front and by the fact that most options expire worthless.

</details>

**3.** An investor buys a put with exercise price 80 for 5.20. At what stock price do they break even, and what is their profit if the stock ends at 62?

<details><summary>Answer</summary>

**Breakeven** = X − p0 = 80 − 5.20 = **74.80**

The stock must fall **below 74.80** for the position to be profitable — the premium must be recovered before any gain accrues.

**At ST = 62:**
Payoff = max(0, 80 − 62) = **18.00**
Profit = 18.00 − 5.20 = **+12.80**

**Maximum possible profit** (if the stock went to zero) = 80 − 5.20 = **74.80**. Finite, unlike a long call.

</details>

**4.** Explain the CDS positions and why a protection buyer is 'short the credit'.

<details><summary>Answer</summary>

**Protection buyer:** pays a **periodic premium** (the CDS spread) to the seller. Receives a payment of approximately `notional × (1 − recovery rate)` if a **credit event** occurs — bankruptcy, failure to pay, or restructuring.

**Protection seller:** receives the premium. Pays out on a credit event.

**Why the buyer is 'short the credit':** their position **gains when the credit deteriorates**. If the reference entity's spreads widen or it defaults, the protection becomes more valuable and the buyer profits — exactly the payoff profile of someone who has sold the bond short. Conversely, if the credit improves, they lose the premiums with nothing in return.

**The seller is 'long the credit':** they earn a steady premium as long as nothing happens, and suffer a large loss if it does. That is economically identical to owning the bond — collect the spread, bear the default risk — but **without funding the bond position**.

**Why the instrument exists:**
- **Hedging without selling.** A bondholder can buy protection to neutralise credit risk while keeping the bond, avoiding a sale that might be tax-inefficient, illiquid, or disruptive to a relationship.
- **Taking credit exposure without funding.** A seller earns the credit spread without putting up capital to buy the bond.
- **Expressing a negative view** — shorting corporate bonds directly is difficult and expensive; buying CDS protection is not.

**The controversy:** a **naked** CDS buyer need not own the underlying bond, making it a pure directional bet. This is why the instrument attracted regulatory attention after 2008, and why naked sovereign CDS is restricted in some jurisdictions.

</details>

**5.** Why is a swap economically equivalent to a series of forward contracts?

<details><summary>Answer</summary>

Because each **payment date** on a swap is itself an agreement to exchange one cash flow for another at a **predetermined** rate — which is precisely what a forward contract is.

Consider a plain vanilla interest rate swap with five annual payments. On each date, the fixed-rate payer pays a known fixed amount and receives whatever the floating rate turns out to be. That is a series of five **forward rate agreements**, one per date.

**The one difference:** a strip of separate forwards would each have its **own** forward price, reflecting the forward rate for that specific period. A swap uses a **single fixed rate** across all periods — set so that the **sum** of the present values of all the exchanges equals zero at initiation.

So the swap's fixed rate is a kind of **average** of the forward rates, weighted by the discount factors. Some individual exchanges have positive value at initiation and some negative; they net to zero.

**Why this matters for the exam:** recognising the equivalence makes swap pricing and valuation (LM7) tractable. You are not learning a new instrument — you are applying the forward-pricing logic of LM5 to a sequence of dates and solving for the single rate that makes the total value zero.

</details>

---

## Done when

- [ ] I can define forwards, futures, swaps, options, and CDS and place each in its family
- [ ] I can compute payoff and profit for all four option positions and state the breakevens
- [ ] I can state maximum gain and loss for all four positions, including the long put's finite cap
- [ ] I can determine moneyness for both calls and puts
- [ ] I can explain the CDS positions and why the buyer is short the credit
- [ ] I can explain why a swap is economically a series of forwards
- [ ] I can reproduce the four-instrument comparison table
- [ ] I answered the self-check cold, several days after first study

---

← [LM01 Derivative Instrument and Derivative Market Features](lm-01-derivative-instrument-and-derivative-market-features.md)  ·  [Topic index](README.md)  ·  [LM03 Derivative Benefits, Risks, and Issuer and Investor Uses](lm-03-derivative-benefits-risks-and-issuer-and-investor-uses.md) →
