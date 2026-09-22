# PM · LM01 — Portfolio Risk and Return: Part I

## At a glance

| | |
| --- | --- |
| **Topic** | Portfolio Management (8-12% of the exam) |
| **Hours budgeted** | 9 |
| **Prerequisites** | QM LM5 (covariance, correlation). Note: QM LM8 covers the same mathematics from the quantitative side and is studied LATER, in Month 5 — this is the first encounter. |
| **Where it shows up** | 2–3 questions. Portfolio variance calculation is a certainty. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe characteristics of the major asset classes that investors consider in forming portfolios
- explain risk aversion and its implications for portfolio selection
- explain the selection of an optimal portfolio, given an investor's utility (or risk aversion) and the capital allocation line
- calculate and interpret the mean, variance, and covariance (or correlation) of asset returns based on historical data
- calculate and interpret portfolio standard deviation
- describe the effect on a portfolio's risk of investing in assets that are less than perfectly correlated
- describe and interpret the minimum-variance and efficient frontiers of risky assets and the global minimum-variance portfolio

---

## Core concepts

### Major asset classes

Historical characteristics you should be able to rank:

| Asset class | Return | Risk (σ) | Liquidity | Inflation protection |
| --- | --- | --- | --- | --- |
| **Cash / Treasury bills** | Lowest | Lowest | Highest | Poor in real terms |
| **Government bonds** | Low | Low–moderate | High | Poor (nominal) |
| **Corporate bonds** | Moderate | Moderate | Moderate | Poor |
| **Public equities** | High | High | High | Moderate to good over long horizons |
| **Real estate** | Moderate–high | Moderate (understated by appraisal smoothing) | **Low** | **Good** |
| **Commodities** | Variable | High | Moderate | **Good** |
| **Private equity / hedge funds** | High (reported) | Understated by stale pricing | **Very low** | Variable |

The general relationship — **higher expected return comes with higher risk** — is not a law of
nature but a consequence of risk aversion: risky assets must offer more, or no one would hold them.

> **A caution on reported risk for illiquid assets.** Real estate, private equity, and some hedge
> funds report **appraisal-based or stale prices**, which smooths the reported return series and
> **understates** both volatility and correlation with public markets. Their diversification benefit
> looks better on paper than it is. This recurs in Alternative Investments.

### Risk aversion

Investors are assumed **risk averse**: for a given expected return they prefer less risk, and will
accept more risk only if compensated with a higher expected return.

| Type | Behaviour |
| --- | --- |
| **Risk averse** | Requires compensation for risk. The standard assumption |
| **Risk neutral** | Indifferent to risk; cares only about expected return |
| **Risk seeking** | Prefers risk for its own sake; will accept a lower expected return for more of it |

**Three consequences:**

1. The **risk premium is positive** — risky assets must offer more than the risk-free rate.
2. **Required return rises with risk** — the basis of the security market line (LM2).
3. **Diversification has value** — reducing risk without sacrificing expected return is a strictly
   favourable trade, and a risk-averse investor always takes it.

**The utility function:**

```
U = E(R) − ½ A σ²
```

`A` is the **risk aversion coefficient**. Higher `A` means more risk averse; `A = 0` is risk
neutral; `A < 0` is risk seeking. Typical values for risk-averse investors run from about 1 to 10.

**Indifference curves** plot combinations of risk and return giving equal utility. A more risk-averse
investor has **steeper** curves — they demand much more return for each additional unit of risk.

### Portfolio return and risk

**The asymmetry that makes portfolio theory work:**

```
E(Rp) = Σ wᵢ E(Rᵢ)                          ← LINEAR, always a weighted average
σp²   = Σ Σ wᵢ wⱼ Cov(Rᵢ, Rⱼ)                ← NOT linear
```

For two assets:

```
σp² = w1²σ1² + w2²σ2² + 2 w1 w2 ρ12 σ1 σ2

where  Cov(1,2) = ρ12 σ1 σ2
```

**From historical data:**

```
Mean:       R̄ = Σ Rt / n
Variance:   s² = Σ(Rt − R̄)² / (n − 1)        ← SAMPLE, so n − 1
Covariance: Cov(A,B) = Σ(RA,t − R̄A)(RB,t − R̄B) / (n − 1)
Correlation: ρ = Cov(A,B) / (σA σB)
```

### The effect of correlation

| ρ | Portfolio standard deviation | Diversification benefit |
| --- | --- | --- |
| **+1** | `w1σ1 + w2σ2` — the weighted average | **None** |
| **+0.5** | Below the weighted average | Moderate |
| **0** | `√(w1²σ1² + w2²σ2²)` | Substantial |
| **−1** | `\|w1σ1 − w2σ2\|` — can reach **zero** | **Maximum** |

> **The key result:** for **any ρ < +1**, portfolio standard deviation is **strictly less than** the
> weighted average of the component standard deviations, while expected return is exactly the
> weighted average. Diversification is therefore a free improvement — and it does **not** require
> negative correlation, only imperfect correlation.

