# QM · LM07 — Estimation and Hypothesis Testing

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 18 |
| **Prerequisites** | LM5 and LM6. The normal distribution, Z-scores, and the t-distribution. |
| **Where it shows up** | 3 questions — the largest single allocation in QM. Test selection and Type I/II errors are near-certain. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the central limit theorem and the application of confidence intervals and sampling methodologies
- explain hypothesis testing and its components, including statistical significance, Type I and Type II errors, and the power of a test; construct appropriate hypothesis tests; and interpret the results
- compare and contrast parametric and non-parametric tests, describe situations in which each is the more appropriate type of test, construct appropriate hypothesis tests, and interpret the results

---

## Core concepts

### The hardest module in Quantitative Methods

18 hours is the largest single allocation in the topic, and it is warranted. Hypothesis testing is
abstract, the notation is unfamiliar, and the errors compound — a mis-set hypothesis produces a
perfectly executed test of the wrong thing. Work slowly and do many questions.

### Sampling

| Method | How | Note |
| --- | --- | --- |
| **Simple random** | Every member equally likely to be selected | The baseline |
| **Systematic** | Every k-th member | Fast; fails if the list has a periodic pattern |
| **Stratified random** | Divide into strata, sample randomly within each in proportion | **Lower sampling error** than simple random; standard for bond index replication |
| **Cluster** | Divide into clusters, randomly select whole clusters | Cheaper, generally **less** precise |
| **Convenience** | Whatever is easy to reach | Non-probability; introduces bias |
| **Judgmental** | Expert selection | Non-probability; useful with real expertise, but not generalisable |

**Sampling error** = sample statistic − population parameter. It exists in every sample and shrinks
as `n` grows.

**Biases to recognise:**

- **Data snooping** — testing a dataset repeatedly until something is significant. With enough tests,
  something always is.
- **Sample selection bias** — the sample is not representative of the population.
- **Survivorship bias** — a special case: failed funds and delisted companies disappear from the
  data, so the surviving sample looks better than reality.
- **Look-ahead bias** — using information that was not actually available at the decision date
  (e.g. using year-end financials on 31 December, before they were published).
- **Time-period bias** — a result that holds only in the chosen window.

### The central limit theorem

> **For a population with mean μ and finite variance σ², the sampling distribution of the sample
> mean approaches a normal distribution with mean μ and variance σ²/n as n becomes large
> (n ≥ 30 as a rule of thumb) — regardless of the shape of the underlying population.**

This is the result that makes inference possible. You almost never know the population's
distribution, and the CLT says you do not need to: the **sample mean** is approximately normal
anyway once n is reasonably large.

The **standard error of the mean** is the standard deviation of that sampling distribution:

```
σ known:     σ_x̄ = σ / √n
σ unknown:   s_x̄ = s / √n
```

> Note the `√n`. To halve the standard error you must **quadruple** the sample size. This is why
> incremental data gets expensive fast, and why long track records are needed to distinguish skill
> from luck.

### Confidence intervals

```
Point estimate ± (Reliability factor × Standard error)

x̄ ± z(α/2) × σ/√n          [σ known]
x̄ ± t(α/2, n−1) × s/√n     [σ unknown — the usual case]
```

**Critical values, memorised:**

| Confidence | z (two-tailed) |
| --- | --- |
| 90% | **1.65** |
| 95% | **1.96** |
| 99% | **2.58** |

**Which distribution to use:**

| | **σ known** | **σ unknown** |
| --- | --- | --- |
| **Normal population, small n** | **z** | **t** |
| **Normal population, large n** | **z** | **t** (z acceptable) |
| **Non-normal, small n** | Not available | **Not available** |
| **Non-normal, large n (≥30)** | **z** (by CLT) | **t** (z acceptable) |

The practical summary: **use t whenever σ is unknown**, which is nearly always. The t-distribution
has fatter tails, so it gives a **wider** (more conservative) interval — appropriate, since you are
estimating the standard deviation as well as the mean.

> **Interpretation trap.** A 95% confidence interval does **not** mean "there is a 95% probability
> the true mean lies in this interval". The true mean is a fixed constant — it either is or is not
> in there. It means: **if you repeated the sampling procedure many times, 95% of the intervals so
> constructed would contain the true mean.** The exam tests this wording.

**Resampling alternatives** — used when the analytical standard error is hard to derive:
**bootstrap** (resample with replacement from your sample, many times, and observe the distribution
of the statistic) and **jackknife** (recompute the statistic leaving out one observation at a time).
Both reappear in LM9.

### Hypothesis testing — the six steps

