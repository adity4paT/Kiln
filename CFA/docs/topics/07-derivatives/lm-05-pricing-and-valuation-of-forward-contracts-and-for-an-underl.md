# DER · LM05 — Pricing and Valuation of Forward Contracts and for an Underlying with Varying Maturities

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM4 (cost of carry and no-arbitrage), Fixed Income LM9 (forward rates). |
| **Where it shows up** | 2-3 questions — the largest allocation in Derivatives. Pricing vs valuation is the central distinction. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain how the value and price of a forward contract are determined at initiation, during the life of the contract, and at expiration
- explain how forward rates are determined for interest rate forward contracts and describe the uses of these forward rates.

---

## Core concepts

### Price versus value — the distinction that organises the module

These are **different concepts** and the exam tests the difference directly.

| | **Price (F0)** | **Value (Vt)** |
| --- | --- | --- |
| What it is | The **agreed transaction price** written into the contract | The **worth of the position** today |
| When determined | **Fixed at initiation** | Changes **continuously** |
| At initiation | Set so the contract's value is **zero** | **Zero** — neither party pays the other |
| During the life | **Unchanged** — it is in the contract | Moves as the spot price and time change |
| At expiration | Irrelevant — the contract settles | `ST − F0` for the long |

> **Memorise this: at initiation the forward PRICE is set so that the forward VALUE is zero.** No
> money changes hands, because the price is chosen to make the contract fair to both sides. As the
> spot price moves, the fixed price becomes favourable to one party — and that is the contract's
> value.

### Pricing at initiation

The no-arbitrage forward price (LM4):

```
F0 = S0 × (1 + r)^T                                 [no costs or benefits]

F0 = [S0 − PV(income)] × (1 + r)^T                  [asset pays income, e.g. dividends or coupons]

F0 = S0 × (1 + r)^T − FV(income) + FV(costs)        [equivalent form]

F0 = S0 × e^((r + c − i) × T)                       [continuous compounding]
```

**Worked example.** A stock trades at 60, will pay a 1.50 dividend in 6 months, and the annual
risk-free rate is 4%. What is the one-year forward price?

```
PV(dividend) = 1.50 / (1.04)^0.5 = 1.4709
F0 = (60 − 1.4709) × (1.04)^1 = 58.5291 × 1.04 = 60.87
```

The dividend **lowers** the forward price, because the forward holder does not receive it.

### Valuation during the life

At any time `t` before expiration, the value of a **long** forward is the difference between what
the asset is worth now and the present value of what you have agreed to pay:

```
Vt(long) = St − F0 / (1 + r)^(T−t)                       [no income]

Vt(long) = [St − PV_t(remaining income)] − F0 / (1 + r)^(T−t)     [with income]
```

Equivalently, and often more intuitively:

```
Vt(long) = [Ft − F0] / (1 + r)^(T−t)
```

— the difference between the **current** forward price for the same maturity and the price you
locked in, discounted back.

**And the short's value is the exact negative:**

```
Vt(short) = −Vt(long)
```

Forwards are **zero-sum**: one party's gain is precisely the other's loss.

**Worked example.** You are long a one-year forward struck at 60.87 (from above). Six months later
the stock trades at 66, no dividends remain, and the rate is still 4%.

```
Vt(long) = 66 − 60.87/(1.04)^0.5 = 66 − 60.87/1.0198 = 66 − 59.69 = 6.31
```

The long position is worth **6.31**; the short's is worth **−6.31**.

### Valuation at expiration

```
VT(long)  = ST − F0
VT(short) = F0 − ST
```

The contract settles, either physically (the asset is delivered for F0) or in cash (the difference
is paid).

### Interest rate forwards

A **forward rate agreement (FRA)** is a forward contract on an **interest rate**. One party agrees
to pay a fixed rate and receive a floating reference rate on a notional principal, for a specified
future period.

**Notation:** a **"3 × 9 FRA"** means the contract starts in **3 months** and covers a period ending
in **9 months** — so it is a **6-month** rate, 3 months forward. (First number = months to start;
second = months to the end; the difference = the length of the underlying period.)

**The forward rate is determined by no-arbitrage**, exactly as in Fixed Income LM9:

```
(1 + z_A)^A × (1 + F(A,B))^B = (1 + z_(A+B))^(A+B)

F(A,B) = [ (1 + z_(A+B))^(A+B) / (1 + z_A)^A ]^(1/B) − 1
```

Investing for the long period must give the same result as investing short and rolling forward at
the forward rate — otherwise arbitrage.

