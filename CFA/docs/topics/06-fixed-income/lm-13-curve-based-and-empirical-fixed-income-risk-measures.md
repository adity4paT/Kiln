# FI · LM13 — Curve-Based and Empirical Fixed-Income Risk Measures

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM11–LM12 (yield-based duration and convexity). |
| **Where it shows up** | 2 questions. Effective duration for option-embedded bonds and key rate duration are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain why effective duration and effective convexity are the most appropriate measures of interest rate risk for bonds with embedded options
- calculate the percentage price change of a bond for a specified change in benchmark yield, given the bond's effective duration and convexity
- define key rate duration and describe its use to measure price sensitivity of fixed-income instruments to benchmark yield curve changes
- describe the difference between empirical duration and analytical duration

---

## Core concepts

### Why yield-based duration fails for option-embedded bonds

Modified duration assumes the bond's **cash flows are fixed** — only the discount rate changes. For
a bond with an embedded option that assumption collapses:

- A **callable** bond will be redeemed early if yields fall enough. Its cash flows **depend on the
  yield path**.
- A **putable** bond may be sold back to the issuer if yields rise.
- A **mortgage-backed security's** principal repayments accelerate when yields fall, because
  homeowners refinance (LM19).

A measure that holds cash flows constant cannot describe an instrument whose cash flows are the
very thing that changes. **Modified duration is not just imprecise here — it is measuring the wrong
object.**

### Effective duration and effective convexity

The solution: shift the **entire benchmark yield curve** up and down, **re-model the cash flows**
under each scenario, and reprice.

```
EffDur = (PV− − PV+) / (2 × ΔCurve × PV0)

EffCon = (PV− + PV+ − 2 × PV0) / (ΔCurve² × PV0)
```

**Note the difference from the approximate formulas in LM11–LM12:** the denominator uses
**ΔCurve** — a shift in the **benchmark yield curve** — not ΔYield, a shift in the bond's own yield.
And critically, `PV−` and `PV+` are obtained from a **valuation model** (a binomial interest rate
tree, or a Monte Carlo simulation for MBS) that **re-determines the cash flows** at each new curve
level, rather than simply re-discounting fixed cash flows.

**The price change estimate is structurally identical to LM12:**

```
%ΔPrice ≈ (−EffDur × ΔCurve) + (½ × EffCon × ΔCurve²)
```

**What effective duration reveals:**

| Bond | Effective duration behaviour |
| --- | --- |
| **Callable** | **Lower** than the straight bond's, and it **falls** as yields fall (the call becomes more likely). **Effective convexity turns negative** at low yields |
| **Putable** | **Lower** than the straight bond's, and it **falls** as yields rise. Effective convexity is **more positive** |
| **MBS** | Low, and can even be **negative** in extreme refinancing conditions |
| **Option-free bond** | Effective duration ≈ modified duration |

> **For a straight bond, effective and modified duration are essentially the same** (the small
> difference arising from curve shape rather than a parallel yield shift). The distinction only
> matters when cash flows are contingent — which is exactly when it matters enormously.

### Key rate duration

**Portfolio duration assumes a parallel shift.** Yield curves do not move in parallel — the short
end is driven by monetary policy, the long end by growth and inflation expectations and term
premia. A portfolio duration-matched to a liability can still lose money on a **steepening** or a
**flattening**.

**Key rate duration (partial duration)** measures a bond's or portfolio's price sensitivity to a
change in **one specific maturity point** on the curve, holding all others constant.

```
KeyRateDur(t) = the % price change for a 1% change in the spot rate at maturity t,
                with all other spot rates unchanged
```

**The key property:**

```
Σ Key rate durations = Effective duration
```

The individual key rate durations sum to the total duration, so they **decompose** it by maturity.

**What it reveals:**

| Portfolio | Key rate duration profile |
| --- | --- |
| **Bullet** (all bonds at 10 years) | Almost all duration concentrated at the 10-year key rate |
| **Barbell** (2-year and 30-year) | Duration split between the 2-year and 30-year key rates, nothing at 10 |
| **Laddered** | Duration spread evenly across maturities |

Two portfolios with **identical total duration** can have completely different key rate profiles and
therefore behave completely differently when the curve **reshapes**. A steepening (long rates rising
relative to short) hurts the barbell far more than the bullet, despite matched durations.

> **This is what key rate duration exists to measure**, and it is why a liability-driven investor
> matches key rate durations, not just total duration.

### Empirical versus analytical duration

