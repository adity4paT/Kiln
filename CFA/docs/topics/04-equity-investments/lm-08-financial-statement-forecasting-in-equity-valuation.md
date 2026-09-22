# EQ · LM08 — Financial Statement Forecasting in Equity Valuation

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | FSA LM12 (pro forma modelling), LM6 (DCF). |
| **Where it shows up** | 1 question. Conceptual — the LOS ask you to explain and evaluate, not to build. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the rationale, construction, and uses of financial statement forecast models in equity valuation
- evaluate the construction of an equity valuation model based on characteristics of the subject company
- estimate and interpret the value of an equity security based on the outputs of a financial statement forecast model

---

## Core concepts

### Why forecast the statements at all

A DCF needs future free cash flows. Free cash flow is derived from the income statement **and** the
balance sheet — you cannot forecast capex, working capital, or net borrowing from a revenue growth
rate alone. A full three-statement forecast model is the machinery that produces internally
consistent cash flows.

The second reason is **discipline**. An integrated model forces the balance sheet to balance, which
catches assumptions that are individually plausible and jointly impossible — 25% revenue growth
with flat capex and constant working capital days, for instance, will not balance.

### Construction, in order

This is FSA LM12 applied to a valuation:

| Step | What you do |
| --- | --- |
| 1 | **Revenue** — top-down (market × share) or bottom-up (units × price), by segment |
| 2 | **COGS and gross margin** — common-size percentage, adjusted for known input-cost and mix changes |
| 3 | **Operating expenses** — split **fixed** from **variable**; variable scales with revenue |
| 4 | **Working capital** — hold DOH, DSO, and days payables constant unless there is a stated reason |
| 5 | **Capex and depreciation** — off fixed asset turnover, the existing asset base's age, and stated plans |
| 6 | **Debt schedule** → interest expense → EBT → tax → net income |
| 7 | **Cash flow statement** — derived from the forecast income statement and balance-sheet movements |
| 8 | **Free cash flow** — FCFF or FCFE (FSA LM5) |
| 9 | **Discount** at WACC or `re`, add a terminal value |
| 10 | **Sensitivity and scenario analysis** on the two or three assumptions that drive the answer |

> **The balance check.** Assets must equal liabilities plus equity in every forecast year. A model
> that does not balance has an error — usually in the cash sweep, the debt schedule, or retained
> earnings. Do not paper over it with a plug.

### Tailoring the model to the company

The LOS asks you to **evaluate the construction of a model based on the characteristics of the
subject company**. The point is that there is no single right structure.

| Company characteristic | What the model must do |
| --- | --- |
| **Cyclical** | Explicit period spanning a **full cycle**; terminal value on **normalised** earnings, not terminal-year earnings |
| **High growth, early stage** | Long explicit period until growth normalises; model the path to profitability explicitly; scenario-weight the outcomes |
| **Mature and stable** | Short explicit period (3–5 years) is sufficient; most value is terminal |
| **Capital intensive** | Model **maintenance versus growth capex separately**; the asset age schedule matters |
| **Asset light** | Working capital and intangible investment matter more than capex |
| **Highly levered** | **FCFF and WACC**, with an explicit debt schedule; FCFE is volatile and misleading here |
| **Multiple segments** | **Sum of the parts** — model and value each segment separately, then aggregate |
| **Subscription model** | Drive revenue from **subscribers × ARPU with churn**, never a single growth rate |
| **Commodity producer** | Revenue = **volume × price**, with price as an explicit, sensitised assumption |
| **Regulated utility** | Model the **regulatory asset base** and the allowed return, not a market-determined margin |

### Interpreting the output

**The equity value bridge** — getting from an enterprise value to a per-share value:

```
Enterprise value (PV of FCFF at WACC, including terminal value)
  − Total debt
  − Preferred stock
  − Minority interest
  + Cash and equivalents
  + Non-operating assets (investments, surplus property, associates at fair value)
  = Equity value
  ÷ Diluted shares outstanding
  = Value per share
```

> **Use diluted shares.** Options and convertibles will be exercised if the valuation is right, and
> ignoring them overstates value per share. (FSA LM2 gives the mechanics.)

**Reading the result:**

1. **Compare to price.** Value > price → undervalued. But first, ask what you must believe that the
   market does not.
2. **Check the terminal value share.** If it is 80% of the total, the model is a statement about
   `g` and `r`, not about your explicit forecast.
3. **Cross-check against multiples** (LM7). What P/E and EV/EBITDA does your value imply? If they
   are far outside the peer range, justify the difference explicitly.
4. **Reverse-engineer the market.** What growth rate, margin, or WACC produces the current price?
   That converts a vague disagreement into a specific one.
