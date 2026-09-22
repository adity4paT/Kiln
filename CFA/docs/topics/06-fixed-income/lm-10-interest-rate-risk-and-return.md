# FI · LM10 — Interest Rate Risk and Return

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM6 (bond pricing), LM9 (term structure). |
| **Where it shows up** | 2 questions. The duration/horizon relationship is the conceptual centrepiece of Fixed Income. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate and interpret the sources of return from investing in a fixed-rate bond;
- describe the relationships among a bond's holding period return, its Macaulay duration, and the investment horizon;
- define, calculate, and interpret Macaulay duration.

---

## Core concepts

### The three sources of return

An investor in a fixed-rate bond earns:

| Source | Description |
| --- | --- |
| **1. Coupon payments** | The contractual interest received |
| **2. Reinvestment income** | Interest earned on the reinvested coupons |
| **3. Capital gain or loss** | The difference between the sale (or redemption) price and the purchase price |

**Total return** is the sum. And the critical observation:

> **Sources 2 and 3 move in OPPOSITE directions when interest rates change.**
>
> Rates **rise** → reinvestment income **rises**, capital value **falls**.
> Rates **fall** → reinvestment income **falls**, capital value **rises**.

This offsetting is the entire idea of the module. Whether a rate change helps or hurts depends
entirely on **how long you hold the bond**.

### Reinvestment risk versus price risk

| | **Reinvestment risk** | **Price (market) risk** |
| --- | --- | --- |
| Harmed by | **Falling** rates | **Rising** rates |
| Matters most for | **Long** holding periods; high-coupon bonds | **Short** holding periods |
| Eliminated by | Holding a zero-coupon bond (no coupons to reinvest) | Holding to maturity (redemption at par) |

**A bond held to maturity** has no price risk — it redeems at par — but full reinvestment risk.
**A bond sold immediately** has no reinvestment risk but full price risk. In between, the two offset.

### Macaulay duration

**Macaulay duration is the weighted average time to receipt of a bond's cash flows**, where each
cash flow's weight is its share of the bond's present value.

```
MacDur = Σ [ t × (PV of cash flow at t) ] / Total price
```

It is measured in **years** (or periods, then converted).

**Properties:**

| Feature | Effect on Macaulay duration |
| --- | --- |
| Longer maturity | **Higher** |
| **Lower coupon** | **Higher** |
| Lower yield | Higher |
| **Zero-coupon bond** | **MacDur = maturity, exactly** |
| Perpetuity | `MacDur = (1 + r)/r`, independent of the coupon |

> A zero-coupon bond's entire value arrives at maturity, so the weighted average time to receipt
> **is** the maturity. Every coupon-paying bond has a Macaulay duration **shorter** than its
> maturity, because some cash flows arrive earlier.

### The duration gap and immunisation — the central idea

```
Duration gap = Macaulay duration − Investment horizon
```

| Situation | Which risk dominates | Effect of a **rise** in rates |
| --- | --- | --- |
| **MacDur > horizon** (positive gap) | **Price risk** | Investor is **worse off** — the capital loss exceeds the reinvestment gain |
| **MacDur = horizon** (zero gap) | Balanced | Investor is **immunised** — the two effects offset |
| **MacDur < horizon** (negative gap) | **Reinvestment risk** | Investor is **better off** — the reinvestment gain exceeds the capital loss |

> **This is the most important single relationship in Fixed Income.** When the **Macaulay duration
> equals the investment horizon**, the loss in market value from a rate rise is exactly offset by
> the gain in reinvestment income, and the investor's realised return is locked in regardless of
> which way rates move. That is **immunisation**.
>
> Memorise the direction: **MacDur > horizon → price risk dominates → rising rates hurt.**

**Worked intuition.** An investor with a 6-year horizon holds a bond with Macaulay duration of 9.
Rates rise 100bp. The bond's price falls substantially, and at the 6-year mark the investor must
sell at that depressed price — a loss they have not had enough time to recoup through higher
reinvestment income. Price risk dominated. Had their horizon been 12 years, the extra reinvestment
income over those years would have more than compensated.

### The relationship to holding period return

```
Horizon yield (realised return) = the IRR of the actual cash flows received,
                                  including reinvestment at the rates that actually prevailed
```

If rates never change, the horizon yield equals the original YTM — which is exactly what the YTM's
reinvestment assumption promises (LM7).

If rates change:

- **Horizon shorter than MacDur** → rate rise reduces the realised return
- **Horizon equals MacDur** → realised return is approximately unchanged (immunised)
- **Horizon longer than MacDur** → rate rise **increases** the realised return

### Carry and rolldown

Two further components of return worth knowing:

- **Carry** — the coupon income earned net of any financing cost, if the position is funded.
- **Rolldown return** — with an **upward-sloping** curve, a bond's yield falls as it ages toward
  shorter maturities, so its price rises even if the curve does not move at all. "Rolling down the
  curve" is a real source of return, and it is largest where the curve is steepest.

> Rolldown is why a steep curve makes owning intermediate bonds attractive: you earn the coupon
> **and** a price gain simply from the passage of time, provided the curve holds its shape.

---

## Formulas to know cold

```
THREE SOURCES OF RETURN
  1. Coupon payments
  2. Reinvestment income        ← helped by RISING rates
  3. Capital gain or loss       ← helped by FALLING rates
  Sources 2 and 3 move in OPPOSITE directions. That offsetting is the whole module.

MACAULAY DURATION
  MacDur = Σ [ t × PV(CFt) ] / Price
         = the weighted average time to receipt of the cash flows, in YEARS

  Zero-coupon bond:  MacDur = maturity, EXACTLY
  Perpetuity:        MacDur = (1 + r)/r
  Longer maturity → higher.  LOWER COUPON → HIGHER.  Lower yield → higher.

DURATION GAP
  Duration gap = Macaulay duration − Investment horizon

  MacDur > horizon  →  PRICE risk dominates        →  rising rates HURT
  MacDur = horizon  →  IMMUNISED                   →  offsetting; return locked in
  MacDur < horizon  →  REINVESTMENT risk dominates →  rising rates HELP

ROLLDOWN
  With an upward-sloping curve, a bond's yield falls as it ages → price rises with no curve move.
```

---

## Exam traps

> **Trap 1 — The duration gap direction.** **MacDur > horizon → price risk dominates → a rate rise
> hurts.** This is the most important relationship in the topic and the one most often inverted.

> **Trap 2 — Confusing Macaulay with modified duration.** **Macaulay is in years** — a weighted
> average time. **Modified duration** is a price sensitivity, `MacDur/(1+r)` (LM11). Different
> objects with different units.

> **Trap 3 — Assuming a rate rise is always bad for a bondholder.** For a **long** holding period
> relative to duration, a rate rise **increases** the realised return through higher reinvestment
> income.

> **Trap 4 — Forgetting that a zero-coupon bond's MacDur equals its maturity.** It has no
> reinvestment risk at all, which makes it the natural immunisation instrument for a single
> liability.

> **Trap 5 — Ignoring reinvestment income's size.** For a long-dated, high-coupon bond held to
> maturity, reinvestment income can exceed the coupons themselves. It is not a rounding item.

> **Trap 6 — Thinking holding to maturity eliminates all risk.** It eliminates **price** risk. Full
> **reinvestment** risk remains, and for a long bond that is the dominant uncertainty.

> **Trap 7 — Overlooking rolldown.** With a steep curve, a bond gains value simply by aging, with no
> change in the curve. This is a real return component, not an artefact.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** An investor with a 5-year horizon holds a bond with a Macaulay duration of 5.0. Rates rise 150bp immediately. What happens to the realised return?

<details><summary>Answer</summary>

**Approximately nothing — the investor is immunised.**

With **Macaulay duration equal to the investment horizon**, the two rate effects offset:
- The bond's **price falls** immediately, which would reduce the sale proceeds at year 5
- But all coupons are now **reinvested at the higher rate**, generating more reinvestment income over the five years

At a duration gap of zero, these two effects are approximately **equal and opposite**, so the realised return over the horizon is close to the original YTM regardless of the rate move.

**Caveats worth stating:** the offset is exact only for a small, **parallel, immediate** shift. Non-parallel curve moves, or rate changes occurring later in the horizon, leave residual risk. And as time passes the bond's duration falls faster than the remaining horizon in some cases, so an immunised portfolio must be **rebalanced** to maintain the match.

</details>

**2.** A bond has a Macaulay duration of 3.2 and the investor's horizon is 8 years. Rates fall sharply. Is the investor better or worse off?

<details><summary>Answer</summary>

**Worse off.**

