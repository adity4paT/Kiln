# QM · LM08 — The Return and Risk of a Financial Portfolio

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 14 |
| **Prerequisites** | LM5 (covariance, correlation), LM6 (expected values). |
| **Where it shows up** | 2 questions here, and this material is the mathematical core of Portfolio Management LM1–LM2. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate, interpret, and evaluate the expected return, variance, standard deviation, covariance, and correlation of portfolio returns
- describe, calculate, and interpret the minimum-variance portfolio and portfolios that lie on the efficient frontier
- explain the selection of an optimal portfolio, given an investor's risk aversion and the capital allocation line, and how this extends to the market portfolio and the capital market line

---

## Core concepts

### The one asymmetry that makes portfolio theory work

**Portfolio expected return is a simple weighted average. Portfolio risk is not.**

```
E(Rp) = Σ wᵢ E(Rᵢ)                           ← linear, always
σp²   = Σ Σ wᵢ wⱼ Cov(Rᵢ, Rⱼ)                 ← NOT linear
```

For two assets:

```
E(Rp) = w1 E(R1) + w2 E(R2)

σp² = w1²σ1² + w2²σ2² + 2 w1 w2 ρ12 σ1 σ2
```

Because `Cov(1,2) = ρ12 σ1 σ2`, the third term is the whole story: **portfolio variance falls as
correlation falls**, while expected return is untouched. That is diversification — a strictly
favourable trade, and it is free.

**The bounds:**

| ρ | Portfolio standard deviation |
| --- | --- |
| **+1** | `σp = w1σ1 + w2σ2` — the weighted average. **No diversification benefit at all** |
| **0** | `σp = √(w1²σ1² + w2²σ2²)` — meaningful reduction |
| **−1** | `σp = \|w1σ1 − w2σ2\|` — can be driven to **exactly zero** with the right weights |

> **The key insight:** for any ρ < +1, portfolio standard deviation is **strictly less than** the
> weighted average of the component standard deviations. Diversification works at any correlation
> below one — it does not require negative correlation, only imperfect correlation.

### Three assets and beyond

```
σp² = Σᵢ Σⱼ wᵢ wⱼ Cov(i,j)
```

For n assets there are `n` variance terms and `n(n − 1)` covariance terms. As `n` grows, the
**covariances dominate** — with 50 assets there are 50 variances and 2,450 covariances.

The consequence is one of the most important results in finance: as you add assets, portfolio
variance converges not to zero but to the **average covariance** among the assets. That residual is
**systematic (non-diversifiable) risk**. Only the asset-specific component disappears.

> This is why the market pays you for bearing systematic risk and **not** for bearing
> non-systematic risk — the latter can be eliminated for free, so no one will pay you to bear it.
> It is the entire argument behind CAPM (PM LM2).

### The minimum-variance frontier and the efficient frontier

Plot every possible portfolio of risky assets in **risk (x-axis) / expected return (y-axis)** space.
The left-hand boundary of that cloud is the **minimum-variance frontier**: for each level of
expected return, the portfolio with the lowest possible variance.

The leftmost point on it is the **global minimum-variance portfolio (GMVP)** — the lowest-risk
combination available from risky assets. For two assets:

```
w1* = (σ2² − Cov(1,2)) / (σ1² + σ2² − 2Cov(1,2))
```

The **efficient frontier** is the portion of the minimum-variance frontier **above and to the right
of the GMVP**. Portfolios on the lower half are *dominated*: for each one there is a portfolio with
the same risk and higher expected return directly above it. No rational investor holds a dominated
portfolio.

> **Trap:** the efficient frontier is only the **upper** half. Portfolios below the GMVP are on the
> minimum-variance frontier but are **not efficient**.

### Adding a risk-free asset: the capital allocation line

Combine the risk-free asset (return `Rf`, standard deviation zero) with a risky portfolio `P`:

```
E(Rp) = w_f × Rf + (1 − w_f) × E(RP)
σp    = (1 − w_f) × σP                    ← linear, because σ_f = 0 and Cov(f, P) = 0
```

Since both are linear in the weight, the set of achievable combinations is a **straight line** from
`Rf` through `P` — the **capital allocation line (CAL)**.

