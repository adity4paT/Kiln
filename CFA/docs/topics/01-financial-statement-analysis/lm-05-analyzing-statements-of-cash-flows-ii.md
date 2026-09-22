# FSA · LM05 — Analyzing Statements of Cash Flows II

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM4. You must be able to build CFO by the indirect method before starting. |
| **Where it shows up** | 1–2 questions. FCFF/FCFE reappear in Equity LM6 — learn them properly here. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- analyze and interpret both reported and common-size cash flow statements
- calculate and interpret free cash flow to the firm, free cash flow to equity, and performance and coverage cash flow ratios

---

## Core concepts

### Common-size cash flow statements

Two accepted approaches, and the exam accepts either — but they answer different questions.

**Approach 1 — as a percentage of revenue.** Every line divided by net revenue. Directly comparable
to the common-size income statement, so you can line them up: if revenue-scaled net income is 8% but
revenue-scaled CFO is 3%, the gap is visible immediately.

**Approach 2 — inflows as a percentage of total inflows, outflows as a percentage of total
outflows.** Answers "where does cash come from, and where does it go?" Useful for spotting a company
whose cash inflows are increasingly from borrowing rather than from customers.

### Reading the statement analytically

Work through four questions in order:

1. **Is CFO positive, and does it exceed net income?** A healthy, mature company generally has
   CFO > net income, because depreciation is added back and working capital is stable. CFO
   persistently *below* net income is the primary earnings-quality warning.
2. **What drives CFO — earnings or working capital?** CFO propped up by stretching payables or
   liquidating inventory is not repeatable.
3. **Does CFO cover capex and dividends?** If not, the shortfall must come from asset sales or new
   financing — check CFF for which.
4. **What does the financing section say about the capital structure trajectory?** Consistent net
   borrowing to fund a CFO shortfall is the classic path into distress.

### Free cash flow

**FCFF — free cash flow to the firm.** Cash available to **all** capital providers (debt and equity)
after operating expenses, taxes, and the investment needed to sustain operations.

```
FCFF = CFO + Interest expense × (1 − tax rate) − Capital expenditure
```

Why add back after-tax interest? Because CFO is stated **after** paying interest to debtholders, and
FCFF is meant to be available to *all* providers of capital — so the payment to one class must be
added back. The `(1 − t)` factor reflects the tax deductibility of interest: the true cash cost to
the firm is the after-tax amount.

Starting from net income instead:

```
FCFF = Net income + Non-cash charges + Interest × (1 − t) − Capex − Increase in working capital
```

**FCFE — free cash flow to equity.** Cash available to **shareholders only**, after debt service.

```
FCFE = CFO − Capital expenditure + Net borrowing
```

where net borrowing = new debt issued − debt repaid. And the bridge between the two:

```
FCFE = FCFF − Interest × (1 − t) + Net borrowing
```

> **Trap:** under **IFRS**, if interest paid was classified as **financing** rather than operating,
> CFO already excludes it — so do **not** add it back again in FCFF. Always check the classification
> before applying the formula. Under US GAAP interest paid is always in CFO, so the add-back always
> applies.

### Cash flow ratios

**Performance ratios** — how much cash each unit of activity generates.

| Ratio | Formula | Reads as |
| --- | --- | --- |
| Cash flow to revenue | CFO / Net revenue | Cash generated per unit of sales |
| Cash return on assets | CFO / Average total assets | Cash generated per unit of assets |
| Cash return on equity | CFO / Average shareholders' equity | Cash generated per unit of equity |
| Cash to income | CFO / Operating income | **Earnings quality.** Persistently < 1 is a warning |
| Cash flow per share | (CFO − Preferred dividends) / Weighted avg common shares | Per-share cash generation |

**Coverage ratios** — can cash flow service the obligations?

| Ratio | Formula | Reads as |
| --- | --- | --- |
| Debt coverage | CFO / Total debt | Years of CFO to repay all debt |
| Interest coverage | (CFO + Interest paid + Taxes paid) / Interest paid | Cash-based interest cover |
| Reinvestment | CFO / Cash paid for long-term assets | Can it self-fund capex? |
| Debt payment | CFO / Cash paid for long-term debt repayment | Can it self-fund repayments? |
| Dividend payment | CFO / Dividends paid | Is the dividend covered by cash? |
| Investing and financing | CFO / (Cash outflows for investing + financing) | Overall self-sufficiency |

The **cash interest coverage** numerator adds back interest *and* taxes paid because both were
deducted in arriving at CFO, and the ratio asks how much cash was available *before* servicing debt.

> The two highest-signal ratios for Level I purposes: **cash to income** (earnings quality) and
> **CFO / total debt** (credit capacity). Both recur in Fixed Income credit analysis.

---

## Formulas to know cold

```
FCFF = CFO + Interest × (1 − t) − Capex
FCFF = Net income + Non-cash charges + Interest × (1 − t) − Capex − ΔWorking capital
FCFE = CFO − Capex + Net borrowing
FCFE = FCFF − Interest × (1 − t) + Net borrowing

Cash flow to revenue      = CFO / Net revenue
Cash return on assets     = CFO / Average total assets
Cash return on equity     = CFO / Average shareholders' equity
Cash to income            = CFO / Operating income
Cash flow per share       = (CFO − Preferred dividends) / Weighted average common shares

Debt coverage             = CFO / Total debt
Cash interest coverage    = (CFO + Interest paid + Taxes paid) / Interest paid
Reinvestment              = CFO / Cash paid for long-term assets
Dividend payment          = CFO / Dividends paid
```

