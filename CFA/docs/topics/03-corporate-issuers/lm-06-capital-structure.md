# CI · LM06 — Capital Structure

## At a glance

| | |
| --- | --- |
| **Topic** | Corporate Issuers (6-9% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM5 (ROIC vs WACC). Equity LM12 covers the cost of equity via CAPM. |
| **Where it shows up** | 2 questions. WACC calculation is near-certain; Modigliani–Miller propositions appear regularly. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate and interpret the weighted-average cost of capital for a company
- explain factors affecting capital structure and the weighted-average cost of capital
- explain the Modigliani–Miller propositions regarding capital structure
- describe optimal and target capital structures

---

## Core concepts

### Weighted average cost of capital

```
WACC = wd × rd × (1 − t)  +  wp × rp  +  we × re

where  wd, wp, we are the weights of debt, preferred, and common equity
       rd = before-tax cost of debt      t = marginal tax rate
       rp = cost of preferred            re = cost of common equity
```

Three points that are tested every time:

1. **Use market values, not book values,** for the weights. Book equity is a historical accounting
   residual; market value is what the capital is actually worth. The one exception in practice is
   debt, where book value is often a reasonable proxy for market value.
2. **Only the cost of debt is tax-adjusted.** Interest is tax-deductible; dividends are not. This is
   the single most examinable asymmetry in the module.
3. **Use the target capital structure**, not necessarily today's, when the company has stated one
   and is moving toward it.

**Component costs:**

| Component | How to estimate it |
| --- | --- |
| **Cost of debt** | The **yield to maturity** on the company's outstanding debt, or the yield on comparably rated debt. **Not** the coupon rate, and **not** the historical rate on old borrowings |
| **Cost of preferred** | `rp = Dp / Pp` — the preferred dividend over the preferred's market price |
| **Cost of equity** | **CAPM:** `re = Rf + β(E(RM) − Rf)`. Or the **dividend discount** approach: `re = D1/P0 + g`. Or a **bond yield plus risk premium**: `re = rd + 3% to 5%` |

### What drives the cost of capital

| Factor | Effect on WACC |
| --- | --- |
| **Interest rate level** | Higher rates raise both rd and re |
| **Business risk** (volatility of operating income) | Higher business risk → higher re and rd |
| **Financial risk** (leverage) | More debt → higher risk for *both* debtholders and shareholders |
| **Tax rate** | A higher tax rate makes debt **cheaper** after tax, lowering WACC |
| **Marketability and liquidity** | Illiquid securities demand a premium |
| **Sales risk and operating leverage** | Together these determine business risk |

**Operating leverage** — the proportion of fixed to variable costs:

```
Degree of operating leverage (DOL) = % change in operating income / % change in units sold
                                   = Q(P − V) / [Q(P − V) − F]
```

**Financial leverage** — the use of fixed-cost financing:

```
Degree of financial leverage (DFL) = % change in net income / % change in operating income
                                   = EBIT / (EBIT − Interest)

Degree of total leverage (DTL) = DOL × DFL
```

> A company with high **operating** leverage should generally carry **less financial** leverage.
> Stacking both magnifies the swing in net income enormously — and a fixed interest bill against
> volatile operating income is what turns a downturn into a default.

### Modigliani–Miller

The MM propositions are a thought experiment, not a description of reality. Their value is that they
isolate **exactly** which frictions make capital structure matter — by assuming them away and showing
that without them, nothing matters.

**The assumptions:** no taxes, no bankruptcy costs, no agency costs, no asymmetric information,
perfect and frictionless markets, and individuals can borrow at the same rate as corporations.

**MM Proposition I (no taxes) — capital structure is irrelevant.**

```
V_levered = V_unlevered
```

The value of a firm is determined by its **assets and their cash flows**, not by how those assets are
financed. Slicing a pie differently does not change the size of the pie. If a levered and an
unlevered firm with identical assets had different values, investors would use **homemade leverage**
— borrowing personally to replicate the levered firm's payoff — and arbitrage the difference away.

**MM Proposition II (no taxes) — the cost of equity rises with leverage, exactly offsetting.**

```
re = r0 + (r0 − rd) × (D/E)
```

Adding cheap debt raises the risk borne by shareholders, so `re` rises by precisely enough to leave
WACC unchanged. **WACC is constant** regardless of capital structure.

**MM with corporate taxes — debt becomes valuable.**

```
V_levered = V_unlevered + (t × D)          ← the value of the interest tax shield
```

Interest is tax-deductible, so a levered firm pays less tax and the government's claim on the cash
flows shrinks. Under this version WACC **declines** with leverage and the implied optimum is
**100% debt** — a conclusion that is obviously wrong, which is the point: something else must be
pushing back.

```
re = r0 + (r0 − rd)(1 − t)(D/E)
```

### What pushes back: the static trade-off theory

```
V_levered = V_unlevered + PV(tax shield) − PV(financial distress costs)
```

**Costs of financial distress:**

| | |
| --- | --- |
| **Direct** | Legal fees, court costs, administration — relatively small |
| **Indirect** | **Much larger.** Lost customers (will they honour the warranty?), lost suppliers (will they extend credit?), key employee departures, forced asset sales at distressed prices, management distraction, inability to fund investment |

The **probability** of distress rises with leverage, and the **cost** if it happens is higher for
companies with intangible assets, high growth options, or customer relationships that depend on
perceived stability. A software company has more to lose from distress than a property company with
hard, saleable assets.

**The optimal capital structure** is where the marginal tax benefit of one more unit of debt equals
the marginal expected cost of distress — equivalently, **where WACC is minimised and firm value is
maximised**. It is a flat-bottomed curve in practice, which is why companies target a *range*.

### Other theories

**Pecking order theory** (asymmetric information). Managers know more than investors, so issuing
equity signals that management believes the shares are overvalued — and the market marks the price
down. Companies therefore prefer, in strict order:

```
1. Internal funds (retained earnings)   ← no signal, no issuance cost
2. Debt                                 ← weak signal
3. Equity                               ← strongest negative signal; last resort
```

This explains an empirical puzzle the trade-off theory cannot: **profitable companies tend to use
less debt**, because they can fund themselves internally.

**Signalling.** Because of that asymmetry, financing decisions convey information. Issuing debt
signals confidence in future cash flows (you must service it); issuing equity signals the opposite.

**Agency costs of free cash flow.** Debt **disciplines** management — a fixed interest obligation
constrains empire-building and forces the return of cash that would otherwise be spent on
value-destroying acquisitions.

### Target vs. actual capital structure

Companies set a **target** (usually a range, e.g. debt/capital of 30–40%) and drift within it,
because:

- Issuance costs make continuous adjustment uneconomic
- Market timing — issue equity when the share price is strong, debt when spreads are tight
- Share price movements change the market-value weights without any action by the company
- Temporary deviations for acquisitions, with a stated plan to de-lever

> **For the analyst:** use the **target** structure in WACC when the company has stated one and is
> credibly moving toward it. Use the current market-value structure when it is not.

**Country and industry differences:** leverage varies systematically with the institutional
environment — the strength of creditor rights and bankruptcy law, the depth of local bond markets,
the tax regime, the prevalence of bank versus market financing, and ownership concentration.
Comparing a US company's leverage to a Japanese or German peer without accounting for these is
meaningless.

---

## Formulas to know cold

```
WACC = wd × rd × (1 − t) + wp × rp + we × re        ← MARKET-value weights
  Only DEBT is tax-adjusted. Preferred and common dividends are not deductible.

COMPONENT COSTS
  Cost of debt      = YTM on outstanding debt (not the coupon)
  Cost of preferred = Dp / Pp
  Cost of equity    = Rf + β(E(RM) − Rf)          [CAPM]
                    = D1/P0 + g                    [dividend discount]
                    = rd + 3% to 5%                [bond yield plus risk premium]

LEVERAGE
  DOL = %Δ operating income / %Δ units = Q(P − V)/[Q(P − V) − F]
  DFL = %Δ net income / %Δ operating income = EBIT/(EBIT − Interest)
  DTL = DOL × DFL

MODIGLIANI-MILLER
  No taxes:
    Prop I:   V_L = V_U                     (capital structure IRRELEVANT)
    Prop II:  re = r0 + (r0 − rd)(D/E)      (WACC CONSTANT)
  With corporate taxes:
    Prop I:   V_L = V_U + tD                (tax shield adds value)
    Prop II:  re = r0 + (r0 − rd)(1 − t)(D/E)   (WACC DECLINES with leverage)

STATIC TRADE-OFF
  V_L = V_U + PV(tax shield) − PV(financial distress costs)
  Optimum: WACC minimised = firm value maximised

PECKING ORDER:  internal funds → debt → equity  (equity is the last resort)
```

---

## Exam traps

> **Trap 1 — Book value weights.** WACC uses **market value** weights. Book equity is a historical
> accounting number with no bearing on what the capital is worth.

> **Trap 2 — Tax-adjusting the wrong component.** **Only debt** gets the `(1 − t)`. Preferred and
> common dividends are paid from after-tax income and are not deductible.

> **Trap 3 — Using the coupon rate as the cost of debt.** It is the **YTM** — the market's current
> required return — not the historical coupon on debt issued years ago.

> **Trap 4 — Taking MM literally.** The propositions assume away taxes, bankruptcy costs, and agency
> costs. Their purpose is to identify which frictions matter, not to describe the world.

> **Trap 5 — Forgetting that MM Proposition II offsets Proposition I.** Under no taxes, adding cheap
> debt raises `re` by **exactly** enough to leave WACC unchanged. The two propositions are one idea.

> **Trap 6 — Assuming debt always lowers WACC.** It does **up to a point**. Beyond the optimum,
> rising distress costs raise both rd and re faster than the tax shield benefits.

> **Trap 7 — Pecking order vs trade-off.** The pecking order explains why **profitable companies
> use less debt** — they fund internally. The trade-off theory predicts the opposite. Know which
> theory answers which empirical question.

> **Trap 8 — Stacking operating and financial leverage.** High DOL with high DFL produces extreme
> DTL. A company with volatile operating income should carry less debt, not more.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company has 300m of debt (market value) at a YTM of 6%, and 700m of equity (market value). Beta is 1.2, the risk-free rate is 3.5%, and the equity risk premium is 5%. The tax rate is 25%. Compute WACC.

<details><summary>Answer</summary>

Cost of equity (CAPM) = 3.5% + 1.2 × 5% = 3.5% + 6.0% = **9.5%**

Weights: total capital = 1,000m.
wd = 300/1,000 = 0.30;  we = 700/1,000 = 0.70

WACC = 0.30 × 6% × (1 − 0.25) + 0.70 × 9.5%
     = 0.30 × 4.5% + 6.65%
     = 1.35% + 6.65%
     = **8.0%**

Note the after-tax cost of debt: 6% × 0.75 = 4.5%. Only debt receives this adjustment.

</details>

**2.** State MM Propositions I and II without taxes, and explain why they are two halves of one idea.

<details><summary>Answer</summary>

**Proposition I:** `V_L = V_U` — the value of the firm is independent of its capital structure. Value comes from the assets and their cash flows; how the claims are divided does not change the total.

**Proposition II:** `re = r0 + (r0 − rd)(D/E)` — the cost of equity rises linearly with the debt-to-equity ratio.

**Why they are one idea:** Proposition II is the *mechanism* that enforces Proposition I. Debt is cheaper than equity, so substituting debt for equity looks like it should lower WACC. But each unit of debt added makes the residual equity claim riskier — the equity now sits behind a larger fixed obligation — so `re` rises by **exactly** enough to offset the cheaper debt. **WACC stays constant**, and firm value is unchanged.

Without Proposition II, Proposition I would not hold. The enforcement mechanism in the market is **homemade leverage**: an investor can replicate any capital structure by borrowing personally, so they will not pay a premium for the company to do it for them.

</details>

**3.** Under MM with corporate taxes, what is the implied optimal capital structure, and why is that conclusion obviously wrong?

<details><summary>Answer</summary>

With corporate taxes, `V_L = V_U + tD`. Firm value rises **linearly** with debt, so the implied optimum is **100% debt**.

That is obviously wrong — no company operates with 100% debt, and companies that approach it fail.

**What the model omits: the costs of financial distress.** As leverage rises, the probability of distress rises, and distress is expensive:
- **Direct costs** — legal and administrative fees (relatively small)
- **Indirect costs** — much larger: customers defect (will the warranty be honoured?), suppliers withdraw credit, key employees leave, assets are sold at fire-sale prices, and management attention goes to survival rather than the business

The **static trade-off theory** adds this back: `V_L = V_U + PV(tax shield) − PV(distress costs)`. The optimum is where the marginal tax benefit equals the marginal expected distress cost — which is where **WACC is minimised**.

The value of the MM exercise is precisely this: by assuming the frictions away, it identifies exactly which frictions make capital structure matter.

</details>

**4.** EBIT is 900 and interest expense is 200. Compute DFL and interpret it.

<details><summary>Answer</summary>

DFL = EBIT / (EBIT − Interest) = 900 / (900 − 200) = 900/700 = **1.286**

Interpretation: a **1% change in operating income produces a 1.286% change in net income**. The fixed interest obligation magnifies the swing.

If EBIT falls 20%, net income falls approximately 25.7%. If operating leverage is also high — say DOL = 2.0 — then DTL = 2.0 × 1.286 = **2.57**, meaning a 10% fall in unit sales produces a roughly 26% fall in net income.

That compounding is why a company with high operating leverage should carry **less** financial leverage: the combination turns an ordinary demand downturn into a solvency problem.

</details>

**5.** Explain the pecking order theory and the empirical puzzle it resolves.

<details><summary>Answer</summary>

**Pecking order theory** starts from **asymmetric information**: managers know more about the firm's prospects than outside investors do.

Because of this, issuing equity carries a **negative signal** — rational investors infer that management would only sell shares if it believed them **overvalued**, so the price falls on announcement. Debt carries a weaker signal (it must be serviced regardless, so issuing it suggests confidence). Internal funds carry none.

So companies finance in strict order: **(1) retained earnings, (2) debt, (3) equity as a last resort.**

**The puzzle it resolves:** the trade-off theory predicts that **profitable** companies — with more taxable income to shield and lower distress probability — should use **more** debt. Empirically, profitable companies use **less** debt.

The pecking order explains it: profitable companies generate enough internal cash that they never reach step 2. Their low leverage is not a target, it is a **residual** — the by-product of having funded themselves internally.

</details>

**6.** Why should an analyst use market-value rather than book-value weights in WACC?

<details><summary>Answer</summary>

Because WACC is the **opportunity cost of capital** — the return investors currently require to provide capital **today**. That requirement is set against what the capital is worth **now**, which is its market value.

Book equity is a historical accounting residual: cumulative retained earnings plus paid-in capital, unaffected by the company's current prospects and distorted by accounting policy (goodwill, impairments, buybacks at prices above book). For a profitable company, market equity typically exceeds book equity by a wide multiple — sometimes 3× or more.

Using book weights therefore **understates the equity weight** and, because equity is the more expensive component, **understates WACC**. That biases every NPV upward and leads systematically to over-investment.

(In practice, book value of **debt** is often used as a proxy for its market value, which is acceptable for investment-grade debt near par but not for distressed debt trading well below face.)

</details>

---

## Done when

- [ ] I can compute WACC with market-value weights and tax-adjust only the debt component
- [ ] I can estimate the cost of equity three ways and the cost of debt correctly (YTM, not coupon)
- [ ] I can state MM Propositions I and II with and without taxes, and explain why II enforces I
- [ ] I can explain why MM with taxes implies 100% debt and what the static trade-off adds back
- [ ] I can compute DOL, DFL, and DTL and explain why they should not both be high
- [ ] I can state the pecking order and the empirical puzzle it resolves
- [ ] I can explain why market-value weights matter and which direction book weights bias WACC
- [ ] I answered the self-check cold, several days after first study

---

← [LM05 Capital Investments and Capital Allocation](lm-05-capital-investments-and-capital-allocation.md)  ·  [Topic index](README.md)  ·  [LM07 Business Models](lm-07-business-models.md) →
