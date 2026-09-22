# DER · LM01 — Derivative Instrument and Derivative Market Features

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | None. Entry point to Derivatives. |
| **Where it shows up** | 1 question. Pure recall, but the vocabulary is used in all ten modules. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- define a derivative and describe basic features of a derivative instrument
- describe the basic features of derivative markets, and contrast over-the-counter and exchange-traded derivative markets

---

## Core concepts

### What a derivative is

> **A derivative is a financial instrument whose value DERIVES from the value of an underlying
> asset, rate, or index.**

Four defining features:

| Feature | Detail |
| --- | --- |
| **Underlying** | The asset, rate, or index the value derives from — equities, bonds, interest rates, currencies, commodities, credit, volatility, even weather |
| **Contractual maturity** | Derivatives have a **finite life** and an expiration date |
| **Exercise/settlement terms** | How and when the contract settles — the exercise price, settlement dates, and the settlement mechanism |
| **Settlement method** | **Physical** (the underlying changes hands) or **cash** (the difference in value is paid) |

> **The implicit leverage point:** a derivative typically requires **little or no initial outlay**
> relative to the notional exposure it creates. A forward contract on 10m of currency may require no
> upfront payment at all. That embedded leverage is what makes derivatives efficient — and what
> makes them dangerous.

### The two families

Every derivative on the Level I syllabus falls into one of two categories, and the distinction
drives everything:

| | **Forward commitments** | **Contingent claims** |
| --- | --- | --- |
| Obligation | **BOTH parties are obliged** to transact | The **buyer has a RIGHT, not an obligation** |
| Payoff | **Symmetric** — linear gains and losses | **Asymmetric** — the buyer's loss is limited to the premium |
| Upfront payment | **None** at initiation (value is zero) | The buyer **pays a premium** |
| Instruments | **Forwards, futures, swaps** | **Options, credit derivatives** |

This single table is the organising structure of the whole topic. LM2 develops it fully.

### Exchange-traded versus over-the-counter

| Dimension | **Exchange-traded (ETD)** | **Over-the-counter (OTC)** |
| --- | --- | --- |
| **Terms** | **Standardised** — fixed size, maturity, and specification | **Customised** — negotiated bilaterally |
| **Counterparty** | The **clearinghouse** guarantees every trade | The **other party** — direct bilateral credit exposure |
| **Credit risk** | **Minimal** — novation to the clearinghouse plus margin | **Significant**, though mitigated by collateral and central clearing where mandated |
| **Regulation** | Heavily regulated | Less so, though post-2008 reforms mandate clearing and reporting for standardised products |
| **Transparency** | **High** — prices published continuously | **Low** — bilateral, though trade reporting is now required in major markets |
| **Liquidity** | **High** for active contracts | Varies; generally lower |
| **Settlement of gains/losses** | **Daily** — mark to market and margin | Typically **at maturity**, though collateral is posted periodically |
| **Closing a position** | **Offsetting trade** on the exchange | Requires the counterparty's agreement, a new offsetting contract, or novation |
| **Instruments** | **Futures**, exchange-traded options | **Forwards, swaps**, most options, credit derivatives |

> **The fundamental trade-off: customisation versus credit risk.** OTC gives you exactly the contract
> you need — any size, any maturity, any underlying — at the cost of bearing the counterparty's
> credit. Exchange-traded gives you a guaranteed counterparty at the cost of accepting standardised
> terms that may not match your exposure exactly (**basis risk**).

### The clearinghouse

The mechanism that removes counterparty risk from exchange-traded derivatives:

1. **Novation** — the clearinghouse becomes the buyer to every seller and the seller to every buyer.
   The original parties no longer face each other.
2. **Margin** — both parties post **initial margin** as a performance bond, and positions are
   **marked to market daily**, with gains and losses settled in cash through **variation margin**.
3. **A guarantee fund** and the clearinghouse's own capital stand behind the system.

```
Initial margin    — posted at inception, as a performance bond
Maintenance margin — the minimum balance that must be maintained
Variation margin  — the daily cash settlement of gains and losses
Margin call       — a demand to restore the balance when it falls below maintenance
```

> **Daily settlement is the key structural difference between a future and a forward.** A futures
> gain is received **in cash, daily**; a forward gain accrues and is paid **only at maturity**. This
> produces small but real valuation differences (LM6) and eliminates the build-up of credit exposure.

**Post-2008 reform** has pushed standardised OTC derivatives toward **central clearing**, blurring
the distinction: a cleared interest rate swap has an OTC's customisation history but an exchange's
counterparty protection. Trade reporting requirements have also raised OTC transparency
substantially.

### Market size and participants

Derivatives markets are enormous by **notional** value, which overstates the economic exposure —
notional is the reference amount for calculating payments, not an amount at risk. A 100m notional
interest rate swap exchanges only the **difference** between two interest streams, which might be a
few hundred thousand.

**Participants:** hedgers (transferring unwanted risk), speculators (taking a view), arbitrageurs
(exploiting price discrepancies and, in doing so, enforcing the pricing relationships in LM4),
market makers, and end users such as corporates, asset managers, banks, and insurers.

---

## Formulas to know cold