5. **Present a range.** A point estimate implies a precision the inputs do not support.

### Sensitivity, scenario, and simulation

| Technique | What it does |
| --- | --- |
| **Sensitivity analysis** | Vary **one** input at a time; a two-way table on `g` and `WACC` is standard |
| **Scenario analysis** | Vary a **consistent set** of inputs together (recession / base / expansion) |
| **Monte Carlo** | Specify distributions for the key inputs and generate a distribution of values (QM LM9) |

Scenario analysis is usually more informative than sensitivity analysis, because inputs are
correlated in reality: a recession scenario lowers revenue growth **and** compresses margins **and**
raises the cost of capital, and modelling those together produces a coherent picture that flexing
one variable cannot.

### The common failure modes

| Failure | What it looks like |
| --- | --- |
| **False precision** | A value of 87.43 from inputs known to two significant figures at best |
| **Assumption stacking** | Each assumption individually optimistic; the compound result implausible |
| **Anchoring on the target** | Building the model backwards from a price you have already decided on |
| **Anchoring on guidance** | Forecasting management's forecast rather than your own |
| **Ignoring the balance sheet** | Growth with no capital to fund it |
| **Terminal value neglect** | Weeks on the explicit years, minutes on the assumption that drives 75% of the value |
| **No falsification test** | No statement of what would prove the thesis wrong |

> **The discipline that separates a model from a spreadsheet:** every assumption must be **anchored
> to history, anchored to a peer, or explicitly justified** — and you must be able to state, in one
> sentence, what would make you abandon the thesis.

---

## Formulas to know cold

```
THE EQUITY VALUE BRIDGE
  Enterprise value (PV of FCFF at WACC, incl. terminal value)
    − Total debt
    − Preferred stock
    − Minority interest
    + Cash and equivalents
    + Non-operating assets
    = Equity value
    ÷ DILUTED shares outstanding
    = Value per share

WORKING CAPITAL, HELD AT CURRENT EFFICIENCY
  Receivables = DSO × Revenue / 365
  Inventory   = DOH × COGS / 365
  Payables    = Days payables × Purchases / 365

COST STRUCTURE
  Variable costs = % of revenue × Forecast revenue
  Fixed costs    = Prior fixed costs × (1 + inflation)     [does NOT scale with revenue]

TERMINAL VALUE
  Perpetuity growth:  TV_n = FCF_(n+1) / (WACC − g),  g ≤ long-run nominal GDP growth
  Exit multiple:      TV_n = Terminal-year metric × peer multiple
  Both give a value AS OF year n → discount back n periods
```

---

## Exam traps

> **Trap 1 — Forecasting all costs as a percentage of revenue.** That assumes zero operating
> leverage. Split fixed from variable.

> **Trap 2 — Forgetting the balance sheet must balance.** A model that does not balance has an error.
> Find it; do not insert a plug.

> **Trap 3 — Using basic rather than diluted shares.** Options and convertibles dilute. Basic shares
> overstate value per share.

> **Trap 4 — Bridge sign errors.** From EV: **subtract** debt, preferred, and minorities; **add**
> cash and non-operating assets.

> **Trap 5 — Terminal value on terminal-year earnings for a cyclical.** Use **normalised** earnings,
> or you capitalise the current phase of the cycle into perpetuity.

> **Trap 6 — Terminal growth above long-run nominal GDP growth.** Always wrong.

> **Trap 7 — Anchoring on management guidance.** Build your own forecast first, then compare.

> **Trap 8 — Confusing sensitivity with scenario analysis.** Sensitivity flexes **one** input;
> scenarios flex a **consistent set** together. Scenarios are usually more informative because real
> inputs are correlated.

> **Trap 9 — Reporting a point estimate.** Present a range, and state what would falsify the thesis.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Your DCF gives an enterprise value of 8,400m. Debt is 2,100m, cash is 450m, minority interest is 180m, and there are 320m shares outstanding with 15m dilutive options. Compute the value per share.

<details><summary>Answer</summary>

```
Enterprise value              8,400
− Total debt                 (2,100)
− Minority interest            (180)
+ Cash and equivalents          450
                             -------
Equity value                  6,570
```
Diluted shares = 320 + 15 = **335m** (approximately — strictly, apply the treasury stock method from FSA LM2, which would give fewer net new shares).

Value per share = 6,570 / 335 = **19.61**

Using basic shares (320m) would give 20.53 — a **4.7% overstatement**. On a marginal call, that difference decides the recommendation.

</details>

**2.** You are building a model for a cyclical mining company currently at a cyclical peak. What must the model do differently?

<details><summary>Answer</summary>

