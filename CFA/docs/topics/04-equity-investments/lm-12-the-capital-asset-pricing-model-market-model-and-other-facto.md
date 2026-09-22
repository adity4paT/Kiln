# EQ · LM12 — The Capital Asset Pricing Model, Market Model, and Other Factor-Based Equity Models

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | QM LM8 (portfolio math, CAL/CML), QM LM10 (regression). |
| **Where it shows up** | 2 questions. CAPM calculation is a certainty. Previews Portfolio Management LM2. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the use of the CAPM and the market model to estimate a company's required return on equity
- describe the arbitrage pricing theory and the importance of multi-factor models used in equity investing

---

## Core concepts

### The capital asset pricing model

```
E(Ri) = Rf + βi × [E(RM) − Rf]
```

| Term | Meaning |
| --- | --- |
| **Rf** | Risk-free rate — a government security matched to the horizon |
| **βi** | The asset's **systematic risk** — sensitivity to market movements |
| **E(RM) − Rf** | The **equity risk premium** — the market's excess return over the risk-free rate |
| **βi × ERP** | The asset's own risk premium |

**The core claim:** only **systematic risk is compensated.** Non-systematic (firm-specific) risk can
be diversified away at no cost (QM LM8), so no investor will pay to avoid it and the market cannot
reward anyone for bearing it.

### Beta

```
βi = Cov(Ri, RM) / Var(RM) = ρ(i,M) × σi / σM
```

This is exactly the **OLS slope coefficient** from regressing the asset's returns on the market's
(QM LM10) — beta *is* a regression slope.

| β | Interpretation |
| --- | --- |
| **> 1** | More volatile than the market; **aggressive**. Higher required return |
| **= 1** | Moves with the market |
| **0 < β < 1** | Less volatile; **defensive** |
| **= 0** | Uncorrelated with the market — required return equals Rf |
| **< 0** | Moves against the market. Rare, and valuable for diversification |

**Estimation issues that matter in practice:**

- **Which market index?** Different proxies give different betas.
- **Which period and frequency?** Five years of monthly data is conventional; daily data over one
  year gives a different answer.
- **Betas are unstable** and tend to revert toward 1 over time, which is why **adjusted beta** is
  widely used: `adjusted β = (2/3) × raw β + (1/3) × 1`.
- **Thinly traded stocks** produce downward-biased betas because prices are stale.
- For a **private company or a project**, use the **pure-play method**: take a listed comparable's
  beta, un-lever it to remove the comparable's capital structure, then re-lever it at the subject's
  capital structure.

### The security market line

The CAPM plotted in **β / expected return** space.

```
E(R)
  │                                    ╱ SML
  │                            ╱ ──── slope = ERP
  │                    ╱  ● A  (above the SML → undervalued)
  │            ╱
  │    ╱  ● B  (below the SML → overvalued)
  │ Rf
  └──────────────────────────────── β
              1.0
```

- A security **above** the SML offers **more** return than its systematic risk requires →
  **undervalued**, buy.
- **Below** the SML → **overvalued**, sell.
- **On** the SML → fairly priced.

> **SML vs. CML — do not confuse them** (QM LM8). The **CML** plots **efficient portfolios** against
> **total risk (σ)**. The **SML** plots **any asset or portfolio** against **systematic risk (β)**.
> Different x-axis, different domain. Only the SML can be used to assess an individual security.

### The market model

The empirical implementation, estimated by regression:

```
Ri = αi + βi RM + εi
```

| Estimate | Interpretation |
| --- | --- |
| **α** | Return not explained by market exposure. **Jensen's alpha** — a significantly positive α indicates outperformance relative to the risk taken |
| **β** | The regression slope — systematic risk |
| **R²** | The proportion of the asset's variance explained by the market — its **systematic share**. `1 − R²` is firm-specific and diversifiable |

> **Interpreting a low R²:** a stock with R² = 0.20 has 80% of its return variation driven by
> firm-specific factors. Per CAPM that 80% is uncompensated — it can be diversified away for free.
> The stock is therefore only sensible to hold inside a portfolio large enough to diversify it.