```
DEFINITION
  A derivative's value DERIVES from an underlying asset, rate, or index.
  Four features: UNDERLYING · finite MATURITY · EXERCISE/settlement terms · SETTLEMENT method

THE TWO FAMILIES — the organising structure of the whole topic
  FORWARD COMMITMENTS   — BOTH parties obliged · SYMMETRIC payoff · no premium
                          → forwards, futures, swaps
  CONTINGENT CLAIMS     — buyer has a RIGHT · ASYMMETRIC payoff · buyer pays a PREMIUM
                          → options, credit derivatives

EXCHANGE-TRADED vs OTC
  Terms:        standardised    vs  customised
  Counterparty: CLEARINGHOUSE   vs  the other party (bilateral credit risk)
  Settlement:   DAILY mark-to-market  vs  typically at maturity
  Closing:      offsetting trade  vs  needs the counterparty, or novation
  Trade-off:    CUSTOMISATION (OTC)  vs  CREDIT PROTECTION (ETD)

CLEARINGHOUSE MECHANICS
  NOVATION — the clearinghouse becomes counterparty to both sides
  Initial margin (performance bond) · Maintenance margin (the floor) · Variation margin (daily cash)
  Margin call when the balance falls below maintenance
```

---

## Exam traps

> **Trap 1 — Forward commitment vs contingent claim.** **Both parties are obliged** under a forward
> commitment; the **buyer has a right, not an obligation**, under a contingent claim. This
> distinction organises the entire topic.

> **Trap 2 — Thinking OTC means unregulated.** Post-2008 reforms mandate **central clearing** and
> **trade reporting** for standardised OTC derivatives. The distinction has narrowed considerably.

> **Trap 3 — Reading notional value as exposure.** Notional is the **reference amount** for
> calculating payments, not an amount at risk. A swap's economic exposure is a small fraction of it.

> **Trap 4 — Assuming exchange-traded is always better.** Standardisation creates **basis risk** when
> the contract does not exactly match the exposure being hedged.

> **Trap 5 — Confusing initial, maintenance, and variation margin.** **Initial** is posted at
> inception; **maintenance** is the floor that triggers a call; **variation** is the daily cash
> settlement of gains and losses.

> **Trap 6 — Missing the significance of daily settlement.** It is the key structural difference
> between futures and forwards, and it drives the valuation difference in LM6.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Contrast a forward commitment and a contingent claim on obligation, payoff shape, and upfront payment.

<details><summary>Answer</summary>

**Forward commitment** (forwards, futures, swaps):
- **Both parties are obliged** to transact at maturity
- Payoff is **symmetric and linear** — gains and losses are unlimited in both directions
- **No upfront payment**; the contract's value at initiation is **zero**, because the terms are set so that neither party has an advantage

**Contingent claim** (options, credit derivatives):
- The **buyer has a right, not an obligation**; only the **seller** is obliged if exercised
- Payoff is **asymmetric** — the buyer's loss is limited to the premium while the upside is large (unlimited for a call)
- The buyer **pays a premium** upfront, which is the price of the option

**The economic consequence:** a forward locks in a price and removes both upside and downside. An option removes the downside while keeping the upside — and you pay for that asymmetry. Choosing between them is fundamentally a question of whether the premium is worth the retained upside.

</details>

**2.** A corporate treasurer needs to hedge exactly 47m of a currency exposure maturing on 14 March. Would you recommend a futures or a forward contract?

<details><summary>Answer</summary>

**A forward contract.**

**Why:** futures are **standardised** — a fixed contract size (say 125,000 units) and fixed quarterly maturity dates (typically the third Wednesday of March, June, September, December). Hedging 47m would require rounding to the nearest whole number of contracts, leaving a residual exposure, and the March expiry would not match 14 March exactly.

Both mismatches create **basis risk** — the hedge does not move exactly with the exposure.

A **forward** is customised: 47m exactly, maturing 14 March exactly. The hedge is perfect.

**The cost of that precision:**
- **Counterparty credit risk** — the treasurer bears the bank's credit, mitigated by a collateral agreement
- **Lower liquidity** — unwinding early requires the counterparty's agreement or an offsetting contract
- **Wider bid-ask spread** than a liquid futures contract

**When futures would win instead:** a large, liquid, standard-sized exposure where the basis risk is trivial, the position may need unwinding early, or the counterparty's credit is a concern. For a corporate hedging a specific known exposure, the forward usually wins.

</details>

**3.** How does a clearinghouse eliminate counterparty risk, and what does it cost participants?

<details><summary>Answer</summary>

**The mechanism, in three parts:**

**(1) Novation.** The clearinghouse **interposes itself** between the original parties — it becomes the buyer to every seller and the seller to every buyer. The two original parties no longer have any claim on each other. Each faces only the clearinghouse.

**(2) Margin and daily settlement.** Both sides post **initial margin** as a performance bond. Positions are **marked to market daily**, and gains and losses are settled in cash through **variation margin**. Credit exposure therefore never accumulates beyond one day's move, and a party that cannot meet a **margin call** has its position closed out immediately.

**(3) A default waterfall.** The defaulter's margin, then a mutualised **guarantee fund** contributed by all members, then the clearinghouse's own capital, stand behind the system.

**What it costs participants:**
- **Capital tied up** in initial margin, which earns little
- **Daily cash flow variability** — variation margin must be funded on demand, which can be substantial in a volatile market and has caused liquidity crises for otherwise solvent hedgers
- **Standardised terms**, and therefore **basis risk**
- **Mutualised risk** — members contribute to a guarantee fund covering other members' defaults

The system converts **credit risk into liquidity risk**, which is usually a good trade, but not a free one.

</details>

---

## Done when

- [ ] I can define a derivative and name its four basic features
- [ ] I can contrast forward commitments and contingent claims on obligation, payoff, and premium
- [ ] I can reproduce the exchange-traded vs OTC comparison table
- [ ] I can explain novation, the three margin types, and how daily settlement removes credit exposure
- [ ] I can explain the customisation-versus-credit-risk trade-off and what basis risk is
- [ ] I can explain why notional value overstates economic exposure
- [ ] I answered the self-check cold, several days after first study

---

[Topic index](README.md)  ·  [LM02 Forward Commitment and Contingent Claim Features and Instruments](lm-02-forward-commitment-and-contingent-claim-features-and-instrum.md) →
