# FI · LM12 — Yield-Based Bond Convexity and Portfolio Properties

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM11 (modified duration). |
| **Where it shows up** | 2 questions. The duration-plus-convexity price estimate is a near-certain calculation. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate and interpret convexity and describe the convexity adjustment
- calculate the percentage price change of a bond for a specified change in yield, given the bond's duration and convexity
- calculate portfolio duration and convexity and explain the limitations of these measures

---

## Core concepts

### What convexity is

**Convexity measures the curvature of the price-yield relationship** — the rate at which duration
itself changes as yields move.

Duration is the **slope** of the price-yield curve at a point. Convexity is its **curvature**. Since
the curve bends away from the tangent line in both directions, duration alone systematically
mis-estimates large moves.

```
Price
  │╲
  │ ╲ ← actual price-yield curve (CONVEX, bows toward the origin)
  │  ╲___
  │   ╲  ‾‾‾───___
  │────╲──────────── ← duration's tangent line (straight)
  │     ╲
  └──────────────────── Yield
        ↑ current yield

  Notice: the ACTUAL curve lies ABOVE the tangent line in BOTH directions.
```

> **The consequence — and why convexity is valuable:** the actual price is **above** the
> duration-predicted price whether yields rise **or** fall. When yields rise, the loss is **smaller**
> than duration predicts. When yields fall, the gain is **larger**. Convexity works in the
> bondholder's favour in **both** directions, which is why investors pay for it (accept a lower
> yield for a more convex bond).

### Computing convexity

**Approximate convexity** — the numerical method, which works for any instrument:

```
ApproxCon = (PV− + PV+ − 2 × PV0) / (ΔYield² × PV0)

where  PV−  = price if the yield FALLS by ΔYield
       PV+  = price if the yield RISES by ΔYield
       PV0  = the current price
```

Note the structure: the numerator measures how much the two repriced values **exceed** twice the
original — i.e. exactly the curvature the tangent line misses.

**Money convexity** for a position:

```
MoneyCon = Convexity × Full price of the position
```

### The duration-plus-convexity price estimate

This is the calculation the exam wants:

```
%ΔPrice ≈ (−ModDur × ΔYield)  +  (½ × Convexity × ΔYield²)
             └ duration term ┘      └ convexity adjustment ┘
```

In currency terms:

```
ΔPrice ≈ (−MoneyDur × ΔYield) + (½ × MoneyCon × ΔYield²)
```

> **The convexity term is always POSITIVE for an option-free bond**, because `ΔYield²` is positive
> regardless of the direction of the move and convexity is positive. It therefore **adds** to the
> price change whichever way yields go — reducing the estimated loss on a rise and increasing the
> estimated gain on a fall.

**Worked example.** ModDur = 7.2, Convexity = 68, yields rise 150bp.

```
Duration term    = −7.2 × 0.015              = −10.80%
Convexity adjust = 0.5 × 68 × (0.015)²       = 0.5 × 68 × 0.000225 = +0.765%
                                                ─────────
Estimated %ΔPrice                              = −10.04%
```

Duration alone predicted a 10.80% fall; the convexity adjustment reduces it to **10.04%**. For a
150bp move that 76bp difference is material — and it grows with the **square** of the yield change,
so for a 300bp move the adjustment would be four times as large.

### What determines convexity

| Feature | Effect on convexity |
| --- | --- |
| **Longer maturity** | **Higher** |
| **Lower coupon** | **Higher** |
| **Lower yield** | **Higher** |
| **More dispersed cash flows** | **Higher** |
| **Higher duration** | Generally higher (they move together) |

> **The dispersion principle:** for two bonds with the **same duration**, the one with **more
> dispersed cash flows** has **greater convexity**. A barbell portfolio (short and long bonds) has
> more convexity than a bullet portfolio (all concentrated at the middle maturity) with the same
> duration. This is the basis of barbell-versus-bullet strategy, and it is a favourite exam point.

**Negative convexity.** Bonds with embedded **call** options exhibit **negative convexity** at low
yields: as yields fall, the call becomes more likely to be exercised, so the price **stops rising** —
it is capped near the call price. The price-yield curve bends the **wrong way**.

```
Callable bond price
  │      ___________  ← price compression: capped by the call
  │     ╱
  │    ╱  ← NEGATIVE convexity region (low yields)
  │   ╱
  │  ╱    ← positive convexity resumes at higher yields
  └──────────────── Yield
```

Negative convexity is **bad for the investor**: the upside is capped while the downside is not.
**Mortgage-backed securities** exhibit it strongly because of prepayment behaviour (LM19) —
homeowners refinance when rates fall, returning principal exactly when it is least wanted.

**Putable bonds** have **greater** positive convexity than straight bonds, because the put supports
the price as yields rise.

### Portfolio duration and convexity

Both are **market-value-weighted averages**:

```
Portfolio ModDur = Σ wᵢ × ModDurᵢ
Portfolio Convexity = Σ wᵢ × Convexityᵢ
```

### The limitations — an explicit LOS

