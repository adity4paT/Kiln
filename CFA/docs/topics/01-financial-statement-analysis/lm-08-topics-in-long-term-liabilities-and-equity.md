# FSA · LM08 — Topics in Long-Term Liabilities and Equity

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 7 |
| **Prerequisites** | LM3 (non-current liabilities), LM7 (depreciation). |
| **Where it shows up** | 1–2 questions. Lease classification effects and the pension funded status are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the financial reporting of leases from the perspectives of lessors and lessees
- explain the financial reporting of defined contribution, defined benefit, and stock-based compensation plans
- describe the financial statement presentation of and disclosures relating to long-term liabilities and share-based compensation

---

## Core concepts

### Leases — the lessee

The old distinction between "on-balance-sheet" and "off-balance-sheet" leases is gone. Under both
IFRS 16 and ASC 842, a lessee recognises a **right-of-use (ROU) asset** and a **lease liability** for
essentially all leases (short-term leases under 12 months and low-value assets are exempt).

The liability is the **present value of the lease payments**, discounted at the rate implicit in the
lease, or the lessee's incremental borrowing rate if that is not determinable. The ROU asset starts
at the same amount (plus initial direct costs and prepayments).

**Where the frameworks differ is the income statement.**

| | **IFRS 16 — all leases** | **US GAAP — finance lease** | **US GAAP — operating lease** |
| --- | --- | --- | --- |
| Balance sheet | ROU asset + lease liability | ROU asset + lease liability | ROU asset + lease liability |
| Income statement | **Amortisation + interest** (two lines) | **Amortisation + interest** | **Single straight-line lease expense** |
| Total expense pattern | **Front-loaded** | Front-loaded | **Level** |
| EBITDA | **Higher** (no lease expense above EBITDA) | Higher | **Lower** (lease expense is operating) |
| CFO | **Higher** — only the interest portion is operating* | Higher | **Lower** — the whole payment is operating |
| CFF | More negative (principal repayment) | More negative | No lease element |

\* Under IFRS the principal portion is financing and interest may be operating or financing; under
US GAAP finance leases, principal is financing and interest is operating.

Why front-loaded? Interest is charged on a **declining** liability balance while amortisation is
straight-line, so total expense is highest in year 1 and falls thereafter.

> **Analytical consequence:** an IFRS reporter and a US GAAP reporter with identical leases show
> identical balance sheets and **different EBITDA, operating income, and CFO**. Any EV/EBITDA
> comparison across the two frameworks needs adjusting.

### Leases — the lessor

| Type | When | Treatment |
| --- | --- | --- |
| **Finance / sales-type** | Risks and rewards (or control) transfer to the lessee | Derecognise the asset; recognise a **lease receivable**; recognise interest income over the term; a dealer-lessor also recognises selling profit at inception |
| **Operating** | They do not | **Keep the asset** on the balance sheet, depreciate it, recognise lease income straight-line |

Lessor accounting retains the classification test that lessee accounting largely abandoned.

### Pensions and other post-employment benefits

**Defined contribution (DC).** The employer promises a **contribution**, not an outcome. The expense
is simply the contribution for the period; any unpaid amount is a liability. **The employee bears
all investment risk.** Trivial to account for, and increasingly the norm.

**Defined benefit (DB).** The employer promises a **benefit** — typically a formula on final salary
and years of service. **The employer bears investment and actuarial risk.** This is where the
complexity lives.

```
Funded status = Fair value of plan assets − Present value of the defined benefit obligation
```

- **Positive funded status → net pension asset** (recognition may be capped).
- **Negative → net pension liability.**

The funded status goes on the balance sheet **net**, as a single line — which means a very large
gross obligation and a very large pool of assets are compressed into one small number. **Read the
note**, because the gross figures, and the sensitivity of the obligation to the discount rate, are
where the risk actually sits.

The obligation is a present value, so it is highly sensitive to the **discount rate**: a lower
discount rate raises the obligation and worsens the funded status. Other key assumptions are the
expected rate of compensation increase and, for healthcare plans, medical cost trend rates. **Higher
discount rate, lower compensation growth, and lower medical trend all flatter the reported
obligation** — so compare a company's assumptions against its peers.

Periodic pension cost splits between **profit or loss** (service cost, and net interest on the net
pension liability/asset) and **other comprehensive income** (actuarial remeasurements). The precise
split differs between IFRS and US GAAP, and Level I asks only that you know the *concept* that some
of the cost bypasses profit or loss.