| Step | What you do |
| --- | --- |
| 1 | **State H0 and Ha** |
| 2 | Identify the **appropriate test statistic** and its distribution |
| 3 | Specify the **significance level α** |
| 4 | State the **decision rule** (critical values / rejection region) |
| 5 | **Collect data and compute** the test statistic |
| 6 | **Make the statistical decision**, then the economic/investment decision |

**Setting the hypotheses.** The **null (H0) always contains the equality** (=, ≤, or ≥). The
**alternative (Ha) is what you are trying to demonstrate**.

> **The rule that prevents most errors:** put what you want to *prove* in the **alternative**. You
> never "prove" the null — you either reject it or fail to reject it. "Fail to reject" is not
> "accept": it means the evidence was insufficient, not that H0 is true.

| Test type | H0 | Ha | Rejection region |
| --- | --- | --- | --- |
| **Two-tailed** | θ = θ0 | θ ≠ θ0 | Both tails, α/2 each |
| **One-tailed (upper)** | θ ≤ θ0 | θ > θ0 | Upper tail, α |
| **One-tailed (lower)** | θ ≥ θ0 | θ < θ0 | Lower tail, α |

### Type I and Type II errors

|  | **H0 is true** | **H0 is false** |
| --- | --- | --- |
| **Reject H0** | **Type I error** (probability **α**) | Correct — **power = 1 − β** |
| **Fail to reject H0** | Correct (1 − α) | **Type II error** (probability **β**) |

- **Type I** — rejecting a true null. A **false positive**. Its probability is exactly the
  significance level **α**, which *you choose*.
- **Type II** — failing to reject a false null. A **false negative**. Probability **β**.
- **Power = 1 − β** — the probability of correctly rejecting a false null. More power is better.

**The trade-off:** for a fixed sample size, **lowering α raises β** (and reduces power). Demanding
more evidence before rejecting means you reject less often — including when you should.

> **The only way to reduce both simultaneously is to increase the sample size.** This is the single
> most examinable relationship in the module.

**Practical framing.** In investing, a Type I error means acting on a strategy that does not work —
you trade, pay costs, and lose. A Type II error means passing on a strategy that does work — an
opportunity cost. Which is worse depends on the situation, and that judgement is what setting α is.

### The test statistic and the decision

```
Test statistic = (Sample statistic − Hypothesised value) / Standard error
```

**Decision rule:** reject H0 if |test statistic| > critical value.

**The p-value** is the smallest significance level at which H0 can be rejected — equivalently, the
probability of observing a result at least as extreme as the one you got, *if H0 were true*.

```
Reject H0 if p-value < α
```

> **Trap:** the p-value is **not** the probability that H0 is true. It is the probability of the
> data given H0, not the probability of H0 given the data. (Reversing a conditional probability
> requires Bayes — LM6.)

**Statistical vs. economic significance.** A result can be statistically significant and
economically worthless: with a large enough sample, a 2 basis point excess return will be
significant — and it will not survive transaction costs. The exam asks about this distinction.

### Choosing the test

| Testing | Conditions | Test statistic | Distribution |
| --- | --- | --- | --- |
| **Mean, σ unknown** | Normal or large sample | `(x̄ − μ0) / (s/√n)` | **t**, df = n − 1 |
| **Mean, σ known** | Normal or large sample | `(x̄ − μ0) / (σ/√n)` | **z** |
| **Difference of means, independent samples** | Normal, variances assumed equal | pooled-variance t | **t** |
| **Mean difference, paired (dependent)** | Paired observations | `(d̄ − μd0) / (sd/√n)` | **t**, df = n − 1 |
| **Single variance** | Normal population | `(n−1)s² / σ0²` | **chi-square**, df = n − 1 |
| **Equality of two variances** | Normal populations | `s1²/s2²` (larger on top) | **F**, df = n1−1, n2−1 |
| **Correlation = 0** | Bivariate normal | `r√(n−2) / √(1−r²)` | **t**, df = n − 2 |

> **Independent vs. paired is a favourite.** Two *different* groups of companies → independent
> samples test. The *same* companies measured before and after → **paired** test on the differences.
> Using the independent test on paired data throws away the pairing and loses power.

### Parametric vs. non-parametric

| | **Parametric** | **Non-parametric** |
| --- | --- | --- |
| Assumes | A specific population distribution (usually normal), and tests parameters | Few or no distributional assumptions |
| Uses | The actual values | **Ranks**, signs, or counts |
| Power when assumptions hold | **Higher** | Lower |
| Robustness | Sensitive to violations and outliers | **Robust** |
| Examples | t-test, z-test, chi-square, F-test | Spearman rank correlation, sign test, Mann–Whitney U, runs test |

**Use a non-parametric test when:**

1. The data are **ranked or ordinal** rather than interval (e.g. fund rankings, credit rating
   categories),
2. The distributional assumptions of the parametric test are **violated** — strong skew, heavy
   outliers, small non-normal samples,