```
E(Rp) = Rf + [(E(RP) − Rf) / σP] × σp
```

The slope is `(E(RP) − Rf)/σP` — the **Sharpe ratio** of the risky portfolio. So:

> **The best CAL is the steepest one.** Among all risky portfolios, the investor wants the one
> whose CAL is tangent to the efficient frontier — the **tangency portfolio**, which is the portfolio
> with the **highest Sharpe ratio**.

Points on the CAL **between** Rf and the tangency portfolio mean lending (holding some risk-free
asset). Points **beyond** the tangency portfolio mean **borrowing** at the risk-free rate and
investing more than 100% of capital in the risky portfolio.

### Choosing the optimal portfolio: risk aversion

Every investor picks a point on the same CAL, but a **different** point, according to their risk
aversion. The standard utility function:

```
U = E(R) − ½ A σ²
```

where **A is the risk aversion coefficient** — higher A means more risk averse.

| A | Investor | Chooses |
| --- | --- | --- |
| High (e.g. 6–10) | Very risk averse | A point **low** on the CAL — mostly risk-free asset |
| Moderate (e.g. 3–4) | Typical | Near the tangency portfolio |
| Low (e.g. 1–2) | Risk tolerant | A point **beyond** the tangency portfolio — borrows to leverage |
| Negative | Risk **seeking** | Prefers risk for its own sake |
| Zero | Risk **neutral** | Cares only about expected return |

**Indifference curves** plot combinations of risk and return giving equal utility. A more risk-averse
investor has **steeper** curves — they demand a lot more return for each unit of extra risk. The
optimal portfolio is where the investor's highest attainable indifference curve is **tangent to the
CAL**.

### From the CAL to the capital market line

This is the step that generalises the result to the whole market.

Assume all investors have the **same expectations** (homogeneous expectations) and can borrow and
lend at the same risk-free rate. Then they all face the same efficient frontier, and all identify
the **same tangency portfolio**. If every investor holds that same risky portfolio, it must — in
equilibrium — be the **market portfolio**: every risky asset, weighted by market capitalisation.

The CAL through the market portfolio is the **capital market line (CML)**:

```
E(Rp) = Rf + [(E(RM) − Rf) / σM] × σp
```

**What follows — the two-fund separation theorem:** every investor holds just two things, the
risk-free asset and the market portfolio. The *proportion* between them is the only personal
decision; the composition of the risky part is the same for everyone.

> **CML vs. SML** — do not confuse them. The **CML** plots efficient portfolios against **total
> risk (σ)** and holds only for efficient portfolios. The **SML** (Portfolio Management LM2) plots
> **any** asset against **systematic risk (β)**. Different x-axis, different domain.

### The Sharpe ratio

```
Sharpe = (E(Rp) − Rf) / σp
```

Excess return per unit of **total** risk. It is the slope of the CAL, so maximising the Sharpe ratio
is the same problem as finding the tangency portfolio. Higher is better.

---

## Formulas to know cold

```
PORTFOLIO RETURN AND RISK
  E(Rp) = Σ wi E(Ri)                                    [always a weighted average]
  σp² = Σi Σj wi wj Cov(i,j)

  Two assets:
    σp² = w1²σ1² + w2²σ2² + 2 w1 w2 ρ12 σ1 σ2
    Cov(1,2) = ρ12 σ1 σ2

  Special cases:
    ρ = +1:  σp = w1σ1 + w2σ2                  [no diversification benefit]
    ρ =  0:  σp = √(w1²σ1² + w2²σ2²)
    ρ = −1:  σp = |w1σ1 − w2σ2|                [can reach ZERO]

GLOBAL MINIMUM-VARIANCE PORTFOLIO (two assets)
  w1* = (σ2² − Cov(1,2)) / (σ1² + σ2² − 2 Cov(1,2))

CAPITAL ALLOCATION LINE
  E(Rp) = Rf + [(E(RP) − Rf)/σP] × σp
  Slope = Sharpe ratio of portfolio P

CAPITAL MARKET LINE  (CAL through the MARKET portfolio)
  E(Rp) = Rf + [(E(RM) − Rf)/σM] × σp

UTILITY
  U = E(R) − ½ A σ²        A = risk aversion coefficient (higher = more risk averse)

SHARPE RATIO
  Sharpe = (E(Rp) − Rf) / σp        ← excess return per unit of TOTAL risk
```

