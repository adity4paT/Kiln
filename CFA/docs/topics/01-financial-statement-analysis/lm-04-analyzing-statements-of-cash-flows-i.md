# FSA · LM04 — Analyzing Statements of Cash Flows I

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM2–LM3. You must be fluent with accruals and the balance sheet before starting. |
| **Where it shows up** | 2–3 questions, and cash flow reasoning appears indirectly across Equity, Corporate Issuers, and Fixed Income credit analysis. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe how the cash flow statement is linked to the income statement and the balance sheet
- describe the steps in the preparation of direct and indirect cash flow statements, including how cash flows can be computed using income statement and balance sheet data
- demonstrate the conversion of cash flows from the indirect to direct method
- contrast cash flow statements prepared under International Financial Reporting Standards (IFRS) and US generally accepted accounting principles (US GAAP)

---

## Core concepts

### Why the cash flow statement is the one that matters

Net income is an opinion; cash is a fact. Revenue recognition, depreciation method, and provision
estimates all move net income without moving cash. The cash flow statement is the reconciliation
between the two — and the gap between them is the most reliable earnings-quality signal in FSA.

### The three sections

| Section | Contains | Rule of thumb |
| --- | --- | --- |
| **Operating (CFO)** | Cash from the core business: customers in, suppliers and employees out, interest and taxes | Should be positive and should broadly track net income |
| **Investing (CFI)** | Buying and selling long-term assets and investments | Normally negative for a growing company |
| **Financing (CFF)** | Debt raised/repaid, equity issued/repurchased, dividends paid | Tells you how the gap between CFO and CFI is plugged |

Reading the **pattern of signs** is a fast diagnostic:

| CFO | CFI | CFF | Likely story |
| --- | --- | --- | --- |
| + | − | − | **Mature, self-funding.** Generates cash, invests, returns the rest |
| + | − | + | **Growing.** Operations positive but investment exceeds it; raising capital |
| + | + | − | **Shrinking or restructuring.** Selling assets and paying down debt |
| − | − | + | **Early stage or in trouble.** Burning cash, funded externally |
| − | + | + | **Distress.** Selling assets *and* borrowing just to fund operations |

### The link to the other two statements

```
Beginning cash  +  CFO  +  CFI  +  CFF  ± FX effect  =  Ending cash
```

And the articulation you must be able to run in both directions:

- **Income statement → CFO:** start from net income, reverse non-cash items, reverse
  investing/financing gains and losses, adjust for working-capital changes.
- **Balance sheet → cash flows:** the *change* in each balance-sheet account is explained by a cash
  flow, a non-cash event, or both. Change in gross PP&E plus depreciation and disposals gives you
  capex. Change in retained earnings equals net income minus dividends — which backs out dividends
  paid when they are not disclosed.

### Direct vs. indirect — the same CFO, two presentations

**Only the operating section differs.** CFI and CFF are presented identically. Both methods produce
**exactly the same CFO total**.

**Direct method:** lists actual operating cash receipts and payments.

```
Cash collected from customers
− Cash paid to suppliers
− Cash paid to employees
− Cash paid for other operating expenses
− Cash paid for interest
− Cash paid for taxes
= CFO
```

More informative for forecasting, and preferred by both standard setters — but rarely used in
practice, because it costs more to produce.

**Indirect method:** reconciles from net income.

```
Net income
+ Non-cash charges (depreciation, amortisation, impairment, share-based comp)
− Gains on asset sales / + Losses on asset sales     ← reverse: these belong in investing
± Changes in working capital
= CFO
```

**The working-capital sign rule** — get this automatic:

| Account | Change | Effect on CFO |
| --- | --- | --- |
| **Asset** (receivables, inventory, prepaid) | Increase | **Subtract** (cash tied up) |
| **Asset** | Decrease | **Add** |
| **Liability** (payables, accrued, deferred revenue) | Increase | **Add** (cash retained) |
| **Liability** | Decrease | **Subtract** |

Mnemonic: **cash moves opposite to assets, and with liabilities.**

### Converting indirect to direct

This is an explicit LOS — practise it until mechanical. Take each income statement line and adjust
it by the related balance-sheet change.

```
Cash collected from customers
    = Revenue − Increase in receivables + Increase in unearned (deferred) revenue

Cash paid to suppliers
    = COGS + Increase in inventory − Increase in accounts payable
      (equivalently: purchases = COGS + ΔInventory; cash paid = purchases − ΔPayables)

Cash paid for operating expenses
    = Operating expenses (excl. D&A) + Increase in prepaid expenses − Increase in accrued liabilities

Cash paid for interest
    = Interest expense − Increase in interest payable
      (+ amortisation of premium / − amortisation of discount, if present)

Cash paid for taxes
    = Income tax expense − Increase in taxes payable − Increase in deferred tax liability
      (+ Increase in deferred tax asset)
```