---

## Exam traps

> **Trap 1 — Double-counting interest under IFRS.** If interest paid was classified as financing,
> CFO never included it. Adding it back in FCFF overstates FCFF. **Check the classification first.**

> **Trap 2 — Interest is added back *after tax*.** `Interest × (1 − t)`, not gross interest.

> **Trap 3 — Net borrowing, not gross.** FCFE uses **issuance minus repayment**. Using only new debt
> issued overstates FCFE.

> **Trap 4 — FCFF vs. FCFE confusion.** FCFF is before debt service and belongs to *everyone*; FCFE
> is after debt service and belongs to shareholders. FCFF is discounted at **WACC**; FCFE at the
> **cost of equity**. Mismatching the cash flow and the discount rate is the classic valuation error
> — it returns in Equity LM6.

> **Trap 5 — Cash interest coverage numerator.** It is `CFO + interest paid + taxes paid`. Omitting
> taxes is a planted error.

> **Trap 6 — Reading CFO growth without its source.** CFO up 30% because payables were stretched by
> 45 days is not a real improvement, and it reverses next year.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** CFO is 1,200 (US GAAP). Interest expense was 150, the tax rate is 25%, capex was 500, debt issued was 300 and debt repaid was 180. Compute FCFF and FCFE.

<details><summary>Answer</summary>

FCFF = 1,200 + 150 × (1 − 0.25) − 500 = 1,200 + 112.5 − 500 = **812.5**

Net borrowing = 300 − 180 = 120.
FCFE = 1,200 − 500 + 120 = **820**

Check via the bridge: FCFE = FCFF − Int(1−t) + Net borrowing = 812.5 − 112.5 + 120 = **820** ✓

</details>

**2.** Same facts, but the company reports under IFRS and classifies interest paid as financing. What changes?

<details><summary>Answer</summary>

CFO of 1,200 now **excludes** the interest payment, so there is nothing to add back:

**FCFF = 1,200 − 500 = 700.**

For FCFE, the interest payment sits in CFF, so it must be deducted:
**FCFE = 1,200 − 500 + 120 − 150 = 670** (using actual interest paid).

The lesson: the formula depends on the classification, not the other way round. Always read the statement first.

</details>

**3.** A company's cash-to-income ratio (CFO / operating income) has fallen from 1.15 to 0.72 over two years. What are you looking for?

<details><summary>Answer</summary>

Operating income is increasingly *not* converting to cash. Candidates:
- Receivables growing faster than revenue (revenue recognised, cash not collected)
- Inventory build
- Payables being paid down faster
- Capitalised costs flattering operating income (though this raises CFO too)
- Aggressive revenue recognition — over-time recognition, bill-and-hold, channel stuffing

Go to the working-capital section of the indirect statement: it names the account absorbing the cash.

</details>

**4.** Why is FCFF discounted at WACC while FCFE is discounted at the cost of equity?

<details><summary>Answer</summary>

FCFF is the cash available to **all** capital providers, so it must be discounted at the **blended required return of all of them** — the weighted average cost of capital. FCFE is what remains **after** debtholders have been paid, so it belongs solely to shareholders and must be discounted at **their** required return, the cost of equity. Discounting FCFF at the cost of equity (or FCFE at WACC) double-counts or omits the debt claim and gives a meaningless value.

</details>

**5.** Net income 900, depreciation 260, increase in working capital 180, capex 400, interest expense 120, tax rate 30%. Compute FCFF from net income.

<details><summary>Answer</summary>

FCFF = 900 + 260 + 120 × (1 − 0.30) − 400 − 180
     = 900 + 260 + 84 − 400 − 180
     = **664**

</details>

**6.** CFO is 800. Capex is 950. Dividends paid are 120. What does this tell you and where do you look next?

<details><summary>Answer</summary>

CFO does not cover capex, let alone the dividend — a shortfall of 950 + 120 − 800 = **270** must be funded from somewhere. Go to **CFF and CFI**: is it new borrowing (leverage rising), an equity issue (dilution), or asset sales (shrinking the earning base)? One year of this can be a normal investment cycle; three consecutive years with rising debt is a trajectory toward distress. Also check whether the capex is growth or maintenance — a company outspending CFO on *growth* capex is a different story from one that cannot fund maintenance.

</details>

---

## Done when

- [ ] I can compute FCFF and FCFE from CFO and from net income, and cross-check one against the other
- [ ] I can adjust the FCFF formula correctly when interest paid is classified as financing under IFRS
- [ ] I can state why FCFF pairs with WACC and FCFE with the cost of equity
- [ ] I can compute the five performance and six coverage cash flow ratios
- [ ] I can read a cash flow statement and say in three sentences what the company is doing
- [ ] I answered the self-check cold, several days after first study

---

← [LM04 Analyzing Statements of Cash Flows I](lm-04-analyzing-statements-of-cash-flows-i.md)  ·  [Topic index](README.md)  ·  [LM06 Analysis of Inventories](lm-06-analysis-of-inventories.md) →
