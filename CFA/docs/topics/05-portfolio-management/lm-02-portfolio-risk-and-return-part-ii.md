# PM · LM02 — Portfolio Risk and Return: Part II

## At a glance

| | |
| --- | --- |
| **Topic** | Portfolio Management (8-12% of the exam) |
| **Hours budgeted** | 11 |
| **Prerequisites** | LM1. Equity LM12 covers CAPM from the valuation side — this develops the portfolio theory behind it. |
| **Where it shows up** | 3 questions — the largest allocation in Portfolio Management. CAPM, the SML, and the four performance ratios are all near-certain. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe the implications of combining a risk-free asset with a portfolio of risky assets
- explain the capital allocation line (CAL) and the capital market line (CML)
- explain systematic and nonsystematic risk, including why an investor should not expect to receive additional return for bearing nonsystematic risk
- explain return generating models (including the market model) and their uses
- calculate and interpret beta
- explain the capital asset pricing model (CAPM), including its assumptions, and the security market line (SML)
- calculate and interpret the expected return of an asset using the CAPM
- describe and demonstrate applications of the CAPM and the SML
- calculate and interpret the Sharpe ratio, Treynor ratio, M2, and Jensen's alpha

---

## Core concepts

### From the CAL to the CML

Combining the risk-free asset with a risky portfolio `P` produces a **straight line**, because both
expected return and standard deviation are linear in the weight (σ of the risk-free asset is zero,
and its covariance with everything is zero):

```
E(Rp) = Rf + [(E(RP) − Rf) / σP] × σp          ← the capital allocation line
```

The slope is `P`'s **Sharpe ratio**, so the best CAL is the **steepest** — tangent to the efficient
frontier.

**Now add two assumptions:** all investors have **homogeneous expectations**, and all can borrow and
lend at the same risk-free rate. Then everyone faces the same efficient frontier and identifies the
**same tangency portfolio**. If every investor holds the identical risky portfolio, in equilibrium
that portfolio must be the **market portfolio** — every risky asset weighted by market
capitalisation.

The CAL through the market portfolio is the **capital market line**:

```
E(Rp) = Rf + [(E(RM) − Rf) / σM] × σp
```

**Two-fund separation:** every investor holds only two things — the risk-free asset and the market
portfolio. Risk aversion determines the **proportion**; the composition of the risky part is
identical for everyone. This is the theoretical case for index investing.

> **Leveraged positions:** points on the CML **beyond** the market portfolio require borrowing at
> `Rf` and investing more than 100% of capital in the market. In practice investors borrow above the
> risk-free rate, which **kinks** the CML downward beyond the tangency point.

### Systematic and non-systematic risk

```
Total risk = Systematic risk + Non-systematic risk
```

| | **Systematic (market) risk** | **Non-systematic (firm-specific) risk** |
| --- | --- | --- |
| Source | Economy-wide factors: rates, growth, inflation, risk appetite | Company or industry events: a product failure, a lawsuit, a strike |
| Diversifiable? | **No** | **Yes** |
| Compensated? | **Yes** | **No** |
| Measured by | **Beta** | Residual variance |

> **Why non-systematic risk is not compensated:** it can be eliminated **at no cost** by holding a
> diversified portfolio. Since any investor can remove it for free, no one will pay to avoid it — so
> the market cannot offer a premium for bearing it. If it did, investors would diversify the risk
> away while keeping the premium, an arbitrage that would be competed away immediately.
>
> Portfolio variance converges to the **average covariance** as assets are added (LM1), and that
> floor is systematic risk.

### Return generating models and beta

The **market model** is the single-factor empirical model:

```
Ri = αi + βi RM + εi
```

**Beta:**

```
βi = Cov(Ri, RM) / Var(RM) = ρ(i,M) × σi / σM
```

This is exactly the OLS slope from regressing the asset on the market (QM LM10). **Beta is a
regression slope.**

| β | Meaning |
| --- | --- |
| > 1 | Aggressive — amplifies market moves |
| = 1 | Moves with the market |
| 0 < β < 1 | Defensive |
| = 0 | Uncorrelated with the market |
| < 0 | Moves against the market |

**Portfolio beta is a simple weighted average:** `βp = Σ wᵢ βᵢ`. Beta is linear because it measures
exposure to one common factor, and exposures add. (Contrast with standard deviation, which is not
linear.)

### CAPM and the security market line

