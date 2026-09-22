# FSA · LM02 — Analyzing Income Statements

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM1. Basic accounting identity: Assets = Liabilities + Equity. |
| **Where it shows up** | 2–3 questions. EPS is near-certain; revenue/expense recognition is heavily tested conceptually. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe general principles of revenue recognition, specific revenue recognition applications, and implications of revenue recognition choices for financial analysis
- describe general principles of expense recognition, specific expense recognition applications, implications of expense recognition choices for financial analysis and contrast costs that are capitalized versus those that are expensed in the period in which they are incurred
- describe the financial reporting treatment and analysis of non-recurring items (including discontinued operations, unusual or infrequent items) and changes in accounting policies
- describe how earnings per share is calculated and calculate and interpret a company's basic and diluted earnings per share for companies with simple and complex capital structures including those with antidilutive securities
- evaluate a company's financial performance using common-size income statements and financial ratios based on the income statement

---

## Core concepts

### The shape of an income statement

```
Revenue (net)
  − Cost of goods sold
  = Gross profit
  − Operating expenses (SG&A, R&D, depreciation & amortisation)
  = Operating profit (EBIT)
  − Interest expense  ± Other income
  = Pre-tax income (EBT)
  − Income tax expense
  = Net income from continuing operations
  ± Income (loss) from discontinued operations, net of tax
  = Net income
```

Two structural facts to internalise now: **discontinued operations sit below the continuing-
operations line, net of tax**, and everything above that line is what you forecast. Analysts build
models off continuing operations; the discontinued line is history.

### Revenue recognition — the five-step model

IFRS 15 / ASC 606 are converged. The core principle: recognise revenue **to depict the transfer of
promised goods or services in an amount reflecting the consideration expected to be entitled to.**

| Step | Question |
| --- | --- |
| 1 | Identify the **contract** with the customer |
| 2 | Identify the **performance obligations** in it |
| 3 | Determine the **transaction price** |
| 4 | **Allocate** the transaction price to the performance obligations |
| 5 | **Recognise revenue** when (or as) each performance obligation is satisfied |

Revenue is recognised when **control transfers**, not when cash is received and not when the
invoice is issued. Control can transfer at a point in time or **over time** (long-term contracts,
subscriptions) — over-time recognition requires that the customer receives benefit as you perform,
or the asset has no alternative use and you have an enforceable right to payment.

**Applications you should recognise:**

- **Principal vs. agent.** A principal controls the good before transfer and reports **gross**
  revenue. An agent arranges the transfer and reports only its **net** commission. The gross/net
  choice does not change net income but transforms revenue and margin — a classic manipulation site.
- **Variable consideration** (rebates, returns, bonuses) is estimated and included only to the
  extent a significant reversal is not probable — a judgement call, and therefore a soft spot.
- **Bill-and-hold**, consignment, and channel stuffing all turn on whether control actually moved.
- **Contract assets / liabilities.** Unbilled revenue earned is a contract asset; cash received
  ahead of performance is a **contract liability** (deferred revenue) — a *liability*, not revenue.

> **Analytical implication:** aggressive revenue recognition shows up as revenue growing faster than
> cash collections. Watch **receivables (DSO) rising faster than revenue**, and revenue growth that
> outpaces operating cash flow.

### Expense recognition

The governing idea is the **matching principle**: recognise costs in the period in which the
associated revenue is recognised. Costs that cannot be matched to specific revenue (period costs —
most SG&A) are expensed as incurred.

Judgement enters through:

| Area | The choice | Effect of the more aggressive option |
| --- | --- | --- |
| **Inventory cost flow** | FIFO / weighted average (LIFO under US GAAP only) | FIFO in rising prices → lower COGS, higher profit |
| **Depreciation** | Straight-line vs. accelerated; useful life; salvage value | Longer life / higher salvage → lower annual expense, higher early profit |
| **Amortisation** | Life of intangible | Longer life → lower expense |
| **Bad debt** | Allowance estimate | Lower allowance → higher profit, higher receivables |
| **Warranty** | Provision estimate | Lower provision → higher profit |

### Capitalising vs. expensing — the single most testable idea here

