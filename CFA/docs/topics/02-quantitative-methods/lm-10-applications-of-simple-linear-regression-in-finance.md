# QM · LM10 — Applications of Simple Linear Regression in Finance

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 18 |
| **Prerequisites** | LM5 (covariance, correlation), LM7 (hypothesis testing, t-tests, F-distribution). |
| **Where it shows up** | 3 questions. Tied with LM7 for the heaviest module in QM. ANOVA and R-squared are near-certain. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe, interpret, and explain simple linear regression, including coefficient estimation using the least squares criterion
- describe and compare the assumptions of simple linear regression, identify violations through analyzing residuals, evaluate the estimated model's goodness-of-fit and regression coefficients, and results of ANOVA estimates
- calculate and interpret predicted values, the standard error of the estimate, and prediction intervals for the dependent variable in a simple linear regression model and describe different functional forms
- calculate and interpret the variable estimates of the capital asset pricing model (CAPM)

---

## Core concepts

### The model

```
Yᵢ = b0 + b1 Xᵢ + εᵢ
```

| Term | Name | Meaning |
| --- | --- | --- |
| **Y** | Dependent / explained variable | What you are trying to explain |
| **X** | Independent / explanatory variable | What you are explaining it with |
| **b0** | Intercept | Predicted Y when X = 0 |
| **b1** | Slope coefficient | **Change in Y per one-unit change in X** |
| **ε** | Error term / residual | What the model does not explain |

Everything in this module is about estimating b0 and b1, judging whether they mean anything, and
checking whether the assumptions that justify the judgement actually hold.

### Least squares estimation

Ordinary least squares chooses the line that **minimises the sum of squared residuals**:

```
minimise  Σ (Yᵢ − Ŷᵢ)²
```

Squaring rather than taking absolute values means large errors are penalised
disproportionately — which is why OLS is sensitive to outliers.

```
b1 = Cov(X,Y) / Var(X)     equivalently    b1 = Σ(Xᵢ − X̄)(Yᵢ − Ȳ) / Σ(Xᵢ − X̄)²

b0 = Ȳ − b1 X̄
```

> Note what `b0 = Ȳ − b1X̄` implies: **the regression line always passes through the point
> (X̄, Ȳ)**, the means of both variables. It is a useful check.

On the BA II Plus: `2ND DATA`, enter X and Y pairs, `2ND STAT`, `2ND SET` to **LIN** mode, then
scroll for `a` (intercept), `b` (slope), and `r` (correlation).

### The six assumptions

| # | Assumption | What it means | Violation is called |
| --- | --- | --- | --- |
| 1 | **Linearity** | The relationship between X and Y is linear in the parameters | Misspecification |
| 2 | **Homoskedasticity** | The variance of the residuals is **constant** across all X | **Heteroskedasticity** |
| 3 | **Independence of errors** | Residuals are uncorrelated with each other | **Serial (auto)correlation** |
| 4 | **Normality** | Residuals are normally distributed | Non-normality |
| 5 | **Independence of X and ε** | X is not correlated with the error term | Endogeneity |
| 6 | **X is not random / has variation** | X takes more than one value | — |

**Detecting violations with residual plots** — this is how the LOS wants you to identify them:

- Plot **residuals against X** (or against the fitted values).
- A **random scatter around zero with constant spread** = assumptions satisfied.
- A **cone or fan shape** (spread widening or narrowing) = **heteroskedasticity**.
- A **curved pattern** = the relationship is not linear; the model is misspecified.
- A **wave or cyclical pattern** over time = **serial correlation**.

**Consequences of violations.** In both heteroskedasticity and serial correlation, the coefficient
estimates remain unbiased, but the **standard errors are wrong** — so the t-statistics, the
F-statistic, and every significance conclusion are unreliable. Typically standard errors are
**understated**, which makes coefficients look **more significant than they are**. That is the
practical danger: you conclude a relationship exists when the evidence does not support it.