```
E(Ri) = Rf + βi [E(RM) − Rf]
```

**Assumptions:** risk-averse, utility-maximising, mean-variance optimising investors; frictionless
markets with no taxes or transaction costs; homogeneous expectations; unlimited borrowing and
lending at `Rf`; infinitely divisible assets; competitive markets.

**The SML** plots CAPM in β / E(R) space:

- **Above the SML** → the asset offers more return than its systematic risk requires →
  **undervalued**, buy
- **Below the SML** → **overvalued**
- **On the SML** → fairly priced

> **CML vs SML — the distinction is tested every time:**
>
> | | **CML** | **SML** |
> | --- | --- | --- |
> | x-axis | **Total risk (σ)** | **Systematic risk (β)** |
> | Applies to | **Efficient portfolios only** | **Any** asset or portfolio |
> | Slope | `(E(RM) − Rf)/σM` | `E(RM) − Rf` (the equity risk premium) |
> | Use | Asset allocation between Rf and the market | Valuing an individual security |
>
> Only the SML can evaluate an individual security, because an individual security is not efficient
> — it carries diversifiable risk the CML does not price.

### The four performance measures

| Measure | Formula | Risk measure used | Use for |
| --- | --- | --- | --- |
| **Sharpe ratio** | `(Rp − Rf) / σp` | **Total risk (σ)** | Comparing **total** portfolios — when the portfolio is the investor's entire holding |
| **Treynor ratio** | `(Rp − Rf) / βp` | **Systematic risk (β)** | Comparing **components** of a larger diversified portfolio |
| **M² (M-squared)** | `(Rp − Rf) × (σM/σp) + Rf` | Total risk | Same ranking as Sharpe, expressed in **percentage return** terms |
| **Jensen's alpha** | `αp = Rp − [Rf + βp(RM − Rf)]` | Systematic risk | **Excess return** over what CAPM requires — the measure of skill |

**Choosing between Sharpe and Treynor** is a genuine decision, and it is examinable:

- Use **Sharpe** when the portfolio being evaluated is the investor's **entire** wealth, so total
  risk is what they actually bear.
- Use **Treynor** when the portfolio is **one sleeve of a larger diversified whole**, so its
  firm-specific risk will be diversified away and only its systematic contribution matters.

**M²** exists because the Sharpe ratio is a dimensionless number that is hard to interpret. M²
rescales the portfolio to the market's volatility and reports the resulting return, so it can be
read directly as "this portfolio's return, adjusted to market risk". **It ranks portfolios
identically to the Sharpe ratio.**

**Jensen's alpha** is the vertical distance from the SML. Positive alpha means the manager earned
more than the systematic risk taken required — the standard measure of skill, subject to the
caveats in Equity LM12 about factor exposure masquerading as alpha.

### Limitations of CAPM

- **Roll's critique:** the true market portfolio (every risky asset, including human capital and
  private assets) is **unobservable**. Every empirical test is a joint test of CAPM and the proxy.
- **Empirical failures:** size, value, momentum, profitability, and low-volatility effects earn
  returns CAPM does not explain.
- **Beta instability** and sensitivity to estimation choices.
- **Single factor and single period.**
- Homogeneous expectations and frictionless markets are plainly false.

Multi-factor models (Equity LM12) address several of these. CAPM survives because its central
insight — **only non-diversifiable risk is compensated** — is correct and does not depend on the
model's specific form.

---

## Formulas to know cold

```
CAPITAL MARKET LINE   (the CAL through the MARKET portfolio)
  E(Rp) = Rf + [(E(RM) − Rf)/σM] × σp          slope = market Sharpe ratio
  Applies to EFFICIENT portfolios only;  x-axis is TOTAL risk (σ)

SECURITY MARKET LINE / CAPM
  E(Ri) = Rf + βi [E(RM) − Rf]                 slope = equity risk premium
  Applies to ANY asset;  x-axis is SYSTEMATIC risk (β)
  Above the SML → undervalued.  Below → overvalued.

BETA
  βi = Cov(Ri,RM)/Var(RM) = ρ(i,M) × σi/σM     ← the OLS regression slope
  βp = Σ wi βi                                  ← linear, a simple weighted average

RISK DECOMPOSITION
  Total risk = Systematic (β, COMPENSATED) + Non-systematic (diversifiable, NOT compensated)

PERFORMANCE MEASURES
  Sharpe  = (Rp − Rf) / σp          ← TOTAL risk;  use for the WHOLE portfolio
  Treynor = (Rp − Rf) / βp          ← SYSTEMATIC risk;  use for a COMPONENT
  M²      = (Rp − Rf) × (σM/σp) + Rf   ← same ranking as Sharpe, in % return terms
  Jensen's α = Rp − [Rf + βp(RM − Rf)]  ← vertical distance from the SML
```