| | **Capitalise** | **Expense** |
| --- | --- | --- |
| Balance sheet | Asset created | No asset |
| Income statement, **year 1** | Only depreciation hits P&L → **higher** net income | Full cost hits P&L → **lower** net income |
| Income statement, **later years** | Depreciation continues → **lower** net income | Nothing further → **higher** net income |
| Total income over asset's life | **Identical** | **Identical** |
| **Cash flow from operations (CFO)** | **Higher** (cash outflow is investing) | **Lower** (outflow is operating) |
| **Cash flow from investing (CFI)** | More negative | Less negative |
| **Total cash flow** | **Identical** | **Identical** |
| Equity, early years | Higher | Lower |
| Debt/equity, ROA, ROE, early years | Lower D/E; higher early ROA and ROE; then reverses | Opposite |
| Earnings volatility | **Smoother** | Lumpier |

Memorise the pattern rather than the table: **capitalising shifts expense from today into the
future, and shifts cash outflow from operating into investing.** Both totals are unchanged; only
timing and classification move. This exact logic returns in LM7 (long-term assets) and in
Corporate Issuers.

Standards-level points: **interest on self-constructed assets is capitalised** under both frameworks.
**Research is always expensed**; **development** may be capitalised under IFRS once technical and
commercial feasibility criteria are met, but is generally expensed under US GAAP (with a software
exception once technological feasibility is reached).

### Non-recurring items

Analysts separate persistent earnings from transitory ones, because only the persistent part should
be extrapolated.

- **Discontinued operations** — a component that has been disposed of or is held for sale, whose
  operations and cash flows are (or will be) eliminated. Reported **separately, net of tax, below
  continuing operations**. **Exclude from forecasts entirely.**
- **Unusual or infrequent items** — reported **within continuing operations, pre-tax**. Examples:
  restructuring charges, impairments, gains/losses on asset sales. Judgement required: a
  "restructuring charge" that appears every year for five years is not unusual — it is an operating
  cost the company would like you to ignore.
- **Changes in accounting policy** — applied **retrospectively**: prior periods are restated so the
  comparison remains valid.
- **Changes in accounting estimate** (useful life, bad debt rate) — applied **prospectively**: only
  current and future periods change; no restatement.
- **Correction of a prior-period error** — **restate** prior statements, with disclosure. A
  restatement is a serious quality signal.

> Memorise the triad: **policy → retrospective; estimate → prospective; error → restate.**

### Earnings per share

**Simple capital structure** — no potentially dilutive securities outstanding. Report **basic EPS**
only.

**Complex capital structure** — convertible debt, convertible preferred, options, warrants, or
contingent shares exist. Report **both basic and diluted EPS**.

**Basic EPS** = (Net income − preferred dividends) ÷ weighted average shares outstanding.

Weighting rules, which is where marks are lost:

- Shares issued or repurchased are weighted by the **fraction of the year outstanding**.
- **Stock splits and stock dividends are applied retroactively** to the start of the period *and* to
  all prior periods presented. They are *not* time-weighted — a 2-for-1 split in November doubles
  the share count for the whole year and for last year's reported EPS too.

**Diluted EPS** applies the *if-converted* method to convertibles and the *treasury stock* method to
options and warrants:

| Security | Numerator adjustment | Denominator adjustment |
| --- | --- | --- |
| **Convertible preferred** | Add back preferred dividends | Add shares from conversion |
| **Convertible debt** | Add back after-tax interest: `interest × (1 − t)` | Add shares from conversion |
| **Options / warrants** | None | Add *net* new shares (treasury stock method) |

**Treasury stock method:** assume options are exercised at the exercise price and the proceeds are
used to repurchase shares at the **average market price**.

```
Net new shares = N × (Average market price − Exercise price) / Average market price
```

Options are dilutive only when they are **in the money** (average market price > exercise price).

**Antidilutive securities are excluded.** Test each security separately: compute its incremental
EPS effect (numerator adjustment ÷ shares added). If that per-share effect is **greater than basic
EPS**, including it would *raise* EPS — it is antidilutive and must be left out. Diluted EPS can
never exceed basic EPS.

### Common-size analysis and income statement ratios

**Vertical common-size income statement:** every line expressed as a **percentage of revenue**. This
strips out size, making a €50m and a €50bn company directly comparable, and makes cost-structure
drift visible over time.

**Horizontal common-size:** every line indexed to a base year (base = 100), which exposes growth
rates cleanly.

