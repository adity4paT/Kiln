# DER · LM07 — Pricing and Valuation of Interest Rate and Other Swaps

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM5 (forward pricing), Fixed Income LM9 (spot and forward rates). |
| **Where it shows up** | 1-2 questions. The swap-as-a-series-of-forwards equivalence is the conceptual target. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe how swap contracts are similar to but different from a series of forward contracts
- contrast the value and price of swaps

---

## Core concepts

### The plain vanilla interest rate swap

Two parties exchange **interest payment streams** on a **notional principal** that is never itself
exchanged.

| Party | Pays | Receives |
| --- | --- | --- |
| **Fixed-rate payer** (the "long", or "payer swap") | A **fixed** rate | A **floating** reference rate |
| **Floating-rate payer** (the "short", or "receiver swap") | The **floating** rate | The **fixed** rate |

Only the **net difference** changes hands on each payment date:

```
Net payment to the fixed-rate payer
    = Notional × (Floating rate − Fixed rate) × (days/360)
```

> **The fixed-rate payer GAINS when rates RISE** — they are locked into paying the lower fixed rate
> while receiving the now-higher floating rate. Same direction as the long FRA in LM5, which is not
> a coincidence.

### Similar to a series of forwards — and how it differs

**The similarity:** each payment date is an agreement to exchange a known fixed amount for an
unknown floating amount at a **predetermined** rate. That is exactly a forward rate agreement. A
five-year annual swap is economically a **strip of five FRAs**.

**The difference, and it is the whole point:**

| | **A strip of separate forwards** | **A swap** |
| --- | --- | --- |
| Rate on each date | **Each has its own forward rate**, reflecting that period's forward | A **single fixed rate** applies to every date |
| Value of each individual exchange at initiation | **Zero** for each one separately | **Non-zero individually** — some positive, some negative |
| Value of the whole package at initiation | Zero | **Zero — they net out** |
| Documentation | Separate contracts | One contract, one master agreement, netted payments |
| Counterparty exposure | Per contract | **Netted** across all payment dates |

> **This is the key insight.** In a strip of forwards, **each contract** is individually priced at
> zero value. In a swap, a **single fixed rate** is chosen so that the **sum** of the present values
> of all the exchanges is zero. With an upward-sloping curve, the early exchanges favour one party
> and the later ones favour the other — and they offset.
>
> The swap's fixed rate is therefore a kind of **weighted average of the forward rates**, weighted by
> the discount factors.

**Practical advantages of a swap over a strip of forwards:** a single contract and master agreement,
netted payments (reducing settlement flows), netted counterparty exposure, lower transaction costs,
and a single rate that is simpler to hedge and account for.

### Pricing a swap

**"Pricing" a swap means finding the fixed rate that makes its value zero at initiation** — exactly
parallel to finding the forward price that makes a forward's value zero (LM5).

```
The swap fixed rate is set so that:
    PV(fixed leg) = PV(floating leg)

Using discount factors derived from the spot curve:

               1 − Z_n
  Swap rate = ─────────────
              Σ(t=1 to n) Z_t

  where Z_t is the discount factor for period t:  Z_t = 1/(1 + z_t)^t
```

**Why this works.** The **floating leg** of a swap is worth **par at each reset**, because its coupon
resets to the current market rate (the same logic as an FRN trading at par in Fixed Income LM8). So
valuing the swap reduces to finding the fixed rate at which a **par fixed-rate bond** has the same
value — which is the **par rate** from the term structure (Fixed Income LM9).

> **The elegant restatement:** a plain vanilla interest rate swap is equivalent to being **long a
> floating-rate bond and short a fixed-rate bond** (for the fixed-rate payer), both with the same
> notional and maturity. The swap fixed rate is simply the **par rate** for that maturity.

### Valuing a swap during its life

**Price versus value, exactly as in LM5:**

| | **Price** | **Value** |
| --- | --- | --- |
| What | The **fixed rate**, agreed at initiation | The worth of the position today |
| At initiation | Set so value = zero | **Zero** |
| During the life | **Unchanged** | Moves with rates |

```
Value to the fixed-rate payer = PV(floating leg) − PV(fixed leg)
```

Or, more usefully for the exam, as the difference between the current market swap rate and the
contracted one:

```
Value to the fixed-rate payer
    ≈ Notional × (Current swap rate − Contracted fixed rate) × Σ(discount factors)
```

**The direction:** if market swap rates have **risen** above the contracted fixed rate, the
fixed-rate payer is **paying below market** and the swap has **positive value** to them. If rates
have fallen, the value is negative.

> **The bond framing again:** for the fixed-rate payer, `Value = Value of the floating-rate bond −
> Value of the fixed-rate bond`. When rates rise, the fixed-rate bond they are effectively short
> falls in value — a gain. The floating-rate bond they are long stays near par.

### Other swap types