> **For analysis:** a large underfunded DB plan is economically debt-like — it is a fixed future
> claim on the company's cash. Many analysts add net underfunding to debt when computing leverage.

### Share-based compensation

The principle: it is **compensation**, so it is an **expense**, measured at **fair value at the grant
date** and recognised over the **vesting (service) period**.

| Instrument | Measurement | Notes |
| --- | --- | --- |
| **Stock grants / restricted stock** | Fair value of the shares at grant date | Expensed over the vesting period |
| **Stock options** | Fair value at grant date from an option-pricing model | Inputs: exercise price, share price, expected life, volatility, risk-free rate, expected dividends |
| **Stock appreciation rights (SARs)** | Fair value | Employee gets the appreciation without putting up capital; no dilution if cash-settled |
| **Phantom shares** | Fair value | Tracks a hypothetical rather than actual shares |

Key analytical points:

- Share-based compensation is a **non-cash expense** — added back in the indirect CFO reconciliation.
  It therefore **reduces net income but not CFO**, which is exactly why companies emphasise adjusted
  measures that exclude it. It is a real economic cost to existing shareholders (dilution), and
  excluding it from "adjusted earnings" is one of the most common non-GAAP distortions (LM10).
- Option **valuation assumptions are discretionary**: higher assumed volatility raises option value
  and therefore expense; a shorter assumed expected life lowers it. Compare assumptions to peers.
- Options and other potentially dilutive instruments feed **diluted EPS** via the treasury stock
  method (LM2).

### Disclosure and presentation

For **long-term liabilities**: the maturity schedule (refinancing risk — how much comes due when),
interest rates and currency, covenants and any breaches, fair value of debt where different from
carrying amount, and collateral pledged.

For **share-based compensation**: the nature and terms of arrangements, the valuation model and its
key assumptions, total compensation cost recognised, and the number and weighted average exercise
prices of options outstanding, exercisable, granted, exercised, and forfeited.

The **maturity schedule** is the single most useful long-term-liability disclosure for a credit
analyst: a company with adequate coverage but a large tower of debt maturing in one year has a
refinancing problem that no coverage ratio will reveal.

---

## Formulas to know cold

```
Lease liability at inception = PV of lease payments, discounted at the rate implicit in the lease
                               (or the lessee's incremental borrowing rate)
ROU asset at inception       = Lease liability + initial direct costs + prepayments − incentives

Interest expense (period)    = Lease liability at start of period × discount rate
Principal reduction          = Lease payment − Interest expense

Funded status = Fair value of plan assets − PV of defined benefit obligation
    Positive → net pension asset;  Negative → net pension liability

Share-based compensation expense = Grant-date fair value / Vesting period   (per period)
```

---

## Exam traps

> **Trap 1 — Assuming lease accounting is now identical.** The **balance sheet** is the same under
> both frameworks; the **income statement and CFO are not**. US GAAP operating leases give a single
> straight-line expense and put the whole payment in CFO; everything else front-loads and splits.

> **Trap 2 — EBITDA and leases.** Finance/IFRS-16 treatment **raises EBITDA** because the cost
> appears as amortisation and interest, both below EBITDA. US GAAP operating-lease expense sits
> *in* operating expenses. EV/EBITDA comparisons across frameworks need adjusting.

> **Trap 3 — Funded status sign.** **Plan assets minus obligation.** Assets > obligation → asset
> (overfunded). Reversing it is a standard error.

> **Trap 4 — Discount rate direction.** A **higher** discount rate gives a **lower** obligation and a
> **better** funded status. It is a present value: rate up, PV down.

> **Trap 5 — Who bears the risk.** **DC → employee** bears investment risk. **DB → employer**. Asked
> directly and often.

> **Trap 6 — Share-based compensation and cash.** Non-cash: reduces net income, **no effect on CFO**
> (it is added back). Any answer claiming a CFO reduction is wrong.

> **Trap 7 — Volatility and option expense.** Higher assumed volatility → **higher** option fair
> value → **higher** expense. Candidates often invert this.

> **Trap 8 — Lessor classification still exists.** Lessee accounting mostly collapsed the
> distinction; **lessor** accounting did not.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A lessee signs a 5-year lease with payments of 100,000 at the end of each year; the incremental borrowing rate is 6%. Compute the initial lease liability, and year 1 interest and principal.

<details><summary>Answer</summary>

Lease liability = PV of a 5-year ordinary annuity of 100,000 at 6%.