**Beyond two assets:** with `n` assets there are `n` variances and `n(n−1)` covariance terms, so
**covariances dominate** as `n` grows. Portfolio variance converges not to zero but to the **average
covariance** — the irreducible **systematic risk**. This is the basis of the CAPM argument in LM2.

### The efficient frontier

Plot every achievable portfolio of risky assets in **σ / E(R)** space.

- The **minimum-variance frontier** is the left-hand boundary: for each level of expected return,
  the lowest-variance portfolio.
- The **global minimum-variance portfolio (GMVP)** is its leftmost point — the lowest-risk
  combination available from risky assets alone.
- The **efficient frontier** is the portion **above and to the right of the GMVP**.

```
E(R)
  │                              ╱───── efficient frontier
  │                        ╱
  │                   ●  ← GMVP (lowest risk available)
  │                  ╲
  │                   ╲──── minimum-variance frontier below GMVP: DOMINATED
  └────────────────────────────── σ
```

Portfolios **below** the GMVP are on the minimum-variance frontier but are **not efficient**: for
each one there is a portfolio with the same risk and a higher expected return directly above it. No
rational investor holds a dominated portfolio.

**For two assets:**

```
w1* (GMVP) = (σ2² − Cov(1,2)) / (σ1² + σ2² − 2 Cov(1,2))
```

### The capital allocation line and the optimal portfolio

Adding a risk-free asset (σ = 0, and zero covariance with everything) makes the achievable set a
**straight line** from `Rf` through any chosen risky portfolio:

```
E(Rp) = Rf + [(E(RP) − Rf) / σP] × σp
```

The slope is the **Sharpe ratio** of the risky portfolio, so the best CAL is the **steepest** — the
one tangent to the efficient frontier. That tangency portfolio is the **optimal risky portfolio**,
and it is the same for every investor.

**The investor's own choice** is then only **where on that line to sit**, determined by risk
aversion:

- **Between Rf and the tangency portfolio** — lending (holding some risk-free asset)
- **Beyond the tangency portfolio** — **borrowing** at the risk-free rate to hold more than 100% in
  the risky portfolio

The optimal portfolio is where the investor's **highest attainable indifference curve is tangent to
the CAL**.

> **Two-fund separation**, which LM2 develops: the choice of *which* risky portfolio to hold is
> separate from *how much* of it to hold. Everyone holds the same risky portfolio; only the
> proportion differs.

---

## Formulas to know cold

```
PORTFOLIO RETURN AND RISK
  E(Rp) = Σ wi E(Ri)                            [always a weighted average]
  σp² = Σi Σj wi wj Cov(i,j)

  Two assets:  σp² = w1²σ1² + w2²σ2² + 2 w1 w2 ρ12 σ1 σ2
               Cov(1,2) = ρ12 σ1 σ2

  ρ = +1:  σp = w1σ1 + w2σ2           [NO diversification benefit]
  ρ =  0:  σp = √(w1²σ1² + w2²σ2²)
  ρ = −1:  σp = |w1σ1 − w2σ2|         [can reach ZERO]

FROM HISTORICAL DATA
  Mean       R̄ = ΣRt / n
  Variance   s² = Σ(Rt − R̄)²/(n − 1)
  Covariance Cov(A,B) = Σ(RA,t − R̄A)(RB,t − R̄B)/(n − 1)
  Correlation ρ = Cov(A,B)/(σA σB)

GLOBAL MINIMUM-VARIANCE PORTFOLIO (two assets)
  w1* = (σ2² − Cov(1,2)) / (σ1² + σ2² − 2 Cov(1,2))

UTILITY
  U = E(R) − ½ A σ²        A = risk aversion; higher A = more risk averse

CAPITAL ALLOCATION LINE
  E(Rp) = Rf + [(E(RP) − Rf)/σP] × σp        slope = Sharpe ratio of P
```

---

## Exam traps

> **Trap 1 — Averaging standard deviations.** Portfolio **return** is a weighted average; portfolio
> **standard deviation is not**, unless ρ = +1.

> **Trap 2 — Forgetting to square the weights.** `w1²σ1²`. Omitting the square is the most common
> calculation error in this module.

> **Trap 3 — Believing diversification needs negative correlation.** **Any ρ < +1** delivers a
> benefit.

> **Trap 4 — Treating the whole minimum-variance frontier as efficient.** Only the portion **above
> the GMVP** is. The rest is dominated.

> **Trap 5 — Sample vs population variance.** Historical data is a **sample**: divide by **n − 1**.
> On the BA II Plus that is **`Sx`**, not `σx`.

> **Trap 6 — Utility sign.** `U = E(R) − ½Aσ²`. The risk term is **subtracted**, and **higher A means
> more risk averse**.

> **Trap 7 — Assuming reported volatility for illiquid assets is real.** Appraisal-based pricing
> **smooths** returns and understates both volatility and correlation.

> **Trap 8 — Portfolio variance converging to zero.** It converges to the **average covariance** —
> systematic risk.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Asset A: E(R) = 13%, σ = 24%. Asset B: E(R) = 6%, σ = 9%. ρ = 0.15. Compute the expected return and standard deviation of a 55/45 A/B portfolio, and compare σp to the weighted average of the σs.

<details><summary>Answer</summary>

