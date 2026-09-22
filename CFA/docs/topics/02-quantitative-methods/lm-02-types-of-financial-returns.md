# QM · LM02 — Types of Financial Returns

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM1. Comfort with exponents and logarithms. |
| **Where it shows up** | 2 questions. Geometric vs arithmetic mean, and annualisation, are the most reliably tested. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate, compare, and interpret different types of returns for financial assets, instruments, and indicators

---

## Core concepts

### The return measures, and when each is correct

Five measures. Choosing the wrong one is the main way marks are lost here — each answers a different
question.

| Measure | Formula | Use when |
| --- | --- | --- |
| **Holding period return** | `(P1 − P0 + D) / P0` | A single period, total return |
| **Arithmetic mean return** | `Σ R / n` | Estimating the return of a **single future period** |
| **Geometric mean return** | `[Π(1 + R)]^(1/n) − 1` | Measuring **compound growth over multiple past periods** |
| **Harmonic mean** | `n / Σ(1/x)` | Averaging **prices paid** under a fixed-currency purchase plan |
| **Continuously compounded** | `ln(1 + HPR)` or `ln(P1/P0)` | Statistical work; options; time-additive returns |

### Arithmetic vs. geometric — the distinction that matters most

**The geometric mean is always ≤ the arithmetic mean**, with equality only when every period's
return is identical. The gap widens with **volatility**.

Why? Because compounding is multiplicative and losses hurt more than equivalent gains help.

**The canonical example.** Two years: +50%, then −50%.

```
Arithmetic mean = (50% + (−50%)) / 2 = 0%
Geometric mean  = [(1.50)(0.50)]^(1/2) − 1 = (0.75)^0.5 − 1 = −13.4%
```

100 becomes 150, then 75. You lost a quarter of your money. The arithmetic mean says you broke even;
the geometric mean tells the truth about what happened to your wealth.

**When to use which:**

- **Geometric** for describing **past performance** — it is the actual compound rate of growth of
  wealth, and it is the only honest way to report a multi-period track record.
- **Arithmetic** for estimating a **single-period expected return** — it is the unbiased estimator
  of next period's return from a sample.

> A useful approximation: `Geometric ≈ Arithmetic − σ²/2`. The **volatility drag**. It explains why
> two funds with the same average annual return but different volatility end with different wealth,
> and it is the reason volatility is costly even to an investor who never sells.

### The harmonic mean and cost averaging

The harmonic mean is the right average when you invest a **fixed amount of money** each period
rather than buying a fixed number of units.

```
Harmonic mean = n / Σ(1 / x_i)
```

Because a fixed sum buys **more** units when the price is low and **fewer** when it is high, the
average price paid is the harmonic mean, which is **lower than the arithmetic mean** of the prices.
This is the mathematics behind dollar-cost averaging.

**Ordering, for positive, non-identical numbers:**

```
Harmonic mean  ≤  Geometric mean  ≤  Arithmetic mean
```

> **Trap:** the exam gives you a series of purchase prices and asks for the "average price paid".
> If the investor spent a fixed **amount** each period, the answer is the **harmonic** mean. If they
> bought a fixed **number of shares**, it is the arithmetic mean.

### Annualising returns

To compare returns measured over different horizons, put them all on an annual basis by
**compounding**, not multiplying.

```
Annualised return = (1 + R_period)^(number of periods per year) − 1
```

| Period return | Periods per year | Annualised |
| --- | --- | --- |
| 1.5% monthly | 12 | `1.015^12 − 1 = 19.56%` |
| 4% quarterly | 4 | `1.04^4 − 1 = 16.99%` |
| 0.05% daily | 252 | `1.0005^252 − 1 = 13.42%` |
| 8% over 18 months | 12/18 = 0.667 | `1.08^(2/3) − 1 = 5.29%` |

> **Trap:** annualising a short-period return **multiplicatively** (1.5% × 12 = 18%) understates it,
> because it ignores compounding. And annualising a very short period (a week, a day) produces a
> number that is statistically meaningless even when computed correctly — the exam sometimes tests
> whether you recognise that.

### Continuously compounded returns

```
r_continuous = ln(1 + HPR) = ln(P1 / P0)
HPR = e^(r_continuous) − 1
```

Two properties that make them indispensable later:

1. **They are additive across time.** The continuously compounded return over two periods is the
   *sum* of the two period returns. Simple returns must be chained multiplicatively.
2. **They are approximately normally distributed** even when simple returns are not, which is why
   option pricing (Derivatives) and much of the statistics in QM LM6–LM10 use them.

