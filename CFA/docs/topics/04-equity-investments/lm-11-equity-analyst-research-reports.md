# EQ · LM11 — Equity Analyst Research Reports

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 3 |
| **Prerequisites** | LM6–LM10. This module assumes you can value a company. |
| **Where it shows up** | 1 question. The lightest module in Equity, but it overlaps directly with Ethics Standard V. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe the elements that should be covered in a detailed company research report
- compare sell-side and buy-side equity analyst reports and their conclusions
- explain why value estimates from the same modeling approach may differ based on analyst assumptions regarding revenue, profitability, investment, and financing

---

## Core concepts

### Elements of a research report

A complete report covers, roughly in this order:

| Element | Contents |
| --- | --- |
| **Summary / investment thesis** | The recommendation, the target price, and the argument in a paragraph |
| **Business description** | What the company does, its segments, and its business model |
| **Industry overview** | Structure, growth, competitive dynamics (LM9) |
| **Competitive position** | Strategy, advantages and their durability (LM10) |
| **Historical financial analysis** | Growth, margins, returns, cash generation, balance sheet |
| **Forecasts and assumptions** | The model and, critically, **the assumptions behind it** |
| **Valuation** | Methods used, inputs, and the resulting value |
| **Investment recommendation** | Buy/hold/sell, target price, and time horizon |
| **Risk factors** | **What would make the thesis wrong** |
| **Disclosures** | Conflicts, relationships, methodology, rating definitions |

> **The two sections that separate a good report from a bad one are the *assumptions* and the
> *risks*.** Anyone can produce a number. A useful report tells the reader exactly what must be true
> for it to hold, and what would falsify it. A report with no falsification condition is advocacy,
> not analysis.

**Ethics connection — Standard V(A) Diligence and Reasonable Basis** requires that recommendations
have a reasonable and adequate basis supported by appropriate research. **Standard V(B)
Communication with Clients** requires distinguishing **fact from opinion**, disclosing the basic
format and general principles of the process, and identifying important factors and risks. The
report structure above is essentially a checklist for complying with both.

### Sell-side versus buy-side

| | **Sell-side** | **Buy-side** |
| --- | --- | --- |
| **Employer** | Brokers and investment banks | Asset managers, pension funds, hedge funds |
| **Audience** | **External** — clients, and the public | **Internal** — the firm's own portfolio managers |
| **Distribution** | Widely published | Confidential |
| **Coverage** | Deep coverage of a defined sector, many companies | Fewer names, driven by portfolio needs |
| **Purpose** | Generate trading commissions and support banking relationships | **Generate investment returns** |
| **Conflicts** | **Significant and structural** | Fewer external conflicts; internal pressures exist |
| **Typical tone** | Skewed toward **buy** ratings | More balanced; short ideas are actionable |

**Sell-side conflicts, which the exam expects you to identify:**

- **Investment banking relationships** — negative research on a client or prospective client
  jeopardises fee income. This is the structural conflict, and it is why regulators mandate
  separation between research and banking.
- **Corporate access** — critical analysts can be denied management meetings, which is a real
  commercial cost.
- **Trading commissions** — a buy recommendation reaches every client; a sell recommendation is only
  actionable by existing holders and short sellers, so buys generate more business.
- **Compensation linked to banking or trading revenue.**

The documented consequence is a **skew toward buy ratings**, with sell recommendations a small
fraction of the total.

> **Ethics Standard I(B) Independence and Objectivity** applies directly. An analyst must use
> reasonable care and exercise independent professional judgement, and must not let issuer pressure,
> banking relationships, or the prospect of losing corporate access compromise a recommendation.

### Why two analysts using the same model get different values

The LOS asks specifically about **revenue, profitability, investment, and financing** assumptions.
This is where a DCF's apparent objectivity dissolves.

