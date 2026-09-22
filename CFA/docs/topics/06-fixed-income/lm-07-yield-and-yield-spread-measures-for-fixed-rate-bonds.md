# FI · LM07 — Yield and Yield Spread Measures for Fixed-Rate Bonds

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM6 (bond pricing and YTM). |
| **Where it shows up** | 2 questions. Periodicity conversion and the spread definitions are the reliable targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate annual yield on a bond for varying compounding periods in a year
- compare, calculate, and interpret yield and yield spread measures for fixed-rate bonds

---

## Core concepts

### Periodicity and yield conversion

A stated annual yield means nothing without its **periodicity** — how many times a year it
compounds. The same economic yield has different stated values at different periodicities.

```
Converting a yield from periodicity m to periodicity n:

    (1 + APR_m / m)^m = (1 + APR_n / n)^n
```

**Worked example.** A bond yields 6.0% with **semiannual** compounding. What is the equivalent
**annual** (annual-pay) yield?

```
(1 + 0.06/2)² = (1 + APR_1/1)¹
(1.03)² = 1.0609
APR_1 = 6.09%
```

And the equivalent **quarterly** yield:

```
(1.03)² = (1 + APR_4/4)⁴
1.0609^(1/4) = 1 + APR_4/4
1.014889 = 1 + APR_4/4
APR_4 = 5.956%
```

> **The pattern: more frequent compounding gives a LOWER stated annual rate for the same economic
> return.** The stated rate falls as periodicity rises because compounding does more of the work.
>
> **Why this matters in practice:** a US bond quoted on a **semiannual bond basis** and a European
> bond quoted on an **annual basis** are not directly comparable. Convert to a common periodicity
> before comparing. This is the most common source of cross-market yield errors.

**Effective annual rate** is the periodicity-1 case:

```
EAR = (1 + APR_m / m)^m − 1
```

### Yield measures for fixed-rate bonds

| Measure | Definition | Note |
| --- | --- | --- |
| **Yield to maturity (YTM)** | The single discount rate equating the price to the present value of all cash flows, assuming the bond is **held to maturity** and **all coupons are reinvested at the YTM** | The standard measure, and the one whose assumptions are least realistic |
| **Current yield** | `Annual coupon / Price` | Ignores capital gain/loss and the time value of money entirely. Crude |
| **Yield to call (YTC)** | YTM computed to a call date at the call price | Relevant for a callable bond |
| **Yield to worst (YTW)** | The **lowest** of the YTM and all possible YTCs | The conservative measure quoted for callable bonds |
| **Street convention yield** | YTM assuming payments fall on scheduled dates, ignoring weekends and holidays | The market standard |
| **True yield** | Uses actual payment dates including business-day adjustments | Slightly lower than street convention |
| **Simple yield** | Coupon plus straight-line amortisation of any premium or discount, over price | Used in Japan |

**The three assumptions embedded in YTM** — each of which can fail:

1. The bond is **held to maturity**
2. All coupons are **reinvested at the YTM** — the **reinvestment assumption**, and the one that
   almost never holds
3. The issuer makes **all payments in full and on time** — no default

> **Trap:** YTM is a **promised** yield, not an expected one. For a bond with meaningful default
> risk, the expected return is materially **below** the YTM. Quoting a distressed bond's 22% YTM as
> if it were an expected return is a category error.

**Yield to call:** for a callable bond, compute the yield to each call date using that date's call
price as the redemption value, then take the **lowest** of all yields (including YTM) as the **yield
to worst**. A premium callable bond will usually have its YTW at the first call date; a deep
discount callable bond's YTW is usually the YTM.

### Yield spread measures

A spread is **compensation for the risks a benchmark government bond does not carry** — primarily
credit and liquidity.

| Spread | Measured over | Definition |
| --- | --- | --- |
| **Benchmark spread / G-spread** | A **government** bond yield | The yield difference over an interpolated government bond of the same maturity |
| **I-spread (interpolated spread)** | The **swap** curve | Yield minus the interpolated swap rate of matching maturity |
| **Z-spread (zero-volatility spread)** | The **government spot curve** | The **constant** spread added to **every spot rate** that makes the present value of the cash flows equal the price |
| **Option-adjusted spread (OAS)** | The government spot curve, **after removing option value** | `Z-spread − option cost` for a callable bond |

**How they differ, and why it matters:**

- **G-spread** is the simplest — one yield minus another. It ignores the shape of the yield curve.
- **Z-spread** accounts for the **whole term structure**: it applies a single spread to each spot
  rate rather than comparing two single-point yields. More accurate when the curve is steep.
- **OAS** removes the value of any embedded option, making bonds with different option features
  **directly comparable**:

```
For a CALLABLE bond (option benefits the issuer):
    OAS = Z-spread − Option cost      →  OAS < Z-spread

For a PUTABLE bond (option benefits the investor):
    OAS = Z-spread + Option value     →  OAS > Z-spread
```

> **OAS is the measure to use when comparing bonds with different optionality.** A callable bond's
> Z-spread looks attractively wide, but part of that width is compensation for having sold a call to
> the issuer — not for credit risk. The OAS strips that out, leaving the credit and liquidity
> compensation that is actually comparable across bonds.

**Decomposing a corporate bond yield:**

```
Corporate bond yield = Benchmark government yield + Spread

where the Spread compensates for:
    credit risk  +  liquidity risk  +  tax differences  +  optionality
```

**What moves spreads:**

| Driver | Effect on spreads |
| --- | --- |
| Deteriorating credit quality | **Wider** |
| Economic slowdown or recession | **Wider** |
| Flight to quality | **Wider** (and government yields fall simultaneously — QM LM1) |
| Falling market liquidity | **Wider** |
| Heavy new issuance supply | Wider |
| Strong demand for yield | Narrower |

> **Spread widening and government yields falling happen together in a crisis.** The corporate
> yield may rise while the government yield falls — a spread move far larger than either yield
> change alone. Do not assume the two move in the same direction.

---

## Formulas to know cold

```
PERIODICITY CONVERSION
  (1 + APR_m/m)^m = (1 + APR_n/n)^n
  EAR = (1 + APR_m/m)^m − 1
  MORE frequent compounding → LOWER stated annual rate for the same economic yield

YIELD MEASURES
  Current yield = Annual coupon / Price
  YTM  = the single rate equating price to PV of all cash flows
         ASSUMES: held to maturity · coupons reinvested AT the YTM · no default
  YTC  = yield computed to a call date, using that date's call price as redemption
  YTW  = the LOWEST of YTM and all YTCs

SPREADS
  G-spread  = bond yield − interpolated GOVERNMENT bond yield (same maturity)
  I-spread  = bond yield − interpolated SWAP rate
  Z-spread  = the CONSTANT spread added to EVERY SPOT RATE that makes PV = price
  OAS       = Z-spread adjusted for the embedded option

  CALLABLE:  OAS = Z-spread − Option cost      →  OAS < Z-spread
  PUTABLE:   OAS = Z-spread + Option value     →  OAS > Z-spread

  Use OAS to compare bonds with DIFFERENT optionality.
```

---

## Exam traps

> **Trap 1 — Comparing yields at different periodicities.** A semiannual-basis yield and an
> annual-basis yield are **not comparable**. Convert first. More frequent compounding gives a
> **lower** stated rate for the same economic return.

> **Trap 2 — Treating YTM as an expected return.** It is a **promised** yield, contingent on no
> default and on reinvestment at the YTM. For risky bonds the expected return is materially lower.

> **Trap 3 — Yield to worst direction.** It is the **lowest** of YTM and all YTCs — the conservative
> figure.

> **Trap 4 — OAS direction for callable bonds.** For a **callable** bond `OAS = Z-spread − option
> cost`, so **OAS is LESS than the Z-spread**. For a **putable** bond it is greater.

> **Trap 5 — G-spread vs Z-spread.** The **G-spread** compares two single-point yields; the
> **Z-spread** applies a constant spread to the **entire spot curve**. They differ more when the
> curve is steep.

> **Trap 6 — Current yield as a return measure.** It ignores capital gain or loss and the time value
> of money. For a deep discount bond it badly understates the return.

> **Trap 7 — Assuming spreads and government yields move together.** In a flight to quality,
> government yields **fall** while spreads **widen**.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A bond yields 5.4% on a semiannual bond basis. Convert it to an annual-pay basis and to a quarterly basis.

<details><summary>Answer</summary>

**Annual basis:**
(1 + 0.054/2)² = (1.027)² = 1.054729
Annual-pay yield = **5.4729%**

**Quarterly basis:**
(1.027)² = (1 + APR_4/4)⁴
1.054729^(1/4) = 1.0134111
APR_4/4 = 0.0134111 → APR_4 = **5.3645%**

Note the pattern: **quarterly (5.36%) < semiannual (5.40%) < annual (5.47%)**. More frequent compounding gives a *lower* stated rate for the identical economic return, because compounding does more of the work. This is why a US bond quoted semiannually and a European bond quoted annually cannot be compared without conversion.

</details>

**2.** A callable bond trades at 104. Its YTM is 3.8%. Yields to the first, second, and third call dates are 2.1%, 3.2%, and 3.6%. What is the yield to worst, and why is it at the first call?