### ANOVA and goodness of fit

The total variation in Y is decomposed into the part the model explains and the part it does not:

```
SST = SSR + SSE

SST (Total sum of squares)     = Σ(Yᵢ − Ȳ)²     total variation in Y
SSR (Regression sum of squares) = Σ(Ŷᵢ − Ȳ)²     variation EXPLAINED by the model
SSE (Sum of squared errors)     = Σ(Yᵢ − Ŷᵢ)²    variation NOT explained
```

> **Notation warning.** Some textbooks reverse SSR and SSE. In the CFA curriculum,
> **SSR = regression (explained)** and **SSE = error (unexplained)**. Check the ANOVA table's
> degrees of freedom column if you are unsure: the regression row has **df = 1** in simple
> regression; the error row has **df = n − 2**.

**The ANOVA table:**

| Source | df | Sum of squares | Mean square |
| --- | --- | --- | --- |
| Regression | **1** | SSR | MSR = SSR / 1 |
| Error | **n − 2** | SSE | MSE = SSE / (n − 2) |
| Total | n − 1 | SST | |

**Coefficient of determination:**

```
R² = SSR / SST = 1 − SSE / SST
```

**R² is the proportion of the variation in Y explained by X.** In *simple* linear regression only,
`R² = r²` — the square of the correlation coefficient. (This is not true in multiple regression.)

**Standard error of the estimate:**

```
SEE = √MSE = √[ SSE / (n − 2) ]
```

SEE is the standard deviation of the residuals — the typical size of a prediction error, in the
**units of Y**. A **lower SEE means a better fit**.

**The F-test:**

```
F = MSR / MSE       with df = 1 and n − 2
```

In simple linear regression the F-test tests exactly the same hypothesis as the t-test on the slope
(`H0: b1 = 0`), and in fact **F = t²**. The F-test becomes genuinely distinct only in multiple
regression, where it tests all slopes jointly.

### Testing the coefficients

```
t = (b1 − hypothesised value) / SE(b1)       with df = n − 2
```

Usually the hypothesis is `H0: b1 = 0` (X has no explanatory power), so `t = b1 / SE(b1)`.

Confidence interval for the slope:

```
b1 ± t(α/2, n−2) × SE(b1)
```

> If this interval **excludes zero**, the slope is significant at that level — the same conclusion
> as the t-test. Useful as a check.

### Prediction and prediction intervals

**Point prediction:**

```
Ŷ = b0 + b1 X
```

**Prediction interval** — the interval for an *individual* future Y, not for the mean:

```
Ŷ ± t(α/2, n−2) × sf

where  sf = SEE × √[ 1 + 1/n + (X − X̄)² / Σ(Xᵢ − X̄)² ]
```

Two things to read out of `sf`:

1. It is **larger than SEE**, always — predicting a single observation carries both the uncertainty
   about the regression line *and* the individual observation's own scatter.
2. The `(X − X̄)²` term means the interval **widens the further X is from its mean**. Predictions
   near the centre of your data are more reliable than predictions at the edges — and
   **extrapolating beyond the data range** is where the interval becomes uselessly wide, and where
   the linearity assumption is least defensible.

### Functional forms

When the relationship is not linear in the raw variables, transform them.

| Form | Equation | Interpretation of b1 | Use when |
| --- | --- | --- | --- |
| **Linear** | Y = b0 + b1X | A one-**unit** change in X → b1 **unit** change in Y | The relationship is linear |
| **Log-lin** | ln(Y) = b0 + b1X | A one-unit change in X → b1 × 100 **percent** change in Y | Y grows **exponentially** |
| **Lin-log** | Y = b0 + b1 ln(X) | A **1% change in X** → b1/100 unit change in Y | Diminishing effect of X |
| **Log-log** | ln(Y) = b0 + b1 ln(X) | A 1% change in X → **b1 % change in Y** — an **elasticity** | Constant elasticity |