| Limitation | Detail |
| --- | --- |
| **Parallel shift assumption** | Both measures assume **all yields move by the same amount**. Real curve moves involve steepening, flattening, and twists — for which key rate durations are needed (LM13) |
| **Small-change accuracy** | Even with convexity, the estimate degrades for very large moves; higher-order terms are omitted |
| **Static** | Duration and convexity change as yields move and as time passes. A hedge set today needs rebalancing |
| **Yield-based measures fail for embedded options** | A callable bond's cash flows **change** with yields, so a yield-based duration is meaningless. **Effective** duration is required (LM13) |
| **Credit risk ignored** | Duration measures sensitivity to **benchmark yield** changes only. A spread widening is a separate risk |
| **Portfolio aggregation is an approximation** | The weighted-average calculation assumes a single yield change applies to every holding |

> **The most consequential limitation is the parallel shift assumption.** Yield curves rarely move in
> parallel — the short end is driven by policy, the long end by growth and inflation expectations
> and term premia. A portfolio duration-matched to a liability can still lose money on a steepening
> or flattening. This is precisely what **key rate durations** exist to measure.

---

## Formulas to know cold

```
APPROXIMATE CONVEXITY
  ApproxCon = (PV− + PV+ − 2 × PV0) / (ΔYield² × PV0)
    PV− = price if the yield FALLS;  PV+ = price if it RISES;  PV0 = current price

MONEY CONVEXITY
  MoneyCon = Convexity × Full price of the position

THE PRICE ESTIMATE — the calculation the exam wants
  %ΔPrice ≈ (−ModDur × ΔY) + (½ × Convexity × ΔY²)
  ΔPrice  ≈ (−MoneyDur × ΔY) + (½ × MoneyCon × ΔY²)

  The convexity term is ALWAYS POSITIVE for an option-free bond (ΔY² > 0),
  so it ADDS to the price change in BOTH directions.

PORTFOLIO MEASURES (market-value weights)
  Portfolio ModDur    = Σ wi × ModDuri
  Portfolio Convexity = Σ wi × Convexityi

CONVEXITY RISES WITH
  longer maturity · LOWER coupon · lower yield · MORE DISPERSED cash flows
  Same duration, more dispersion → MORE convexity (barbell > bullet)

NEGATIVE CONVEXITY
  CALLABLE bonds and MBS at LOW yields — price appreciation is capped. BAD for the investor.
  PUTABLE bonds have MORE positive convexity than straight bonds.
```

---

## Exam traps

> **Trap 1 — Forgetting the ½.** The convexity adjustment is `½ × Convexity × ΔY²`. Omitting the
> half doubles it.

> **Trap 2 — Squaring the yield change.** `ΔY²`, not `ΔY`. This is why the adjustment grows
> **quadratically** — four times larger for a doubled yield move.

> **Trap 3 — Sign of the convexity term.** It is **always positive** for an option-free bond,
> regardless of the direction of the yield move, because `ΔY²` is positive.

> **Trap 4 — Approximate convexity numerator.** `(PV− + PV+ − 2×PV0)` — the two repriced values are
> **added**, then twice the original is subtracted. (Contrast with duration, where they are
> **subtracted** from each other.)

> **Trap 5 — Believing convexity is always good.** **Negative convexity** — callable bonds and MBS
> at low yields — is **bad** for the investor: upside capped, downside not.

> **Trap 6 — Missing the dispersion principle.** For the **same duration**, more **dispersed** cash
> flows means **more convexity**. Barbell beats bullet on convexity.

> **Trap 7 — Applying yield-based duration to a callable bond.** Its cash flows **change** with
> yields. Use **effective** duration (LM13).

> **Trap 8 — Forgetting the parallel shift assumption.** Duration and convexity say nothing about
> steepening or flattening.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A bond has modified duration 9.1 and convexity 112. Estimate the percentage price change for (a) a 200bp rise in yield and (b) a 200bp fall.

<details><summary>Answer</summary>

**(a) Yields rise 200bp:**
```
Duration term    = −9.1 × 0.020            = −18.20%
Convexity adjust = 0.5 × 112 × (0.020)²  = 0.5 × 112 × 0.0004 = +2.24%
                                            ─────────
Estimated %ΔPrice                          = −15.96%
```

**(b) Yields fall 200bp:**
```
Duration term    = −9.1 × (−0.020)       = +18.20%
Convexity adjust = 0.5 × 112 × (0.020)²  = +2.24%    ← SAME sign, positive
                                            ─────────
Estimated %ΔPrice                          = +20.44%
```

**The asymmetry is the point:** the bond falls 15.96% on a 200bp rise but gains 20.44% on a 200bp fall. The convexity adjustment is **+2.24% in both cases**, because `ΔY²` is positive regardless of direction. This asymmetry is exactly why investors value convexity.

</details>

**2.** A bond is priced at 98.60. At a yield 50bp higher it prices at 94.80; at 50bp lower, 102.55. Compute the approximate modified duration and approximate convexity.

<details><summary>Answer</summary>