| Assumption | How it differs | Effect on value |
| --- | --- | --- |
| **Revenue growth** | Market size, share gains, price versus volume, product cycle timing | Large — compounds over the explicit period and drives the terminal base |
| **Terminal growth rate `g`** | 2% vs 3% is a small-sounding difference | **Enormous** — the `1/(r − g)` multiplier is hypersensitive |
| **Operating margin** | Pass-through ability, operating leverage, mix, competitive response | Large — flows to every year |
| **Capital investment** | Capex intensity, working capital requirements, maintenance vs growth split | Direct reduction in free cash flow |
| **Discount rate (`r`, WACC)** | Beta estimate, equity risk premium, cost of debt, target weights | **Enormous** — same hypersensitivity as `g` |
| **Forecast horizon** | 5 vs 10 explicit years changes how much sits in the terminal value | Moderate to large |
| **Terminal value method** | Perpetuity growth vs exit multiple | Can differ materially |

**A worked illustration.** Take a company with a terminal free cash flow of 100.

| WACC | g | Multiplier `1/(r−g)` | Terminal value |
| --- | --- | --- | --- |
| 9% | 2% | 14.3 | 1,430 |
| 9% | 3% | 16.7 | **1,670** (+17%) |
| 8% | 3% | 20.0 | **2,000** (+40%) |
| 10% | 2% | 12.5 | **1,250** (−13%) |

A one-percentage-point disagreement on **each** of two unobservable inputs produces a **60% range**
in terminal value — and the terminal value is typically 60–80% of the total. Two competent, honest
analysts can reach very different targets without either being unreasonable.

> **What follows for practice:** a DCF is **not** an objective measurement. It is a structured
> argument whose conclusion is determined by a handful of judgements. The useful outputs are
> therefore (1) a **range**, not a point, (2) explicit **sensitivity tables** on `g` and `r`, and
> (3) the **reverse-engineered** market assumptions, so the disagreement with the market is stated
> as a specific claim about growth or margin rather than as a bare price target.

---

## Formulas to know cold

No formulas. Two structures to memorise:

```
RESEARCH REPORT ELEMENTS
  Summary / thesis · Business description · Industry overview · Competitive position
  · Historical financial analysis · Forecasts AND ASSUMPTIONS · Valuation
  · Recommendation and target · RISK FACTORS · Disclosures

WHY VALUATIONS DIFFER (the four the LOS names)
  REVENUE      — market size, share, price vs volume, timing
  PROFITABILITY— margins, pass-through, operating leverage, competitive response
  INVESTMENT   — capex intensity, working capital, maintenance vs growth
  FINANCING    — discount rate (beta, ERP, cost of debt, target weights)
  Plus: terminal growth rate, forecast horizon, terminal value method

  Sensitivity of the terminal value:  TV = CF/(r − g)
  A 1pp change in EITHER r or g moves TV by roughly 15-25%.
```

---

## Exam traps

> **Trap 1 — Omitting the risk section.** A report with no statement of what would make the thesis
> wrong is advocacy, not analysis — and it breaches **Standard V(B)**, which requires identifying
> important factors and risks.

> **Trap 2 — Failing to distinguish fact from opinion.** Required by **Standard V(B)**. A forecast is
> an opinion and must be labelled as one.

> **Trap 3 — Assuming a DCF is objective.** The same model with different judgements produces very
> different answers. Present a range and a sensitivity table.

> **Trap 4 — Underestimating sell-side conflicts.** Banking relationships, corporate access, and
> commission generation all skew ratings toward buy. **Standard I(B)** applies directly.

> **Trap 5 — Thinking buy-side research is conflict-free.** It has fewer **external** conflicts, but
> internal pressures exist — supporting an existing position, or a portfolio manager's prior view.

> **Trap 6 — Treating a target price as a forecast.** It is a conditional statement: *if* these
> assumptions hold, *then* this is the value. State the conditions.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Two analysts value the same company with identical DCF structures. One reaches 45, the other 78. Name the likely sources of the difference.

<details><summary>Answer</summary>

In descending order of likely impact:

**(1) Terminal growth rate.** A difference of 1–2 percentage points in `g` moves the terminal value by 15–40%, and the terminal value is usually 60–80% of the total.

**(2) Discount rate.** Different beta estimates (which period? which index? raw or adjusted?), different equity risk premium assumptions (historical or forward-looking?), or different target capital structure weights.

**(3) Revenue growth in the explicit period.** Different views on market size, share gains, and the split between price and volume — these compound and also set the base for the terminal value.

**(4) Operating margin.** One analyst assumes margin expansion from operating leverage; the other assumes competitive response caps it.

**(5) Capital investment.** Different assumptions about capex intensity and working capital directly reduce free cash flow.