BA II Plus: N=5, I/Y=6, PMT=100,000, FV=0, CPT PV → **421,236**.

Year 1 interest = 421,236 × 6% = **25,274**.
Year 1 principal = 100,000 − 25,274 = **74,726**.
Closing liability = 421,236 − 74,726 = 346,510.

Under IFRS (or a US GAAP finance lease), the income statement shows 25,274 interest plus amortisation of about 84,247 (421,236/5) = 109,521 total in year 1 — more than the 100,000 cash payment. That is the front-loading.

</details>

**2.** Two companies have identical leases. One reports under IFRS 16, the other treats them as US GAAP operating leases. Compare EBITDA, operating income, net income in year 1, CFO, and total assets.

<details><summary>Answer</summary>

- **Total assets and lease liability: identical.**
- **EBITDA: IFRS higher** — its lease cost appears as amortisation and interest, both below EBITDA; the US GAAP operating lease expense is an operating cost inside EBITDA.
- **Operating income: IFRS higher** (interest is below the operating line).
- **Net income year 1: IFRS lower** — front-loading means total year-1 expense exceeds the straight-line figure.
- **CFO: IFRS higher** — only the interest portion is operating, while under a US GAAP operating lease the **entire payment** is operating.

</details>

**3.** Plan assets have a fair value of 820m; the defined benefit obligation is 1,150m. State the funded status and how it appears. If the discount rate rises by 50bp, which way does funded status move?

<details><summary>Answer</summary>

Funded status = 820 − 1,150 = **−330m**, i.e. **underfunded**, presented as a **net pension liability of 330m** on the balance sheet.

A **higher discount rate lowers the present value of the obligation**, so the obligation falls, and funded status **improves** (the liability shrinks). Note this is a purely actuarial improvement — no cash has changed hands and no benefit promise has changed.

</details>

**4.** Why might an analyst add a company's net pension underfunding to its reported debt?

<details><summary>Answer</summary>

An underfunded DB obligation is a **fixed, non-discretionary future claim on the company's cash**, ranking economically alongside debt and often ahead of shareholders. It must be funded from future cash flows regardless of business conditions. Leaving it out of leverage understates the claims on the enterprise — so many analysts add net underfunding (often after tax) to debt when computing debt-to-EBITDA and debt-to-capital, and add it to enterprise value in multiple work.

</details>

**5.** A company excludes share-based compensation from its 'adjusted EBITDA'. Is that legitimate?

<details><summary>Answer</summary>

It is legal and common, but analytically it is a **real cost being removed**. Share-based compensation transfers value from existing shareholders to employees through dilution; the fact that it consumes no cash does not make it free.

The defensible test: if the company must keep granting equity to retain the staff who generate the earnings, it is a **recurring operating cost** and excluding it overstates sustainable profitability. Cross-check by looking at share count growth — if shares outstanding grow 3% a year, the 'non-cash' expense has a very visible per-share cost. Flag it, quantify it, and if you use adjusted EBITDA, at least be consistent across the peer group.

</details>

**6.** Distinguish who bears the risk under defined contribution and defined benefit plans, and what each puts on the balance sheet.

<details><summary>Answer</summary>

**Defined contribution:** the employer promises a contribution only. The **employee bears investment risk** — the eventual benefit depends on investment returns. Balance sheet: just any unpaid contribution, a small accrual.

**Defined benefit:** the employer promises a specified benefit. The **employer bears investment and actuarial risk** — if assets underperform or people live longer, the employer must make up the shortfall. Balance sheet: the **net funded status** (plan assets minus obligation) as a single asset or liability line.

</details>

---

## Done when

- [ ] I can compute a lease liability as a PV and split a payment into interest and principal
- [ ] I can state how IFRS 16 and US GAAP operating-lease treatment differ on EBITDA, operating income, and CFO
- [ ] I can define funded status, state its sign convention, and say which way the discount rate moves it
- [ ] I can explain who bears risk under DC vs DB plans
- [ ] I can explain why share-based compensation is non-cash but not costless, and how it reaches diluted EPS
- [ ] I can say what the debt maturity schedule tells a credit analyst that coverage ratios do not
- [ ] I answered the self-check cold, several days after first study

---

← [LM07 Analysis of Long-Term Assets](lm-07-analysis-of-long-term-assets.md)  ·  [Topic index](README.md)  ·  [LM09 Analysis of Income Taxes](lm-09-analysis-of-income-taxes.md) →
