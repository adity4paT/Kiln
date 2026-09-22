# FSA · LM11 — Financial Analysis Techniques

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM2–LM10. This module consolidates every ratio in FSA. |
| **Where it shows up** | 2–3 questions, plus DuPont reappears in Equity and Corporate Issuers. Highest reuse in the whole topic. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe tools and techniques used in financial analysis, including their uses and limitations
- calculate and interpret activity, liquidity, solvency, and profitability ratios
- describe relationships among ratios and evaluate a company using ratio analysis
- demonstrate the application of DuPont analysis of return on equity and calculate and interpret effects of changes in its components
- describe the uses of industry-specific ratios used in financial analysis
- describe how ratio analysis and other techniques can be used to model and forecast earnings

---

## Core concepts

### Tools, and what each is for

| Tool | Answers | Limitation |
| --- | --- | --- |
| **Ratio analysis** | How do the pieces relate? | Meaningless without a benchmark; distorted by accounting choice |
| **Common-size analysis** | What is the composition, independent of size? | Hides absolute scale |
| **Trend / horizontal analysis** | What direction, at what rate? | Base-year choice drives the impression |
| **Graphical analysis** | Where is the inflection? | Axis choice can mislead |
| **Regression** | Which driver explains the variation? | Correlation is not causation; needs data |

**The three limitations of ratios, which the LOS asks for:** (1) ratios are not useful in isolation —
they require comparison to history, peers, or a threshold; (2) **differences in accounting policy**
across companies destroy comparability unless adjusted; (3) **heterogeneous companies** (conglomerates
spanning several industries) have no meaningful single peer group.

### Activity ratios — how efficiently are assets used?

| Ratio | Formula |
| --- | --- |
| Inventory turnover | COGS / Average inventory |
| Days of inventory on hand (DOH) | 365 / Inventory turnover |
| Receivables turnover | Revenue / Average receivables |
| Days of sales outstanding (DSO) | 365 / Receivables turnover |
| Payables turnover | Purchases / Average payables |
| Number of days of payables | 365 / Payables turnover |
| Working capital turnover | Revenue / Average working capital |
| Fixed asset turnover | Revenue / Average net fixed assets |
| Total asset turnover | Revenue / Average total assets |

**The cash conversion cycle** ties three of them together:

```
Cash conversion cycle = DOH + DSO − Days of payables
```

It measures the days between paying for inventory and collecting from customers — the length of time
the company must **fund itself**. Shorter is better. Some retail and subscription businesses achieve
a **negative** cycle (they collect before they pay suppliers), which is a genuine competitive
advantage: the business funds its own growth. This returns in Corporate Issuers LM4.

> **Trap:** inventory turnover uses **COGS**, receivables turnover uses **revenue**, payables turnover
> uses **purchases**. Three different numerators. Using revenue for inventory turnover is a standard
> planted error.

### Liquidity ratios

| Ratio | Formula |
| --- | --- |
| Current | Current assets / Current liabilities |
| Quick | (Cash + Short-term investments + Receivables) / Current liabilities |
| Cash | (Cash + Short-term investments) / Current liabilities |
| Defensive interval | (Cash + Short-term investments + Receivables) / Daily cash expenditures |

### Solvency ratios

| Ratio | Formula |
| --- | --- |
| Debt-to-assets | Total debt / Total assets |
| Debt-to-capital | Total debt / (Total debt + Total equity) |
| Debt-to-equity | Total debt / Total equity |
| Financial leverage | Average total assets / Average total equity |
| Interest coverage | **EBIT** / Interest payments |
| Fixed charge coverage | (EBIT + Lease payments) / (Interest payments + Lease payments) |

### Profitability ratios

| Ratio | Formula |
| --- | --- |
| Gross profit margin | Gross profit / Revenue |
| Operating profit margin | Operating income (EBIT) / Revenue |
| Pre-tax margin | EBT / Revenue |
| Net profit margin | Net income / Revenue |
| Operating ROA | Operating income / Average total assets |
| ROA | Net income / Average total assets |
| Return on total capital | EBIT / (Average short- and long-term debt + equity) |
| **ROE** | Net income / Average shareholders' equity |
| Return on common equity | (Net income − Preferred dividends) / Average common equity |