### Assumptions and limitations of CAPM

**The assumptions:** investors are risk-averse, utility-maximising, and mean-variance optimisers;
**homogeneous expectations**; a single-period horizon; unlimited borrowing and lending at the
risk-free rate; frictionless markets with no taxes or transaction costs; infinitely divisible assets.

**The limitations:**

- **The market portfolio is unobservable** — Roll's critique. Any test of CAPM is a joint test of the
  model and of whether the chosen index proxies the true market portfolio.
- **Empirically, CAPM underperforms.** Size, value, momentum, profitability, and low-volatility
  effects have persistently earned returns CAPM does not explain.
- **Beta is unstable** over time and sensitive to estimation choices.
- **Single factor.** Real return variation clearly has multiple systematic sources.
- **Single period.** Real investment horizons are multi-period.

> **Why it is still taught and used:** CAPM is **simple, intuitive, and internally coherent**, and it
> establishes the central idea that only **non-diversifiable risk is compensated**. That insight
> survives the model's empirical failures and underlies everything that replaced it.

### Arbitrage pricing theory

APT generalises CAPM to **multiple systematic factors**:

```
E(Ri) = Rf + βi,1 λ1 + βi,2 λ2 + ... + βi,k λk
```

where each `βi,k` is the asset's sensitivity to factor `k` and each `λk` is that factor's risk
premium.

**APT's assumptions are far weaker than CAPM's** — which is its main advantage:

1. Returns are generated by a **factor model**
2. Asset-specific risk can be diversified away
3. **No arbitrage opportunities** exist in well-diversified portfolios

Notably, APT does **not** require the market portfolio, homogeneous expectations, or mean-variance
optimising investors.

**The catch:** APT does **not tell you what the factors are**, or how many there are. It is a
framework, not a specification. That is both its flexibility and its practical weakness.

### Multi-factor models

| Type | Factors | Used for |
| --- | --- | --- |
| **Macroeconomic** | GDP growth, inflation, interest rates, credit spreads | Explaining returns by economic surprises |
| **Fundamental** | Size, value (book-to-market), momentum, profitability, quality, low volatility | Style analysis, portfolio construction, performance attribution |
| **Statistical** | Factors extracted by principal components analysis | Maximum explanatory power, minimum interpretability |

**The best-known fundamental models:**

- **Fama–French three-factor:** market, **size** (SMB — small minus big), **value** (HML — high minus
  low book-to-market).
- **Carhart four-factor:** adds **momentum** (WML — winners minus losers).
- **Fama–French five-factor:** adds **profitability** (RMW) and **investment** (CMA).

**Why practitioners use them:**

- Better **explanation** of realised returns than a single factor
- **Performance attribution** — separating a manager's return into factor exposure (cheaply
  replicable) and genuine skill (alpha)
- **Risk management** — identifying unintended factor bets in a portfolio
- **Portfolio construction** — deliberate, targeted factor exposures ("smart beta")

> **The most consequential practical use:** if a manager's outperformance is fully explained by a
> persistent small-cap and value tilt, it is **factor exposure, not skill** — and it can be bought
> through a cheap index fund rather than paid for at active fees. Multi-factor attribution is how
> that question is answered, and it has reshaped the asset management industry.

---

## Formulas to know cold

```
CAPM
  E(Ri) = Rf + βi [E(RM) − Rf]

BETA
  βi = Cov(Ri, RM) / Var(RM) = ρ(i,M) × σi / σM      ← this IS the OLS regression slope
  Adjusted beta = (2/3) × raw β + (1/3) × 1
  Portfolio beta = Σ wi βi                           ← weighted average, and it IS linear

MARKET MODEL (the empirical regression)
  Ri = αi + βi RM + εi
  α = Jensen's alpha (return unexplained by market exposure)
  R² = systematic share of variance;  1 − R² = firm-specific, diversifiable

SECURITY MARKET LINE
  Above the SML → undervalued (buy).  Below → overvalued.  On → fairly priced.
  CML: efficient portfolios vs TOTAL risk (σ).  SML: ANY asset vs SYSTEMATIC risk (β).

ARBITRAGE PRICING THEORY
  E(Ri) = Rf + βi,1 λ1 + βi,2 λ2 + ... + βi,k λk
  Assumes only: a factor model, diversifiable specific risk, no arbitrage.
  Does NOT specify the factors.

FAMA-FRENCH / CARHART
  3-factor: market + SMB (size) + HML (value)
  4-factor: + WML (momentum)
  5-factor: + RMW (profitability) + CMA (investment)
```