A continuously compounded return is always **less than** the equivalent simple return, and the gap
grows with the size of the return: `ln(1.10) = 9.53%` versus a 10% simple return.

### Gross, net, pre-tax, after-tax, and leveraged returns

```
Net return = Gross return − Management fees − Administrative and other expenses
After-tax return = Pre-tax return × (1 − tax rate)          [simplified]
Leveraged return = HPR on assets × (Total position / Equity) − Borrowing cost × (Debt / Equity)
```

**Leverage magnifies in both directions.** An investor with 100 of equity who borrows 100 and buys
200 of an asset that rises 10% earns 20 on 100 of equity, less the cost of the borrowing — roughly
a 20% return before financing cost. If the asset falls 10%, the loss is 20%. The leverage ratio
scales the outcome symmetrically; the borrowing cost shifts it down.

### Other return measures

- **Real return** — `(1 + nominal)/(1 + inflation) − 1` (LM1).
- **Money-weighted and time-weighted returns** — LM3, where they get full treatment.
- **Return on an index** — LM3.

---

## Formulas to know cold

```
Holding period return:     HPR = (P1 − P0 + D1) / P0
Multi-period chaining:     (1 + R_total) = (1 + R1)(1 + R2)...(1 + Rn)

Arithmetic mean:  R̄ = Σ Ri / n
Geometric mean:   RG = [(1+R1)(1+R2)...(1+Rn)]^(1/n) − 1
Harmonic mean:    XH = n / Σ(1/Xi)

Ordering (positive, non-identical values):  Harmonic ≤ Geometric ≤ Arithmetic
Volatility drag:  Geometric ≈ Arithmetic − σ²/2

Annualising:      R_annual = (1 + R_period)^(periods per year) − 1

Continuous compounding:
    r_cc = ln(1 + HPR) = ln(P1/P0)
    HPR  = e^(r_cc) − 1
    Additive across time:  r_cc(0→2) = r_cc(0→1) + r_cc(1→2)

Leveraged return = r_asset × (V_total / V_equity) − r_borrow × (V_debt / V_equity)
```

---

## Exam traps

> **Trap 1 — Using the arithmetic mean to describe past performance.** Past multi-period performance
> is the **geometric** mean. Reporting the arithmetic mean of a volatile series overstates what an
> investor actually earned, sometimes enormously.

> **Trap 2 — Using the geometric mean to forecast a single period.** For a one-period expected
> return, the **arithmetic** mean is the unbiased estimator.

> **Trap 3 — Multiplying instead of compounding when annualising.** `1.5% × 12` is not the annual
> return. Use `(1.015)^12 − 1`.

> **Trap 4 — The harmonic mean question.** Fixed **amount** invested each period → **harmonic** mean
> gives the average price paid. Fixed **number of shares** → arithmetic mean.

> **Trap 5 — Forgetting the geometric ≤ arithmetic inequality.** If your geometric answer exceeds
> your arithmetic answer, you have made an arithmetic error. It is a free check.

> **Trap 6 — Continuously compounded vs. simple.** `ln(1 + R)`, not `ln(R)`. And the continuously
> compounded return is always **smaller** than the simple return it corresponds to.

> **Trap 7 — Leveraged return asymmetry.** Leverage magnifies gains *and* losses proportionally. The
> borrowing cost makes the downside slightly worse than the mirror image of the upside.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Annual returns are +22%, −15%, +8%, +30%. Compute the arithmetic and geometric mean returns.

<details><summary>Answer</summary>

Arithmetic = (22 − 15 + 8 + 30)/4 = 45/4 = **11.25%**

Geometric = [(1.22)(0.85)(1.08)(1.30)]^(1/4) − 1
= [1.22 × 0.85 × 1.08 × 1.30]^(0.25) − 1
= [1.45595]^(0.25) − 1
= 1.09843 − 1 = **9.84%**

The 1.4 percentage point gap is the volatility drag. The geometric figure is what the investor's wealth actually compounded at.

</details>

**2.** An investor buys shares at 25, 20, and 40, investing a fixed 1,000 each time. What is the average price paid?

<details><summary>Answer</summary>

Fixed **amount** invested → **harmonic mean**.

XH = 3 / (1/25 + 1/20 + 1/40) = 3 / (0.04 + 0.05 + 0.025) = 3 / 0.115 = **26.09**

Check directly: 1,000/25 = 40 shares, 1,000/20 = 50 shares, 1,000/40 = 25 shares → 115 shares for 3,000 → 3,000/115 = **26.09** ✓