**Settlement.** FRAs settle **at the start** of the underlying period, in cash, at the **present
value** of the interest differential:

```
Settlement = Notional × (Reference rate − FRA rate) × (days/360)
             ─────────────────────────────────────────────────────
                        1 + Reference rate × (days/360)
```

The denominator discounts back from the end of the period (when the interest would naturally have
been paid) to the settlement date at the start.

> The **long** (fixed-rate payer) **gains when rates rise** — they have locked in a lower rate than
> the market now offers.

### Uses of interest rate forwards

| Use | Detail |
| --- | --- |
| **Hedging a future borrowing** | A company planning to borrow in 3 months can lock the rate now with a 3 × 9 FRA |
| **Hedging a future investment** | The reverse — lock in the rate on cash expected to arrive |
| **Speculating on rate direction** | Without taking a balance sheet position |
| **Constructing swaps** | A swap is a series of FRAs (LM7) |
| **Extracting market expectations** | Forward rates reveal the no-arbitrage implied path of future rates (with the term premium caveat from Fixed Income LM9) |

> **The caveat from Fixed Income LM9 applies here too:** the forward rate is a **no-arbitrage**
> construction, not a forecast. It systematically **exceeds** the realised future spot rate, because
> it embeds a **term premium**. Locking in a forward rate is not the same as betting that rates will
> reach it.

### A note on credit risk

A forward's value accrues over its life and is settled only **at maturity**, so **credit exposure
builds up** as the contract moves in one party's favour. This is precisely what daily settlement in
futures markets eliminates (LM6), and what collateral agreements in OTC markets mitigate.

---

## Formulas to know cold

```
PRICE vs VALUE
  PRICE  F0 — agreed at initiation, FIXED for the contract's life
  VALUE  Vt — ZERO at initiation, then changes continuously
  At initiation the PRICE is set so that the VALUE is zero.

PRICING AT INITIATION
  F0 = S0 × (1 + r)^T                            [no costs or benefits]
  F0 = [S0 − PV(income)] × (1 + r)^T             [asset pays income]
  F0 = S0 × (1 + r)^T − FV(income) + FV(costs)
  F0 = S0 × e^((r + c − i) × T)                  [continuous]

VALUATION DURING THE LIFE
  Vt(long) = St − F0/(1 + r)^(T−t)                       [no income]
  Vt(long) = [St − PV_t(remaining income)] − F0/(1 + r)^(T−t)
  Vt(long) = [Ft − F0] / (1 + r)^(T−t)                   [equivalent, often easier]
  Vt(short) = −Vt(long)                                   [zero-sum]

AT EXPIRATION
  VT(long) = ST − F0        VT(short) = F0 − ST

FORWARD RATE AGREEMENTS
  "3 × 9 FRA" = starts in 3 months, ends in 9 → a SIX-MONTH rate, three months forward

  F(A,B) = [ (1 + z_(A+B))^(A+B) / (1 + z_A)^A ]^(1/B) − 1

  Settlement (paid at the START of the period, discounted):
    = Notional × (Reference − FRA rate) × (days/360) / [1 + Reference × (days/360)]

  The LONG (fixed-rate payer) GAINS when rates RISE.
```

---

## Exam traps

> **Trap 1 — Confusing price and value.** The **price is fixed** at initiation; the **value changes**.
> At initiation the price is set so the **value is zero**.

> **Trap 2 — Income direction.** Income received by the asset holder **lowers** the forward price,
> because the forward holder does not receive it. Costs **raise** it.

> **Trap 3 — Forgetting to discount F0 in the valuation.** `Vt(long) = St − F0/(1+r)^(T−t)`. The
> agreed price is paid at **T**, so it must be discounted back to **t**.

> **Trap 4 — FRA notation.** A **"3 × 9"** starts in 3 months and ends in 9 — the underlying is a
> **6-month** rate. The difference between the numbers is the period length.

> **Trap 5 — FRA settlement timing.** It settles at the **START** of the underlying period, at the
> **present value** of the differential. Forgetting the discounting overstates the payment.

> **Trap 6 — FRA direction.** The **long / fixed-rate payer gains when rates RISE**.

> **Trap 7 — Treating forward rates as forecasts.** They are no-arbitrage constructions embedding a
> **term premium** (Fixed Income LM9).

> **Trap 8 — Missing that forwards accumulate credit exposure.** Value builds up and settles only at
> maturity — which is exactly what futures' daily settlement eliminates.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A stock trades at 45 and pays a 0.80 dividend in 4 months. The annual risk-free rate is 3.5%. Compute the 9-month forward price.