**Worked example.** Revenue 10,000; receivables rose 400. COGS 6,000; inventory rose 200; payables
rose 150. Operating expenses excluding D&A 1,500; accrued liabilities fell 50.

```
Cash collected from customers = 10,000 − 400                    =  9,600
Cash paid to suppliers        = 6,000 + 200 − 150               = −6,050
Cash paid for operating exp.  = 1,500 + 50                      = −1,550
                                                                  ------
CFO (before interest and tax)                                   =  2,000
```

Every one of these is the same idea: **accrual figure, adjusted by the change in the related
balance-sheet account.** If you understand *why* the sign is what it is, you never need to memorise
the list.

### Computing capex and other investing flows

```
Ending gross PP&E = Beginning gross PP&E + Capex − Gross cost of assets disposed
Ending net PP&E   = Beginning net PP&E + Capex − Depreciation − Net book value of disposals

Cash received from a disposal = Net book value of the asset sold + Gain (or − Loss)
```

Dividends paid, when not given:

```
Dividends paid = Beginning retained earnings + Net income − Ending retained earnings
```

### IFRS vs. US GAAP — the classification differences

This is the most directly examinable content in the module.

| Item | **IFRS** | **US GAAP** |
| --- | --- | --- |
| **Interest paid** | Operating **or** financing | **Operating** |
| **Interest received** | Operating **or** investing | **Operating** |
| **Dividends paid** | Operating **or** financing | **Financing** |
| **Dividends received** | Operating **or** investing | **Operating** |
| **Taxes paid** | Operating, unless specifically identifiable with investing or financing | **Operating** |
| **Bank overdrafts** | May be included in cash and cash equivalents | Classified as **financing** |
| **Format** | Direct or indirect | Direct or indirect; if direct, a reconciliation to net income is required |

The pattern worth remembering: **IFRS offers choice; US GAAP is prescriptive and puts almost
everything in operating — except dividends paid, which are financing.**

> **Analytical consequence:** a company reporting under IFRS can boost CFO simply by classifying
> interest paid as financing. When comparing cross-framework, **restate to a common basis** — most
> analysts move interest paid and dividends paid out of CFO to compare the underlying operations.

---

## Formulas to know cold

```
Beginning cash + CFO + CFI + CFF ± FX effect = Ending cash

INDIRECT CFO:
  Net income
  + Depreciation, amortisation, impairment, share-based compensation
  − Gains on asset disposals   (+ Losses on asset disposals)
  − Increase in operating assets      (+ Decrease)
  + Increase in operating liabilities (− Decrease)
  = CFO

INDIRECT → DIRECT:
  Cash from customers   = Revenue − ΔReceivables + ΔUnearned revenue
  Cash to suppliers     = COGS + ΔInventory − ΔAccounts payable
  Cash for opex         = Opex (excl. D&A) + ΔPrepaid − ΔAccrued liabilities
  Cash for interest     = Interest expense − ΔInterest payable
  Cash for taxes        = Tax expense − ΔTaxes payable − ΔDeferred tax liability + ΔDeferred tax asset

Capex           = Ending gross PP&E − Beginning gross PP&E + Gross cost of disposals
Disposal proceeds = Net book value of asset sold + Gain (− Loss)
Dividends paid  = Beginning RE + Net income − Ending RE
```

---

## Exam traps

> **Trap 1 — Working-capital signs.** An **increase in an asset reduces CFO**; an **increase in a
> liability increases CFO**. Reversing this is the most common single error in FSA, and it costs
> whole questions because the rest of the calculation follows from it.

> **Trap 2 — Gains and losses on asset sales.** A gain is **subtracted** from net income in the
> indirect method (and a loss **added back**) because the *entire* proceeds belong in **investing**.
> Leaving the gain in CFO double-counts it.

> **Trap 3 — Dividends paid.** **Financing under US GAAP.** Under IFRS they may be operating or
> financing. Dividends *received* are operating under US GAAP.

> **Trap 4 — Direct vs. indirect totals.** The two methods always give the **same CFO**. Any answer
> implying otherwise is wrong. Only the *presentation* of the operating section differs.

> **Trap 5 — Depreciation "generates" cash.** It does not. It is added back only because it was
> deducted in arriving at net income and involved no cash outflow.

> **Trap 6 — Non-cash transactions.** Acquiring an asset by issuing debt or equity, or converting
> debt to equity, appears **nowhere** in the three sections. It is disclosed separately — but it
> absolutely changes the balance sheet, so it matters for leverage.

> **Trap 7 — Gross vs. net PP&E in the capex formula.** Use **gross** PP&E and the **gross cost** of
> disposals, or use net PP&E *and* remember to subtract depreciation. Mixing the two is a standard
> planted error.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Net income is 500. Depreciation is 120. Receivables rose 80, inventory fell 30, accounts payable rose 45. There was a 25 gain on the sale of equipment. Compute CFO.

<details><summary>Answer</summary>