### DuPont analysis — the most reused idea in FSA

DuPont decomposes ROE to answer **why** it is what it is. Two companies with identical 15% ROE can
be completely different businesses.

**Three-part DuPont:**

```
ROE = Net profit margin × Total asset turnover × Financial leverage

    = (Net income / Revenue) × (Revenue / Avg total assets) × (Avg total assets / Avg equity)
```

Read it as: **profitability × efficiency × leverage.** The middle terms cancel algebraically, which
is the proof that it is an identity, not an approximation.

**Five-part DuPont** splits net profit margin into tax, interest, and operating effects:

```
ROE = Tax burden × Interest burden × Operating margin × Asset turnover × Financial leverage

    = (Net income / EBT) × (EBT / EBIT) × (EBIT / Revenue) × (Revenue / Avg assets) × (Avg assets / Avg equity)
```

| Component | Formula | What it isolates |
| --- | --- | --- |
| **Tax burden** | Net income / EBT | The fraction of pre-tax profit kept after tax. Equals (1 − effective tax rate). **Higher is better** |
| **Interest burden** | EBT / EBIT | The fraction of operating profit surviving interest. **Higher is better** (= 1.0 with no debt) |
| **Operating margin** | EBIT / Revenue | Operating profitability |
| **Asset turnover** | Revenue / Avg total assets | Asset efficiency |
| **Financial leverage** | Avg assets / Avg equity | Balance-sheet leverage |

> **The insight the exam tests:** leverage appears **twice, with opposite signs**. More debt raises
> the **financial leverage** multiplier (good for ROE) but lowers the **interest burden** ratio (bad
> for ROE). Whether borrowing raises ROE depends on which effect dominates — i.e. on whether the
> return on the borrowed assets exceeds the after-tax cost of the debt.

**Using it:** when ROE changes, compute all five components for both periods and find which one
moved. ROE rising because operating margin improved is a different (and far better) company from
ROE rising because leverage went from 2× to 4×.

### Industry-specific ratios

Standard ratios fail for businesses with unusual economics. Know that these exist and roughly what
they measure:

| Industry | Ratio | Measures |
| --- | --- | --- |
| **Retail** | Same-store (like-for-like) sales growth | Organic growth, stripping out new store openings |
| **Retail** | Sales per square metre | Space productivity |
| **Banking** | Net interest margin | (Interest income − interest expense) / earning assets |
| **Banking** | Capital adequacy, loan loss coverage | Solvency under regulation |
| **Insurance** | Combined ratio (loss ratio + expense ratio) | Underwriting profitability; **below 100% = profitable underwriting** |
| **Airlines / hotels** | Load factor, RevPAR, yield | Capacity utilisation and pricing |
| **Telecom / subscription** | ARPU, churn rate, subscriber acquisition cost | Revenue quality and retention |
| **Extractive** | Reserve replacement ratio, production cost per unit | Sustainability of the resource base |
| **Software / SaaS** | Net revenue retention, CAC payback | Growth quality |

### Ratios in forecasting

The ratio framework is also a **model-building** framework. The standard sales-driven approach:

1. **Forecast revenue** — from volume × price, market size × share, or a historical growth rate
   adjusted for known changes.
2. **Apply margin assumptions** to get EBIT — usually a common-size percentage anchored to history
   and peer levels.
3. **Apply the interest burden and tax burden** to reach net income.
4. **Drive the balance sheet off activity ratios** — hold DOH, DSO, and days payables constant (or
   trend them) to derive working capital, and drive fixed assets off fixed asset turnover.
5. **Derive cash flow** from the forecast income statement and balance sheet movements.
6. **Sensitivity-test** the two or three assumptions that matter most.

This is precisely the machinery of FSA LM12 and Equity LM8. Learning it here means learning it once.

> The discipline that separates a model from a spreadsheet: **every assumption must be either
> anchored to history, anchored to a peer, or explicitly justified.** A margin forecast that has
> never been achieved by the company or anyone in its industry is not a forecast.

---

## Formulas to know cold