---

## Exam traps

> **Trap 1 — Confusing the CML and the SML.** **CML: total risk (σ), efficient portfolios only.**
> **SML: systematic risk (β), any asset.** Only the SML evaluates an individual security.

> **Trap 2 — Thinking CAPM compensates total risk.** It compensates **systematic risk only**.
> Firm-specific risk is diversifiable and therefore unpaid.

> **Trap 3 — Portfolio beta is not a weighted average.** It **is** — beta is linear. (Unlike
> standard deviation, which is not.) This one is the reverse trap: candidates over-apply the
> "risk isn't linear" rule.

> **Trap 4 — Misreading R².** R² is the **systematic** share of variance. `1 − R²` is firm-specific.
> A low R² means most of the stock's movement is idiosyncratic.

> **Trap 5 — Thinking APT specifies its factors.** It does **not**. APT says a factor structure
> exists; identifying the factors is an empirical problem outside the theory.

> **Trap 6 — Forgetting Roll's critique.** The true market portfolio is unobservable, so every
> empirical test of CAPM is a **joint test** of the model and the index proxy.

> **Trap 7 — Treating factor returns as alpha.** Outperformance explained by a persistent size or
> value tilt is **factor exposure**, replicable cheaply — not skill.

> **Trap 8 — Using a raw beta for a private company or project.** Use the **pure-play method**:
> un-lever a comparable's beta, then re-lever at the subject's capital structure.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** The risk-free rate is 3.2%, the expected market return is 8.7%, and a stock's beta is 1.35. Compute the required return. If the stock's expected return is 12%, is it undervalued?

<details><summary>Answer</summary>

Equity risk premium = 8.7% − 3.2% = 5.5%

Required return = 3.2% + 1.35 × 5.5% = 3.2% + 7.425% = **10.63%**

Expected return (12%) **exceeds** required return (10.63%) by 1.37 percentage points → the stock plots **above the SML** → it is **undervalued**. Buy.

The 1.37% gap is the stock's **alpha** on this estimate. Whether to act on it depends on how confident you are in the 12% expected return — which is your own forecast, not an observable.

</details>

**2.** A portfolio holds 40% in a stock with beta 0.8, 35% in a stock with beta 1.4, and 25% in a stock with beta 1.9. Compute the portfolio beta.

<details><summary>Answer</summary>

βp = 0.40(0.8) + 0.35(1.4) + 0.25(1.9)
   = 0.32 + 0.49 + 0.475
   = **1.285**

Note that **beta is linear** — the portfolio beta is a simple weighted average, unlike standard deviation, which requires the covariance terms. This is because beta measures exposure to a single common factor, and exposures add.

The portfolio is more volatile than the market in systematic terms: a 1% market move implies roughly a 1.29% portfolio move.

</details>

**3.** Explain why CAPM says firm-specific risk is not compensated.

<details><summary>Answer</summary>

Because it can be **eliminated at no cost**.

As assets are added to a portfolio, the asset-specific component of variance diversifies away — portfolio variance converges to the **average covariance**, not to zero (QM LM8). The residual is systematic risk, which no amount of diversification within the asset class removes.

Since any investor can eliminate firm-specific risk for free simply by diversifying, **no investor will pay to avoid it**, and therefore **no market can offer compensation for bearing it**. If it did, investors would diversify away the risk while keeping the premium — an arbitrage that would be competed away instantly.

Only **systematic risk** — the exposure everyone must bear because it cannot be diversified — commands a premium. That is the single most important idea in CAPM, and it survives the model's empirical failures.

</details>