Core margins:

| Ratio | Reads as |
| --- | --- |
| **Gross margin** = Gross profit / Revenue | Pricing power and input costs |
| **Operating margin** = Operating income / Revenue | Operating efficiency, before financing and tax |
| **Pre-tax margin** = EBT / Revenue | Adds the effect of financing |
| **Net profit margin** = Net income / Revenue | The bottom line, after everything |

Reading them *together* is the skill: gross margin flat but operating margin falling means the
problem is in **operating expenses**, not pricing. Operating margin flat but net margin falling
means the problem is **financing or tax**. The exam asks exactly this kind of question.

---

## Formulas to know cold

```
Basic EPS = (Net income − Preferred dividends) / Weighted average shares outstanding

Diluted EPS = [Net income − Pref. div. + Convertible pref. div. + Convertible debt interest × (1 − t)]
              ─────────────────────────────────────────────────────────────────────────────────────
              [Weighted avg shares + Shares from conv. pref. + Shares from conv. debt + Net new option shares]

Treasury stock method:
    Net new shares = N × (Average market price − Exercise price) / Average market price
    (zero if the option is out of the money)

Antidilution test for a security:
    Incremental EPS effect = Δ Numerator / Δ Denominator
    If Δ Numerator / Δ Denominator > Basic EPS  →  ANTIDILUTIVE, exclude it

Gross margin      = Gross profit / Revenue
Operating margin  = Operating income / Revenue
Pre-tax margin    = EBT / Revenue
Net profit margin = Net income / Revenue
```

---

## Exam traps

> **Trap 1 — Stock splits are not time-weighted.** A split or stock dividend is applied
> **retroactively** to the beginning of the earliest period presented. Weighting it by months
> outstanding is the most common EPS error at Level I.

> **Trap 2 — Forgetting to exclude antidilutive securities.** Diluted EPS ≤ basic EPS, always. If
> your diluted answer exceeds basic, you included an antidilutive security. Test each one separately —
> a security can be dilutive in one year and antidilutive in the next.

> **Trap 3 — Convertible debt interest must be added back *after tax*.** Use `interest × (1 − t)`.
> Adding back the pre-tax figure is a planted wrong answer.

> **Trap 4 — Policy vs. estimate.** Changing depreciation *method* is a change in **policy**
> (retrospective) in most cases; changing the *useful life* or *salvage value* is a change in
> **estimate** (prospective). The exam swaps these deliberately.

> **Trap 5 — Capitalising and CFO.** Capitalising **raises CFO** and lowers CFI. Candidates
> routinely say it raises net income *and* has no cash effect. It has no effect on *total* cash, but
> a large effect on the *classification* — which is what ratios built on CFO pick up.

> **Trap 6 — Deferred revenue is a liability.** Cash received before performance is a contract
> liability. It is not revenue, and it is not an asset.

> **Trap 7 — Gross vs. net (principal vs. agent).** The choice does not change net income at all.
> Any answer claiming a net income effect is wrong; the effect is on revenue and margin percentages.

> **Trap 8 — Reading one margin alone.** Questions give you two margins moving differently and ask
> where the problem is. Always locate the change between the two lines that bracket it.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company has 1,000,000 shares outstanding on 1 January, issues 240,000 shares on 1 April, and executes a 2-for-1 stock split on 1 December. What is the weighted average share count?

<details><summary>Answer</summary>

Apply the split retroactively to *everything*, then time-weight the issuance.

- 1 Jan shares: 1,000,000 × 2 = 2,000,000, outstanding 12/12
- 1 Apr issuance: 240,000 × 2 = 480,000, outstanding 9/12

Weighted average = 2,000,000 + 480,000 × (9/12) = 2,000,000 + 360,000 = **2,360,000 shares**.

The split is *not* weighted for the one month it was in force.

</details>

**2.** Net income is 12,000,000. There are 4,000,000 weighted average shares and 500,000 options outstanding with an exercise price of 20. The average market price for the year was 25. Compute basic and diluted EPS.

<details><summary>Answer</summary>

Basic EPS = 12,000,000 / 4,000,000 = **3.00**.

Treasury stock method: net new shares = 500,000 × (25 − 20)/25 = 500,000 × 0.20 = 100,000.