| Swap | Exchanges |
| --- | --- |
| **Currency swap** | Interest payments in **two different currencies** — and unlike an interest rate swap, the **principal IS exchanged**, at initiation and at maturity |
| **Equity swap** | The return on an equity or index for a fixed or floating rate. Used to gain or hedge equity exposure without trading the shares |
| **Commodity swap** | A fixed price for a floating commodity price. Used by producers and consumers to lock in prices |
| **Credit default swap** | Protection against a credit event (LM2). A contingent claim, unlike the others |
| **Basis swap** | One floating rate for a different floating rate |

> **The currency swap exception matters:** in an **interest rate** swap the notional is never
> exchanged, because both legs are in the same currency and only the net difference is meaningful.
> In a **currency** swap the two legs are in **different currencies**, so netting is impossible and
> the **principal is exchanged** at both ends.

### Uses

| Use | Detail |
| --- | --- |
| **Converting floating debt to fixed** | A company with floating-rate debt enters a **pay-fixed** swap, locking in its cost (Corporate Issuers LM6) |
| **Converting fixed debt to floating** | The reverse, with a receive-fixed swap |
| **Managing portfolio duration** | A pay-fixed swap has negative duration — it reduces a bond portfolio's rate sensitivity |
| **Gaining exposure without owning the asset** | Equity and commodity swaps |
| **Exploiting comparative advantage** | Two borrowers each fund where they borrow most cheaply, then swap into the exposure they want |

---

## Formulas to know cold

```
PLAIN VANILLA INTEREST RATE SWAP
  Fixed-rate payer PAYS fixed, RECEIVES floating → GAINS when rates RISE
  Net payment to the fixed payer = Notional × (Floating − Fixed) × (days/360)
  The NOTIONAL IS NEVER EXCHANGED (except in a CURRENCY swap, where it IS).

SWAP ≈ A SERIES OF FORWARDS
  Strip of forwards: EACH contract has its OWN rate and is INDIVIDUALLY worth zero
  Swap:              ONE fixed rate; individual exchanges have NON-zero value;
                     the SUM of their present values is zero

PRICING (finding the fixed rate that makes the value zero)
                 1 − Z_n
  Swap rate = ────────────────     where Z_t = 1/(1 + z_t)^t
               Σ(t=1..n) Z_t

  The swap rate is the PAR RATE for that maturity (Fixed Income LM9).
  The FLOATING leg is worth PAR at each reset.

EQUIVALENT BOND POSITION (fixed-rate payer)
  = LONG a floating-rate bond + SHORT a fixed-rate bond, same notional and maturity

VALUATION DURING THE LIFE
  Value to the fixed-rate payer = PV(floating leg) − PV(fixed leg)
     ≈ Notional × (Current swap rate − Contracted fixed rate) × Σ(discount factors)

  Market rates RISE  → POSITIVE value to the fixed-rate payer
  Market rates FALL  → NEGATIVE value to the fixed-rate payer
```

---

## Exam traps

> **Trap 1 — Thinking the notional is exchanged.** In an **interest rate** swap it is **not** — only
> the net interest difference. In a **currency** swap the principal **is** exchanged at both ends.

> **Trap 2 — Getting the fixed payer's direction wrong.** The **fixed-rate payer gains when rates
> RISE**. Same as the long FRA.

> **Trap 3 — Assuming each exchange in a swap has zero value at initiation.** Only the **total** is
> zero. Individual exchanges have positive and negative values that offset.

> **Trap 4 — Confusing price and value.** The swap **price is the fixed rate**, set at initiation and
> unchanged. The **value** starts at zero and moves with rates.

> **Trap 5 — Forgetting the floating leg resets to par.** This is what makes swap valuation
> tractable: only the fixed leg needs full discounting.

> **Trap 6 — Missing the equivalent bond position.** The fixed-rate payer is **long a floater and
> short a fixed-rate bond**. This framing makes the valuation direction obvious.

> **Trap 7 — Treating a CDS as a swap like the others.** A CDS is a **contingent claim** — it pays
> only on a credit event — while interest rate, currency, equity, and commodity swaps are **forward
> commitments**.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company with 50m of floating-rate debt enters a pay-fixed swap at 4.2%. Rates subsequently rise sharply. What has happened to the company's economics and to the swap's value?

<details><summary>Answer</summary>

**Economically: the hedge worked.** The company's floating-rate debt now costs more, but the swap pays it the higher floating rate while it pays the fixed 4.2%. The two floating legs offset, leaving the company with a **synthetic fixed cost of 4.2%** regardless of where rates went.

**The swap's value: positive to the company.** As the fixed-rate payer, it is now paying 4.2% when the market rate is higher — it locked in a below-market cost. If it wanted to unwind the swap today, the counterparty would have to pay it.

```
Value to the fixed payer ≈ Notional × (Current swap rate − 4.2%) × Σ(discount factors)
```

**The bond framing:** the company is effectively **long a floating-rate bond and short a fixed-rate bond**. When rates rise, the fixed-rate bond it is short **falls in value** — a gain to a short position. The floater stays near par.