---

## Exam traps

> **Trap 1 — Averaging standard deviations.** Portfolio **return** is a weighted average; portfolio
> **standard deviation is not**, unless ρ = +1. Never average σ.

> **Trap 2 — Squaring the weights.** In `w1²σ1²` the weight is **squared**. Forgetting the square is
> one of the most common calculation errors in this module.

> **Trap 3 — Believing diversification needs negative correlation.** Any **ρ < +1** delivers a
> benefit. Negative correlation makes it larger, but is not required.

> **Trap 4 — The whole minimum-variance frontier is efficient.** Only the portion **above the GMVP**
> is. The lower half is dominated.

> **Trap 5 — Confusing the CML and the SML.** CML: **total risk (σ)**, efficient portfolios only.
> SML: **systematic risk (β)**, any asset. Different axes, different scope.

> **Trap 6 — Forgetting that diversifiable risk is unpaid.** The market compensates **systematic**
> risk only, because non-systematic risk can be removed at no cost.

> **Trap 7 — Portfolio variance converging to zero.** It converges to the **average covariance**,
> not to zero. That floor is systematic risk.

> **Trap 8 — Utility sign.** `U = E(R) − ½Aσ²`. The risk term is **subtracted**, and higher A means
> **more** risk averse, so a risky portfolio's utility falls faster for them.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Asset A: E(R) = 12%, σ = 20%. Asset B: E(R) = 7%, σ = 11%. ρ = 0.25. Compute the expected return and standard deviation of a 60/40 A/B portfolio.

<details><summary>Answer</summary>

E(Rp) = 0.60(12) + 0.40(7) = 7.2 + 2.8 = **9.6%**

σp² = (0.60)²(20)² + (0.40)²(11)² + 2(0.60)(0.40)(0.25)(20)(11)
    = 0.36(400) + 0.16(121) + 2(0.24)(0.25)(220)
    = 144 + 19.36 + 26.4
    = 189.76

σp = √189.76 = **13.77%**

Note: the weighted average of the standard deviations would be 0.60(20) + 0.40(11) = **16.4%**. The portfolio achieves 13.77% — a 2.63 percentage point reduction, for free, purely because ρ = 0.25 < 1.

</details>

**2.** Two assets have σ1 = 30%, σ2 = 30%, and ρ = −1. What weights produce a zero-risk portfolio?

<details><summary>Answer</summary>

With ρ = −1, σp = |w1σ1 − w2σ2|. Setting this to zero:

w1(30) = w2(30), and w1 + w2 = 1 → **w1 = w2 = 0.50**

An equally weighted portfolio of two perfectly negatively correlated assets with **equal** standard deviations has **zero** risk.

In general, w1 = σ2/(σ1 + σ2). With unequal σ, the weights tilt toward the less volatile asset. Perfect negative correlation essentially never occurs in practice, but the case establishes the theoretical limit of diversification.

</details>

**3.** Explain why portfolio variance converges to the average covariance rather than to zero as assets are added.

<details><summary>Answer</summary>

For an equally weighted portfolio of n assets, portfolio variance is:

`σp² = (1/n)(average variance) + (1 − 1/n)(average covariance)`

As **n → ∞**, the first term goes to **zero** — the asset-specific (idiosyncratic) risk is fully diversified away. The second term goes to the **average covariance**, which is a positive constant.

That residual is **systematic risk**: the common exposure every asset shares to economy-wide factors — interest rates, growth, risk appetite. No amount of diversification within the asset class removes it.

This is the structural basis for CAPM: since idiosyncratic risk is removable at zero cost, no investor will pay to avoid it, and therefore the market cannot compensate anyone for bearing it. Only **systematic** risk earns a return.

</details>

**4.** Rf = 3%. A risky portfolio has E(R) = 11%, σ = 16%. Write the CAL and find the expected return of a portfolio with σ = 10%.

<details><summary>Answer</summary>

Slope = Sharpe ratio = (11 − 3)/16 = 8/16 = **0.50**

