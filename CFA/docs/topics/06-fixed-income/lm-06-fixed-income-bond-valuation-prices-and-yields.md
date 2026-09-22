# FI · LM06 — Fixed-Income Bond Valuation: Prices and Yields

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | QM LM4 (discounting). BA II Plus TVM fluency is mandatory before starting. |
| **Where it shows up** | 2–3 questions. Bond pricing and YTM are certainties, and they recur throughout the topic. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate a bond's price given a yield-to-maturity on or between coupon dates
- identify the relationships among a bond's price, coupon rate, maturity, and yield-to-maturity
- describe matrix pricing

---

## Core concepts

### Pricing a bond on a coupon date

A bond is an annuity of coupons plus a lump sum:

```
PV = Σ [ Coupon / (1 + r)^t ]  +  Face value / (1 + r)^N
```

On the BA II Plus this is one TVM setup. **Periodicity is everything:**

| Annual terms | Calculator inputs, semiannual |
| --- | --- |
| 5% coupon, 7% yield, 8 years, 1,000 face | **N = 16, I/Y = 3.5, PMT = 25, FV = 1000** → CPT PV = **−878.67** |

**Halve the coupon and the yield; double the years.** And if you solve for `I/Y`, **double the
result** to get the annual yield.

**Using spot rates instead of a single yield:**

```
PV = C/(1+z1)¹ + C/(1+z2)² + ... + (C + F)/(1+zN)^N
```

Discounting each cash flow at its own **spot rate** is the theoretically correct approach (LM9). The
yield to maturity is the single rate that produces the same price — a weighted average of the spot
rates, dominated by the maturity where most of the value sits.

### The five price-yield relationships

Memorise these. They generate a large share of the qualitative questions in Fixed Income.

**1. Price and yield move inversely.** Always.

**2. The relationship is convex, not linear.** A given fall in yield raises the price by **more**
than the same rise in yield lowers it. This asymmetry is **convexity** (LM12), and it favours the
bondholder.

**3. Premium, par, discount:**

| Condition | Price |
| --- | --- |
| Coupon rate > YTM | **Premium** |
| Coupon rate = YTM | **Par** |
| Coupon rate < YTM | **Discount** |

**4. Pull to par.** As maturity approaches, the price converges to par — a premium bond's price
falls toward par, a discount bond's rises toward par, holding yield constant. The "return" on a
premium bond therefore includes a **capital loss** that offsets its high coupon, and vice versa.

**5. Interest rate sensitivity rises with maturity and falls with coupon:**

| Feature | Price sensitivity to a yield change |
| --- | --- |
| **Longer maturity** | **Greater** |
| **Shorter maturity** | Less |
| **Lower coupon** | **Greater** |
| **Higher coupon** | Less |
| **Lower yield level** | **Greater** |
| **Higher yield level** | Less |

> **The intuition behind the coupon effect:** a low-coupon bond returns more of its value at
> maturity, so its cash flows are **weighted toward the distant future** where discounting bites
> hardest. A zero-coupon bond has *all* its value at maturity and is therefore the **most
> interest-rate-sensitive** bond of a given maturity. This is the duration argument (LM10–LM11)
> stated before duration is formally introduced.

### Pricing between coupon dates

Between coupon dates, part of the next coupon has been "earned" by the seller. That portion is
**accrued interest**, and the buyer must pay it.

```
Accrued interest = Coupon × (Days since last coupon / Days in the coupon period)

Full price (dirty price) = Flat price (clean price) + Accrued interest
```

| Term | Meaning |
| --- | --- |
| **Flat (clean) price** | The **quoted** price. Excludes accrued interest |
| **Accrued interest** | The seller's share of the current coupon period |
| **Full (dirty, invoice) price** | What the buyer **actually pays** |

**Day-count conventions** determine how the fraction is computed:

| Convention | Used for |
| --- | --- |
| **Actual/actual** | **Government bonds** |
| **30/360** | **Corporate bonds** and most non-government issues; assumes 30-day months and a 360-day year |
| **Actual/360** | Money market instruments |

**Computing the full price directly:**

```
Full price = PV at the last coupon date × (1 + r)^(t/T)

where t/T is the fraction of the coupon period elapsed
```

Then subtract accrued interest to get the quoted flat price.

> **Why prices are quoted flat:** the full price jumps discontinuously downward on each coupon date
> as the accrued interest resets to zero. Quoting flat removes that sawtooth artefact, so the quoted
> price reflects only changes in the market's required yield. It makes price series comparable
> across time and across bonds with different coupon dates.

### Matrix pricing

