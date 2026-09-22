# FSA · LM09 — Analysis of Income Taxes

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM2 (expense recognition), LM3 (non-current liabilities), LM7 (depreciation). |
| **Where it shows up** | 2 questions. Deferred tax asset vs liability creation, and the ETR reconciliation, are near-certain. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- contrast accounting profit, taxable income, taxes payable, and income tax expense and temporary versus permanent differences between accounting profit and taxable income
- explain how deferred tax liabilities and assets are created and the factors that determine how a company's deferred tax liabilities and assets should be treated for the purposes of financial analysis
- calculate, interpret, and contrast an issuer's effective tax rate, statutory tax rate, and cash tax rate
- analyze disclosures relating to deferred tax items and the effective tax rate reconciliation and explain how information included in these disclosures affects a company's financial statements and financial ratios

---

## Core concepts

### Two sets of books, and why that is legitimate

Companies compute profit twice, under two different rule sets, for two different audiences:

| | **Financial reporting** (IFRS / US GAAP) | **Tax reporting** (tax code) |
| --- | --- | --- |
| Profit measure | **Accounting profit** (pre-tax income) | **Taxable income** |
| The charge | **Income tax expense** | **Taxes payable** (actual cash owed) |
| Purpose | Inform investors | Raise revenue and direct policy |

This is not evasion; the two systems have different objectives. The gap between them is where
deferred taxes come from.

```
Income tax expense = Taxes payable + ΔDeferred tax liability − ΔDeferred tax asset
```

Read it as: **the expense is what you actually owe now, adjusted for what the period's transactions
have committed you to owe (or to save) later.**

### Temporary vs. permanent differences

**Temporary differences** arise when an item is recognised in *both* systems but in **different
periods**. They **reverse** over time, and they create deferred tax assets and liabilities.

**Permanent differences** are items recognised in one system and **never** in the other. They never
reverse, they create **no deferred tax**, and they are precisely what drives the effective tax rate
away from the statutory rate.

| Permanent difference | Effect on effective tax rate |
| --- | --- |
| Tax-exempt interest (e.g. municipal bonds) | **Lowers** it |
| Non-deductible fines and penalties | **Raises** it |
| Non-deductible portion of entertainment expenses | Raises it |
| Tax credits (R&D, investment) | **Lowers** it |
| Income earned in lower-tax foreign jurisdictions | **Lowers** it |

### How deferred tax liabilities and assets are created

Work from a single question: **relative to accounting, does the tax code let me pay *less* now and
more later, or *more* now and less later?**

**Deferred tax liability (DTL)** — pay less tax now, more later.
Arises when **taxable income < accounting profit** in the current period.

- Classic case: **accelerated depreciation for tax, straight-line for books.** Tax depreciation is
  larger early, so taxable income is lower early, so tax paid is lower early. That deferral is a real
  future obligation → a liability.
- Also: revenue recognised for books before it is taxable; capitalised development costs deducted
  faster for tax.

**Deferred tax asset (DTA)** — pay more tax now, less later.
Arises when **taxable income > accounting profit** in the current period.

- Classic cases: **warranty provisions and bad debt allowances** — expensed for books when estimated,
  deductible for tax only when actually incurred.
- **Unearned (deferred) revenue** taxed on receipt but recognised for books later.
- **Tax loss carryforwards** — a loss today reduces tax in future profitable years.

> The reliable shortcut: **books recognise the expense first → DTA. Tax recognises the expense first
> → DTL.** Equivalently, revenue first for books → DTL; revenue first for tax → DTA.

**Measurement:** deferred tax items are measured at the tax rates **expected to apply when the
difference reverses**, i.e. the enacted future rate.

> **Rate change effect:** if the tax rate **falls**, both DTLs and DTAs are **remeasured downward**.
> A company with a large net DTL gets a **one-off gain** (lower future obligation → income tax
> expense falls → net income rises). A company with a large net DTA takes a **one-off charge**.
> This is a non-cash, non-recurring item and must be stripped out before forecasting.

### Valuation allowance

A DTA is only worth something if there will be **future taxable income to use it against**. Where it
is **more likely than not** that some or all of a DTA will not be realised, a **valuation allowance**
reduces it.

| Action | Effect |
| --- | --- |
| **Increase** the valuation allowance | DTA down → income tax expense **up** → net income **down** |
| **Decrease/release** the allowance | DTA up → income tax expense **down** → net income **up** |

The allowance is a **management estimate about future profitability**, which makes it a powerful and
well-documented earnings-management lever: a release adds directly to net income with no operating
improvement whatsoever. Any large swing in the valuation allowance deserves explanation.

### The three tax rates