<details><summary>Answer</summary>

**Yield to worst = 2.1%** — the lowest of all the yields computed, which here is the yield to the **first** call date.

**Why the first call:** the bond trades at a **premium** (104). If called early, the investor receives the call price — typically close to par, and certainly less than 104 — and loses the remaining premium quickly. The earlier the call, the less time to earn the above-market coupon that justifies paying 104, so the return is lowest at the first call date.

**The general rule:** for a **premium** callable bond, the YTW is usually at the **first call**. For a **deep discount** callable bond, the call is unlikely to be exercised (the issuer has no incentive to refinance cheap debt), so the YTW is usually the **YTM**.

YTW is quoted for callable bonds precisely because it is the conservative assumption — the investor should not plan on the highest of the possible outcomes.

</details>

**3.** A callable corporate bond has a Z-spread of 185bp and an OAS of 130bp. What is the option cost, and what does the comparison tell you?

<details><summary>Answer</summary>

Option cost = Z-spread − OAS = 185 − 130 = **55bp**.

**What it means:** 55 basis points of the bond's apparent 185bp spread is compensation for having **sold a call option to the issuer** — not for credit or liquidity risk. The investor bears the risk of having the bond redeemed when rates fall, and 55bp is what the market prices that at.

**The genuine credit and liquidity compensation is 130bp**, and that is the figure comparable to another bond's OAS.

**Why this matters:** a straight bond from the same issuer with a 150bp Z-spread looks *narrower* than this callable bond's 185bp — apparently worse value. But on an **OAS** basis the callable offers 130bp versus the straight bond's 150bp (a straight bond's OAS equals its Z-spread, since there is no option), so the **straight bond is actually the better credit value**. Comparing Z-spreads across bonds with different optionality produces exactly the wrong conclusion.

</details>

**4.** State the three assumptions embedded in yield to maturity and say which is most often violated.

<details><summary>Answer</summary>

**(1) The bond is held to maturity.** Violated whenever the investor sells early — realised return then depends on the price at sale, which depends on yields at that time.

**(2) All coupons are reinvested at the YTM.** This is the **reinvestment assumption**, and it is the one that **almost never holds**. Coupons are reinvested at whatever rates prevail when they are received, which will differ — often substantially — from today's YTM. For a long-dated, high-coupon bond, reinvestment income is a large share of total return, so the error can be material (LM10).

**(3) The issuer makes all payments in full and on time.** Violated on default. This is why YTM is a **promised** yield, not an expected one — for a bond with meaningful default risk, the probability-weighted expected return is well below the quoted YTM.

**The practical consequence:** quoting a distressed bond's 22% YTM as if it were an expected return is a category error. The expected return incorporates the probability of default and the expected recovery; the YTM assumes neither happens.

</details>

**5.** Why can the yield on a corporate bond rise while the government yield falls, and what is happening?

<details><summary>Answer</summary>

Because the two are driven by **different components** of the required return (QM LM1):

```
Corporate yield = Government (benchmark) yield + Spread
```

In a **flight to quality** — a crisis, a growth scare, a credit event — investors move out of risky assets and into government securities:

- **Demand for governments rises** → their prices rise → the **government yield falls**
- **Perceived credit and liquidity risk on corporates rises** → the **spread widens**, and by more than the government yield fell

The corporate yield, being the sum of the two, **rises** even as its benchmark component falls.

**The magnitude:** if the government yield falls 40bp while the spread widens 150bp, the corporate yield rises 110bp and the **spread move is 190bp** — far larger than either yield change alone. This is why credit spreads are the right lens for corporate bonds, not absolute yields, and why spread widening is most violent in exactly the periods when government yields are falling.

</details>

---

## Done when

- [ ] I can convert a yield between any two periodicities and state which direction the stated rate moves
- [ ] I can define YTM, current yield, YTC, YTW, and state which is quoted for callable bonds
- [ ] I can state the three YTM assumptions and explain why it is a promised, not expected, yield
- [ ] I can define G-spread, I-spread, Z-spread, and OAS and say what each is measured over
- [ ] I can compute option cost from Z-spread and OAS and get the direction right for callable and putable bonds
- [ ] I can explain why OAS is the correct comparison measure across different optionality
- [ ] I can explain why corporate yields rise while government yields fall in a flight to quality
- [ ] I answered the self-check cold, several days after first study

---

← [LM06 Fixed-Income Bond Valuation: Prices and Yields](lm-06-fixed-income-bond-valuation-prices-and-yields.md)  ·  [Topic index](README.md)  ·  [LM08 Yield and Yield Spread Measures for Floating-Rate Instruments](lm-08-yield-and-yield-spread-measures-for-floating-rate-instrument.md) →