---

## Exam traps

> **Trap 1 — Confusing the CML and the SML.** **CML: total risk (σ), efficient portfolios only.**
> **SML: systematic risk (β), any asset.** Only the SML evaluates an individual security.

> **Trap 2 — Using Sharpe when Treynor is correct.** Use **Treynor** for a **component** of a larger
> diversified portfolio (its specific risk will diversify away); use **Sharpe** when the portfolio
> is the investor's **entire** wealth.

> **Trap 3 — Thinking M² ranks differently from Sharpe.** It does **not** — it is a monotonic
> transformation. It exists only to express the same ranking in interpretable percentage terms.

> **Trap 4 — Believing total risk is compensated.** Only **systematic** risk is.

> **Trap 5 — Averaging standard deviations but not betas.** It is the reverse: **portfolio beta IS a
> weighted average**; portfolio standard deviation is not.

> **Trap 6 — Jensen's alpha sign errors.** `α = actual return − CAPM-required return`. Compute the
> required return first, then subtract.

> **Trap 7 — Forgetting the CML kink.** Investors borrow above the risk-free rate, so the CML is
> flatter beyond the tangency portfolio in practice.

> **Trap 8 — Overlooking Roll's critique.** The market portfolio is unobservable; every CAPM test is
> a joint test of the model and the index proxy.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Rf = 3%, E(RM) = 9%, σM = 16%. A portfolio has E(R) = 11%, σ = 22%, β = 1.3. Compute its Sharpe ratio, Treynor ratio, M², and Jensen's alpha.

<details><summary>Answer</summary>

**Sharpe** = (11 − 3)/22 = 8/22 = **0.364**
(Market Sharpe = (9 − 3)/16 = 0.375 — the portfolio is slightly *worse* on total risk.)

**Treynor** = (11 − 3)/1.3 = 8/1.3 = **6.15**

**M²** = (11 − 3) × (16/22) + 3 = 8 × 0.7273 + 3 = 5.818 + 3 = **8.82%**
The market returned 9%, so on a risk-adjusted basis the portfolio **underperformed by 0.18 percentage points** — consistent with its lower Sharpe ratio.

**Jensen's alpha** = 11 − [3 + 1.3(9 − 3)] = 11 − [3 + 7.8] = 11 − 10.8 = **+0.20%**

Note the conflict: **positive alpha but a below-market Sharpe ratio.** The portfolio beat its CAPM requirement on *systematic* risk, but carries substantial *non-systematic* risk (σ of 22% is high for β of 1.3). If this is the investor's entire portfolio, Sharpe is the right measure and it underperformed. If it is one sleeve of a diversified whole, alpha and Treynor are right and it added value.

</details>

**2.** Explain why the CML cannot be used to evaluate an individual stock.

<details><summary>Answer</summary>

The CML prices **total risk (σ)**, and it does so on the assumption that the portfolio is **efficient** — that it carries no diversifiable risk.

An individual stock is **not efficient**. Most of its total risk is **firm-specific**, which the market does not compensate because it can be eliminated for free. Plotting a single stock against the CML would ask the market to pay for diversifiable risk, which it does not do — so virtually every individual stock plots **below** the CML, and that tells you nothing about whether it is mispriced.

The **SML** is the correct tool: it prices **systematic risk (β)** only, and it applies to **any** asset, efficient or not. A stock above the SML offers more than its systematic risk requires and is undervalued; below it, overvalued.

In short: the CML is for **asset allocation** between the risk-free asset and the market; the SML is for **security selection**.

</details>

**3.** A stock has β = 0.75, and the risk-free rate is 4% with an equity risk premium of 5.5%. Its expected return is 9%. Is it correctly priced?

<details><summary>Answer</summary>

CAPM required return = 4% + 0.75(5.5%) = 4% + 4.125% = **8.125%**

Expected return of 9% **exceeds** the required 8.125% by **0.875 percentage points** — a positive alpha. The stock plots **above the SML** and is **undervalued**. Buy.

