# FSA · LM06 — Analysis of Inventories

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM2 (expense recognition), LM3 (balance sheet ratios). |
| **Where it shows up** | 2 questions, reliably. LIFO/FIFO conversion is one of the most predictable calculations on the exam. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe the measurement of inventory at the lower of cost and net realisable value and its implications for financial statements and ratios
- calculate and explain how inflation and deflation of inventory costs affect the financial statements and ratios of companies that use different inventory valuation methods
- describe the presentation and disclosures relating to inventories and explain issues that analysts should consider when examining a company's inventory disclosures and other sources of information

---

## Core concepts

### The identity that governs everything here

```
Beginning inventory + Purchases = Cost of goods sold + Ending inventory
```

Every cost-flow question is this identity with a different rule for splitting the available cost
between COGS (the income statement) and ending inventory (the balance sheet). **What goes into one
cannot go into the other** — that reciprocal relationship is the key to every question in this module.

### Cost flow methods

| Method | COGS reflects | Ending inventory reflects | Permitted |
| --- | --- | --- | --- |
| **FIFO** (first in, first out) | **Oldest** costs | **Newest** costs | IFRS and US GAAP |
| **LIFO** (last in, first out) | **Newest** costs | **Oldest** costs | **US GAAP only** |
| **Weighted average cost** | Average cost | Average cost | IFRS and US GAAP |
| **Specific identification** | Actual cost of the specific item | Actual cost | Both; used for unique, high-value items |

### Rising prices — the master table

This is the highest-yield table in FSA. Learn it so you can reproduce it under pressure.

**Assuming rising prices and stable or rising inventory quantities:**

| | **FIFO** | **LIFO** |
| --- | --- | --- |
| COGS | **Lower** (old, cheap costs) | **Higher** (new, expensive costs) |
| Gross profit / Net income | **Higher** | **Lower** |
| Ending inventory (balance sheet) | **Higher** (new costs — closer to economic value) | **Lower** (stale old costs) |
| Taxes paid | **Higher** | **Lower** |
| **Cash flow after tax** | **Lower** | **Higher** ← the reason LIFO exists |
| Working capital | Higher | Lower |
| Current ratio | Higher | Lower |
| Inventory turnover | **Lower** (low COGS ÷ high inventory) | **Higher** (high COGS ÷ low inventory) |
| Debt-to-equity | Lower (equity higher) | Higher |
| ROA, ROE | Higher | Lower |
| Gross margin | Higher | Lower |

**With falling prices, every row reverses.** Do not memorise a second table — memorise the logic:
*LIFO puts the most recent costs in COGS.* Everything follows from that one sentence.

> **Why any company chooses LIFO:** in the US, the **LIFO conformity rule** requires that a company
> using LIFO for tax must also use it for financial reporting. In an inflationary environment LIFO
> raises COGS, lowers taxable income, and therefore **reduces cash taxes** — a real, permanent cash
> benefit paid for with lower reported earnings.

### The LIFO reserve — converting LIFO to FIFO

US LIFO reporters must disclose the **LIFO reserve**: the difference between what inventory would be
under FIFO and what it is under LIFO. This is what makes a LIFO company comparable to an IFRS peer.

```
FIFO inventory = LIFO inventory + LIFO reserve
FIFO COGS      = LIFO COGS − Increase in LIFO reserve during the period
FIFO net income = LIFO net income + Increase in LIFO reserve × (1 − t)
FIFO equity    = LIFO equity + LIFO reserve × (1 − t)
```

The `(1 − t)` on income and equity is the tax effect: converting to FIFO would have raised pre-tax
income, and the tax on that increase is a liability, so only the after-tax portion accrues to equity.

**Worked example.** LIFO inventory 1,000 (opening) and 1,400 (closing). LIFO reserve 300 (opening),
420 (closing). LIFO COGS 5,000. Tax rate 25%.

```
FIFO closing inventory = 1,400 + 420           = 1,820
Increase in LIFO reserve = 420 − 300           =   120
FIFO COGS = 5,000 − 120                        = 4,880
FIFO net income = LIFO net income + 120 × 0.75 = LIFO NI + 90
FIFO equity = LIFO equity + 420 × 0.75         = LIFO equity + 315
```

### LIFO liquidation

When a LIFO company's inventory **quantity falls**, it sells goods carried at **old, low costs**.
COGS falls artificially and gross margin spikes.

This is not an operating improvement — it is a one-off, non-repeatable accounting effect from
inventory depletion, and it also **raises taxable income**. Detect it by watching for a **decline in
the LIFO reserve** combined with a fall in inventory quantity. Analysts strip the effect out before
forecasting margins.

