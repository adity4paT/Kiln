# QM · LM05 — Statistical Characteristics of Asset Returns

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM2 (means). BA II Plus DATA/STAT worksheet. |
| **Where it shows up** | 2 questions. Sample vs population standard deviation, and skew/kurtosis direction, are the reliable targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate, interpret, and evaluate various measures of (1) central tendency and location and (2) dispersion
- describe, interpret, and evaluate measures of skewness and kurtosis
- calculate, interpret, and evaluate covariance and correlation
- calculate, interpret, and evaluate semi-deviation and coefficient of variation

---

## Core concepts

### Central tendency

| Measure | Definition | Best when |
| --- | --- | --- |
| **Arithmetic mean** | Σx / n | Symmetric data with no extreme outliers |
| **Median** | The middle value when ordered | **Skewed data or outliers present** — it is robust |
| **Mode** | The most frequent value | Categorical data; identifying multiple peaks |
| **Weighted mean** | Σ(wᵢ xᵢ) | Components contribute unequally — e.g. portfolio returns |
| **Geometric mean** | [Π(1+x)]^(1/n) − 1 | Compound growth over time (LM2) |
| **Harmonic mean** | n / Σ(1/x) | Averaging prices under fixed-money purchases (LM2) |

The mean is the only measure that uses every observation, which is both its strength and its
weakness — **one extreme value drags it**, while the median does not move.

**Trimmed and winsorised means** handle outliers explicitly: a trimmed mean **discards** the highest
and lowest k% of observations; a winsorised mean **replaces** them with the nearest surviving value.
Winsorising keeps the sample size; trimming reduces it.

### Measures of location — quantiles

Quantiles divide ordered data into groups: **quartiles** (4), **quintiles** (5), **deciles** (10),
**percentiles** (100).

```
Position of the y-th percentile:  Ly = (n + 1) × y / 100
```

If `Ly` is not an integer, interpolate linearly between the neighbouring observations.

The **interquartile range (IQR) = Q3 − Q1** is a robust measure of spread, unaffected by extremes.
A **box plot** shows the median, Q1, Q3, and the whiskers — and asymmetry in the box is a fast visual
test for skew.

### Dispersion

| Measure | Formula | Note |
| --- | --- | --- |
| **Range** | Max − Min | Uses only two observations; very sensitive to outliers |
| **Mean absolute deviation (MAD)** | Σ\|xᵢ − x̄\| / n | Uses absolute values, so it is not differentiable — rarely used in theory |
| **Variance (population)** | σ² = Σ(xᵢ − μ)² / N | Divide by **N** |
| **Variance (sample)** | s² = Σ(xᵢ − x̄)² / (**n − 1**) | Divide by **n − 1** |
| **Standard deviation** | √variance | Same units as the data — this is why it is preferred |
| **Target semi-deviation** | √[Σ(xᵢ − B)² / (n − 1)] for xᵢ **< B** only | Downside risk only |
| **Coefficient of variation** | CV = s / x̄ | Risk **per unit of return** — unitless, so it compares across assets |

**Why n − 1?** The sample mean is itself estimated from the data, which uses up one degree of
freedom. Dividing by n would systematically **underestimate** the true variance. The correction
makes the estimator unbiased.

> **On the BA II Plus:** in `2ND DATA` / `2ND STAT`, **`Sx` is the sample** standard deviation
> (÷ n−1) and **`σx` is the population** standard deviation (÷ N). Exam data is almost always a
> **sample**, so you want `Sx`. Grabbing the wrong one gives an answer close enough to look right.

### Semi-deviation — measuring only the downside

Standard deviation treats a 10% gain and a 10% loss as equally "risky", which does not match how
investors experience them. **Target semi-deviation** measures dispersion **below a target B only**:

```
Target semi-deviation = √[ Σ (xᵢ − B)² / (n − 1) ]   summed over observations where xᵢ < B
```

When B is the mean, it is simply **semi-deviation** (downside deviation).

Note the denominator: it is `n − 1` using the **total** sample size, not the count of
below-target observations. This trips people up.