Diluted EPS = 12,000,000 / 4,100,000 = **2.927**.

The numerator is unchanged — options never affect the numerator.

</details>

**3.** A company has 8% convertible bonds with a face value of 10,000,000, convertible into 300,000 shares. The tax rate is 25%, net income is 9,000,000, and there are 3,000,000 weighted average shares. Is the convertible dilutive?

<details><summary>Answer</summary>

Basic EPS = 9,000,000 / 3,000,000 = **3.00**.

Incremental effect of the convertible:
- Numerator add-back = 10,000,000 × 8% × (1 − 0.25) = 800,000 × 0.75 = 600,000
- Denominator addition = 300,000 shares
- Incremental EPS = 600,000 / 300,000 = **2.00**

2.00 < 3.00, so it is **dilutive** — include it.

Diluted EPS = (9,000,000 + 600,000) / 3,300,000 = 9,600,000 / 3,300,000 = **2.909**.

</details>

**4.** A company capitalises a cost that its competitor expenses. In year 1, how do net income, CFO, CFI, and total cash flow compare?

<details><summary>Answer</summary>

Versus the expensing competitor, the capitalising company reports **higher net income** (only the depreciation portion hits P&L), **higher CFO** (the cash outflow is classified as investing), **more negative CFI**, and **identical total cash flow**. In later years the net income relationship reverses as depreciation continues while the expenser has no further charge. Cumulative net income over the asset's life is identical under both.

</details>

**5.** Distinguish the accounting treatment of: (a) a change in depreciation method, (b) a change in estimated useful life, (c) discovery of a prior-period error.

<details><summary>Answer</summary>

(a) Change in **accounting policy** → applied **retrospectively**; prior periods restated.
(b) Change in **accounting estimate** → applied **prospectively**; no restatement.
(c) **Error** → prior-period statements are **restated**, with disclosure. A restatement is a significant reporting-quality red flag.

</details>

**6.** Gross margin has been stable at 42% for three years, but operating margin has fallen from 18% to 12%. What does that tell you, and what would you investigate?

<details><summary>Answer</summary>

Stable gross margin means pricing and direct input costs are not the problem — the deterioration is **between gross profit and operating profit**, i.e. in operating expenses (SG&A, R&D, or depreciation/amortisation). Investigate: SG&A growing faster than revenue (overhead not scaling), a step-up in R&D, higher D&A from a recent capex or acquisition cycle, or recurring 'unusual' charges being run through operating expenses.

</details>

**7.** A company reports revenue gross rather than net after concluding it is a principal rather than an agent. What changes?

<details><summary>Answer</summary>

**Revenue and cost of sales both rise by the same amount; net income is unchanged.** Gross margin *percentage* falls (same gross profit over a much larger revenue base), and every revenue-scaled metric — net margin, asset turnover — shifts. Because net income is unaffected, the gross/net question is purely about the *quality and comparability* of the revenue line, which is why it attracts manipulation.

</details>

**8.** Why must the incremental EPS effect of each potentially dilutive security be tested individually rather than throwing them all into diluted EPS at once?

<details><summary>Answer</summary>

Because a security whose incremental EPS effect exceeds basic EPS is **antidilutive** — including it would raise EPS, which the standards prohibit. Securities must be ranked by incremental effect (most dilutive first) and included only while EPS continues to fall. Dumping them all in can produce a diluted figure above basic, which is always wrong.

</details>

---

## Done when

- [ ] I can state the five-step revenue recognition model and explain what 'control transfers' means
- [ ] I can reproduce the capitalise-vs-expense table from memory, including the CFO/CFI effects
- [ ] I can compute weighted average shares with an issuance, a repurchase, and a split in the same year
- [ ] I can compute diluted EPS with convertible debt, convertible preferred, and options all present
- [ ] I can test a security for antidilution and explain why it must be excluded
- [ ] I can state the triad: policy → retrospective, estimate → prospective, error → restate
- [ ] I can read two margins moving differently and locate where the problem is
- [ ] I answered the self-check cold, several days after first study

---

← [LM01 Introduction to Financial Statement Analysis](lm-01-introduction-to-financial-statement-analysis.md)  ·  [Topic index](README.md)  ·  [LM03 Analyzing Balance Sheets](lm-03-analyzing-balance-sheets.md) →
