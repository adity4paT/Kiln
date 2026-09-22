# QM · LM04 — The Time Value of Money in Finance

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 10 |
| **Prerequisites** | LM2 (compounding), and fluency with the BA II Plus TVM keys. |
| **Where it shows up** | 2–3 questions, and this module is load-bearing for Equity LM6, all of Fixed Income, and Derivatives. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate and interpret the present value of fixed-income and equity instruments based on expected future cash flows
- calculate and interpret the implied return of fixed-income instruments and required return and implied growth of equity instruments given their present value and cash flows
- explain the cash flow additivity principle and its importance for the condition of no arbitrage, and explain its use in calculating implied forward interest rates, forward exchange rates, and option values

---

## Core concepts

### The single most important module in Quantitative Methods

Everything in Fixed Income is this module applied to bonds. Everything in Equity valuation is this
module applied to dividends and free cash flow. Derivatives pricing is this module plus no-arbitrage.
Budget the full 10 hours and do not move on until the calculator work is automatic.

### The core relationship

```
PV = Σ  CFt / (1 + r)^t
```

A value today is the sum of future cash flows, each discounted by the required return over the time
until it arrives. Three variables, and any question gives you two of them:

- Given cash flows and **r**, solve for **PV** → *valuation*
- Given cash flows and **PV**, solve for **r** → *implied return* (YTM, IRR, required return)
- Given **PV**, **r**, and some cash flows, solve for a growth rate → *implied growth*

### Valuing fixed-income instruments

**A coupon bond** is an annuity of coupons plus a lump sum at maturity:

```
PV = Σ [Coupon / (1 + r)^t]  +  Face value / (1 + r)^N
```

On the BA II Plus this is one TVM setup: `N`, `I/Y`, `PMT` (the coupon), `FV` (the face), `CPT PV`.

**Periodicity.** For a semiannual bond, halve the annual coupon and the annual yield and double the
number of years. Always.

| Annual terms | Calculator inputs, semiannual |
| --- | --- |
| 6% coupon, 8% yield, 5 years, 1,000 face | N=10, I/Y=4, PMT=30, FV=1000 |

**A zero-coupon bond** has a single cash flow:

```
PV = Face / (1 + r)^N
```

**A perpetual bond** pays forever:

```
PV = Coupon / r
```

**The three price relationships** (memorise the direction, derive the rest):

| Condition | Price |
| --- | --- |
| Coupon rate > required yield | **Premium** (price above par) |
| Coupon rate = required yield | **Par** |
| Coupon rate < required yield | **Discount** (price below par) |

And **price moves inversely to yield**, always.

### Valuing equity instruments

**Preferred stock** — a fixed dividend in perpetuity:

```
PV = D / r
```

**Constant growth (Gordon growth) model** — a dividend growing at a constant rate `g` forever:

```
PV = D1 / (r − g)  where D1 = D0 × (1 + g)
```

Valid only when `r > g`. If `g ≥ r` the formula returns a negative or infinite value, which is the
mathematics telling you the assumption is impossible — a company cannot grow faster than its
required return forever.

**Multistage growth** — an explicit high-growth period, then a terminal value at the constant-growth
rate:

```
PV = Σ [Dt / (1 + r)^t]  +  [D(n+1) / (r − g)] / (1 + r)^n
      (explicit dividends)      (terminal value, discounted back)
```

> **The most common multistage error:** the terminal value computed at time `n` must be discounted
> back **n** periods, not n+1. `D(n+1)/(r − g)` gives a value **as of time n**, because the Gordon
> formula always values the stream *one period before* its first cash flow.

### Solving for the implied return or implied growth

Rearranging the same equations:

**Implied return on a bond (yield to maturity):** enter N, PV (negative), PMT, FV, then `CPT I/Y`.

**Implied required return on equity**, from the Gordon model:

```
r = D1 / P0 + g          (dividend yield + growth)
```

**Implied growth**, from the same rearrangement:

```
g = r − D1 / P0
```

These two are how analysts back out what the *market* is assuming. If a share trading at 50 with a
2.00 expected dividend implies `g = r − 4%`, and you believe `r = 9%`, the market is pricing 5%
perpetual growth. You can then ask whether that is plausible — which is a far more useful question
than arguing about a price.

### Cash flow additivity and no arbitrage

**The principle:** the present value of any stream of cash flows equals the sum of the present values
of the individual cash flows. Cash flows *at the same point in time* can be added.

It sounds trivial. It is the foundation of derivative pricing, and here is why:

> **If two combinations of assets produce identical future cash flows, they must have the same price
> today.** If they do not, you buy the cheap one, sell the expensive one, and collect a riskless
> profit with no capital at risk. Arbitrage forces the prices together.

The LOS names three applications.

**1. Implied forward interest rates.** Investing for two years must give the same result as
investing for one year and reinvesting at the one-year rate prevailing then — otherwise arbitrage.

```
(1 + S2)² = (1 + S1) × (1 + F1,1)

so:  F1,1 = (1 + S2)² / (1 + S1) − 1
```

