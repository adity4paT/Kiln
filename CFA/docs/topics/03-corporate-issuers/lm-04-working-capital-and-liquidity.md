# CI · LM04 — Working Capital and Liquidity

## At a glance

| | |
| --- | --- |
| **Topic** | Corporate Issuers (6-9% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | FSA LM11 (activity ratios, cash conversion cycle). |
| **Where it shows up** | 2 questions. The cash conversion cycle is near-certain; money market yield calculations appear regularly. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the cash conversion cycle and compare issuers' cash conversion cycles
- explain liquidity and compare issuers' liquidity levels
- describe issuers' objectives and compare methods for managing working capital and liquidity

---

## Core concepts

### Working capital

```
Working capital     = Current assets − Current liabilities
Net working capital = (Current assets − Cash) − (Current liabilities − Short-term debt)
```

The second definition strips out financing items to isolate the **operating** working capital that
the business genuinely requires. It is the more useful measure for analysis and forecasting.

### The cash conversion cycle

```
Cash conversion cycle (CCC) = DOH + DSO − Days of payables

where   DOH = 365 / (COGS / Average inventory)
        DSO = 365 / (Revenue / Average receivables)
        Days of payables = 365 / (Purchases / Average payables)
```

The CCC is the number of days between **paying for inventory** and **collecting from customers** —
the period the company must fund itself. **Shorter is better.**

```
  ┌── Inventory purchased ──────────── Inventory sold ─────── Cash collected ──┐
  │                                                                            │
  │◄──────────────── DOH ──────────────►│◄────────── DSO ────────────►│        │
  │◄─── Days payables ───►│                                                     │
  │                       │◄───────────── CASH CONVERSION CYCLE ───────►│       │
  │                    Supplier paid                                            │
```

**A negative CCC** means the company **collects from customers before it pays suppliers**. Growth is
then self-funding — expanding the business *generates* cash instead of consuming it. Supermarkets,
some subscription businesses, and large retailers with supplier power achieve this, and it is a
genuine structural advantage rather than an accounting artefact.

**Comparing issuers:** the CCC is only meaningful **within an industry**. A jeweller carrying
high-value, slow-moving stock will always have a longer CCC than a grocer. What matters is the
company against its own history and its direct peers, and the **direction of travel**.

> **Diagnostic value:** a lengthening CCC is one of the earliest warnings of operational trouble —
> inventory building because sales are slowing, or receivables stretching because customers are
> struggling or credit terms have been loosened to hold volume.

### Liquidity

**Liquidity** is the ability to meet short-term obligations as they come due. It has two dimensions:

- **Asset liquidity** — how quickly assets convert to cash at fair value
- **Funding liquidity** — the ability to raise cash when needed

**Primary sources of liquidity** — the everyday ones:

- Cash and cash equivalents on hand
- Cash generated from operations
- Short-term investments (marketable securities)
- Available committed credit facilities and revolvers
- Trade credit from suppliers

**Secondary sources** — the ones that signal distress, because using them is costly:

- Liquidating operating assets or inventory at a discount
- Renegotiating or restructuring debt
- Filing for bankruptcy protection
- Emergency equity issuance at a depressed price

> **The distinction matters analytically:** a company drawing on secondary sources is already in
> trouble, regardless of what its current ratio says. The move from primary to secondary is the
> event, not the ratio level.

**Drags and pulls on liquidity:**

| **Drags** (cash comes in more slowly) | **Pulls** (cash goes out more quickly) |
| --- | --- |
| Uncollected receivables, bad debts | Suppliers tightening credit terms |
| Obsolete inventory | Limits on short-term credit lines |
| Tight short-term credit availability | Making payments early |

**Liquidity ratios** (FSA LM11): current, quick, cash, and defensive interval. Plus the activity
ratios that drive them — DOH, DSO, days of payables.

### Managing working capital — the three components

**Inventory.** The objective is to hold the minimum consistent with meeting demand.

- **Economic order quantity (EOQ)** — balances ordering cost against holding cost
- **Just-in-time (JIT)** — minimises inventory but raises supply-chain fragility
- The trade-off is explicit: less inventory frees cash but raises the risk of **stock-outs**, which
  cost sales and customer relationships

**Receivables.** The objective is to collect quickly without losing customers.

- **Credit policy** — who gets credit, on what terms, with what limits
- **Discounts for early payment** (e.g. "2/10 net 30" — 2% off if paid in 10 days, otherwise due in 30)
- **Ageing schedule** monitoring and active collections
- **Factoring** — selling receivables for immediate cash at a discount
- The trade-off: tighter credit collects faster but **loses sales** to customers who need terms

> **The cost of trade credit is usually large and invisible.** Declining "2/10 net 30" to pay on day
> 30 costs 2% for 20 days of extra credit — an effective annual rate of roughly **44.6%**. Companies
> that routinely forgo discounts are often revealing a genuine cash constraint.

**Payables.** The objective is to pay as late as the terms and the relationship permit.

- Stretching payables is **free financing** — up to the point where it damages supplier
  relationships, forfeits discounts, or triggers worse terms
- The trade-off: paying late improves the CCC but can cost you priority of supply and goodwill

### Short-term investment and funding

**Investing surplus cash** — priorities in order: **safety of principal**, then **liquidity**, then
yield. Instruments: treasury bills, commercial paper, certificates of deposit, repurchase
agreements, money market funds.

**Money market yield conventions** are examinable and easy to confuse:

```
Holding period yield      HPY = (P1 − P0 + D1) / P0
Effective annual yield    EAY = (1 + HPY)^(365/t) − 1
Money market yield        r_MM = HPY × (360/t)
Bank discount yield       r_BD = (D/F) × (360/t)       ← based on FACE value, not price
Bond equivalent yield     BEY  = HPY × (365/t)
```

> **The bank discount yield is the odd one out and is therefore the one tested.** It uses the
> **discount from face value** divided by **face value** (not the purchase price) and a **360-day**
> year. It **understates** the true return on both counts, and it is not directly comparable with
> any other yield measure.

**Short-term funding sources:** committed and uncommitted bank lines, revolving credit facilities,
commercial paper (for high-quality issuers), banker's acceptances, factoring, and secured borrowing
against receivables or inventory.

---

## Formulas to know cold

```
Working capital      = Current assets − Current liabilities
Net working capital  = (CA − Cash) − (CL − Short-term debt)

CASH CONVERSION CYCLE
  CCC = DOH + DSO − Days of payables
    DOH = 365 / (COGS / Average inventory)
    DSO = 365 / (Revenue / Average receivables)
    Days payables = 365 / (Purchases / Average payables)
  NEGATIVE CCC = collects before paying = self-funding growth

LIQUIDITY RATIOS
  Current = CA/CL    Quick = (Cash + ST inv + Receivables)/CL    Cash = (Cash + ST inv)/CL
  Defensive interval = (Cash + ST inv + Receivables) / Daily cash expenditures

COST OF TRADE CREDIT (forgoing a discount)
  Cost = [1 + Discount/(1 − Discount)]^(365 / days beyond discount period) − 1
  e.g. "2/10 net 30":  [1 + 0.02/0.98]^(365/20) − 1 = 44.6%

MONEY MARKET YIELDS
  HPY  = (P1 − P0 + D1)/P0
  EAY  = (1 + HPY)^(365/t) − 1
  r_MM = HPY × (360/t)
  r_BD = (D/F) × (360/t)        ← uses FACE value and a 360-day year — understates the return
  BEY  = HPY × (365/t)
```

---

## Exam traps

> **Trap 1 — Cash conversion cycle sign.** Days of payables is **subtracted**. A negative CCC is a
> good thing, not an error.

> **Trap 2 — Bank discount yield.** Based on **face value** and a **360-day** year. It is **not**
> comparable to EAY or BEY, and it **understates** the true yield.

> **Trap 3 — The three numerators.** DOH uses **COGS**; DSO uses **revenue**; days of payables uses
> **purchases**. Three different numerators (FSA LM11).

> **Trap 4 — Assuming a longer CCC is always bad.** Compare **within an industry** and against the
> company's own history. Absolute levels across industries are meaningless.

> **Trap 5 — Thinking stretching payables is free.** It costs forfeited discounts, supplier
> goodwill, and eventually worse terms or loss of supply priority.

> **Trap 6 — Underestimating the cost of forgoing a discount.** "2/10 net 30" costs about **44.6%
> annualised**. It is rarely rational unless the company cannot pay.

> **Trap 7 — Confusing primary and secondary liquidity sources.** Using secondary sources —
> discounted asset sales, debt restructuring — is itself a **distress signal**.

> **Trap 8 — Ignoring stock-out cost.** Minimising inventory is not free. Lost sales and lost
> customers are a real cost that the CCC does not show.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company has DOH of 55, DSO of 38, and days of payables of 62. Compute the CCC and interpret it.

<details><summary>Answer</summary>

CCC = 55 + 38 − 62 = **31 days**

The company funds 31 days of operations. Inventory sits for 55 days and customers take 38 more to pay — 93 days from purchase to collection — but suppliers are not paid for 62 of those days, so the self-funded gap is 31.

Each unit of sales growth requires 31 days' worth of incremental working capital. To shorten it: turn inventory faster, tighten collections, or extend supplier terms — with the caveat that each has a cost (stock-outs, lost sales, supplier goodwill).

</details>

**2.** A supermarket has DOH of 18, DSO of 3, and days of payables of 45. Compute the CCC and explain the strategic implication.

<details><summary>Answer</summary>

CCC = 18 + 3 − 45 = **−24 days**

**Negative.** The supermarket collects cash from customers 24 days **before** it pays suppliers. Growth generates cash rather than consuming it — every additional store expands the float.

Strategic implications:
- Expansion can be **self-funded** from the working capital release, reducing reliance on external finance
- Effectively an interest-free loan from suppliers that **scales with revenue**
- But it depends on **supplier bargaining power**. If suppliers consolidate, or the retailer's volume advantage erodes, terms tighten and the float reverses — which consumes cash at exactly the moment the business is weakening

The fragility is real: a negative CCC is an advantage borrowed from the supply chain, not generated internally.

</details>

**3.** Terms are '2/10 net 30'. What is the annualised cost of forgoing the discount, and when would it be rational to do so?

<details><summary>Answer</summary>

Forgoing the 2% discount buys 20 extra days of credit (day 10 to day 30).

Cost = [1 + 0.02/0.98]^(365/20) − 1
     = [1.020408]^18.25 − 1
     = 1.4459 − 1 = **44.6%** annualised

**When it is rational:** essentially only when the company's alternative cost of funds exceeds 44.6% — which effectively means it has no access to credit at all. A company with a revolving credit facility at even 12% should always borrow to take the discount.

**Analytical signal:** a company that routinely forgoes early-payment discounts is revealing a genuine liquidity constraint, whatever its current ratio says. It is one of the more reliable soft indicators of cash stress.

</details>

**4.** A 90-day treasury bill with a face value of 100,000 is purchased for 98,200. Compute the HPY, bank discount yield, money market yield, and EAY.

<details><summary>Answer</summary>

Discount D = 100,000 − 98,200 = 1,800

**HPY** = 1,800 / 98,200 = **1.833%**

**Bank discount yield** = (1,800/100,000) × (360/90) = 0.018 × 4 = **7.20%**

**Money market yield** = 1.833% × (360/90) = 1.833% × 4 = **7.33%**

**EAY** = (1.01833)^(365/90) − 1 = (1.01833)^4.0556 − 1 = **7.64%**

Note the ordering: **r_BD < r_MM < EAY**. The bank discount yield is lowest because it divides by **face value** (larger denominator) and uses a 360-day year, understating the return on both counts. EAY is highest because it compounds and uses 365 days.

</details>

**5.** Distinguish primary from secondary sources of liquidity and explain why the distinction matters more than the current ratio.

<details><summary>Answer</summary>

**Primary sources** are the everyday ones, used without disrupting operations: cash on hand, cash from operations, short-term investments, committed credit facilities, and trade credit.

**Secondary sources** are used when primary sources are exhausted, and using them is **costly and disruptive**: liquidating operating assets at a discount, renegotiating or restructuring debt, emergency equity issuance at a depressed price, and bankruptcy protection.

**Why it matters more than the ratio:** the current ratio is a **snapshot of stocks**; the primary/secondary distinction is about **behaviour**. A company with a current ratio of 2.0 that is selling operating assets to make payroll is in far worse shape than one at 1.1 funding itself comfortably from operations and an undrawn revolver.

The transition from primary to secondary sources **is** the distress event. Watch for asset sales outside the normal course, covenant waivers, and any equity raise at a discount — those tell you more than any liquidity ratio.

</details>

**6.** A company's DSO has risen from 34 to 51 days over six quarters while revenue growth has slowed from 12% to 3%. What do you conclude?

<details><summary>Answer</summary>

Two readings, both concerning, and they are not mutually exclusive:

**(1) Loosened credit terms to defend volume.** As demand slowed, the company extended more generous terms to hold sales. Revenue is being bought with credit rather than earned — and the reported growth of 3% may overstate underlying demand.

**(2) Customer financial stress.** Customers are paying more slowly because they are themselves under pressure. This raises **bad debt risk** and predicts future write-offs.

**What to check:** the **receivables ageing schedule** (is the increase concentrated in the 90+ day bucket?), the **allowance for doubtful accounts** as a percentage of receivables (is it rising in line, or is the company under-providing to protect earnings?), customer concentration, and whether CFO has diverged from net income (FSA LM5).

Either way the **cash conversion cycle has lengthened by 17 days**, consuming working capital at exactly the point when growth is slowing — a combination that puts pressure on liquidity.

</details>

---

## Done when

- [ ] I can compute the cash conversion cycle and explain what a negative cycle means economically
- [ ] I can name the three numerators for DOH, DSO, and days of payables without hesitating
- [ ] I can distinguish primary from secondary liquidity sources and explain why it beats the current ratio
- [ ] I can list drags and pulls on liquidity
- [ ] I can compute the annualised cost of forgoing a trade discount
- [ ] I can compute HPY, bank discount yield, money market yield, BEY, and EAY, and rank them
- [ ] I can state the trade-off in managing each of inventory, receivables, and payables
- [ ] I answered the self-check cold, several days after first study

---

← [LM03 Corporate Governance: Conflicts, Mechanisms, Risks, and Benefits](lm-03-corporate-governance-conflicts-mechanisms-risks-and-benefits.md)  ·  [Topic index](README.md)  ·  [LM05 Capital Investments and Capital Allocation](lm-05-capital-investments-and-capital-allocation.md) →