The arithmetic mean of the prices would be (25+20+40)/3 = 28.33 — higher, and wrong for this question.

</details>

**3.** A fund returns 2.1% per quarter. What is its annualised return? What if it returned 2.1% over a single week?

<details><summary>Answer</summary>

Quarterly: (1.021)^4 − 1 = 1.08670 − 1 = **8.67%**

Weekly: (1.021)^52 − 1 = **195.3%**

The second calculation is arithmetically correct and **analytically meaningless**. Annualising a single week's return assumes 52 consecutive identical weeks, which no fund achieves. The exam sometimes tests whether you recognise that short-period annualisation produces a number with no forecasting content.

</details>

**4.** Two funds both average 10% arithmetically over ten years. Fund A has a standard deviation of 5%, Fund B has 25%. Which ended with more wealth, and roughly how much does the difference cost?

<details><summary>Answer</summary>

**Fund A.** Using the volatility drag approximation `Geometric ≈ Arithmetic − σ²/2`:

- Fund A: 10% − (0.05²)/2 = 10% − 0.125% ≈ **9.88%**
- Fund B: 10% − (0.25²)/2 = 10% − 3.125% ≈ **6.88%**

Over ten years: 1.0988^10 = 2.566 versus 1.0688^10 = 1.945. Fund A ends with about **32% more wealth** from the identical arithmetic average return.

This is why volatility is costly even to a long-term investor who never sells: it directly reduces the compound growth rate.

</details>

**5.** A price rises from 50 to 58. Compute the simple and continuously compounded returns, and explain why the continuously compounded figure is smaller.

<details><summary>Answer</summary>

Simple HPR = (58 − 50)/50 = **16.00%**
Continuously compounded = ln(58/50) = ln(1.16) = **14.84%**

The continuously compounded figure is smaller because it is the rate that, **compounded continuously**, produces the same ending value. Continuous compounding is the most frequent compounding possible, so a lower stated rate achieves the same result. Formally, `e^0.1484 = 1.16` ✓

The gap widens with the size of the return: for a 100% simple return, the continuously compounded equivalent is only ln(2) = 69.3%.

</details>

**6.** An investor has 200,000 of equity, borrows 300,000 at 5%, and invests 500,000 in an asset that returns 12%. Compute the return on equity. Then repeat if the asset returns −12%.

<details><summary>Answer</summary>

**Asset +12%:**
Gain on assets = 500,000 × 12% = 60,000
Borrowing cost = 300,000 × 5% = 15,000
Net to equity = 60,000 − 15,000 = 45,000
Return on equity = 45,000 / 200,000 = **22.5%**

**Asset −12%:**
Loss on assets = −60,000
Borrowing cost = −15,000
Net to equity = −75,000
Return on equity = −75,000 / 200,000 = **−37.5%**

The 2.5× leverage magnified a ±12% asset move into +22.5%/−37.5%. The downside is worse than the mirror image because the 5% borrowing cost is owed regardless of which way the asset moved.

</details>

**7.** Why are continuously compounded returns preferred for statistical analysis?

<details><summary>Answer</summary>

Two reasons.

**(1) Time additivity.** The continuously compounded return over multiple periods is the simple **sum** of the period returns: `r(0→3) = r1 + r2 + r3`. Simple returns must be chained multiplicatively. Additivity makes aggregation across horizons trivial and makes standard statistical machinery (which assumes additive errors) applicable.

**(2) Distributional behaviour.** Simple returns are bounded below at −100% and unbounded above, so they cannot be normally distributed. Continuously compounded returns are unbounded in both directions and are far better approximated by a normal distribution — which is the assumption underlying option pricing and most of the hypothesis testing in QM LM6–LM10.

</details>

---

## Done when

- [ ] I can compute arithmetic, geometric, and harmonic means and state the ordering between them
- [ ] I can say which mean is correct for describing the past and which for forecasting one period
- [ ] I can explain the volatility drag and quantify it with σ²/2
- [ ] I can annualise a return from any period length, by compounding
- [ ] I can convert between simple and continuously compounded returns in both directions
- [ ] I can compute a leveraged return and explain its asymmetry
- [ ] I can recognise when a question calls for the harmonic mean
- [ ] I answered the self-check cold, several days after first study

---

← [LM01 Returns of Financial Assets and Instruments](lm-01-returns-of-financial-assets-and-instruments.md)  ·  [Topic index](README.md)  ·  [LM03 Benchmarking Returns](lm-03-benchmarking-returns.md) →