3. The hypothesis does not concern a parameter at all (e.g. testing **randomness** with a runs test).

**Chi-square test of independence** — a non-parametric test on a contingency table:

```
χ² = Σ (Observed − Expected)² / Expected      df = (rows − 1)(columns − 1)
```

**Spearman rank correlation** — the Pearson correlation computed on the **ranks** rather than the
values. Robust to outliers and to non-linear but monotonic relationships.

---

## Formulas to know cold

```
STANDARD ERROR
  σ known:    σ_x̄ = σ/√n            σ unknown:  s_x̄ = s/√n

CONFIDENCE INTERVAL
  x̄ ± z(α/2) × σ/√n        [σ known]
  x̄ ± t(α/2, n−1) × s/√n   [σ unknown — the usual case]
  Critical z (two-tailed):  90% → 1.65 | 95% → 1.96 | 99% → 2.58

TEST STATISTIC (general form)
  (Sample statistic − Hypothesised value) / Standard error

SPECIFIC TESTS
  Mean, σ unknown:      t = (x̄ − μ0)/(s/√n),         df = n − 1
  Mean, σ known:        z = (x̄ − μ0)/(σ/√n)
  Paired differences:   t = (d̄ − μd0)/(sd/√n),       df = n − 1
  Single variance:      χ² = (n−1)s²/σ0²,            df = n − 1
  Two variances:        F = s1²/s2² (larger on top), df = n1−1, n2−1
  Correlation = 0:      t = r√(n−2)/√(1−r²),         df = n − 2
  Independence:         χ² = Σ(O − E)²/E,            df = (r−1)(c−1)

ERRORS
  Type I  = reject a TRUE null   → probability α (you choose it)
  Type II = fail to reject a FALSE null → probability β
  Power = 1 − β
  For fixed n: lowering α RAISES β.  Only a larger n reduces both.

DECISION
  Reject H0 if |test statistic| > critical value,  or if p-value < α
```

---

## Exam traps

> **Trap 1 — Which hypothesis gets the equality.** **H0 always contains the equality** (=, ≤, ≥).
> Put what you want to demonstrate in **Ha**.

> **Trap 2 — "Accepting" the null.** You **fail to reject** it. That is a statement about
> insufficient evidence, not about H0 being true.

> **Trap 3 — The α/β trade-off.** For a fixed n, **lowering α raises β** and reduces power. Only
> increasing the sample size reduces both.

> **Trap 4 — Misinterpreting the p-value.** It is `P(data this extreme | H0 true)`, **not**
> `P(H0 true | data)`. Reversing a conditional needs Bayes.

> **Trap 5 — Misinterpreting a confidence interval.** "95% of intervals constructed this way contain
> the true mean", **not** "95% probability the true mean is in this interval".

> **Trap 6 — z vs. t.** Use **t whenever σ is unknown**, regardless of sample size. t is wider and
> more conservative.

> **Trap 7 — Paired vs. independent samples.** Same subjects measured twice → **paired** test on
> the differences. Different groups → independent-samples test.

> **Trap 8 — One-tailed vs. two-tailed critical values.** For 95%, two-tailed uses **1.96**;
> one-tailed uses **1.65**. Read the alternative hypothesis to decide which.

> **Trap 9 — Statistical significance mistaken for economic significance.** A large sample makes
> tiny effects significant. Always ask whether the effect survives transaction costs and taxes.

> **Trap 10 — Degrees of freedom.** Mean test: n − 1. Correlation test: **n − 2**. Chi-square
> independence: (r − 1)(c − 1). These differ and are tested.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A sample of 36 monthly returns has mean 1.4% and sample standard deviation 3.0%. Test at 5% whether the true mean differs from zero.

<details><summary>Answer</summary>

**H0:** μ = 0    **Ha:** μ ≠ 0    (two-tailed, α = 0.05)

σ is unknown → **t-test**, df = 35.

Standard error = 3.0/√36 = 3.0/6 = 0.50
t = (1.4 − 0)/0.50 = **2.80**

Critical t at 5%, two-tailed, df = 35 ≈ **2.03**.

2.80 > 2.03 → **reject H0**. The mean return is statistically significantly different from zero at the 5% level.

Economic follow-up: 1.4% a month is about 18% annualised — economically large as well as statistically significant. But check whether the sample period is representative (time-period bias) before acting.

</details>

**2.** Construct a 95% confidence interval for the mean in the previous question.

<details><summary>Answer</summary>

x̄ ± t(0.025, 35) × s/√n = 1.4 ± 2.03 × 0.50 = 1.4 ± 1.015

**(0.385%, 2.415%)**

The interval excludes zero, which is the same conclusion as the hypothesis test — as it must be. A two-tailed test at α rejects exactly when the (1 − α) confidence interval excludes the hypothesised value.