> **The log-log form is the one to remember:** its slope is directly an **elasticity**. It is
> standard in demand estimation and in any context where you want a proportional relationship.

Choose the form by plotting the data and inspecting the residuals — if a linear fit leaves a curved
residual pattern, a transformation is called for.

### CAPM as a regression — the market model

The LOS asks you to **calculate and interpret the variable estimates of the CAPM**. The empirical
vehicle is the market model:

```
Rᵢ = αᵢ + βᵢ RM + εᵢ
```

| Estimate | Interpretation |
| --- | --- |
| **β (slope)** | **Systematic risk** — the sensitivity of the asset's return to the market's. β = 1.4 means a 1% market move is associated with a 1.4% move in the asset |
| **α (intercept)** | The return not explained by market exposure. A significantly **positive alpha** is evidence of outperformance relative to the risk taken |
| **R²** | The proportion of the asset's variation explained by the market — i.e. the **systematic** share. `1 − R²` is the diversifiable, firm-specific share |

And the theoretical relationship:

```
β = Cov(Ri, RM) / Var(RM) = ρ(i,M) × σᵢ / σM
```

Note this is exactly the OLS slope formula `b1 = Cov(X,Y)/Var(X)` with the market as X. **Beta is a
regression slope** — that is the connection this module exists to make.

> **Interpreting R² in this context is a favourite exam item.** A stock with R² = 0.25 has 25% of
> its return variation explained by the market (systematic) and **75% firm-specific** — the latter
> being diversifiable and therefore, per CAPM, uncompensated.

---

## Formulas to know cold

```
MODEL:  Yi = b0 + b1 Xi + εi

ESTIMATION (least squares — minimises Σ(Yi − Ŷi)²)
  b1 = Cov(X,Y) / Var(X) = Σ(Xi−X̄)(Yi−Ȳ) / Σ(Xi−X̄)²
  b0 = Ȳ − b1 X̄                    [the line passes through (X̄, Ȳ)]

ANOVA
  SST = SSR + SSE
    SST = Σ(Yi − Ȳ)²     total
    SSR = Σ(Ŷi − Ȳ)²     regression / EXPLAINED       df = 1
    SSE = Σ(Yi − Ŷi)²    error / UNEXPLAINED          df = n − 2

  MSR = SSR / 1          MSE = SSE / (n − 2)
  R²  = SSR/SST = 1 − SSE/SST       [= r² in SIMPLE regression only]
  SEE = √MSE = √[SSE/(n−2)]         [lower is better; units of Y]
  F   = MSR / MSE,  df = 1, n−2     [in simple regression, F = t²]

INFERENCE
  t = (b1 − b1,hypothesised) / SE(b1),   df = n − 2
  CI for slope:  b1 ± t(α/2, n−2) × SE(b1)

PREDICTION
  Ŷ = b0 + b1 X
  sf = SEE × √[1 + 1/n + (X − X̄)²/Σ(Xi − X̄)²]
  Prediction interval:  Ŷ ± t(α/2, n−2) × sf     [widens as X moves from X̄]

FUNCTIONAL FORMS
  Linear    Y = b0 + b1X            1 unit ΔX → b1 units ΔY
  Log-lin   lnY = b0 + b1X          1 unit ΔX → 100·b1 % ΔY
  Lin-log   Y = b0 + b1 lnX         1% ΔX → b1/100 units ΔY
  Log-log   lnY = b0 + b1 lnX       1% ΔX → b1 % ΔY   ← ELASTICITY

CAPM / MARKET MODEL
  Ri = αi + βi RM + εi
  β = Cov(Ri,RM)/Var(RM) = ρ(i,M) × σi/σM       ← the OLS slope with the market as X
  R² = systematic share of variance;  1 − R² = firm-specific (diversifiable)
```

---

## Exam traps

> **Trap 1 — SSR vs SSE notation.** In the CFA curriculum **SSR = regression (explained)** and
> **SSE = error (unexplained)**. Other texts reverse them. Check the df column: regression has
> **df = 1**, error has **df = n − 2**.

