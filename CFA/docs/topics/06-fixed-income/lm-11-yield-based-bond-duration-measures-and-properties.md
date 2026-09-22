# FI · LM11 — Yield-Based Bond Duration Measures and Properties

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM10 (Macaulay duration). |
| **Where it shows up** | 2–3 questions. Modified duration and PVBP are among the most reliable calculations on the exam. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- define, calculate, and interpret modified duration, money duration, and the price value of a basis point (PVBP)
- explain how a bond's maturity, coupon, and yield level affect its interest rate risk

---

## Core concepts

### From Macaulay to modified duration

**Macaulay duration** is a time measure. **Modified duration** converts it into a **price
sensitivity**:

```
ModDur = MacDur / (1 + r)

where r is the yield per period
```

**Interpretation:** modified duration is the **approximate percentage price change for a 1
percentage point (100bp) change in yield**.

```
%ΔPrice ≈ −ModDur × ΔYield
```

The minus sign captures the inverse relationship. A bond with ModDur of 6.5 falls approximately
6.5% in price if yields rise 100bp.

> **Units matter.** If the yield is semiannual, `MacDur/(1 + r/2)` gives a **semiannual** modified
> duration — divide by 2 (or work in annual terms throughout) to get the annual figure. Getting this
> wrong doubles or halves the answer.

**Approximate modified duration** — when you cannot compute Macaulay duration directly, or for bonds
with embedded options:

```
ApproxModDur = (PV− − PV+) / (2 × ΔYield × PV0)

where  PV−  = price if the yield FALLS by ΔYield
       PV+  = price if the yield RISES by ΔYield
       PV0  = the current price
```

This is a numerical derivative — reprice the bond at a slightly higher and a slightly lower yield,
and measure the slope. It works for **any** instrument, including callable bonds, which is why it
becomes the basis for **effective duration** (LM13).

### Money duration and PVBP

**Money duration (dollar duration)** expresses sensitivity in **currency terms** rather than
percentage terms:

```
MoneyDur = ModDur × Full price of the bond position

ΔPrice ≈ −MoneyDur × ΔYield
```

**Price value of a basis point (PVBP)** is the money change for a **one basis point** move:

```
PVBP = MoneyDur × 0.0001

or directly:  PVBP = (PV− − PV+) / 2   using a 1bp shift up and down
```

> **Why practitioners use money duration and PVBP rather than modified duration:** a portfolio
> manager hedging needs to know **how many currency units** are at risk, not a percentage. PVBP is
> the standard risk unit on a trading desk — "this position is 40,000 a basis point" is immediately
> actionable, while "this position has a modified duration of 6.2" requires a further calculation.

**Portfolio duration** is the **weighted average** of the component durations, using **market value
weights**:

```
Portfolio ModDur = Σ wᵢ × ModDurᵢ         where wᵢ = market value weight
```

This is an approximation that assumes a **parallel shift** in the yield curve — all yields move by
the same amount. It is the weakness of the measure, addressed by key rate durations in LM13.

### What determines interest rate risk

| Feature | Effect on duration and price sensitivity | Why |
| --- | --- | --- |
| **Longer maturity** | **Higher** | Cash flows arrive further out, where discounting bites hardest |
| **Lower coupon** | **Higher** | Less value returned early; more weight at maturity |
| **Lower yield level** | **Higher** | At low yields the price-yield curve is steeper |
| **Zero coupon** | **MacDur = maturity** — the maximum for that maturity | All value at the end |
| **Embedded call** | **Lower** than the straight bond | The call caps price appreciation as yields fall |
| **Embedded put** | **Lower** than the straight bond | The put supports the price as yields rise |
| **Floating rate** | **Very low** — approximately the time to the next reset | The coupon resets to the market rate |

> **A partial exception on maturity:** for a **deep discount** bond, duration can *fall* as maturity
> extends beyond a certain very long point, because the enormous weight on the final payment is so
> heavily discounted. This is a curiosity rather than an exam staple, but the general rule — longer
> maturity means higher duration — holds for all normal cases.

**The coupon intuition, restated:** duration is a weighted average time to cash flow receipt. A high
coupon returns much of the bond's value **early**, pulling the average time down. A zero coupon
returns everything at the end, so the average time equals the maturity — the maximum possible.