And the correct interpretation: if this sampling procedure were repeated many times, 95% of the intervals so constructed would contain the true mean. Not: there is a 95% chance the true mean is between 0.385% and 2.415%.

</details>

**3.** An analyst lowers the significance level from 5% to 1% to be more careful. What happens to the probability of each error type and to the power of the test?

<details><summary>Answer</summary>

- **Type I error probability (α): falls** from 5% to 1%. The analyst rejects a true null less often.
- **Type II error probability (β): rises.** More evidence is now required to reject, so genuinely false nulls escape rejection more often.
- **Power (1 − β): falls.**

For a **fixed sample size**, α and β trade off directly. The analyst has bought protection against false positives at the price of more false negatives.

The **only** way to reduce both simultaneously is to **increase n**, which shrinks the standard error and tightens the sampling distribution.

</details>

**4.** You want to test whether a new screening rule improves returns, using the same 40 stocks measured before and after implementation. Which test, and why does it matter?

<details><summary>Answer</summary>

A **paired (dependent) samples t-test** on the **differences**, df = 39.

Why it matters: each stock serves as its own control. Computing `d_i = after_i − before_i` for each stock removes all the cross-sectional variation between stocks — differences in sector, size, and beta — leaving only the effect of the rule.

Using an **independent-samples** test would treat the before and after sets as two unrelated groups, leaving all that cross-sectional noise in the standard error. The test would be far less powerful and could easily fail to detect a real effect.

</details>

**5.** A backtest over 2,000,000 observations finds a strategy with a mean excess return of 1.5 basis points, significant with a p-value of 0.001. What is your conclusion?

<details><summary>Answer</summary>

**Statistically significant, economically meaningless.** A sample of two million observations produces a tiny standard error, so almost any non-zero effect becomes significant.

1.5 bp per trade will not survive **transaction costs** (bid-ask spread, commissions, market impact), which in most markets exceed that by an order of magnitude. Add taxes and the strategy loses money.

Also be alert to **data snooping**: if many strategies were tested on this dataset, one reaching p = 0.001 is expected by chance. Ask how many hypotheses were tried before this one, and whether the result holds out of sample.

</details>

**6.** When would you prefer a Spearman rank correlation to a Pearson correlation?

<details><summary>Answer</summary>

Three situations:

(1) **Ordinal data** — the data are ranks to begin with (fund rankings, credit rating categories, survey responses), where the intervals between values are not meaningful.

(2) **Outliers present** — Pearson correlation is extremely sensitive to extreme values; a single outlier can create or destroy an apparent relationship. Ranks compress outliers to just the next rank, so Spearman is robust.

(3) **Monotonic but non-linear relationships** — if Y rises consistently with X but along a curve, Pearson (which measures only the *linear* association) understates the relationship while Spearman captures it fully.

The cost: when the data are interval-scaled, roughly normal, and outlier-free, Spearman discards information and has somewhat **lower power** than Pearson.

</details>

**7.** State the central limit theorem and explain why it is the result that makes inference possible.

<details><summary>Answer</summary>

**CLT:** for a population with mean μ and finite variance σ², the sampling distribution of the sample mean approaches a **normal** distribution with mean μ and variance σ²/n as n grows large (n ≥ 30 as a rule of thumb) — **regardless of the shape of the underlying population**.

Why it is indispensable: in practice you almost never know the population distribution, and financial data are visibly non-normal (skewed, leptokurtic — LM5). Without the CLT you could not construct a confidence interval or a test statistic at all.

The CLT says you do not need to know the population's shape. Once n is reasonably large, the **sample mean** is approximately normal, so z and t critical values apply. That single result is what turns a sample into an inference.

</details>

---

## Done when

- [ ] I can state the CLT precisely, including the 'regardless of the population distribution' clause
- [ ] I can compute a standard error and explain why halving it requires quadrupling n
- [ ] I can construct a confidence interval and state its correct interpretation in words
- [ ] I can set up H0 and Ha correctly, with the equality always in the null
- [ ] I can complete the Type I / Type II table including power, and explain the α–β trade-off
- [ ] I can select the right test from a described situation, including paired vs independent
- [ ] I can state the correct degrees of freedom for each test in the table
- [ ] I can explain what a p-value is and what it is not
- [ ] I can say when a non-parametric test is preferable and name three examples
- [ ] I answered the self-check cold, several days after first study

---

← [LM06 Statistical Distributions for Financial Asset Prices and Returns](lm-06-statistical-distributions-for-financial-asset-prices-and-ret.md)  ·  [Topic index](README.md)  ·  [LM08 The Return and Risk of a Financial Portfolio](lm-08-the-return-and-risk-of-a-financial-portfolio.md) →