**Matrix pricing estimates the price or yield of a bond that does not trade**, by interpolating from
comparable bonds that do.

**The process:**

1. Identify bonds with **similar credit quality** (same rating and sector) that **do** trade.
2. Find their yields at maturities **bracketing** the target bond's maturity.
3. **Interpolate linearly** between them to estimate the target's yield.
4. Discount the target's cash flows at that yield to get a price.

**Worked example.** A 4-year A-rated bond does not trade. Comparable A-rated bonds yield 3.80% at
3 years and 4.40% at 6 years.

```
Interpolating to 4 years:
  3.80% + [(4 − 3)/(6 − 3)] × (4.40% − 3.80%)
= 3.80% + (1/3) × 0.60%
= 3.80% + 0.20%
= 4.00%
```

**Uses:**

- Valuing **illiquid or infrequently traded** bonds — essential for portfolio marking, since most
  bonds do not trade on most days (LM3)
- Estimating the **required yield on a new issue** before it comes to market
- Providing prices for **index construction**, where thousands of constituents must be valued daily

**Limitations:** it assumes the comparables really are comparable — same credit quality, same
sector, same covenant strength, same optionality, same liquidity. Differences in any of these make
the interpolation unreliable, and the method cannot capture issue-specific features at all.

---

## Formulas to know cold

```
BOND PRICE ON A COUPON DATE
  PV = Σ C/(1+r)^t + F/(1+r)^N
  BA II Plus: N, I/Y, PMT, FV → CPT PV
  SEMIANNUAL: N × 2,  I/Y ÷ 2,  PMT ÷ 2.  A computed semiannual I/Y must be DOUBLED.

USING SPOT RATES
  PV = C/(1+z1)¹ + C/(1+z2)² + ... + (C+F)/(1+zN)^N

BETWEEN COUPON DATES
  Accrued interest = Coupon × (days since last coupon / days in the coupon period)
  Full (dirty) price = Flat (clean) price + Accrued interest
  Full price = PV(at last coupon date) × (1 + r)^(t/T)

  Day counts:  Actual/actual → GOVERNMENT bonds
               30/360        → CORPORATE bonds
               Actual/360    → money market

THE FIVE RELATIONSHIPS
  1. Price and yield move INVERSELY
  2. The relationship is CONVEX — a yield fall raises price more than an equal rise lowers it
  3. Coupon > YTM → premium;  = → par;  < → discount
  4. PULL TO PAR as maturity approaches
  5. Sensitivity RISES with maturity, FALLS with coupon, RISES as the yield level falls

MATRIX PRICING (linear interpolation)
  y_target = y_lower + [(M_target − M_lower)/(M_upper − M_lower)] × (y_upper − y_lower)
```

---

## Exam traps

> **Trap 1 — Periodicity.** A semiannual bond needs `N × 2`, `I/Y ÷ 2`, `PMT ÷ 2` — and a computed
> semiannual `I/Y` must be **doubled**. This single error accounts for a large share of Fixed Income
> mistakes.

> **Trap 2 — Flat vs full price.** The **quoted** price is **flat** (clean). The buyer **pays** the
> **full** (dirty) price, which includes accrued interest.

> **Trap 3 — Day-count convention.** **Actual/actual for governments; 30/360 for corporates.** Using
> the wrong one gives a plausible but wrong accrued interest figure.

> **Trap 4 — The coupon effect on sensitivity.** A **lower** coupon means **greater** price
> sensitivity. A zero-coupon bond is the most sensitive bond of a given maturity. Candidates
> frequently invert this.

> **Trap 5 — Forgetting pull to par.** A premium bond's price **falls** toward par over time even if
> yields never move. Its total return is the coupon **minus** that capital loss.

> **Trap 6 — Assuming the price-yield line is straight.** It is **convex**. Estimating a large yield
> move with duration alone overstates the price fall and understates the price rise (LM12).

> **Trap 7 — Matrix pricing comparability.** The method is only as good as the comparables. Different
> sector, optionality, or liquidity makes the interpolation unreliable.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A bond has a 4.5% annual coupon paid semiannually, 12 years to maturity, face 1,000, and a YTM of 6.2%. Compute its price and state whether it is at a premium or discount.

<details><summary>Answer</summary>

Semiannual inputs: N = 24, I/Y = 3.1, PMT = 22.50, FV = 1000.

CPT PV → **−855.94**, so the price is **855.94**.

**Discount** — the 4.5% coupon is below the 6.2% required yield, so the bond must sell below par for its total return to reach 6.2%. The investor earns 4.5% in coupons plus the accretion from 855.94 toward 1,000 at maturity.