### Using duration

**Estimating a price change:**

```
%ΔPrice ≈ −ModDur × ΔYield                    (percentage)
ΔPrice  ≈ −MoneyDur × ΔYield                  (currency)
ΔPrice  ≈ −PVBP × (basis points of yield change)
```

**Hedging:** to hedge a position, take an offsetting position with equal and opposite money
duration. The number of hedging instruments required:

```
Number of hedge instruments = − (MoneyDur of the position) / (MoneyDur of one hedge instrument)
```

**The limitation, which LM12 addresses:** duration is a **linear** approximation to a **convex**
relationship. It is accurate for small yield changes and progressively **less** accurate for larger
ones — and it errs in a consistent direction: it **overestimates the price fall** when yields rise
and **underestimates the price rise** when yields fall. That systematic error is **convexity**, and
correcting for it is the subject of the next module.

---

## Formulas to know cold

```
MODIFIED DURATION
  ModDur = MacDur / (1 + r)          r = yield PER PERIOD
  %ΔPrice ≈ −ModDur × ΔYield

APPROXIMATE MODIFIED DURATION (works for ANY instrument, incl. embedded options)
  ApproxModDur = (PV− − PV+) / (2 × ΔYield × PV0)
    PV− = price if yield FALLS;  PV+ = price if yield RISES;  PV0 = current price

MONEY DURATION AND PVBP
  MoneyDur = ModDur × Full price of the position
  ΔPrice ≈ −MoneyDur × ΔYield
  PVBP = MoneyDur × 0.0001
       = (PV− − PV+) / 2   using a 1bp shift each way

PORTFOLIO DURATION
  Portfolio ModDur = Σ wi × ModDuri     (MARKET VALUE weights)
  Assumes a PARALLEL shift in the yield curve.

HEDGING
  Number of hedge instruments = − MoneyDur(position) / MoneyDur(one hedge instrument)

INTEREST RATE RISK RISES WITH
  longer maturity · LOWER coupon · lower yield level
  Zero coupon = maximum duration for its maturity (MacDur = maturity)
  Call, put, and floating-rate features all REDUCE duration
```

---

## Exam traps

> **Trap 1 — Macaulay vs modified duration.** **Macaulay is in years** (a weighted average time);
> **modified is a percentage price sensitivity**. `ModDur = MacDur/(1+r)`.

> **Trap 2 — Periodicity in the conversion.** For a semiannual bond, `r` is the **semiannual** yield
> and the result is a semiannual duration. Convert to annual terms consistently or the answer is out
> by a factor of two.

> **Trap 3 — The sign.** `%ΔPrice ≈ −ModDur × ΔYield`. A **rise** in yield gives a **negative** price
> change. Dropping the minus sign is a standard error.

> **Trap 4 — Approximate duration's numerator order.** `(PV− − PV+)`, with the **lower-yield price
> first**. Reversing it gives a negative duration.

> **Trap 5 — Portfolio duration weights.** Use **market value** weights, not par value weights and
> not equal weights.

> **Trap 6 — Assuming duration is accurate for large moves.** It is a **linear** approximation to a
> **convex** curve. It **overestimates the price fall** on a yield rise and **underestimates the
> price rise** on a yield fall (LM12).

> **Trap 7 — The coupon direction.** A **lower** coupon means **higher** duration and **greater**
> sensitivity. Frequently inverted.

> **Trap 8 — PVBP scaling.** PVBP uses **one** basis point, i.e. `MoneyDur × 0.0001`. Using 0.01
> gives the value for 100bp.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A bond has a Macaulay duration of 7.4 years and a yield of 5.6% (annual). Compute its modified duration and estimate the price change for a 60bp rise in yield.

<details><summary>Answer</summary>

ModDur = MacDur / (1 + r) = 7.4 / 1.056 = **7.008**

%ΔPrice ≈ −ModDur × ΔYield = −7.008 × 0.0060 = **−4.205%**

The bond falls approximately **4.2%** in price.

Note this is an **approximation**. Because the price-yield relationship is convex, the actual fall will be slightly **less** than 4.205% — duration overestimates the loss on a yield rise. LM12 adds the convexity correction.

</details>