**ApproxModDur** = (PV− − PV+) / (2 × ΔY × PV0)
= (102.55 − 94.80) / (2 × 0.005 × 98.60)
= 7.75 / 0.986
= **7.860**

**ApproxCon** = (PV− + PV+ − 2 × PV0) / (ΔY² × PV0)
= (102.55 + 94.80 − 2 × 98.60) / (0.005² × 98.60)
= (197.35 − 197.20) / (0.000025 × 98.60)
= 0.15 / 0.002465
= **60.85**

Note the structural difference between the two numerators: duration **subtracts** the two repriced values from each other (measuring slope), while convexity **adds** them and subtracts twice the original (measuring curvature).

</details>

**3.** Explain why a callable bond exhibits negative convexity at low yields, and why that is bad for the investor.

<details><summary>Answer</summary>

As yields **fall**, an ordinary bond's price rises steadily and at an accelerating rate — positive convexity.

For a **callable** bond, falling yields make it increasingly attractive for the **issuer to call** and refinance more cheaply. As the call becomes more likely, the bond's price stops rising: it becomes **compressed toward the call price**, because no rational buyer pays much above the price at which the bond will be redeemed.

The price-yield curve therefore **flattens and then bends the wrong way** — the curvature turns **negative**.

**Why it is bad for the investor:**
- **Upside is capped.** The rally the investor should enjoy when yields fall does not arrive.
- **Downside is not capped.** If yields **rise**, the call becomes irrelevant and the bond falls like any other bond — full positive convexity resumes, in the losing direction.
- The investor faces **reinvestment risk** too: called at par, they must reinvest at the new, lower rates.

**The asymmetry — capped gains, uncapped losses — is why callable bonds must offer a higher yield** (LM7: `OAS = Z-spread − option cost`).

**Mortgage-backed securities** exhibit this strongly because homeowners prepay and refinance when rates fall (LM19), returning principal precisely when it is least wanted.

</details>

**4.** Two portfolios both have a modified duration of 6.0. Portfolio A holds only 6-year bonds. Portfolio B holds a mix of 1-year and 15-year bonds. Which has greater convexity, and does it matter?

<details><summary>Answer</summary>

**Portfolio B** (the **barbell**) has greater convexity.

**Why:** for a given duration, **more dispersed cash flows produce more convexity**. A **bullet** portfolio concentrates all cash flows near the duration point; a **barbell** spreads them to the extremes, and the curvature contributed by the long-dated bonds outweighs that of the short ones.

**Does it matter?** Yes, in two ways:

**(1) It is valuable in a large parallel move.** Both portfolios perform identically for small shifts, but for a **large** move B outperforms in **both** directions — smaller loss on a rise, larger gain on a fall. The market knows this, so B will typically offer a **lower yield**: the convexity is paid for.

**(2) It is exposed to non-parallel moves.** The barbell's performance depends on the **shape** of the curve, not just its level. A **flattening** (long rates falling relative to short) benefits the barbell; a **steepening** hurts it. The bullet is far less exposed to curve shape.

**So the choice is a view:** buy the barbell if you expect large moves or a flattening, and are willing to pay in yield for it. This is what key rate durations (LM13) measure.

</details>

**5.** State four limitations of duration and convexity as risk measures.

<details><summary>Answer</summary>

**(1) The parallel shift assumption.** Both assume **all yields move by the same amount**. Real curves steepen, flatten, and twist — the short end driven by policy, the long end by growth and inflation expectations. A duration-matched portfolio can still lose on a curve reshaping. **Key rate durations** (LM13) address this.

**(2) They fail for bonds with embedded options.** A callable bond's **cash flows change** with yields, so a yield-based duration is meaningless. **Effective duration**, which reprices under a benchmark curve shift, is required.

**(3) They are static.** Duration and convexity both change as yields move and as time passes. A hedge constructed today drifts out of alignment and needs **rebalancing**.

**(4) They measure only benchmark yield risk.** A **credit spread widening** moves the price without any change in the benchmark yield, and duration says nothing about it. Credit risk is a separate exposure requiring separate measurement.

Also: even with the convexity term, the estimate degrades for very large moves, since higher-order terms are omitted; and portfolio aggregation by weighted average is itself an approximation.

</details>

---

## Done when

- [ ] I can compute approximate convexity and distinguish its numerator from duration's
- [ ] I can apply the duration-plus-convexity price estimate with the ½ and the squared yield change
- [ ] I can explain why the convexity term is positive in both directions
- [ ] I can state what raises convexity, including the dispersion principle
- [ ] I can explain negative convexity in callable bonds and MBS and why it harms the investor
- [ ] I can compare barbell and bullet portfolios on convexity and curve-shape exposure
- [ ] I can state four limitations of duration and convexity, led by the parallel shift assumption
- [ ] I answered the self-check cold, several days after first study

---

← [LM11 Yield-Based Bond Duration Measures and Properties](lm-11-yield-based-bond-duration-measures-and-properties.md)  ·  [Topic index](README.md)  ·  [LM13 Curve-Based and Empirical Fixed-Income Risk Measures](lm-13-curve-based-and-empirical-fixed-income-risk-measures.md) →