The duration gap is `3.2 − 8 = −4.8`, i.e. **MacDur < horizon**, so **reinvestment risk dominates**.

The investor will hold well beyond the bond's duration, so most of their return comes from **reinvesting** the coupons (and the principal, when the bond matures at year 3.2-ish and must be rolled into something else). With rates now lower, all that reinvestment happens at **worse rates** for the remaining years.

The immediate **capital gain** from the rate fall is real but small relative to the bond's short duration, and it is far outweighed by five-plus years of diminished reinvestment income.

**The general rule: a long horizon relative to duration means you are effectively a future lender, and falling rates hurt future lenders.**

</details>

**3.** Compute the Macaulay duration of a 3-year 6% annual-coupon bond with a yield of 6% and face value 100.

<details><summary>Answer</summary>

At a 6% yield with a 6% coupon, the bond prices at **par = 100**.

```
t    CF     PV = CF/(1.06)^t    Weight = PV/100    t × Weight
1    6      5.6604              0.056604           0.056604
2    6      5.3400              0.053400           0.106800
3   106    89.0000              0.890000           2.670000
           ------                                  --------
           100.0000                                2.833404
```

**Macaulay duration = 2.83 years.**

Note it is **less than the 3-year maturity**, because some cash flows (the year 1 and 2 coupons) arrive earlier. A 3-year **zero-coupon** bond would have a Macaulay duration of exactly 3.00 and would be more interest-rate-sensitive.

</details>

**4.** Why does holding a bond to maturity not eliminate all risk?

<details><summary>Answer</summary>

It eliminates **price risk** — the bond redeems at par regardless of where rates have gone, so the investor cannot be forced to sell at a depressed price.

It does **not** eliminate **reinvestment risk**. Every coupon received must be reinvested at whatever rate prevails when it arrives, and those rates are unknown at purchase. The YTM quoted at purchase **assumes all coupons are reinvested at the YTM** (LM7) — an assumption that essentially never holds.

**How large is this?** For a long-dated, high-coupon bond, reinvestment income can exceed the sum of the coupons themselves over a 20- or 30-year life. A 30-year 7% bond held to maturity derives the majority of its total return from reinvestment, not from the coupons directly. A prolonged period of low rates therefore produces a realised return well **below** the original YTM even with no default and no sale.

**The only way to eliminate reinvestment risk entirely** is to hold a **zero-coupon** bond to maturity — there are no coupons to reinvest, so the promised yield is the realised yield with certainty (absent default).

</details>

**5.** What is rolldown return, and when is it largest?

<details><summary>Answer</summary>

**Rolldown return** is the price gain a bond earns simply from **aging**, when the yield curve is upward sloping and does not move.

As time passes, a 5-year bond becomes a 4-year bond. On an upward-sloping curve, the 4-year yield is **lower** than the 5-year yield, so the bond is now priced at a lower yield — and a lower yield means a **higher price**. The investor gains without any change in the curve at all.

**It is largest where the curve is steepest** — typically at the shorter end in a normal environment. A steep segment between 2 and 5 years means a 5-year bond rolls down a large yield decline each year; a flat segment between 20 and 30 years offers essentially no rolldown.

**Practical significance:** rolldown is a genuine, forecastable component of expected return that the yield alone does not show. Two bonds with identical yields can have very different expected returns if one sits on a steep part of the curve and the other on a flat part. It is also why 'riding the yield curve' — buying intermediate bonds and selling them before maturity — is a standard strategy when the curve is steep and expected to stay so.

</details>

---

## Done when

- [ ] I can name the three sources of return and explain why two of them offset
- [ ] I can define Macaulay duration precisely and compute it for a short bond by hand
- [ ] I can state that a zero-coupon bond's MacDur equals its maturity and explain why
- [ ] I can state the duration gap relationship in all three cases with the correct direction
- [ ] I can explain immunisation and what makes the offset imperfect in practice
- [ ] I can explain why holding to maturity leaves reinvestment risk
- [ ] I can define rolldown return and say where on the curve it is largest
- [ ] I answered the self-check cold, several days after first study

---

← [LM09 The Term Structure of Interest Rates: Spot, Par, and Forward Curves](lm-09-the-term-structure-of-interest-rates-spot-par-and-forward-cu.md)  ·  [Topic index](README.md)  ·  [LM11 Yield-Based Bond Duration Measures and Properties](lm-11-yield-based-bond-duration-measures-and-properties.md) →