<details><summary>Answer</summary>

PV of the dividend = 0.80 / (1.035)^(4/12) = 0.80 / 1.01152 = **0.7909**

F0 = (S0 − PV(income)) × (1 + r)^T
   = (45 − 0.7909) × (1.035)^(9/12)
   = 44.2091 × (1.035)^0.75
   = 44.2091 × 1.02597
   = **45.36**

The dividend **reduces** the forward price relative to what it would be with no income: without the dividend, F0 = 45 × 1.02597 = 46.17. The forward holder does not receive the 0.80, so they must not pay for it.

</details>

**2.** Three months after entering a long 9-month forward at 45.36, the stock trades at 48.50, the dividend has been paid, and the rate is still 3.5%. Value the long and the short positions.

<details><summary>Answer</summary>

Six months remain (T − t = 0.5), and no income is outstanding.

Vt(long) = St − F0/(1 + r)^(T−t)
        = 48.50 − 45.36/(1.035)^0.5
        = 48.50 − 45.36/1.01735
        = 48.50 − 44.59
        = **+3.91**

Vt(short) = **−3.91**

The long is ahead by 3.91: they locked in a purchase at 45.36 for an asset now worth 48.50, and the present value of that advantage is 3.91. The short has an exactly offsetting loss — forwards are **zero-sum**.

Note the **credit exposure** this creates: the short now owes the long 3.91 in economic terms, but nothing settles until maturity. That accumulating exposure is what futures' daily settlement eliminates (LM6).

</details>

**3.** Explain what a '6 x 12 FRA' is and who gains if rates rise.

<details><summary>Answer</summary>

A **6 × 12 FRA** is a forward rate agreement that:
- **Starts in 6 months**
- **Ends in 12 months**
- Therefore covers a **6-month period** (12 − 6), beginning 6 months from today

So it locks in **today** the rate on a six-month borrowing or investment that will begin in six months.

**Who gains if rates rise: the LONG — the fixed-rate payer.**

The long has agreed to pay a fixed rate and receive the floating reference rate. If the reference rate at settlement exceeds the agreed FRA rate, they receive the difference. Economically, they locked in a **lower** borrowing cost than the market now offers.

**The typical user:** a company that knows it will need to borrow in six months. Buying the FRA (going long) fixes its cost today. If rates rise, the FRA gain offsets the higher borrowing cost; if rates fall, the FRA loss offsets the cheaper borrowing. Either way the effective cost is locked.

</details>

**4.** Explain why a forward contract's value is zero at initiation but its price is not.

<details><summary>Answer</summary>

**They answer different questions.**

The **price (F0)** is the **agreed transaction price** — the amount that will be exchanged for the asset at maturity. It is a substantial number: the forward price of a stock trading at 45 might be 46. It is written into the contract and **never changes**.

The **value (Vt)** is the **worth of the position** — what someone would pay to take over your side of the contract today. At initiation it is **zero**, and that is by construction: the price F0 is deliberately **chosen** so that neither party has an advantage. Since neither side is better off, neither pays the other anything to enter, and no money changes hands.

**An analogy:** agreeing today to buy a car for 20,000 next year. The **price** is 20,000. The **value** of that agreement to you, right now, is **zero** — because 20,000 is a fair price for delivery next year. If the car's market value then rises, your agreement becomes **valuable** (you can buy below market) even though the agreed **price** is still 20,000.

**Why it matters on the exam:** questions often ask for one when you are tempted to compute the other. 'What is the value of the forward at initiation?' is **zero**, always, and requires no calculation. 'What is the forward price?' requires the cost-of-carry formula.

</details>

---

## Done when

- [ ] I can state the price-value distinction and explain why value is zero at initiation
- [ ] I can compute a forward price with and without income, with correct signs
- [ ] I can value a forward during its life, remembering to discount F0
- [ ] I can state the value at expiration for both the long and the short
- [ ] I can read FRA notation and identify the underlying period
- [ ] I can compute an FRA settlement, including the discounting to the start of the period
- [ ] I can say who gains from a rate rise and explain the hedging application
- [ ] I answered the self-check cold, several days after first study

---

← [LM04 Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives](lm-04-arbitrage-replication-and-the-cost-of-carry-in-pricing-deriv.md)  ·  [Topic index](README.md)  ·  [LM06 Pricing and Valuation of Futures Contracts](lm-06-pricing-and-valuation-of-futures-contracts.md) →