**2.** A 1,000,000 par position in a bond priced at 96.4 has a modified duration of 5.8. Compute the money duration and PVBP.

<details><summary>Answer</summary>

Full market value of the position = 1,000,000 × 0.964 = **964,000**

**Money duration** = 5.8 × 964,000 = **5,591,200**

**PVBP** = 5,591,200 × 0.0001 = **559.12**

Interpretation: for every **one basis point** move in yield, this position gains or loses about **559**. A 25bp rate rise would cost roughly 25 × 559 = **13,978**.

On a trading desk this is the standard risk unit — 'the position is 559 a basis point' tells you immediately how much a rate move costs, without further calculation.

</details>

**3.** A bond is priced at 101.20. If its yield rises 25bp the price falls to 100.05; if the yield falls 25bp the price rises to 102.38. Compute the approximate modified duration.

<details><summary>Answer</summary>

ApproxModDur = (PV− − PV+) / (2 × ΔYield × PV0)
             = (102.38 − 100.05) / (2 × 0.0025 × 101.20)
             = 2.33 / (0.506)
             = **4.605**

**Note the ordering:** `PV−` is the price when the yield **falls** (102.38, the higher price), and it comes **first** in the numerator. Reversing them gives −4.605, which is wrong.

This method works for **any** instrument, including bonds with embedded options where an analytical duration formula does not apply — which is exactly why it becomes **effective duration** in LM13.

</details>

**4.** Rank these bonds by interest rate sensitivity, highest first: (a) 10-year 2% coupon, (b) 10-year 8% coupon, (c) 10-year zero coupon, (d) 3-year 2% coupon.

<details><summary>Answer</summary>

**(c) 10-year zero coupon** — Macaulay duration = 10.0 exactly, the maximum possible for a 10-year maturity. All value arrives at maturity.

**(a) 10-year 2% coupon** — long maturity and a low coupon; duration close to but below 10.

**(b) 10-year 8% coupon** — same maturity, but the high coupon returns much value early, pulling the weighted average time down substantially.

**(d) 3-year 2% coupon** — the short maturity dominates. Low coupon raises its duration relative to a 3-year high-coupon bond, but it cannot compete with any 10-year bond.

**Order: c > a > b > d.**

The two principles: **maturity dominates**, and within a maturity, **lower coupon means higher duration**.

</details>

**5.** Why does duration overestimate the price fall when yields rise?

<details><summary>Answer</summary>

Because duration is a **linear** approximation to a **convex** relationship.

The price-yield curve is not a straight line — it is **curved**, bowing toward the origin. Duration measures the **slope of the tangent** at the current yield. For small moves the tangent and the curve nearly coincide, so duration is accurate.

For **larger** moves, the actual curve **pulls away from the tangent line — upward, in both directions**:
- When yields **rise**, the actual price stays **above** the tangent line → the real fall is **smaller** than duration predicts → duration **overestimates the loss**
- When yields **fall**, the actual price rises **above** the tangent line → the real gain is **larger** than duration predicts → duration **underestimates the gain**

**The error is systematically in the bondholder's favour in both directions** — which is why **convexity is a valuable property**, and why investors pay for it. LM12 quantifies the correction:

```
%ΔPrice ≈ −ModDur × ΔY + ½ × Convexity × (ΔY)²
```

The convexity term is always **positive** for an option-free bond (since `(ΔY)²` is positive), so it adds to the price change in both directions.

</details>

---

## Done when

- [ ] I can convert Macaulay to modified duration with correct periodicity handling
- [ ] I can estimate a percentage price change from modified duration with the correct sign
- [ ] I can compute approximate modified duration from three prices, in the right order
- [ ] I can compute money duration and PVBP and explain why traders use them
- [ ] I can compute portfolio duration with market value weights and state the parallel-shift assumption
- [ ] I can rank bonds by interest rate sensitivity using the maturity and coupon effects
- [ ] I can explain why duration overestimates the loss on a yield rise
- [ ] I answered the self-check cold, several days after first study

---

← [LM10 Interest Rate Risk and Return](lm-10-interest-rate-risk-and-return.md)  ·  [Topic index](README.md)  ·  [LM12 Yield-Based Bond Convexity and Portfolio Properties](lm-12-yield-based-bond-convexity-and-portfolio-properties.md) →