E(Rp) = 0.55(13) + 0.45(6) = 7.15 + 2.70 = **9.85%**

σp² = (0.55)²(24)² + (0.45)²(9)² + 2(0.55)(0.45)(0.15)(24)(9)
    = 0.3025(576) + 0.2025(81) + 2(0.2475)(0.15)(216)
    = 174.24 + 16.40 + 16.04
    = 206.68

σp = √206.68 = **14.38%**

Weighted average of the σs = 0.55(24) + 0.45(9) = 13.20 + 4.05 = **17.25%**.

The portfolio achieves **14.38%** against a 17.25% weighted average — a 2.87 percentage point reduction, obtained **for free**, purely because ρ = 0.15 < 1. Expected return is exactly the weighted average; risk is strictly below it.

</details>

**2.** Two assets have σ1 = 20% and σ2 = 30% with ρ = −1. What weights give a zero-risk portfolio?

<details><summary>Answer</summary>

With ρ = −1, σp = |w1σ1 − w2σ2|. Setting it to zero: w1(20) = w2(30), with w1 + w2 = 1.

w1 = σ2/(σ1 + σ2) = 30/(20 + 30) = **0.60**, w2 = **0.40**

Check: 0.60(20) − 0.40(30) = 12 − 12 = **0** ✓

The weights tilt toward the **less volatile** asset — you need more of the low-σ asset to offset the high-σ one. Perfect negative correlation essentially never occurs in practice, but it establishes the theoretical limit: with ρ = −1, risk can be eliminated entirely while retaining a positive expected return.

</details>

**3.** An investor with A = 7 is choosing between (i) E(R) = 7%, σ = 10% and (ii) E(R) = 12%, σ = 20%. Which do they prefer? What about an investor with A = 2?

<details><summary>Answer</summary>

U = E(R) − ½Aσ², with returns and σ in decimal form.

**A = 7:**
(i) U = 0.07 − 0.5(7)(0.01) = 0.07 − 0.035 = **0.035**
(ii) U = 0.12 − 0.5(7)(0.04) = 0.12 − 0.14 = **−0.020**
→ **Prefers (i)**, and finds (ii) worse than holding nothing.

**A = 2:**
(i) U = 0.07 − 0.5(2)(0.01) = 0.07 − 0.01 = **0.060**
(ii) U = 0.12 − 0.5(2)(0.04) = 0.12 − 0.04 = **0.080**
→ **Prefers (ii)**.

Same two portfolios, opposite conclusions. This is precisely why every investor selects a different point on the same capital allocation line: the efficient set is common to everyone, but the preferred point on it is personal.

</details>

**4.** Why is only the portion of the minimum-variance frontier above the GMVP considered efficient?

<details><summary>Answer</summary>

Because everything below it is **dominated**.

The minimum-variance frontier gives, for each level of **expected return**, the portfolio with the lowest variance. Plotted in σ/E(R) space it is a curve that bends back on itself, with the **global minimum-variance portfolio** at its leftmost point.

For any portfolio on the **lower** branch, there exists a portfolio on the **upper** branch with **exactly the same standard deviation and a higher expected return** — directly above it on the chart.

A risk-averse, return-maximising investor would never choose the lower one: it offers less return for identical risk. So only the **upper branch — from the GMVP rightward — is the efficient frontier**, and it is the only part of the opportunity set that any rational investor will hold.

</details>

**5.** Why does reported volatility understate true risk for private equity and real estate?

<details><summary>Answer</summary>

Because those assets are **valued by appraisal or by infrequent transactions**, not by continuous market pricing.

**Appraisal smoothing:** an appraiser anchors on the previous valuation and adjusts partially toward current conditions. The reported value therefore moves less than the true economic value, and the reported return series is artificially smooth.

**Stale pricing:** private assets are marked quarterly at best, and often with a lag. Sharp market moves within a quarter simply never appear in the series.

**Consequences:**
- **Volatility is understated** — sometimes by half or more
- **Correlation with public markets is understated**, because the smoothed series does not move in sync with observable prices
- Both distortions make the asset look like a **better diversifier than it is**, which flatters any mean-variance optimisation that includes it

**In practice:** un-smooth the return series before using it in an optimisation, or apply a haircut to the reported Sharpe ratio. And note the correlations tend to reveal themselves in a crisis, exactly when the diversification was needed.

</details>

---

## Done when

- [ ] I can rank the major asset classes on return, risk, and liquidity, and state the illiquidity caveat
- [ ] I can define risk aversion and state its three consequences
- [ ] I can compute portfolio expected return and standard deviation for two assets from scratch
- [ ] I can compute mean, variance, covariance, and correlation from historical data with the right denominator
- [ ] I can state what happens at ρ = +1, 0, and −1 and show diversification needs only ρ < 1
- [ ] I can identify the GMVP and explain why the lower frontier is dominated
- [ ] I can compute utility and show two investors ranking the same portfolios differently
- [ ] I answered the self-check cold, several days after first study

---

[Topic index](README.md)  ·  [LM02 Portfolio Risk and Return: Part II](lm-02-portfolio-risk-and-return-part-ii.md) →