Two caveats worth stating: the 9% expected return is **your forecast**, not an observable, so the conclusion is only as good as that estimate. And a 0.875% alpha is small relative to the estimation error in beta and the equity risk premium — it is not a conviction-sized mispricing.

</details>

**4.** Two funds: Fund X has Sharpe 0.62 and Treynor 5.8. Fund Y has Sharpe 0.48 and Treynor 7.1. Which is better?

<details><summary>Answer</summary>

**It depends on how the fund will be held.**

**If it is the investor's entire portfolio → Fund X.** With no other holdings, the investor bears the fund's **total risk**, so the **Sharpe ratio** (excess return per unit of σ) is the right measure. X delivers more return per unit of total risk.

**If it is one sleeve of a larger diversified portfolio → Fund Y.** The fund's firm-specific risk will be diversified away by the rest of the portfolio, so only its **systematic** contribution matters — measured by the **Treynor ratio**. Y delivers more return per unit of beta.

**Why the rankings conflict:** Fund Y must have substantially more **non-systematic** risk relative to its beta (a lower R² against the market). That extra idiosyncratic volatility penalises its Sharpe ratio but not its Treynor ratio. Standing alone, Y is carrying uncompensated risk; inside a diversified portfolio, that risk disappears and Y's superior systematic efficiency shows through.

This is exactly the scenario the Sharpe/Treynor distinction exists to resolve.

</details>

**5.** Why must the tangency portfolio be the market portfolio in equilibrium?

<details><summary>Answer</summary>

Because of **homogeneous expectations**.

If every investor has the same estimates of expected returns, variances, and covariances, then every investor constructs the **same efficient frontier**. If they can also all borrow and lend at the same risk-free rate, every investor draws the **same CAL** and identifies the **same tangency portfolio** — the one with the highest Sharpe ratio.

Now ask what happens in **equilibrium**, when all securities must be held by someone. If every investor holds the identical risky portfolio, then the aggregate of all investors' holdings *is* that portfolio. But the aggregate of all holdings is, by definition, **every risky asset in proportion to its market value** — the market portfolio.

Therefore the tangency portfolio **must be** the market portfolio. Any asset not in it would have no buyers and its price would fall until it became attractive enough to include.

**The consequence — two-fund separation:** every investor holds only the risk-free asset and the market portfolio, differing solely in the proportion. It is the theoretical case for index investing.

</details>

**6.** Explain the difference between Jensen's alpha and the Treynor ratio, given that both use beta.

<details><summary>Answer</summary>

Both adjust for **systematic risk only**, but they express the result differently.

**Treynor ratio = (Rp − Rf)/βp** is a **ratio** — excess return **per unit** of beta. It is scale-free, so it ranks portfolios regardless of their risk level.

**Jensen's alpha = Rp − [Rf + βp(RM − Rf)]** is a **difference** — the excess return **above** what CAPM required, in percentage points. It is the vertical distance from the SML.

**When they diverge:** consider two portfolios each with alpha of +1%, one with β = 0.5 and one with β = 2.0. Their alphas are equal, but the low-beta portfolio generated that 1% on far less systematic risk, so its **Treynor ratio is much higher**. The ratio rewards efficiency; alpha rewards magnitude.

**Practical use:** alpha answers 'how much value did this manager add?' — which matters for fees and for attribution. Treynor answers 'how efficiently did they use the systematic risk they took?' — which matters when choosing between managers of different risk levels to slot into a portfolio.

</details>

---

## Done when

- [ ] I can explain how the CAL becomes the CML and what assumptions the step requires
- [ ] I can state two-fund separation and why it implies index investing
- [ ] I can decompose total risk and explain why non-systematic risk earns no premium
- [ ] I can compute beta from covariance and correlation, and portfolio beta as a weighted average
- [ ] I can compute a CAPM required return and place a security relative to the SML
- [ ] I can reproduce the CML vs SML table from memory on all four rows
- [ ] I can compute all four performance measures and choose between Sharpe and Treynor correctly
- [ ] I can explain why M² ranks identically to Sharpe
- [ ] I can state CAPM's assumptions and limitations including Roll's critique
- [ ] I answered the self-check cold, several days after first study

---

← [LM01 Portfolio Risk and Return: Part I](lm-01-portfolio-risk-and-return-part-i.md)  ·  [Topic index](README.md)  ·  [LM03 Portfolio Management: An Overview](lm-03-portfolio-management-an-overview.md) →