**(1) Long explicit horizon** — at least a full cycle, typically 7–10 years, so the forecast spans both peak and trough. A 3-year model from a peak carries peak margins straight into the terminal value.

**(2) Explicit price assumptions.** Revenue = **volume × commodity price**, with price modelled separately and sensitised heavily. A single revenue growth rate hides the only variable that matters.

**(3) Normalised terminal value.** Base the terminal value on **mid-cycle** margins and volumes averaged across a full historical cycle — not on terminal-year figures. Or use a mid-cycle exit multiple on normalised EBITDA.

**(4) Model the cost curve position.** Where the company sits on the industry cost curve determines whether it survives a trough, which is the dominant risk.

**(5) Scenario analysis, not just sensitivity.** A downturn scenario must move price, volume, margin, **and** the cost of capital together.

The error to avoid is capitalising peak earnings at a peak multiple — the standard way cyclicals get overvalued at exactly the wrong moment.

</details>

**3.** Why is scenario analysis usually more informative than sensitivity analysis?

<details><summary>Answer</summary>

Because **real inputs are correlated**, and sensitivity analysis assumes they are not.

Flexing revenue growth alone, holding everything else constant, describes a world that does not exist. In an actual recession, revenue growth falls **and** operating margin compresses (operating leverage) **and** working capital stretches **and** the cost of capital rises **and** the terminal growth assumption should probably come down.

**Scenario analysis** moves a **consistent set** of assumptions together, producing a coherent picture of what the company is worth in a recognisable state of the world. That is something you can reason about and communicate.

Sensitivity analysis still has a role — a two-way table on `g` and `WACC` is the standard way to show how much of the answer rests on the terminal assumption. But it answers a narrower question: **how fragile is this number**, rather than **what happens if things go badly**.

</details>

**4.** What does it mean if your model's implied P/E is 34× while the peer group trades at 15×?

<details><summary>Answer</summary>

Your valuation embeds assumptions materially more favourable than the market's. Before accepting it, identify **which**:

- **Higher growth** — does your `g` exceed the peers', and is there a specific, defensible reason (a product cycle, a structural share gain, a regulatory tailwind)?
- **Higher margins** — are you forecasting profitability the company has never achieved, or that no peer achieves?
- **A lower discount rate** — is your beta or equity risk premium out of line?
- **A higher terminal growth rate** — the most likely culprit, and the hardest to defend.

**Then decide between two readings:**
1. The market is wrong and you have identified something it has not. This requires an articulable reason — what do you know, or what are you willing to believe, that others are not?
2. **Your model is wrong** — most likely assumption stacking, where each input is individually plausible and the compound result is not.

The base rate strongly favours reading 2. A 2× premium to a peer group needs a one-sentence thesis you could defend to a sceptical portfolio manager, not a spreadsheet.

</details>

**5.** Name four ways a forecast model can be structurally wrong even when every individual assumption looks reasonable.

<details><summary>Answer</summary>

**(1) Assumption stacking.** Each input is at the optimistic end of a plausible range; compounded over ten years, the joint outcome is implausible. Each 'reasonable' choice multiplies.

**(2) Internal inconsistency.** Revenue growing 25% with flat capex and constant working capital days — the balance sheet cannot support the growth. An integrated model catches this; a standalone income statement forecast does not.

**(3) Ignoring competitive response.** Forecasting sustained margin expansion in a fragmented, low-barrier industry contradicts the five forces (FSA LM12). Abnormal returns attract entry.

**(4) Terminal assumptions inconsistent with the explicit period.** Forecasting 20% growth for ten years and then a perpetuity growth rate of 2% with no transition, or a terminal ROIC far above the cost of capital sustained forever.

Also: **anchoring on a target price** and building backwards; and **modelling the market's forecast** (consensus or guidance) rather than your own, which guarantees you never disagree with the price.

</details>

---

## Done when

- [ ] I can lay out the ten steps of building a valuation-grade forecast model
- [ ] I can explain what the balance check catches and why a plug is never acceptable
- [ ] I can tailor the model structure to a cyclical, a high-growth, a levered, and a multi-segment company
- [ ] I can execute the equity value bridge with correct signs and diluted shares
- [ ] I can state four things to check before acting on a DCF output
- [ ] I can distinguish sensitivity, scenario, and simulation analysis and say when each is appropriate
- [ ] I can name the common structural failure modes of forecast models
- [ ] I answered the self-check cold, several days after first study

---

← [LM07 Relative Value Equity Valuation Approaches](lm-07-relative-value-equity-valuation-approaches.md)  ·  [Topic index](README.md)  ·  [LM09 Industry and Competitive Analysis](lm-09-industry-and-competitive-analysis.md) →