| | **Analytical (model) duration** | **Empirical duration** |
| --- | --- | --- |
| Derived from | A **valuation model** — the mathematics of discounting | **Regression** of observed bond price changes on observed benchmark yield changes |
| Assumes | A specified relationship between yields and prices; a parallel shift | Nothing — it measures what actually happened |
| Captures | Interest rate sensitivity in isolation | The **combined** effect of rates and correlated spread movements |
| Weakness | May not reflect actual market behaviour | Needs data; noisy; backward-looking; unstable |

**Why they differ — and this is the key insight:**

For **high-yield bonds**, the two can diverge sharply. Analytical duration might say 5.0. But when
benchmark yields **fall** because of a recession scare, **credit spreads widen simultaneously** — and
the widening partly or wholly offsets the benchmark rally. The bond's price barely moves, or even
falls.

**Empirical duration for high-yield bonds is therefore much LOWER than analytical duration**, and
can approach zero or turn negative for distressed credits, which behave more like equity than like
bonds.

> **The general principle:** the lower the credit quality, the more the bond's price is driven by
> **spread** rather than by the benchmark rate, and the less its analytical (rate) duration
> describes its actual behaviour. For a AAA government bond the two measures agree closely; for a
> CCC credit they describe different worlds.

This is also why empirical duration is **preferred in practice for portfolios containing credit
risk**, despite its statistical weaknesses — it captures how the instrument actually behaves rather
than how the model says it should.

---

## Formulas to know cold

```
EFFECTIVE DURATION AND CONVEXITY  (shift the BENCHMARK CURVE, re-model the CASH FLOWS)
  EffDur = (PV− − PV+) / (2 × ΔCurve × PV0)
  EffCon = (PV− + PV+ − 2 × PV0) / (ΔCurve² × PV0)

  PV− and PV+ come from a VALUATION MODEL (binomial tree, or Monte Carlo for MBS)
  that RE-DETERMINES the cash flows at each curve level.

  %ΔPrice ≈ (−EffDur × ΔCurve) + (½ × EffCon × ΔCurve²)

KEY RATE DURATION
  KeyRateDur(t) = % price change for a 1% change in the spot rate at maturity t,
                  ALL OTHER rates held constant
  Σ Key rate durations = Effective duration

  Decomposes total duration by maturity → reveals exposure to curve RESHAPING,
  which total duration cannot show.

EMPIRICAL vs ANALYTICAL DURATION
  ANALYTICAL = from a valuation model
  EMPIRICAL  = from REGRESSION of observed price changes on observed benchmark yield changes

  For HIGH-YIELD bonds, EMPIRICAL duration is much LOWER than analytical,
  because spreads WIDEN when benchmark yields FALL — the two effects offset.
```

---

## Exam traps

> **Trap 1 — Using modified duration for a callable bond or an MBS.** Its cash flows **change** with
> yields, so a fixed-cash-flow measure is measuring the wrong object. Use **effective** duration.

> **Trap 2 — The denominator in effective duration.** It is **ΔCurve** — a shift in the **benchmark
> curve** — not a shift in the bond's own yield.

> **Trap 3 — Forgetting that PV− and PV+ must be re-modelled.** The cash flows are re-determined at
> each curve level, not merely re-discounted. That is the entire point.

> **Trap 4 — Assuming key rate durations sum to something else.** They sum to **effective duration**.

> **Trap 5 — Treating two portfolios with equal duration as equivalent.** A bullet and a barbell with
> identical total duration have completely different **key rate profiles** and behave very
> differently when the curve reshapes.

> **Trap 6 — Getting the empirical/analytical relationship backwards for high yield.** **Empirical
> duration is LOWER** than analytical for high-yield bonds, because spreads widen as benchmark
> yields fall and the effects offset.

> **Trap 7 — Assuming effective and modified duration always differ.** For an **option-free** bond
> they are essentially the same. The distinction matters only with contingent cash flows.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A callable bond prices at 101.4. Under a 25bp parallel curve rise the model gives 100.2; under a 25bp fall, 102.1. Compute the effective duration and effective convexity.

<details><summary>Answer</summary>

**EffDur** = (PV− − PV+) / (2 × ΔCurve × PV0)
= (102.1 − 100.2) / (2 × 0.0025 × 101.4)
= 1.9 / 0.507
= **3.748**

**EffCon** = (PV− + PV+ − 2 × PV0) / (ΔCurve² × PV0)
= (102.1 + 100.2 − 2 × 101.4) / (0.0025² × 101.4)
= (202.3 − 202.8) / (0.00000625 × 101.4)
= −0.5 / 0.00063375
= **−789**

**Effective convexity is NEGATIVE** — the signature of a callable bond near or above its call price. Notice the asymmetry in the prices: the bond falls 1.2 when yields rise but gains only 0.7 when they fall. The call is capping the upside, which is exactly what negative convexity describes.

</details>

**2.** Why can modified duration not be used for a mortgage-backed security?