Where `S` are spot rates and `F1,1` is the one-year rate, one year forward.

**Example.** S1 = 4%, S2 = 5%. Then `F1,1 = (1.05)²/(1.04) − 1 = 1.1025/1.04 − 1 = 6.01%`. The market
is implying that the one-year rate in a year's time will be about 6%.

**2. Forward exchange rates (covered interest rate parity).** Converting to a foreign currency,
investing there, and converting back at an agreed forward rate must equal investing domestically:

```
F = S × (1 + r_price currency) / (1 + r_base currency)
```

with `S` and `F` quoted as price-currency units per one base-currency unit. The **higher-interest-
rate currency trades at a forward discount** — otherwise you could borrow the low-rate currency,
invest in the high-rate one, and lock in a riskless profit. (Full treatment in Economics LM8.)

**3. Option values.** A one-period binomial option value is built by constructing a portfolio of the
underlying and borrowing that **replicates** the option's payoffs exactly. By additivity and
no-arbitrage, the option must cost the same as the replicating portfolio. (Derivatives LM10.)

> The unifying idea worth carrying for the rest of the course: **you never need a forecast to price
> a derivative.** You need a replicating portfolio and the assertion that riskless profits do not
> persist.

---

## Formulas to know cold

```
PV = Σ CFt / (1 + r)^t

FIXED INCOME
  Coupon bond:  PV = Σ [C/(1+r)^t] + FV/(1+r)^N     [BA II: N, I/Y, PMT, FV → CPT PV]
  Zero coupon:  PV = FV / (1+r)^N
  Perpetual:    PV = C / r
  Semiannual:   halve the coupon and the yield; double the number of years
  YTM:          [BA II: N, PV (negative), PMT, FV → CPT I/Y]  ×2 if semiannual

EQUITY
  Preferred:            PV = D / r
  Gordon growth:        PV = D1 / (r − g),   D1 = D0(1+g),   requires r > g
  Implied return:       r = D1/P0 + g
  Implied growth:       g = r − D1/P0
  Multistage:  PV = Σ Dt/(1+r)^t + [D(n+1)/(r−g)] / (1+r)^n
                                    └ terminal value is AS OF time n → discount n periods

NO ARBITRAGE
  Forward rate:   (1 + S2)² = (1 + S1)(1 + F1,1)
                  F1,1 = (1+S2)²/(1+S1) − 1
  General:        (1 + S_A)^A × (1 + F_A,B−A)^(B−A) = (1 + S_B)^B
  Forward FX:     F = S × (1 + r_price) / (1 + r_base)
```

---

## Exam traps

> **Trap 1 — Periodicity.** A semiannual bond needs `N × 2`, `I/Y ÷ 2`, `PMT ÷ 2`. And a computed
> semiannual `I/Y` must be **doubled** to give the annual YTM. This single trap accounts for a large
> share of Fixed Income errors.

> **Trap 2 — Terminal value discounting in a multistage model.** `D(n+1)/(r−g)` is a value **at time
> n**. Discount it back **n** periods. Discounting n+1 periods is the classic error.

> **Trap 3 — Using D0 instead of D1 in the Gordon model.** The numerator is **next** period's
> dividend: `D1 = D0 × (1 + g)`.

> **Trap 4 — g ≥ r.** Mathematically invalid, and it signals a bad assumption, not a huge valuation.
> A perpetual growth rate above the required return is impossible.

> **Trap 5 — Calculator sign convention.** PV and FV must have opposite signs when solving for I/Y,
> or the BA II Plus returns `Error 5`.

> **Trap 6 — Forward rate formula direction.** `(1+S2)² = (1+S1)(1+F1,1)` — the *longer* rate is on
> the left. Inverting it gives a plausible-looking wrong answer.

> **Trap 7 — Forward FX quote convention.** `F = S × (1+r_price)/(1+r_base)`. Which currency is the
> base determines the whole answer. Write the quote as "price currency per 1 base currency" before
> you start.

> **Trap 8 — Thinking arbitrage pricing needs a forecast.** It does not. It needs a replicating
> portfolio. This is the single most important conceptual point in Derivatives.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A bond has a 7% annual coupon paid semiannually, 8 years to maturity, face value 1,000, and a yield to maturity of 5.4%. Compute its price.

<details><summary>Answer</summary>

Semiannual: N = 16, I/Y = 2.7, PMT = 35, FV = 1000.

CPT PV → **−1,103.31**, so the price is **1,103.31**.

It trades at a **premium** because the 7% coupon exceeds the 5.4% required yield — the bond pays more than the market demands, so it is worth more than par.

</details>

**2.** A share is expected to pay a dividend of 2.40 next year, growing at 4% in perpetuity. The required return is 9%. Compute the value. Then compute the implied growth if the share trades at 60.

<details><summary>Answer</summary>

Value = D1/(r − g) = 2.40 / (0.09 − 0.04) = 2.40 / 0.05 = **48.00**