```
ACTIVITY
  Inventory turnover = COGS / Avg inventory           DOH = 365 / Inventory turnover
  Receivables turnover = Revenue / Avg receivables    DSO = 365 / Receivables turnover
  Payables turnover = Purchases / Avg payables        Days payables = 365 / Payables turnover
  Total asset turnover = Revenue / Avg total assets
  Cash conversion cycle = DOH + DSO − Days of payables

LIQUIDITY
  Current = CA / CL     Quick = (Cash + ST inv + Receivables) / CL     Cash = (Cash + ST inv) / CL
  Defensive interval = (Cash + ST inv + Receivables) / Daily cash expenditures

SOLVENCY
  Debt-to-assets / Debt-to-capital / Debt-to-equity
  Financial leverage = Avg total assets / Avg total equity
  Interest coverage = EBIT / Interest payments
  Fixed charge coverage = (EBIT + Lease payments) / (Interest payments + Lease payments)

PROFITABILITY
  Margins: Gross, Operating, Pre-tax, Net  (each ÷ Revenue)
  ROA = Net income / Avg total assets      ROE = Net income / Avg equity

DUPONT (3-part)
  ROE = (NI/Revenue) × (Revenue/Avg assets) × (Avg assets/Avg equity)

DUPONT (5-part)
  ROE = (NI/EBT) × (EBT/EBIT) × (EBIT/Revenue) × (Revenue/Avg assets) × (Avg assets/Avg equity)
        tax burden  interest burden  op margin    asset turnover      financial leverage
```

---

## Exam traps

> **Trap 1 — Wrong numerator in activity ratios.** Inventory turnover uses **COGS**; receivables
> turnover uses **revenue**; payables turnover uses **purchases**. Three different numerators.

> **Trap 2 — Averages vs. period-end.** Any ratio mixing an income-statement flow with a
> balance-sheet stock uses the **average** balance. Pure balance-sheet ratios use period-end.

> **Trap 3 — Interest coverage uses EBIT, not net income.** EBIT is *before* interest, which is the
> whole point of a coverage ratio.

> **Trap 4 — The double role of leverage in DuPont.** It raises the leverage multiplier and lowers
> the interest burden. Questions ask which dominates — the answer is not automatic.

> **Trap 5 — Interpreting the interest burden backwards.** EBT/EBIT: **higher is better** (closer to
> 1 means less profit consumed by interest). Same for tax burden. Candidates often invert both.

> **Trap 6 — Cash conversion cycle sign.** Days of **payables is subtracted**. Adding it is a
> planted error. Negative cycles are good, not an error.

> **Trap 7 — Comparing ratios across accounting policies.** LIFO vs FIFO, differing depreciation
> lives, IFRS vs US GAAP leases — adjust before comparing.

> **Trap 8 — A high current ratio read as unambiguously good.** It may signal excess idle cash,
> bloated receivables, or unsold inventory. Decompose it before concluding.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company has net profit margin 6%, total asset turnover 1.8, and financial leverage 2.5. Compute ROE. Then it lifts leverage to 3.2 while net margin falls to 5.4% (higher interest). What is the new ROE?

<details><summary>Answer</summary>

ROE = 0.06 × 1.8 × 2.5 = **27.0%**

After: ROE = 0.054 × 1.8 × 3.2 = **31.1%**

ROE rose — but entirely through **leverage**, with operating performance unchanged and profitability *falling*. The company is riskier, not better. This is exactly why the decomposition matters: the headline ROE improvement is misleading on its own.

</details>

**2.** Compute the 5-part DuPont: net income 240, EBT 320, EBIT 420, revenue 3,000, average assets 2,400, average equity 1,000.

<details><summary>Answer</summary>

Tax burden = 240/320 = **0.750**
Interest burden = 320/420 = **0.762**
Operating margin = 420/3,000 = **0.140**
Asset turnover = 3,000/2,400 = **1.250**
Financial leverage = 2,400/1,000 = **2.400**

ROE = 0.750 × 0.762 × 0.140 × 1.250 × 2.400 = **0.240 = 24.0%**

Check: 240 / 1,000 = 24.0% ✓