### Lower of cost and net realisable value

Inventory must be written down when its value falls below cost.

| | **IFRS** | **US GAAP** |
| --- | --- | --- |
| Measurement rule | Lower of cost and **net realisable value (NRV)** | Lower of cost and NRV; **for LIFO and retail method**, lower of cost or **market** |
| NRV definition | Estimated selling price − estimated costs of completion and sale | Same |
| "Market" (LIFO/retail only) | n/a | Replacement cost, bounded by NRV (ceiling) and NRV − normal profit margin (floor) |
| **Reversal of a write-down** | **Permitted**, up to the original cost, if value recovers | **Prohibited** |

A write-down **increases COGS** (or is presented as a separate expense), reduces inventory, reduces
net income and equity, lowers the current ratio, and **raises inventory turnover**. It is a
**non-cash** charge — CFO is unaffected.

> **Trap:** the IFRS reversal rule is a favourite. IFRS **permits** reversal up to original cost;
> US GAAP **prohibits** it. Same direction as the impairment rule in LM3 — IFRS allows reversals,
> US GAAP does not (goodwill excepted under both).

### Presentation, disclosure, and what the analyst does with it

Required disclosures: the **cost formula used**, total carrying amount by classification (raw
materials, work in progress, finished goods), inventory carried at fair value less costs to sell,
the **cost of inventories recognised as an expense** in the period, **write-downs and any reversals**
with the circumstances, and the carrying amount of inventory pledged as security.

What to do with it:

- **Compare DOH against peers and history.** Rising days of inventory on hand means slowing turnover
  — obsolescence risk and a future write-down.
- **Watch the mix.** Raw materials rising is a production ramp (forward-looking, often positive);
  **finished goods rising faster than sales** means product is not selling — a genuine warning.
- **Recurring write-downs** signal chronic over-production or poor demand forecasting, not bad luck.
- **Read the MD&A alongside it.** Management explaining a build as "positioning for demand" while
  finished goods days rise for four quarters is a story the numbers do not support.

---

## Formulas to know cold

```
Beginning inventory + Purchases = COGS + Ending inventory

FIFO inventory  = LIFO inventory + LIFO reserve
FIFO COGS       = LIFO COGS − Increase in LIFO reserve
FIFO net income = LIFO net income + Increase in LIFO reserve × (1 − t)
FIFO equity     = LIFO equity + LIFO reserve × (1 − t)

Inventory turnover        = COGS / Average inventory
Days of inventory on hand = 365 / Inventory turnover

NRV = Estimated selling price − Estimated costs of completion and sale

US GAAP "market" (LIFO / retail only):
    Ceiling = NRV
    Floor   = NRV − normal profit margin
    Market  = Replacement cost, bounded by [Floor, Ceiling]
```

---

## Exam traps

> **Trap 1 — Which way round LIFO goes.** LIFO puts the **newest** costs in **COGS**. In inflation
> that means **higher COGS, lower income, lower inventory, lower taxes, higher after-tax cash flow.**
> Derive the rest from that one sentence rather than memorising twenty rows.

> **Trap 2 — LIFO produces *higher* cash flow.** Lower reported profit but lower cash taxes. Answers
> that pair "lower net income" with "lower cash flow" are wrong.

> **Trap 3 — Adding rather than subtracting the reserve change in COGS.** Inventory: **add** the
> reserve. COGS: **subtract** the *increase* in the reserve. Opposite directions.

> **Trap 4 — Forgetting the tax effect.** Inventory conversion uses the **full** reserve. Income and
> equity conversions use **× (1 − t)**.

> **Trap 5 — LIFO liquidation read as an improvement.** A margin spike accompanied by a **falling
> LIFO reserve** and falling inventory quantity is a liquidation, not operating performance. Strip
> it out before forecasting.

> **Trap 6 — Write-down reversals.** **IFRS permits** (capped at original cost); **US GAAP prohibits**.

> **Trap 7 — Turnover after a write-down.** A write-down cuts average inventory, so inventory
> turnover **rises** — which looks like an efficiency gain and is not one.

> **Trap 8 — Inventory turnover uses COGS, not revenue.** Using revenue in the numerator is a
> planted error, and it silently changes the answer.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A US company reports LIFO inventory of 2,400 and a LIFO reserve that rose from 500 to 680 during the year. LIFO COGS was 9,000 and the tax rate is 30%. Convert inventory, COGS, net income, and equity to a FIFO basis.

<details><summary>Answer</summary>

FIFO inventory = 2,400 + 680 = **3,080**
Increase in reserve = 680 − 500 = 180
FIFO COGS = 9,000 − 180 = **8,820**
FIFO net income = LIFO NI + 180 × (1 − 0.30) = LIFO NI + **126**
FIFO equity = LIFO equity + 680 × 0.70 = LIFO equity + **476**