**Neither analyst need be unreasonable.** A 1pp disagreement on each of `g` and `r` alone can produce a 60% range in terminal value. This is why the useful output is a range with sensitivity tables, plus the reverse-engineered market assumptions — which turn 'we disagree by 73%' into 'we disagree about whether long-run growth is 2% or 3.5%'.

</details>

**2.** Why do sell-side analysts issue far more buy than sell recommendations?

<details><summary>Answer</summary>

**(1) Investment banking relationships.** Negative research on a current or prospective banking client jeopardises fee income. This is the structural conflict, and it is why regulators require separation between research and banking functions.

**(2) Corporate access.** An analyst who publishes a sell rating can be cut off from management meetings, conference calls, and site visits — a real commercial cost to the franchise, because clients value that access.

**(3) Commission economics.** A buy recommendation is actionable by **every** client. A sell recommendation is actionable only by existing holders and by the minority who can short. Buys therefore generate materially more trading revenue.

**(4) Compensation.** Where analyst pay is linked to banking or trading revenue, the incentive is direct.

**The Ethics dimension: Standard I(B) Independence and Objectivity.** An analyst must exercise independent professional judgement and must not allow issuer pressure, banking relationships, or the threat of losing access to compromise a recommendation. Firms discharge this through information barriers, restricting banking influence over research, and compensation structures not tied to specific deals.

</details>

**3.** What does a research report's risk section need to contain to be useful?

<details><summary>Answer</summary>

Not a generic list. It needs the **specific conditions under which this thesis fails**:

- **Which assumption is most fragile**, and what would change it. If the valuation rests on margins expanding 300bp, say so, and say what would prevent it.
- **Quantified sensitivity** — what the value becomes if growth is 2% instead of 4%, or if the key customer is lost.
- **Company-specific risks** — customer concentration, covenant headroom, patent expiry, key-person dependence, pending litigation.
- **Industry and competitive risks** — new entrants, substitution, regulatory change.
- **What would make you change the recommendation** — a stated falsification condition.

**Why it matters beyond usefulness:** Ethics **Standard V(B)** requires identifying important factors and risks and distinguishing fact from opinion. A report presenting only the bull case, with boilerplate risk language, does not discharge that obligation regardless of how good the analysis is.

</details>

**4.** Contrast the purpose and conflicts of sell-side and buy-side research.

<details><summary>Answer</summary>

**Sell-side.** Produced by brokers and investment banks for **external distribution** to clients and the market. Its commercial purpose is to **generate trading commissions and support banking relationships** — research is a cost centre justified by the revenue it attracts elsewhere. Conflicts are **structural and significant**: banking relationships, corporate access, and commission economics all skew ratings toward buy, and the documented rating distributions reflect it.

**Buy-side.** Produced inside asset managers for **internal use** by the firm's own portfolio managers. Its purpose is directly to **generate investment returns** — it is judged by whether the recommendations make money. Coverage is narrower and driven by portfolio needs rather than sector completeness, and short ideas are genuinely actionable.

**Buy-side conflicts are fewer but not absent:** pressure to support an existing position rather than recommend selling it, deference to a senior portfolio manager's prior view, and incentives tied to short-term performance.

**For a reader:** sell-side research is valuable for industry knowledge, data, and modelling detail, but its **conclusion** should be discounted for the known skew. Read the assumptions, not the rating.

</details>

---

## Done when

- [ ] I can list the ten elements of a research report
- [ ] I can explain why the assumptions and risks sections matter most, and which Standards they serve
- [ ] I can contrast sell-side and buy-side research on employer, audience, purpose, and conflicts
- [ ] I can name four structural sell-side conflicts and connect them to Standard I(B)
- [ ] I can explain why identical DCF structures produce very different values
- [ ] I can quantify the sensitivity of a terminal value to 1pp changes in r and g
- [ ] I answered the self-check cold, several days after first study

---

← [LM10 Company Analysis: Past, Present, and Future](lm-10-company-analysis-past-present-and-future.md)  ·  [Topic index](README.md)  ·  [LM12 The Capital Asset Pricing Model, Market Model, and Other Factor-Based Equity Models](lm-12-the-capital-asset-pricing-model-market-model-and-other-facto.md) →