> **Trap 2 — Degrees of freedom.** Simple linear regression uses **n − 2**, not n − 1, because two
> parameters (b0 and b1) are estimated.

> **Trap 3 — R² = r² only in simple regression.** This identity breaks in multiple regression.

> **Trap 4 — High R² means a good model.** It does not. R² measures fit, not validity. A model can
> have a high R², violated assumptions, and no predictive value — and R² says nothing about
> causation.

> **Trap 5 — Consequences of heteroskedasticity and serial correlation.** Coefficients stay
> **unbiased**; the **standard errors are wrong**, usually **understated**, which inflates
> t-statistics and makes results look more significant than they are.

> **Trap 6 — Confusing a confidence interval for the mean with a prediction interval.** The
> prediction interval is **wider**, because it adds the individual observation's own variability to
> the uncertainty about the line.

> **Trap 7 — Extrapolating beyond the data.** The prediction interval widens as X moves from X̄, and
> the linearity assumption is least defensible outside the observed range.

> **Trap 8 — Log-log slope interpretation.** In `ln(Y) = b0 + b1 ln(X)`, **b1 is an elasticity** —
> a percent-for-percent relationship, not a unit-for-unit one.

> **Trap 9 — Reading CAPM R².** R² is the **systematic** share of variance. `1 − R²` is the
> firm-specific, diversifiable share — which CAPM says is uncompensated.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A regression of a stock's return on the market's gives SST = 480, SSE = 168, with n = 42. Compute R², SEE, and the F-statistic, and interpret R².

<details><summary>Answer</summary>

SSR = SST − SSE = 480 − 168 = 312

**R² = 312/480 = 0.650** — 65% of the variation in the stock's return is explained by the market.

MSE = 168/(42 − 2) = 168/40 = 4.20
**SEE = √4.20 = 2.049**

MSR = 312/1 = 312
**F = 312/4.20 = 74.29**, with df = 1 and 40 — far above any conventional critical value, so the market's explanatory power is highly significant.

Interpretation: 65% of this stock's return variation is **systematic**; the remaining **35% is firm-specific** and diversifiable, and per CAPM earns no compensation.

</details>

**2.** The slope coefficient is 1.32 with a standard error of 0.41, from a sample of 30. Test at 5% whether beta differs from 1.

<details><summary>Answer</summary>

**H0:** b1 = 1    **Ha:** b1 ≠ 1    (note: **not** zero — the question asks about 1)

t = (1.32 − 1)/0.41 = 0.32/0.41 = **0.780**

df = n − 2 = 28. Critical t at 5% two-tailed ≈ **2.048**.

0.780 < 2.048 → **fail to reject H0**. The beta is not statistically distinguishable from 1 at the 5% level, despite the point estimate of 1.32.

This is a good illustration of why the point estimate alone is not enough: a 1.32 beta *sounds* meaningfully above market risk, but with SE = 0.41 the data cannot support that conclusion.

</details>

**3.** A residual plot shows the spread of residuals widening steadily as X increases. Name the violation and state its consequence.

<details><summary>Answer</summary>

A fan or cone shape is **heteroskedasticity** — the variance of the errors is not constant across X.

**Consequences:** the coefficient estimates b0 and b1 remain **unbiased** (they are still centred on the true values), but the **standard errors are biased**, typically **understated**.

That means t-statistics are **inflated** and p-values are **too small**, so coefficients look more significant than the evidence justifies. Every inference — the t-test, the F-test, the confidence intervals — is unreliable.

Remedies: use robust (heteroskedasticity-consistent) standard errors, transform the dependent variable (often a log transformation), or use weighted least squares.

</details>

**4.** In a regression of ln(sales) on ln(advertising), the slope is 0.34. Interpret it.

<details><summary>Answer</summary>

This is a **log-log** specification, so the slope is an **elasticity**.