Semi-deviation is more relevant for **asymmetric return distributions** — options strategies, hedge
funds, and anything with an embedded optionality. For a symmetric distribution it carries no extra
information over the standard deviation.

### Coefficient of variation

```
CV = Standard deviation / Mean
```

CV is **unitless**, so it compares risk across assets with different scales and different average
returns. **Lower CV is better** — less risk per unit of return.

> **Trap:** CV is the inverse of a risk-adjusted return measure. Comparing two assets, the one with
> the **lower** CV has more return per unit of risk. Candidates routinely pick the higher one.

CV becomes unreliable when the mean is near zero (the denominator explodes) or negative (the sign
makes it uninterpretable).

### Skewness

Skewness measures **asymmetry**.

| | **Positive (right) skew** | **Negative (left) skew** |
| --- | --- | --- |
| Long tail on the | Right | Left |
| Ordering | **Mean > Median > Mode** | **Mean < Median < Mode** |
| Frequent | Many small losses, a few large gains | Many small gains, a few large losses |
| Investors | **Prefer** it | **Dislike** it |
| Example | Lottery-like payoffs; long call options | Most equity index returns; selling insurance or options |

**Skewness = 0 for a symmetric distribution.** As a rule of thumb, |skew| > 0.5 is meaningful.

> **The memory hook:** the **mean chases the tail**. A long right tail pulls the mean above the
> median. So positive skew → mean > median. Derive the ordering from that rather than memorising it.

**Why it matters:** equity returns are typically **negatively skewed** — most periods are modestly
positive, and crashes are large and sudden. A risk model assuming symmetry systematically
understates the probability of a severe loss.

### Kurtosis

Kurtosis measures the weight in the **tails** — the propensity for extreme outcomes.

| Term | Excess kurtosis | Meaning |
| --- | --- | --- |
| **Mesokurtic** | 0 | Normal distribution |
| **Leptokurtic** | **> 0** | **Fat tails** and a higher peak. More extreme outcomes than normal |
| **Platykurtic** | **< 0** | Thin tails, flatter. Fewer extreme outcomes |

```
Excess kurtosis = Kurtosis − 3
```

The normal distribution has kurtosis of exactly 3, so excess kurtosis re-bases it to zero. As a rule
of thumb, **excess kurtosis > 1.0 is considered significant**.

**Financial asset returns are almost universally leptokurtic.** Extreme moves happen far more often
than a normal distribution predicts. This is the single most important empirical fact about return
distributions, and it means models built on normality **understate tail risk** — which is precisely
what goes wrong in crises.

> **Memory hook:** **lepto**kurtic — think "leap", it **leaps** out to the extremes. Fat tails.

### Covariance and correlation

**Covariance** measures how two variables move together:

```
Cov(X,Y) = Σ (xᵢ − x̄)(yᵢ − ȳ) / (n − 1)
```

Its sign is interpretable (positive = they move together) but its **magnitude is not**, because it
depends on the units of both variables. Covariance of 0.004 tells you nothing about strength.

**Correlation** standardises it:

```
ρ = Cov(X,Y) / (σx × σy)
```

`ρ` is bounded in **[−1, +1]** and is unitless, so magnitude is interpretable:

| ρ | Meaning |
| --- | --- |
| **+1** | Perfect positive linear relationship |
| **0** | **No linear** relationship |
| **−1** | Perfect negative linear relationship |

Three cautions the exam tests:

1. **Correlation measures only the *linear* relationship.** Y = X² over a symmetric range has
   correlation near zero despite a perfect deterministic relationship. Always look at a scatter plot.
2. **Correlation is not causation.** It may reflect a common third factor, or coincidence
   (spurious correlation).
3. **Correlation is extremely sensitive to outliers.** A single extreme point can create or destroy
   an apparent relationship.

Correlation is the input that makes diversification work (Portfolio Management LM1): portfolio
variance falls as correlation falls, and the benefit is largest when correlation is negative.

---

## Formulas to know cold

