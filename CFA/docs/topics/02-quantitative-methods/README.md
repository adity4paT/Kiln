# Quantitative Methods

*The only topic deliberately cut in half — and the split point is exact.*

| | |
| --- | --- |
| **Exam weight** | 6-9% — roughly 10–16 of 180 questions |
| **Study block** | Month 1 & 5, days 21–150 |
| **Budget** | 30 days · 120 hours |
| **Modules** | 11 |
| **Position in study order** | 2 of 10 |

## Why this topic sits here

Quantitative Methods is one topic, studied in **two separate blocks four months apart**. This is the
most unusual feature of the plan, and it is deliberate.

**LM1–LM5 in Month 1 (days 21–30, 40 hours).** Returns, types of returns, benchmarking, time value
of money, and the statistical characteristics of returns. These are **tools**. Discounting in
particular is load-bearing for Equity, Fixed Income, Corporate Issuers, and Derivatives — learning
it in month 5 would be like learning arithmetic in the last week.

**LM6–LM11 in Month 5 (days 131–150, 80 hours).** Distributions, estimation and hypothesis testing,
portfolio risk and return, simulation, regression, and financial data science. These are **heavy,
abstract, and fast-fading**. Studied in Month 1 they would be forgotten by exam day. Studied in
Month 5 they are fresh — and by then you have real assets, real portfolios, and a real CAPM to hang
the statistics on, which is the difference between memorising a t-test and understanding one.

Note the hour allocation: **40 hours for five modules, then 80 hours for six.** Estimation and
hypothesis testing (LM7) and simple linear regression (LM10) are the two most reliably difficult
modules at Level I, and both sit in the second block.

> **The split is not optional.** LM4 (time value of money) must be solid before you start Corporate
> Issuers on day 31 — every NPV, WACC, and bond price in the next four months depends on it. And
> LM8 (portfolio risk and return) deliberately sits *after* Portfolio Management in the calendar,
> so the second encounter with the efficient frontier is a consolidation rather than a first pass.

## Modules

| LM | Module | Hours | Focus |
| --- | --- | --- | --- |
| 01 | [Returns of Financial Assets and Instruments](lm-01-returns-of-financial-assets-and-instruments.md) | 6 | Vocabulary: required vs expected return, the Fisher relation, risk premia. |
| 02 | [Types of Financial Returns](lm-02-types-of-financial-returns.md) | 8 | Arithmetic vs geometric vs harmonic means; annualising; continuous compounding. |
| 03 | [Benchmarking Returns](lm-03-benchmarking-returns.md) | 8 | **MWR vs TWR**, and the three index weighting methods. |
| 04 | [The Time Value of Money in Finance](lm-04-the-time-value-of-money-in-finance.md) | 10 | **The most important module in QM.** Discounting, Gordon growth, no-arbitrage forwards. |
| 05 | [Statistical Characteristics of Asset Returns](lm-05-statistical-characteristics-of-asset-returns.md) | 8 | Dispersion, skew, kurtosis, covariance, correlation. Sample vs population. |
| 06 | [Statistical Distributions for Financial Asset Prices and Returns](lm-06-statistical-distributions-for-financial-asset-prices-and-ret.md) | 14 | — *Month 5 resumes here* — Probability, Bayes, normal and lognormal. |
| 07 | [Estimation and Hypothesis Testing](lm-07-estimation-and-hypothesis-testing.md) | 18 | **Hardest module in QM.** CLT, confidence intervals, Type I/II errors, test selection. |
| 08 | [The Return and Risk of a Financial Portfolio](lm-08-the-return-and-risk-of-a-financial-portfolio.md) | 14 | Portfolio math, efficient frontier, CAL/CML. Consolidates Portfolio Management. |
| 09 | [Simulation of Financial Asset Prices and Returns](lm-09-simulation-of-financial-asset-prices-and-returns.md) | 10 | Historical simulation, bootstrap, Monte Carlo. Conceptual only. |
| 10 | [Applications of Simple Linear Regression in Finance](lm-10-applications-of-simple-linear-regression-in-finance.md) | 18 | **Second hardest.** OLS, ANOVA, R², prediction intervals, beta as a regression slope. |
| 11 | [Introduction to Financial Data Science](lm-11-introduction-to-financial-data-science.md) | 6 | Big data, ML categories, overfitting. Pure recall. |

## The formulas this topic lives on

Five things from this topic must be automatic. They are used in four other topics.

```
1. PV = Σ CFt/(1+r)^t — and the calculator fluency to do it in 25 seconds
2. Gordon growth:  P0 = D1/(r − g),  and rearranged: r = D1/P0 + g,  g = r − D1/P0
3. Forward rate:   (1+S2)² = (1+S1)(1+F1,1)
4. σp² = w1²σ1² + w2²σ2² + 2w1w2ρ12σ1σ2    — the diversification engine
5. t = (statistic − hypothesised)/standard error,  df = n−1 (mean) or n−2 (regression)
```

Plus three critical values, cold: **1.65 (90%) · 1.96 (95%) · 2.58 (99%)**, two-tailed.

## Topic wrap-up

**After Block 2 (day 30)** — before starting Corporate Issuers:

- [ ] LM1–LM5 ticked
- [ ] I can price a bond and solve for YTM on the BA II Plus in under 30 seconds each
- [ ] I can apply the Gordon growth model forwards and backwards
- [ ] I can compute MWR and TWR and explain which is which without hesitating
- [ ] I can compute sample standard deviation on the calculator and know why it is `Sx` not `σx`

**After Block 10 (day 150)** — the end of new material:

- [ ] All 11 modules ticked
- [ ] I can select the correct hypothesis test from a described situation, every time
- [ ] I can complete an ANOVA table and compute R², SEE, and F from sums of squares
- [ ] I can explain the α/β trade-off and why only a larger n reduces both
- [ ] I can interpret α, β, and R² from a market model regression
- [ ] I have completed **80+ QM questions** across both blocks, logged in `trackers/weak-areas.md`

**A warning specific to this topic.** QM is where candidates most often mistake *having read it* for
*being able to do it*. The modules are abstract and the notation is unfamiliar, so familiarity
arrives long before competence. The only reliable test is closed-book questions — if you can answer
LM7 and LM10 questions cold, you know it; if you can follow the worked examples, you do not yet.

---

[← Master study plan](../../study-plan/master-plan.md)  ·  [All topics](../)  ·  [Progress tracker](../../../trackers/progress-tracker.md)