**A 1% increase in advertising is associated with a 0.34% increase in sales.**

Because 0.34 < 1, the relationship is **inelastic** — sales respond less than proportionally to advertising spend. Doubling the advertising budget (+100%) would be associated with only about a 34% increase in sales, which on most cost structures would not pay for itself.

Note the wording: *associated with*, not *causes*. The regression establishes correlation; causation requires an argument the regression itself cannot supply.

</details>

**5.** Why is a prediction interval wider than a confidence interval for the mean of Y at the same X?

<details><summary>Answer</summary>

They answer different questions and therefore carry different amounts of uncertainty.

A **confidence interval for the mean** of Y at a given X reflects only the uncertainty in **where the regression line is** — the sampling error in estimating b0 and b1.

A **prediction interval** for an **individual** future observation must reflect that uncertainty **plus** the observation's own scatter around the line — the ε term, with variance estimated by MSE.

That extra component is the `1 +` inside the `sf` formula: `sf = SEE × √[1 + 1/n + (X − X̄)²/Σ(Xi − X̄)²]`. Without it you would have the interval for the mean; with it you have the interval for a single outcome, which must be wider.

</details>

**6.** A stock's market model regression gives α = 0.004 (monthly, not statistically significant), β = 0.78, R² = 0.31. Summarise what this tells you.

<details><summary>Answer</summary>

**β = 0.78** — the stock is **less volatile than the market** in its systematic exposure. A 1% market move is associated with a 0.78% move in the stock. It is a defensive stock in CAPM terms, with a below-market required return.

**α = 0.004 but not significant** — the point estimate suggests 0.4% a month of return unexplained by market exposure, but the data cannot distinguish it from zero. **You cannot claim outperformance.** Reporting a 4.8% annualised alpha on an insignificant estimate would be an overstatement of the evidence.

**R² = 0.31** — only 31% of the stock's return variation is explained by the market. **69% is firm-specific**, which is diversifiable and, per CAPM, uncompensated. In a portfolio context, this stock brings a lot of idiosyncratic noise for its systematic exposure; it contributes most when held alongside enough other positions to diversify that 69% away.

</details>

**7.** Why does OLS minimise squared residuals rather than absolute residuals, and what does that cost?

<details><summary>Answer</summary>

**Why squares:** the squared-error criterion has a closed-form analytical solution (the formulas for b0 and b1), it is differentiable everywhere (absolute values are not, at zero), and under the classical assumptions it yields the **best linear unbiased estimator** — lowest variance among all unbiased linear estimators.

**What it costs:** squaring penalises large errors **disproportionately** — an error of 10 counts 100 times as much as an error of 1, not 10 times. That makes OLS highly **sensitive to outliers**. A single extreme observation can pull the fitted line substantially and dominate the estimate.

This is why residual inspection matters, and why robust regression methods (which use absolute deviations or down-weight outliers) exist for data with extreme values.

</details>

---

## Done when

- [ ] I can estimate b0 and b1 by hand and on the BA II Plus in LIN mode
- [ ] I can list the six assumptions and identify each violation from a residual plot
- [ ] I can state that violations leave coefficients unbiased but corrupt the standard errors
- [ ] I can fill in a complete ANOVA table including the correct degrees of freedom
- [ ] I can compute R², SEE, and F, and explain what each measures
- [ ] I can test a slope against any hypothesised value with the right df
- [ ] I can build a prediction interval and explain why it widens away from X̄
- [ ] I can interpret the slope in all four functional forms, especially log-log as an elasticity
- [ ] I can interpret α, β, and R² from a market model regression
- [ ] I answered the self-check cold, several days after first study

---

← [LM09 Simulation of Financial Asset Prices and Returns](lm-09-simulation-of-financial-asset-prices-and-returns.md)  ·  [Topic index](README.md)  ·  [LM11 Introduction to Financial Data Science](lm-11-introduction-to-financial-data-science.md) →