```
CENTRAL TENDENCY
  Arithmetic mean  x̄ = Σx / n
  Weighted mean    x̄w = Σ(wi xi)
  Percentile position:  Ly = (n + 1) × y/100     [interpolate if non-integer]
  IQR = Q3 − Q1

DISPERSION
  Population variance   σ² = Σ(xi − μ)² / N
  Sample variance       s² = Σ(xi − x̄)² / (n − 1)        ← n−1 for a SAMPLE
  Standard deviation    = √variance
  Mean absolute deviation MAD = Σ|xi − x̄| / n
  Target semi-deviation = √[ Σ(xi − B)² / (n − 1) ]  over xi < B only
  Coefficient of variation  CV = s / x̄               ← LOWER is better

SHAPE
  Skewness = 0 symmetric;  > 0 right/positive skew;  < 0 left/negative skew
     Positive skew: Mean > Median > Mode
     Negative skew: Mean < Median < Mode
  Excess kurtosis = Kurtosis − 3
     > 0 leptokurtic (FAT tails);  = 0 mesokurtic (normal);  < 0 platykurtic (thin tails)

CO-MOVEMENT
  Cov(X,Y) = Σ(xi − x̄)(yi − ȳ) / (n − 1)
  ρ = Cov(X,Y) / (σx σy)          bounded [−1, +1]

BA II Plus:  2ND DATA → enter → 2ND STAT → Sx = sample SD, σx = population SD
```

---

## Exam traps

> **Trap 1 — Sample vs population variance.** Sample divides by **n − 1**; population by **N**. Exam
> data is nearly always a sample. On the calculator that means **`Sx`, not `σx`** — and the wrong
> one gives an answer close enough to be believable.

> **Trap 2 — Skew direction and the mean/median ordering.** **Positive skew → mean > median.** The
> mean chases the tail. Derive it; do not memorise it backwards.

> **Trap 3 — Excess kurtosis vs kurtosis.** Normal kurtosis is **3**; **excess** kurtosis is
> kurtosis − 3, so a normal distribution has excess kurtosis of **zero**. Read which one the question
> asks for.

> **Trap 4 — Leptokurtic direction.** Lepto = **fat** tails = **more** extreme outcomes = excess
> kurtosis > 0.

> **Trap 5 — Coefficient of variation direction.** **Lower CV is better** — less risk per unit of
> return.

> **Trap 6 — Target semi-deviation denominator.** Divide by `n − 1` using the **total** sample size,
> not the number of below-target observations.

> **Trap 7 — Reading covariance magnitude.** Only its **sign** is meaningful. Use correlation for
> strength.

> **Trap 8 — Correlation of zero means independence.** It means **no linear** relationship. A strong
> non-linear relationship can have zero correlation.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A sample of returns: 8%, −3%, 12%, 5%, −6%, 14%. Compute the sample mean and sample standard deviation.

<details><summary>Answer</summary>

Mean = (8 − 3 + 12 + 5 − 6 + 14)/6 = 30/6 = **5.0%**

Deviations: 3, −8, 7, 0, −11, 9
Squared: 9, 64, 49, 0, 121, 81 → Σ = 324

s² = 324/(6 − 1) = 64.8
s = √64.8 = **8.05%**

On the BA II Plus: enter via `2ND DATA` in 1-V mode and read **`Sx`** (not `σx`, which would divide by 6 and give 7.35%).

</details>

**2.** A distribution has mean 6.2, median 7.1, and mode 8.0. Describe its skew and what it implies for an equity investor.

<details><summary>Answer</summary>

**Mean < Median < Mode** → **negative (left) skew**. There is a long tail of large negative outcomes pulling the mean down below the median.

For an investor: most periods are modestly good (the bulk of the distribution sits to the right), but the losses, when they come, are **large**. This is the characteristic shape of equity index returns and of option-selling strategies.

The practical warning: the *average* return understates the typical experience while the *tail* is where the damage is. Risk measures built on standard deviation alone will understate the danger — which is why semi-deviation and downside measures matter here.

</details>

**3.** Asset A: mean return 14%, standard deviation 22%. Asset B: mean return 9%, standard deviation 12%. Which has better risk-adjusted characteristics on a CV basis?

<details><summary>Answer</summary>