**What to note:** the swap's positive value does **not** mean the company profited. It offset a loss on the debt. That is the nature of a hedge: gains on one leg, losses on the other, and a locked-in net cost. If rates had fallen, the swap's value would be negative and the debt cheaper — same locked-in result.

</details>

**2.** Explain precisely how a swap differs from a strip of forward rate agreements covering the same dates.

<details><summary>Answer</summary>

**The similarity:** each swap payment date is an agreement to exchange a known fixed amount for an unknown floating amount at a **predetermined** rate. That is exactly what an FRA does. A five-year annual swap covers the same economic ground as five FRAs.

**The difference — the rate structure:**

In a **strip of FRAs**, each contract is priced off its **own** forward rate for that period. With an upward-sloping curve, the 1×2 FRA is struck at a lower rate than the 4×5 FRA. **Each contract is individually worth zero** at initiation.

In a **swap**, a **single fixed rate** applies to every date. That rate is chosen so the **sum** of the present values of all exchanges is zero. Individually, the early exchanges have **positive** value to one party (the fixed rate exceeds the early forward rates) and the later ones have **negative** value — and they **offset**.

**So the swap's fixed rate is a discount-factor-weighted average of the forward rates.**

**The practical advantages of the swap form:**
- **One contract** and one master agreement rather than five
- **Netted payments** — only the difference changes hands on each date
- **Netted counterparty exposure** across all dates, rather than separate exposures per contract
- **Lower transaction costs** and a single rate to hedge and account for
- Simpler to unwind or novate as a package

</details>

**3.** Why is the floating leg of an interest rate swap worth par at each reset date, and why does that simplify valuation?

<details><summary>Answer</summary>

**Why it is worth par:** at each reset, the floating rate is set to the **current market rate** for the next period. The leg then promises to pay exactly the market rate on the notional for that period, plus (conceptually) the notional back at the end.

Discounting a cash flow at the very rate used to generate it returns the principal:

```
[Notional × (1 + r)] / (1 + r) = Notional
```

So immediately after each reset, the floating leg's present value is the **notional — par**. This is the same argument that keeps a floating-rate note priced near par (Fixed Income LM8).

**Why it simplifies valuation enormously:** you do not need to forecast future floating rates. The entire floating leg collapses to a known value — par at the next reset, discounted back to today.

Valuing the swap therefore reduces to:
```
Value to the fixed payer = PV(floating leg) − PV(fixed leg)
                         = [known, ≈ par] − [an ordinary fixed-rate bond valuation]
```

And **pricing** the swap at initiation reduces to finding the fixed rate at which a **par fixed-rate bond** has the same value — which is simply the **par rate** from the term structure (Fixed Income LM9).

**Between reset dates** the floating leg is worth slightly more or less than par, because the next payment is already fixed at the previous reset's rate while discounting is at the current rate. The adjustment is small and mechanical.

</details>

**4.** Why is the principal exchanged in a currency swap but not in an interest rate swap?

<details><summary>Answer</summary>

**Because netting is only possible when both legs are in the same currency.**

In an **interest rate swap**, both legs are denominated in the **same currency**. A payment of 2.1m fixed and a receipt of 2.4m floating can be netted to a single 0.3m transfer. Exchanging the notional would be pointless — each party would pay the other the identical amount in the identical currency, netting to zero. So the notional is purely a **reference amount** for calculating the interest.

In a **currency swap**, the legs are in **different currencies** — say EUR interest against USD interest. A EUR payment and a USD receipt **cannot be netted**; both must be made in full.

More fundamentally, the economic purpose differs. A currency swap is typically used to **convert a borrowing from one currency to another**. A company that has issued EUR debt but needs USD funding swaps into USD: it needs the **actual USD principal at the start** and must **repay EUR principal at the end**. The principal exchange is the point of the transaction, not an administrative detail.

**The consequence for risk:** because principal is exchanged, a currency swap carries **far greater counterparty credit exposure** than an interest rate swap of the same notional — the amount at risk includes the principal, not just accumulated interest differences.

</details>

---

## Done when

- [ ] I can state who pays what in a plain vanilla swap and who gains when rates rise
- [ ] I can explain precisely how a swap differs from a strip of forwards
- [ ] I can state the swap pricing formula and explain that the swap rate is the par rate
- [ ] I can explain why the floating leg is worth par at reset and why that simplifies valuation
- [ ] I can state the equivalent bond position for a fixed-rate payer
- [ ] I can determine the direction of a swap's value after a rate move
- [ ] I can explain why the principal is exchanged in a currency swap but not an interest rate swap
- [ ] I answered the self-check cold, several days after first study

---

← [LM06 Pricing and Valuation of Futures Contracts](lm-06-pricing-and-valuation-of-futures-contracts.md)  ·  [Topic index](README.md)  ·  [LM08 Pricing and Valuation of Options](lm-08-pricing-and-valuation-of-options.md) →