Implied growth at a price of 60:
g = r − D1/P0 = 0.09 − 2.40/60 = 0.09 − 0.04 = **5.0%**

At 60 the market is pricing 5% perpetual growth versus your 4% assumption — so on your numbers the share is overvalued. Note how much more useful this framing is than 'it should be worth 48': it tells you exactly what you must disagree with the market about.

</details>

**3.** Spot rates are S1 = 3.2% and S3 = 4.5%. Compute the implied two-year rate, one year forward (F1,2).

<details><summary>Answer</summary>

(1 + S3)³ = (1 + S1) × (1 + F1,2)²

(1.045)³ = 1.141166
1.141166 / 1.032 = 1.105781
F1,2 = (1.105781)^(1/2) − 1 = 1.051561 − 1 = **5.156%**

Interpretation: the market is implying that a two-year investment beginning one year from now will yield about 5.16% a year. No forecast was required — only the assertion that the two routes to a three-year horizon must give the same result.

</details>

**4.** Dividends are 3.00, 3.60, and 4.32 in years 1–3, after which growth settles at 5% forever. The required return is 11%. Compute the value today.

<details><summary>Answer</summary>

**Explicit dividends, discounted:**
```
3.00 / 1.11    = 2.7027
3.60 / 1.11²   = 2.9218
4.32 / 1.11³   = 3.1589
                 -------
                  8.7834
```
**Terminal value at time 3:**
D4 = 4.32 × 1.05 = 4.536
TV3 = 4.536 / (0.11 − 0.05) = **75.60**

Discount **3** periods: 75.60 / 1.11³ = **55.28**

**Value = 8.78 + 55.28 = 64.06**

Note the terminal value is 86% of the total — which is why the `g` assumption deserves far more scrutiny than the year-2 dividend.

</details>

**5.** Explain the cash flow additivity principle and why it makes arbitrage pricing possible without any forecast.

<details><summary>Answer</summary>

**Additivity:** the present value of a set of cash flows equals the sum of the present values of each cash flow individually; cash flows occurring at the same date can be added.

The consequence: if two portfolios produce **identical cash flows in every future state**, additivity says they have the same present value, so they must have the **same price today**. If they did not, you would buy the cheaper, sell the dearer, and lock in a riskless profit with zero net investment — and that trade would be repeated until the prices converged.

This is why derivative pricing needs no forecast. To price an option you do not predict the stock; you construct a portfolio of the stock and borrowing that **replicates** the option's payoffs, and the option must cost what the replicating portfolio costs.

</details>

**6.** A share trades at 42 and pays a dividend of 1.68 next year. If the required return is 10%, what growth does the market imply, and what would make you doubt it?

<details><summary>Answer</summary>

g = r − D1/P0 = 0.10 − 1.68/42 = 0.10 − 0.04 = **6%** perpetual growth.

Reasons to doubt it: 6% forever exceeds plausible long-run **nominal GDP growth** in most developed economies, which is the hard ceiling on any company's perpetual growth. It would require the company to grow faster than the economy indefinitely, taking an ever-increasing share of it.

Check: is the 6% supported by the company's sustainable growth rate (retention ratio × ROE)? Does the industry structure support returns above the cost of capital indefinitely (Porter — FSA LM12)? If neither holds, the market is over-paying.

</details>

**7.** The US one-year rate is 5% and the euro one-year rate is 3%. The spot rate is 1.10 USD per EUR. Compute the one-year forward rate and explain the direction.

<details><summary>Answer</summary>

USD is the **price** currency, EUR is the **base** currency (the quote is USD per 1 EUR).

F = S × (1 + r_price)/(1 + r_base) = 1.10 × (1.05/1.03) = 1.10 × 1.019417 = **1.1214 USD/EUR**

The USD, with the **higher** interest rate, trades at a **forward discount** — it takes more USD to buy a EUR forward than spot.

Why it must be so: if it were not, you could borrow EUR at 3%, convert to USD, invest at 5%, and lock in the conversion back at a forward rate that left a riskless profit. The forward rate adjusts precisely to eliminate that trade. This is covered interest rate parity, and it is cash flow additivity again.

</details>

---

## Done when

- [ ] I can price a coupon bond, a zero, and a perpetuity, with correct periodicity handling
- [ ] I can compute YTM on the BA II Plus and double it correctly for a semiannual bond
- [ ] I can apply the Gordon growth model and rearrange it for implied return and implied growth
- [ ] I can build a multistage model and discount the terminal value by the right number of periods
- [ ] I can state the cash flow additivity principle and explain why it forces no-arbitrage pricing
- [ ] I can compute an implied forward interest rate from two spot rates
- [ ] I can compute a forward FX rate and say which currency trades at a discount, and why
- [ ] I answered the self-check cold, several days after first study

---

← [LM03 Benchmarking Returns](lm-03-benchmarking-returns.md)  ·  [Topic index](README.md)  ·  [LM05 Statistical Characteristics of Asset Returns](lm-05-statistical-characteristics-of-asset-returns.md) →