CV_A = 22/14 = **1.571**
CV_B = 12/9 = **1.333**

**Asset B** has the lower CV — less risk per unit of return — so on this measure it is more efficient, despite its lower absolute return.

Caveat: CV ignores the risk-free rate (unlike the Sharpe ratio, PM LM2) and says nothing about how the assets **combine** in a portfolio. A high-CV asset with low correlation to the rest of the portfolio can still improve the overall result.

</details>

**4.** A return distribution has excess kurtosis of 2.8. What does that mean and why does it matter for risk management?

<details><summary>Answer</summary>

**Excess kurtosis > 0 → leptokurtic → fat tails.** Extreme outcomes, in both directions, occur substantially more often than a normal distribution would predict. (Kurtosis itself is 2.8 + 3 = 5.8, well above the normal's 3.)

Why it matters: a risk model assuming normality will **systematically understate the probability of severe losses**. A '1-in-100-year' event under the normal assumption may in reality occur every few years. Value at Risk computed on a normal assumption is too low; capital held against it is insufficient.

This is not an edge case — financial asset returns are **almost universally leptokurtic**, which makes it one of the most consequential empirical facts in the curriculum.

</details>

**5.** Cov(X,Y) = 0.0042, σx = 0.14, σy = 0.09. Compute the correlation and interpret it.

<details><summary>Answer</summary>

ρ = 0.0042 / (0.14 × 0.09) = 0.0042 / 0.0126 = **0.333**

A **moderate positive linear** relationship. Note that the covariance of 0.0042 told you only the *sign*; its magnitude was uninterpretable because it depends on the units of both variables. Standardising by the two standard deviations puts it on the [−1, +1] scale where magnitude means something.

For portfolio construction: ρ = 0.33 is well below 1, so combining these assets delivers real diversification benefit.

</details>

**6.** Two variables have a correlation of 0.02. Can you conclude they are unrelated?

<details><summary>Answer</summary>

**No.** Correlation measures only the **linear** relationship.

A perfect non-linear relationship can produce near-zero correlation — for example Y = X² over a symmetric range around zero: every Y is exactly determined by X, yet ρ ≈ 0 because the relationship is U-shaped, not straight.

Also check for **outliers**: a single extreme point can mask an otherwise strong relationship, or manufacture one that is not there.

The remedy is always the same: **plot the data**. A scatter plot reveals non-linearity, clusters, and outliers that no single summary statistic can.

</details>

**7.** Why is target semi-deviation more informative than standard deviation for a strategy that sells put options?

<details><summary>Answer</summary>

Selling puts produces a **highly negatively skewed** return distribution: many small premium gains, punctuated by occasional large losses when the options are exercised against you.

Standard deviation treats upside and downside dispersion identically, so it counts the (small, frequent) positive variation and the (large, rare) negative variation on the same footing — understating exactly the risk the investor cares about.

**Target semi-deviation measures dispersion below a threshold only**, so it isolates the downside. For a symmetric distribution it adds nothing over standard deviation; for an asymmetric one like this, it is the measure that reflects the actual risk being taken.

</details>

---

## Done when

- [ ] I can compute sample and population variance and say which the exam data calls for
- [ ] I can find `Sx` and `σx` on the BA II Plus and explain the difference
- [ ] I can compute a percentile position and interpolate when it is non-integer
- [ ] I can state the mean/median/mode ordering for both skew directions, derived not memorised
- [ ] I can define excess kurtosis, state the normal's value, and explain why leptokurtosis matters
- [ ] I can compute covariance and correlation and explain why only correlation's magnitude is meaningful
- [ ] I can compute CV and target semi-deviation and say when each is the right measure
- [ ] I can give an example where correlation is near zero but the variables are strongly related
- [ ] I answered the self-check cold, several days after first study

---

← [LM04 The Time Value of Money in Finance](lm-04-the-time-value-of-money-in-finance.md)  ·  [Topic index](README.md)  ·  [LM06 Statistical Distributions for Financial Asset Prices and Returns](lm-06-statistical-distributions-for-financial-asset-prices-and-ret.md) →