**4.** Compare CAPM and APT on their assumptions and their practical usefulness.

<details><summary>Answer</summary>

**CAPM's assumptions are strong:** homogeneous expectations, a single period, frictionless markets, unlimited risk-free borrowing and lending, and — critically — the existence of an **identifiable market portfolio** containing every risky asset.

**APT's assumptions are far weaker:** returns follow a factor model, asset-specific risk is diversifiable, and **no arbitrage opportunities** exist in well-diversified portfolios. It needs no market portfolio, no homogeneous expectations, and no mean-variance optimising investors.

**APT's advantages:** weaker assumptions, multiple systematic factors (which matches the evidence far better than one), and immunity to Roll's critique.

**APT's practical weakness:** it does **not tell you what the factors are** or how many exist. It is a framework, not a specification. That leaves the hard empirical work — identifying the factors and estimating their premia — entirely outside the theory, and different researchers reach different answers.

**In practice:** CAPM is used for its simplicity and because a single-factor cost of equity is often good enough for valuation. APT-style **multi-factor models** are used where the question is explanation, attribution, or risk decomposition.

</details>

**5.** A fund has outperformed its benchmark by 3% a year for eight years. A four-factor regression shows significant positive loadings on size and value, and an alpha of 0.2% that is not statistically significant. What do you conclude?

<details><summary>Answer</summary>

**The outperformance is factor exposure, not skill.**

The fund has persistently tilted toward **small-cap** and **value** stocks. Both have historically earned premia over the broad market, and a four-factor model attributes the 3% almost entirely to those loadings. The residual alpha of 0.2% is **not statistically distinguishable from zero** — there is no evidence of skill beyond the factor bets.

**Implications:**
- The same exposure can be obtained through a **cheap small-cap value index fund**, at a fraction of active fees. Paying active fees for replicable factor exposure is a poor bargain.
- The fund's future returns depend on whether **those factor premia persist**, not on the manager's stock selection. Both size and value have gone through long periods of underperformance.
- The correct **benchmark** for this fund is a small-cap value index, not the broad market. Measured against the right benchmark, the fund has been roughly flat.

This is the most consequential practical application of multi-factor models, and it is the analysis that reshaped the asset management fee structure.

</details>

**6.** Why is adjusted beta used, and what does the formula assume?

<details><summary>Answer</summary>

**Raw betas are unstable.** A beta estimated from five years of monthly returns is a noisy statistic, and empirically betas **revert toward 1.0** over time — an extreme beta of 2.2 or 0.3 is unlikely to persist at that level.

Part of this is genuine (companies mature, diversify, and change capital structure) and part is estimation error, which by definition does not repeat.

**Adjusted beta = (2/3) × raw β + (1/3) × 1.0** shrinks the estimate one-third of the way toward 1.0.

**What it assumes:** that the true beta follows a mean-reverting process with the market beta of 1.0 as its long-run centre, and that the 2/3–1/3 weighting reflects the relative reliability of the sample estimate versus the prior. The specific weights come from empirical work (Blume) and are a convention, not a derivation.

**Practical effect:** it produces more stable required-return estimates and reduces the tendency to over-extrapolate extreme sample betas — which matters, because a beta error flows directly into the cost of equity and therefore into every valuation.

</details>

---

## Done when

- [ ] I can compute a required return with CAPM and assess over/undervaluation against the SML
- [ ] I can compute beta from covariance and from correlation, and explain that it is a regression slope
- [ ] I can state why portfolio beta is a weighted average while portfolio standard deviation is not
- [ ] I can distinguish the CML from the SML on both axis and domain
- [ ] I can explain why only systematic risk is compensated
- [ ] I can list CAPM's assumptions and limitations, including Roll's critique
- [ ] I can state APT's three assumptions and explain what it does not specify
- [ ] I can name the Fama-French and Carhart factors and explain factor attribution versus alpha
- [ ] I answered the self-check cold, several days after first study

---

← [LM11 Equity Analyst Research Reports](lm-11-equity-analyst-research-reports.md)  ·  [Topic index](README.md)