CAL: **E(Rp) = 3 + 0.50 × σp**

At σp = 10: E(Rp) = 3 + 0.50(10) = **8.0%**

The implied weight in the risky portfolio: σp = w × σP → 10 = w(16) → w = **62.5%** risky, 37.5% risk-free.

Check: 0.625(11) + 0.375(3) = 6.875 + 1.125 = **8.0%** ✓

</details>

**5.** Two risky portfolios: X has E(R) = 14%, σ = 22%. Y has E(R) = 9%, σ = 12%. Rf = 3%. Which gives the better CAL, and what does an investor wanting 14% expected return do?

<details><summary>Answer</summary>

Sharpe_X = (14 − 3)/22 = **0.500**
Sharpe_Y = (9 − 3)/12 = **0.500**

Identical Sharpe ratios → **identical CALs**. Neither dominates.

An investor wanting 14% can either hold X outright, or **borrow at 3%** and lever Y:
14 = 3 + 0.50σp → σp = 22%, the same risk. With Y: 22 = w(12) → w = 183%, i.e. borrow 83% of capital.

The Sharpe ratio is the only thing that matters in choosing the risky portfolio; leverage then sets the position on the line. If the two Sharpe ratios differed, every investor at every risk level would prefer the higher one.

</details>

**6.** An investor has A = 5. Compare the utility of (i) E(R) = 6%, σ = 8% and (ii) E(R) = 11%, σ = 18%.

<details><summary>Answer</summary>

U = E(R) − ½Aσ²  (with returns and σ in decimal form)

(i) U = 0.06 − 0.5(5)(0.08²) = 0.06 − 2.5(0.0064) = 0.06 − 0.016 = **0.044**

(ii) U = 0.11 − 0.5(5)(0.18²) = 0.11 − 2.5(0.0324) = 0.11 − 0.081 = **0.029**

**Portfolio (i) is preferred** despite offering 5 percentage points less expected return. With A = 5 this investor is highly risk averse, and the risk penalty on (ii) — 8.1 percentage points — more than consumes the extra return.

An investor with A = 2 would get U(i) = 0.0536 and U(ii) = 0.0776 and prefer **(ii)**. Same portfolios, opposite conclusion — which is exactly why every investor picks a different point on the same CAL.

</details>

**7.** State the assumptions that turn the CAL into the CML, and what the two-fund separation theorem says.

<details><summary>Answer</summary>

**Assumptions:** (1) **homogeneous expectations** — all investors share the same estimates of expected returns, variances and covariances; (2) all investors can **borrow and lend at the same risk-free rate**; (3) investors are rational mean-variance optimisers.

If everyone sees the same efficient frontier and the same Rf, everyone identifies the **same tangency portfolio**. But if every investor holds the identical risky portfolio, then in equilibrium that portfolio must contain **every risky asset in proportion to its market capitalisation** — it is the **market portfolio**. The CAL through it is the **CML**.

**Two-fund separation:** every investor's optimal portfolio is a combination of just **two funds** — the risk-free asset and the market portfolio. Risk aversion determines only the *proportion*; the composition of the risky component is identical for everyone. This is the theoretical justification for index investing.

</details>

---

## Done when

- [ ] I can compute portfolio expected return and standard deviation for two assets from scratch
- [ ] I can state what happens at ρ = +1, 0, and −1 and prove diversification needs only ρ < 1
- [ ] I can explain why portfolio variance converges to the average covariance
- [ ] I can identify the GMVP and explain why only the upper frontier is efficient
- [ ] I can write the CAL equation and explain why its slope is the Sharpe ratio
- [ ] I can compute utility with U = E(R) − ½Aσ² and rank portfolios for different A
- [ ] I can explain the assumptions that turn the CAL into the CML and state two-fund separation
- [ ] I can state the difference between the CML and the SML on both axes and scope
- [ ] I answered the self-check cold, several days after first study

---

← [LM07 Estimation and Hypothesis Testing](lm-07-estimation-and-hypothesis-testing.md)  ·  [Topic index](README.md)  ·  [LM09 Simulation of Financial Asset Prices and Returns](lm-09-simulation-of-financial-asset-prices-and-returns.md) →