</details>

**2.** A 6% semiannual corporate bond last paid a coupon 73 days ago; the coupon period is 180 days (30/360 basis). The flat price is quoted as 102.40. What does the buyer pay?

<details><summary>Answer</summary>

Semiannual coupon = 6%/2 = 3.00 per 100 of par.

Accrued interest = 3.00 × (73/180) = 3.00 × 0.40556 = **1.2167** per 100 of par.

**Full (dirty) price = 102.40 + 1.2167 = 103.62** per 100 of par.

On a 1,000 face bond the buyer pays **1,036.17**.

Note: 30/360 is the **corporate** convention. A government bond would use actual/actual, giving a slightly different accrued figure.

</details>

**3.** Two bonds have the same 10-year maturity and 5% yield. Bond A has a 2% coupon, Bond B has an 8% coupon. Which is more sensitive to a rate change, and why?

<details><summary>Answer</summary>

**Bond A** (the 2% coupon) is more sensitive.

**Why:** a low-coupon bond returns proportionally more of its total value at **maturity**, so its cash flows are weighted toward the **distant future** — where discounting has the largest effect. The high-coupon bond returns much of its value early, in coupons, which are discounted less severely and therefore move less when the discount rate changes.

Formally, Bond A has a longer **Macaulay duration** (LM10): the weighted average time to receipt of its cash flows is closer to 10 years, while Bond B's is meaningfully shorter.

**The limiting case:** a **zero-coupon** bond has *all* its value at maturity, so its Macaulay duration equals its maturity exactly, and it is the most interest-rate-sensitive bond of any given maturity.

</details>

**4.** A 5-year BBB-rated bond does not trade. Comparable BBB bonds yield 4.10% at 3 years and 4.90% at 7 years. Estimate the yield and state the method's limitations.

<details><summary>Answer</summary>

Linear interpolation:

y = 4.10% + [(5 − 3)/(7 − 3)] × (4.90% − 4.10%)
  = 4.10% + (2/4) × 0.80%
  = 4.10% + 0.40%
  = **4.50%**

**Limitations:**
- **Comparability.** The comparables must share credit quality, **sector**, **covenant strength**, **optionality** (a callable bond is not comparable to a bullet), and **liquidity**. Any difference makes the interpolation wrong in an unknown direction.
- **Linearity.** The yield curve is not straight. Interpolating linearly across a wide maturity gap, or across a curve with meaningful curvature, introduces error.
- **Issue-specific features** — a change-of-control put, a step-up coupon, structural subordination — cannot be captured at all.
- **Stale comparables.** If the 'trading' comparables last traded days ago, their yields are themselves estimates.

Despite this, matrix pricing is unavoidable: most bonds do not trade on most days, yet portfolios and indexes must be marked daily.

</details>

**5.** Why are bond prices quoted flat rather than full?

<details><summary>Answer</summary>

Because the **full price contains a sawtooth artefact** that has nothing to do with the market's view of the bond.

Accrued interest builds steadily through each coupon period and then **resets to zero** on the coupon date. So the full price rises gradually and then **drops discontinuously** by the coupon amount — every period, mechanically, regardless of whether anything has changed about the bond or about interest rates.

Quoting the **flat (clean) price** removes that mechanical component. What remains moves only when the market's **required yield** changes, which is the information a trader actually wants.

**Consequences:**
- Flat price series are **comparable over time** and across bonds with different coupon dates
- Price charts reflect yield changes rather than the coupon calendar
- But the buyer still **pays the full price** — the flat quote is a convention for comparison, not the settlement amount

</details>

---

## Done when

- [ ] I can price a coupon bond on the BA II Plus in under 30 seconds with correct periodicity
- [ ] I can solve for YTM and double it correctly for a semiannual bond
- [ ] I can state all five price-yield relationships from memory
- [ ] I can compute accrued interest under both 30/360 and actual/actual and reach the full price
- [ ] I can explain why a lower coupon means greater interest rate sensitivity
- [ ] I can perform matrix pricing by interpolation and state its limitations
- [ ] I can explain pull to par and why it affects a premium bond's total return
- [ ] I answered the self-check cold, several days after first study

---

← [LM05 Fixed-Income Markets for Government Issuers](lm-05-fixed-income-markets-for-government-issuers.md)  ·  [Topic index](README.md)  ·  [LM07 Yield and Yield Spread Measures for Fixed-Rate Bonds](lm-07-yield-and-yield-spread-measures-for-fixed-rate-bonds.md) →