```
Net income                     500
+ Depreciation                 120
− Gain on sale                 (25)   ← belongs in investing
− Increase in receivables      (80)
+ Decrease in inventory         30
+ Increase in payables          45
                              -----
CFO                            590
```
**CFO = 590.**

</details>

**2.** Revenue is 8,000 and accounts receivable increased by 350. Unearned revenue increased by 90. How much cash was collected from customers?

<details><summary>Answer</summary>

Cash from customers = 8,000 − 350 + 90 = **7,740**.

The receivable increase means 350 of recognised revenue was not collected. The unearned revenue increase means 90 of cash came in for performance not yet delivered — cash received, no revenue recognised.

</details>

**3.** COGS is 5,000. Inventory rose 400 and accounts payable fell 120. How much cash was paid to suppliers?

<details><summary>Answer</summary>

Purchases = COGS + ΔInventory = 5,000 + 400 = 5,400.
Cash paid = Purchases − ΔPayables = 5,400 − (−120) = 5,400 + 120 = **5,520**.

Both adjustments push the same way: you bought more than you sold, *and* you paid down what you owed.

</details>

**4.** Beginning gross PP&E was 4,200; ending gross PP&E is 4,900. Equipment with an original cost of 300 and a net book value of 110 was sold for 140. Compute capex and the investing cash flow from the disposal.

<details><summary>Answer</summary>

Capex = 4,900 − 4,200 + 300 = **1,000**.

Disposal proceeds = **140** (given). The gain of 140 − 110 = 30 appears in net income and must be **subtracted** in the indirect CFO reconciliation, because the full 140 belongs in investing.

Net CFI from these items = −1,000 + 140 = **−860**.

</details>

**5.** A company reporting under IFRS classifies interest paid as financing. A US GAAP peer must classify it as operating. Both paid 200 of interest. How does this distort a comparison of CFO, and what do you do?

<details><summary>Answer</summary>

The IFRS company's **CFO is 200 higher** purely by classification — nothing economic differs. Any CFO-based ratio (CFO/debt, CFO/revenue, free cash flow to the firm derived from CFO) is not comparable.

Restate to a common basis: move the IFRS company's 200 of interest paid into CFO (or move the US company's out of CFO). State the adjustment explicitly in your analysis.

</details>

**6.** Net income has grown 15% a year for three years while CFO has been flat. Name three explanations and say how you would distinguish them.

<details><summary>Answer</summary>

(1) **Receivables ballooning** — revenue recognised, cash not collected. Check DSO and the receivables balance against revenue growth.
(2) **Inventory building** — production outpacing sales. Check days of inventory on hand.
(3) **Aggressive revenue recognition or capitalisation** — e.g. recognising over time on weak grounds, or capitalising costs a peer expenses (which flatters net income *and* CFO, so if CFO is flat too, this is less likely to be the sole cause).

Also consider payables being paid down (a financing-of-suppliers reversal) and non-cash gains inflating net income. The distinguishing tool is the working-capital section of the indirect statement: it tells you exactly which account absorbed the cash.

</details>

**7.** A company acquires a building by issuing 50m of shares directly to the seller. Where does this appear in the cash flow statement?

<details><summary>Answer</summary>

**Nowhere in the three sections** — there is no cash flow. It is disclosed as a significant **non-cash investing and financing transaction**, in a supplemental schedule or note.

This matters: the balance sheet gains a 50m asset and 50m of equity, changing every leverage and return ratio, while the cash flow statement shows nothing. Analysts must pick it up from the note.

</details>

**8.** Company X shows CFO +, CFI +, CFF +. What does this pattern suggest?

<details><summary>Answer</summary>

Operations generate cash, **yet the company is also selling assets and raising capital**. On its own CFO+ looks healthy, but combined with asset sales *and* new financing it suggests a large investment or acquisition being funded, a liquidity build ahead of a known obligation, or an operating business whose cash generation is insufficient for its plans. Read the three together and check the size of each — a small CFO alongside large CFI and CFF inflows is a very different story from a large CFO with marginal ones.

</details>

---

## Done when

- [ ] I can state what belongs in CFO, CFI, and CFF, and read a company's story from the pattern of signs
- [ ] I can compute CFO by the indirect method with non-cash items, gains/losses, and working-capital changes
- [ ] I can convert indirect to direct for customers, suppliers, operating expenses, interest, and taxes
- [ ] I can derive capex, disposal proceeds, and dividends paid from balance-sheet movements
- [ ] I can reproduce the IFRS vs US GAAP classification table from memory
- [ ] I can explain why the two methods always produce the same CFO
- [ ] I answered the self-check cold, several days after first study

---

← [LM03 Analyzing Balance Sheets](lm-03-analyzing-balance-sheets.md)  ·  [Topic index](README.md)  ·  [LM05 Analyzing Statements of Cash Flows II](lm-05-analyzing-statements-of-cash-flows-ii.md) →