Note the asymmetry: inventory uses the full reserve (680); income uses the *change* after tax (126); equity uses the *full reserve* after tax (476).

</details>

**2.** Prices are rising. Company F uses FIFO and Company L uses LIFO; they are otherwise identical. Compare gross margin, inventory turnover, current ratio, and after-tax cash flow.

<details><summary>Answer</summary>

- **Gross margin:** F higher (lower COGS from old cheap costs)
- **Inventory turnover:** L higher — its COGS is larger *and* its inventory is smaller, so both the numerator and denominator push the ratio up
- **Current ratio:** F higher (higher inventory carrying value)
- **After-tax cash flow:** **L higher** — lower taxable income means lower cash taxes

L looks worse on every profitability measure and is genuinely better off in cash.

</details>

**3.** A company's gross margin jumps from 31% to 38% in one year. Its LIFO reserve fell from 900 to 610 and inventory quantities declined. What happened, and what do you do?

<details><summary>Answer</summary>

A **LIFO liquidation**. The company sold inventory carried at old, low costs, so COGS is artificially depressed and margin artificially inflated. The falling LIFO reserve alongside falling quantities is the fingerprint.

It is **not repeatable** and it **raises taxable income** (so cash taxes rise). Strip the effect out before forecasting: the sustainable margin is much closer to 31%. Check whether the depletion was deliberate (a demand surge, a supply constraint) or a sign of scaling down.

</details>

**4.** Inventory cost is 500. Estimated selling price is 540, costs to complete and sell are 70. What is the carrying amount under IFRS, and what if the value later recovers to 520?

<details><summary>Answer</summary>

NRV = 540 − 70 = **470**. Since NRV (470) < cost (500), write down to **470** and recognise a 30 loss.

If value later recovers to 520, IFRS **permits reversal up to original cost**: reverse 30 to bring it back to **500**, not 520. Under US GAAP no reversal is permitted — it stays at 470.

</details>

**5.** Explain why LIFO is prohibited under IFRS.

<details><summary>Answer</summary>

IFRS takes the view that LIFO does not faithfully represent the physical flow of inventory for most businesses, and — more importantly for an analyst — it leaves the **balance sheet** carrying inventory at stale historical costs that can be decades out of date, which undermines the relevance of the reported financial position. IFRS prioritises a balance sheet that reflects current costs; LIFO sacrifices that to make the income statement reflect current costs instead.

</details>

**6.** Finished goods inventory has grown 40% while revenue grew 5%. Raw materials are flat. What does the mix tell you?

<details><summary>Answer</summary>

Product is **being made and not sold**. If raw materials were rising too, you could read it as a production ramp ahead of expected demand. Raw materials flat with finished goods ballooning means output is piling up at the end of the line — a demand shortfall, not a build-up strategy.

Expect: rising days of inventory on hand, pressure on CFO, and a **write-down risk** in coming periods. Check the inventory note for write-downs already taken and compare management's MD&A narrative against the mix.

</details>

**7.** Inventory turnover rose from 5.1x to 6.4x. Management calls it improved inventory management. What else could explain it?

<details><summary>Answer</summary>

(1) A **write-down** cut average inventory — turnover rises with no operating improvement. (2) A **LIFO liquidation** raised COGS relative to a shrinking inventory base. (3) **Stock-outs** — the company is turning inventory fast because it does not have enough, which costs sales. (4) A **shift in product mix** toward faster-moving, lower-margin goods.

Cross-check with gross margin, the write-down disclosure, the LIFO reserve, and revenue growth. Genuine improvement shows up as higher turnover *with* stable or rising margin and no lost sales.

</details>

---

## Done when

- [ ] I can reproduce the rising-prices FIFO vs LIFO table from memory, from the one-sentence logic
- [ ] I can convert LIFO inventory, COGS, net income, and equity to FIFO, with the tax effect in the right places
- [ ] I can detect a LIFO liquidation from the reserve and quantity movement, and explain why it is not repeatable
- [ ] I can apply lower of cost and NRV and state the IFRS/US GAAP difference on reversals
- [ ] I can explain what a rising finished-goods share of inventory implies
- [ ] I can state why inventory turnover uses COGS and not revenue
- [ ] I answered the self-check cold, several days after first study

---

← [LM05 Analyzing Statements of Cash Flows II](lm-05-analyzing-statements-of-cash-flows-ii.md)  ·  [Topic index](README.md)  ·  [LM07 Analysis of Long-Term Assets](lm-07-analysis-of-long-term-assets.md) →