| Rate | Formula | Tells you |
| --- | --- | --- |
| **Statutory** | The legislated rate in the home jurisdiction | The benchmark |
| **Effective (ETR)** | Income tax **expense** / Pre-tax accounting profit | The accrual-based burden. Differs from statutory because of **permanent differences**, foreign rate mix, valuation allowance changes, and rate-change remeasurement |
| **Cash tax rate** | **Cash taxes paid** / Pre-tax accounting profit | The actual cash burden. Differs from ETR because of **temporary differences** |

Reading the three together is the analytical skill:

- **ETR well below statutory, persistently** → check *why*. Permanent tax credits or a genuinely
  low-tax foreign footprint are durable. A one-off valuation allowance release or a rate-change gain
  is not, and must not be extrapolated.
- **Cash tax rate well below ETR, persistently** → large and growing deferred tax liabilities, often
  from capital intensity. Useful cash flow now; watch for reversal.
- **ETR volatile year to year** → the tax line is doing work it should not be doing. Frequently a
  quality-of-earnings signal.

### The ETR reconciliation disclosure

Companies must reconcile the statutory rate to the effective rate, line by line. It is one of the
most information-dense disclosures in the notes:

```
Statutory rate                                    21.0%
Foreign income taxed at different rates           (3.4%)
Tax-exempt income                                 (1.1%)
Non-deductible expenses                             0.8%
Change in valuation allowance                     (2.9%)   ← non-recurring, strip out
Effect of tax rate change                         (1.2%)   ← non-recurring, strip out
R&D credits                                       (0.7%)
Other                                               0.3%
                                                  ------
Effective tax rate                                12.8%
```

The analyst's job: **separate the durable lines from the one-off lines.** Here, the sustainable ETR
is roughly 12.8% + 2.9% + 1.2% ≈ **16.9%**, not 12.8%. Forecasting with 12.8% would overstate every
future year's net income.

### Treating deferred taxes in analysis

There is no single right answer, and the exam expects you to know the judgement:

| Situation | Treatment |
| --- | --- |
| DTL expected to **reverse** (the difference will unwind and cash will be paid) | Treat as a **liability** |
| DTL expected to **grow indefinitely** (continuous capex keeps generating new deferrals faster than old ones reverse) | Treat as **equity** — it is effectively a permanent, interest-free source of funds |
| DTL highly uncertain in timing and amount | **Exclude from both**, and disclose the treatment |

The classification materially changes debt-to-equity, so state which you used. A capital-intensive
utility with a permanently growing DTL is the textbook case for the equity treatment.

---

## Formulas to know cold

```
Income tax expense = Taxes payable + ΔDeferred tax liability − ΔDeferred tax asset

Deferred tax liability arises when: Taxable income < Accounting profit  (pay less tax now)
Deferred tax asset arises when:     Taxable income > Accounting profit  (pay more tax now)

Deferred tax item = Temporary difference × Expected future tax rate

Statutory tax rate  = The legislated rate
Effective tax rate  = Income tax expense / Pre-tax accounting profit
Cash tax rate       = Cash taxes paid / Pre-tax accounting profit

Valuation allowance: reduces a DTA when realisation is not "more likely than not"
```

---

## Exam traps

> **Trap 1 — DTA/DTL direction.** **Tax deducts it first → DTL.** **Books expense it first → DTA.**
> Derive it every time from "am I paying less tax now, or more?" rather than memorising examples.

> **Trap 2 — Permanent differences create no deferred tax.** They never reverse. They only move the
> **effective** rate away from statutory.

> **Trap 3 — Rate-change remeasurement.** A **rate cut** produces a **gain** for a net-DTL company
> and a **charge** for a net-DTA company. Non-cash and non-recurring — strip it out.

> **Trap 4 — Valuation allowance direction.** **Increasing** the allowance **raises** tax expense and
> **lowers** net income. Releasing it does the opposite. It is an estimate of future profitability,
> and therefore discretionary.

> **Trap 5 — ETR vs. cash tax rate.** The **effective** rate uses income tax **expense**; the **cash**
> rate uses **cash taxes paid**. Permanent differences move the ETR; temporary differences drive the
> wedge between ETR and the cash rate.

> **Trap 6 — Extrapolating a one-off ETR.** Always work through the reconciliation and remove
> non-recurring lines before forecasting.

> **Trap 7 — Automatically treating DTLs as debt.** For a company whose DTL grows every year and
> never reverses, the equity treatment is more faithful. Know that the judgement exists.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company uses straight-line depreciation for reporting and accelerated depreciation for tax. Which deferred tax item arises, and why?

<details><summary>Answer</summary>

A **deferred tax liability**. Accelerated tax depreciation is larger in early years, so **taxable income is below accounting profit** and cash tax paid is lower than the expense recognised. The company is paying less tax now and will pay more later when the tax depreciation runs out — a future obligation, hence a liability.