<details><summary>Answer</summary>

Because an MBS's **cash flows are contingent on the level of interest rates**, and modified duration assumes they are fixed.

When rates **fall**, homeowners **refinance** their mortgages. The MBS receives principal back early — exactly when the investor least wants it, because it must be reinvested at the new, lower rates. When rates **rise**, prepayments slow and the investor is locked into a below-market yield for longer. This is **extension risk** and **contraction risk** (LM19).

So the security's **cash flow schedule itself changes** as rates move. Modified duration, which re-discounts a **fixed** set of cash flows, is not merely imprecise — it is describing a different instrument.

**Effective duration** solves this by shifting the entire benchmark curve, running a **prepayment model** to re-determine the cash flows under each scenario, and repricing. For MBS this typically requires **Monte Carlo simulation** across many interest rate paths, because prepayment behaviour is path-dependent (it depends on the rate history, not just the current level — a 'burnout' effect where pools that have already refinanced heavily prepay less).

The result is low, sometimes negative, effective duration and strongly **negative effective convexity** at low yields.

</details>

**3.** Two portfolios both have effective duration of 7.0. Portfolio A's key rate durations are: 2-year 0.2, 5-year 0.4, 10-year 6.2, 30-year 0.2. Portfolio B's are: 2-year 3.0, 5-year 0.5, 10-year 0.5, 30-year 3.0. How will they behave differently?

<details><summary>Answer</summary>

Both sum to 7.0, so they respond **identically to a parallel shift**. They will respond very differently to a **reshaping**.

**Portfolio A is a bullet** — 6.2 of its 7.0 duration sits at the **10-year** point. It is almost purely a bet on 10-year rates.

**Portfolio B is a barbell** — duration split between the **2-year (3.0)** and **30-year (3.0)** points, with almost nothing in the middle.

**On a steepening** (short rates unchanged, long rates rise 50bp): B loses roughly 3.0 × 0.50% = **1.5%** from its 30-year exposure; A loses only 0.2 × 0.50% = **0.1%**. **B is hurt far more.**

**On a flattening** (long rates fall 50bp): B gains about 1.5%; A gains 0.1%. **B benefits far more.**

**On a curve twist** where 10-year rates rise while 2- and 30-year rates fall: A is hurt badly; B benefits. Total duration predicts nothing about this.

**The lesson:** total duration is a single number that hides the maturity distribution. A liability-driven investor must match **key rate durations**, not just total duration, or they remain exposed to every curve reshaping.

</details>

**4.** A high-yield bond has an analytical duration of 5.2 but an empirical duration of 1.8. Explain the gap and say which to use.

<details><summary>Answer</summary>

**Analytical duration (5.2)** is derived from the valuation model: it says that if the benchmark yield changes by 100bp with the credit spread held constant, the price moves 5.2%.

**Empirical duration (1.8)** comes from regressing this bond's **actual observed price changes** on **actual observed benchmark yield changes**. It measures what really happens.

**Why they diverge:** benchmark yields and credit spreads for high-yield bonds are **negatively correlated**. When Treasury yields fall — typically on recession fears or a flight to quality — **credit spreads widen** simultaneously, because the same recession that lowers government yields raises default expectations. The benchmark rally and the spread widening **largely offset**, so the high-yield bond's price barely moves.

The analytical measure holds the spread constant, which is a scenario that essentially never occurs for this asset class.

**Which to use: the empirical duration, for risk management and hedging.** It describes how the instrument actually behaves. If you hedged this bond using its 5.2 analytical duration, you would be **massively over-hedged** — the Treasury hedge would move three times as much as the bond it is supposed to protect.

**The general principle:** the lower the credit quality, the more the bond behaves like equity and the less its rate duration describes it. Distressed bonds can have empirical durations near zero or negative.

</details>

---

## Done when

- [ ] I can explain why yield-based duration is the wrong measure for option-embedded bonds
- [ ] I can compute effective duration and convexity and state what ΔCurve means
- [ ] I can describe how PV− and PV+ are obtained for a callable bond and for an MBS
- [ ] I can define key rate duration and state that the key rate durations sum to effective duration
- [ ] I can compare bullet and barbell key rate profiles and predict their behaviour on a steepening
- [ ] I can distinguish empirical from analytical duration and explain the high-yield gap
- [ ] I can say which duration measure to use for hedging a credit portfolio, and why
- [ ] I answered the self-check cold, several days after first study

---

← [LM12 Yield-Based Bond Convexity and Portfolio Properties](lm-12-yield-based-bond-convexity-and-portfolio-properties.md)  ·  [Topic index](README.md)  ·  [LM14 Credit Risk](lm-14-credit-risk.md) →