Reading it: an effective tax rate of 25%, interest consuming about 24% of operating profit (a meaningfully levered company), a 14% operating margin, and 2.4× leverage.

</details>

**3.** DOH is 62 days, DSO is 41 days, days of payables is 38 days. Compute the cash conversion cycle and interpret it.

<details><summary>Answer</summary>

CCC = 62 + 41 − 38 = **65 days**.

The company funds 65 days of operations itself: it pays suppliers 38 days after purchase, but cash from customers does not arrive until 103 days after inventory arrives. Every unit of growth requires 65 days' worth of incremental working capital funding.

To shorten it: turn inventory faster, collect faster, or negotiate longer supplier terms. A retailer with a negative CCC collects from customers before paying suppliers — its growth is self-funding, which is a structural advantage.

</details>

**4.** ROE fell from 18% to 13%. Tax burden and interest burden are unchanged; asset turnover rose from 1.1 to 1.3; leverage is unchanged. Where is the problem?

<details><summary>Answer</summary>

If ROE fell while asset turnover **rose** and tax burden, interest burden, and leverage were all flat, the only remaining component is **operating margin (EBIT/revenue)** — it must have fallen, and by more than enough to offset the turnover improvement.

The company is selling more per unit of assets but earning less on each sale: price competition, input cost inflation not passed through, an unfavourable mix shift toward lower-margin products, or operating costs growing faster than revenue. Go to the common-size income statement and locate the line.

</details>

**5.** Why does interest coverage use EBIT rather than net income?

<details><summary>Answer</summary>

Because the ratio asks: **how many times over can operating profit cover the interest bill?** Interest is deducted in arriving at net income, so using net income would ask whether profit *after* paying interest can pay interest — circular and meaningless.

EBIT is the earnings available *before* the interest claim, which is exactly the pool a lender cares about. The same logic explains fixed charge coverage, which adds lease payments to both numerator and denominator because leases are a similar fixed claim.

</details>

**6.** Company A has a current ratio of 2.8; Company B, a direct competitor, has 1.3. Is A more liquid?

<details><summary>Answer</summary>

**Not necessarily.** Decompose before concluding.

A's high ratio may reflect **slow-moving inventory** (check DOH) or **stretched receivables** (check DSO) — current assets that are large precisely because they are not converting to cash. Compute A's **quick ratio**: if it is far below the current ratio, the strength is all inventory.

B's 1.3 may be perfectly healthy if it turns inventory in 20 days and collects in 25 — a short cash conversion cycle means it needs less liquidity buffer. Compare the **cash conversion cycles**, not the balance-sheet snapshot.

</details>

**7.** You are forecasting a manufacturer. Revenue is expected to grow 8%. How do you forecast receivables and inventory, and what would make you depart from that method?

<details><summary>Answer</summary>

Default: hold the **activity ratios constant**. Forecast receivables as `Revenue_forecast / Receivables turnover` (equivalently, `DSO × Revenue / 365`), and inventory as `DOH × COGS / 365`. This assumes working capital scales with activity, which is usually the best neutral assumption.

Depart from it when you have a reason: a stated change in credit terms, a known customer-mix shift toward slower payers, a deliberate inventory build for a product launch, a new distribution model, or a historical trend in DSO/DOH that is clearly directional rather than noisy. Every departure must be named and justified — that is the difference between a model and a guess.

</details>

---

## Done when

- [ ] I can reproduce every ratio in the four families from memory, with the correct numerator
- [ ] I can compute the cash conversion cycle and explain what a negative cycle means economically
- [ ] I can perform both three-part and five-part DuPont and verify the result against ROE directly
- [ ] I can explain why leverage appears twice in the five-part decomposition with opposing effects
- [ ] I can take a change in ROE and identify which component caused it
- [ ] I can name an industry-specific ratio for at least five industries and say what it measures
- [ ] I can describe the six steps of building a ratio-driven earnings forecast
- [ ] I answered the self-check cold, several days after first study

---

← [LM10 Financial Reporting Quality](lm-10-financial-reporting-quality.md)  ·  [Topic index](README.md)  ·  [LM12 Introduction to Financial Statement Modeling](lm-12-introduction-to-financial-statement-modeling.md) →