It reverses in later years, when tax depreciation falls below book depreciation.

</details>

**2.** Pre-tax accounting profit is 2,000. Taxes payable are 380. The DTL rose by 60 and the DTA rose by 25. Compute income tax expense, the effective tax rate, and the cash tax rate (cash taxes paid were 380).

<details><summary>Answer</summary>

Income tax expense = 380 + 60 − 25 = **415**

Effective tax rate = 415 / 2,000 = **20.75%**
Cash tax rate = 380 / 2,000 = **19.0%**

The cash rate is below the ETR because net deferred tax liabilities grew (60 − 25 = 35), meaning the period's transactions deferred tax into the future.

</details>

**3.** A company has a large net deferred tax liability. The statutory rate is cut from 25% to 20%. What happens to income tax expense and net income in the year of enactment?

<details><summary>Answer</summary>

The DTL is **remeasured downward** at the new 20% rate — the future obligation is smaller. That reduction flows through as a **credit to income tax expense**, so tax expense **falls** and **net income rises**.

It is **non-cash and non-recurring**: no cash tax changed hands, and it happens once. Strip it out before forecasting, and note that the ETR reported that year is meaningless as a guide to the future.

(A company with a large net **DTA** would take a **charge** on the same rate cut.)

</details>

**4.** A company releases 90m of valuation allowance against its deferred tax assets. What happened economically, and what is the effect on the statements?

<details><summary>Answer</summary>

Management has concluded it is now **more likely than not** that the DTAs will be realised — i.e. it expects sufficient **future taxable income** to use them. Often this follows a return to profitability after losses.

Effects: DTA **up 90m**, income tax expense **down 90m**, net income **up 90m**, equity **up 90m**, **no cash effect**.

Analytically: net income rose 90m with **no operating improvement**. It is a forward-looking management estimate, it is non-recurring, and a company that releases allowance in a weak operating year deserves scrutiny.

</details>

**5.** Given this reconciliation — statutory 25.0%, foreign rate differential (4.0%), valuation allowance release (6.0%), tax credits (1.5%), non-deductible expenses 1.0%, effective rate 14.5% — what rate would you use to forecast next year?

<details><summary>Answer</summary>

Remove the **non-recurring** line: the 6.0% valuation allowance release.

Sustainable ETR ≈ 14.5% + 6.0% = **20.5%**.

The foreign rate differential (−4.0%), tax credits (−1.5%) and non-deductible expenses (+1.0%) are recurring structural features and should stay — though check that the foreign mix is stable and that the credits are not expiring. Forecasting with 14.5% would overstate net income by roughly 6% of pre-tax profit every year.

</details>

**6.** Under what circumstances would you classify a deferred tax liability as equity rather than debt?

<details><summary>Answer</summary>

When the DTL is expected to **grow indefinitely and never reverse in cash**. This happens in capital-intensive businesses with continuous capex: each year's new assets generate fresh accelerated tax depreciation faster than older differences unwind, so the aggregate balance ratchets up permanently.

Economically that is a **perpetual, interest-free source of funding**, which behaves far more like equity than like debt. Classifying it as debt overstates leverage. Always state the treatment you used — it materially changes debt-to-equity.

</details>

**7.** A company accrues a 40m warranty provision that is not deductible for tax until claims are paid. The tax rate is 25%. What deferred tax item arises and for how much?

<details><summary>Answer</summary>

Books expense the 40m now; tax deducts it later. So **accounting profit is 40m lower than taxable income** this period — the company pays **more** tax now and less later.

That creates a **deferred tax asset of 40 × 25% = 10m**.

It reverses when the warranty claims are actually paid and become deductible. Whether the DTA is carried at full value depends on whether future taxable income is expected to absorb it — otherwise a valuation allowance applies.

</details>

---

## Done when

- [ ] I can distinguish accounting profit, taxable income, taxes payable, and income tax expense
- [ ] I can determine whether a given difference creates a DTA or a DTL by reasoning, not memory
- [ ] I can classify a difference as temporary or permanent and say which affects the ETR
- [ ] I can compute income tax expense from taxes payable and the deferred movements
- [ ] I can compute and contrast the statutory, effective, and cash tax rates
- [ ] I can read an ETR reconciliation and strip out the non-recurring lines to get a forecastable rate
- [ ] I can state the three analyst treatments of a DTL and when each applies
- [ ] I answered the self-check cold, several days after first study

---

← [LM08 Topics in Long-Term Liabilities and Equity](lm-08-topics-in-long-term-liabilities-and-equity.md)  ·  [Topic index](README.md)  ·  [LM10 Financial Reporting Quality](lm-10-financial-reporting-quality.md) →
