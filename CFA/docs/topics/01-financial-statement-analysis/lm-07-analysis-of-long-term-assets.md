# FSA · LM07 — Analysis of Long-Term Assets

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM2 (capitalise vs expense), LM3 (intangibles and goodwill). |
| **Where it shows up** | 2 questions. Depreciation-choice effects and impairment are the reliable targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- compare the financial reporting of the following types of intangible assets: purchased, internally developed, and acquired in a business combination
- explain and evaluate how impairment and derecognition of property, plant, and equipment and intangible assets affect the financial statements and ratios
- analyze and interpret financial statement disclosures regarding property, plant, and equipment and intangible assets

---

## Core concepts

### Capitalisation, revisited as a balance-sheet question

LM2 established the *timing* consequences of capitalising. This module is about what happens to the
asset afterwards: how it is depreciated, when it is written down, and what happens when it leaves.

**What gets capitalised into the cost of an asset:** purchase price, plus all costs directly
attributable to bringing the asset to the location and condition necessary for its intended use —
delivery, installation, testing, site preparation, and **capitalised interest** on self-constructed
assets during construction. Training costs, administrative overhead, and losses during start-up are
**expensed**.

**Subsequent costs:** capitalise only if they extend the useful life, increase capacity, or improve
output quality. Routine maintenance and repairs are expensed.

### Three origins of intangibles — an explicit LOS

| Origin | Recognition | Initial measurement |
| --- | --- | --- |
| **Purchased separately** | Capitalise | Cost |
| **Internally developed** | Research: **expense**. Development: **capitalise under IFRS** once criteria met; **expense under US GAAP** (software excepted after technological feasibility) | Directly attributable costs from the date criteria are met |
| **Acquired in a business combination** | Capitalise each **identifiable** intangible separately; the residual is goodwill | Fair value at acquisition date |

The consequence — worth stating out loud because it is the point of the LOS: **the same economic
asset is on one company's balance sheet and absent from another's, purely because of how it was
obtained.** A brand built over thirty years of advertising is invisible; the identical brand bought
last year is an asset.

### Depreciation and amortisation methods

| Method | Formula | Pattern |
| --- | --- | --- |
| **Straight-line** | (Cost − Salvage) / Useful life | Equal each year |
| **Declining balance** (e.g. double-declining) | Rate × Beginning **net book value** | Front-loaded |
| **Units of production** | (Cost − Salvage) × (Units this period / Total expected units) | Tracks usage |

Two mechanical points that cost marks:

- **Declining balance ignores salvage value in the formula** — but you stop depreciating once book
  value reaches salvage value. Double-declining rate = 2 / useful life.
- **IFRS requires component depreciation**: significant parts of an asset with different useful
  lives are depreciated separately (an aircraft's engines separately from its airframe). US GAAP
  permits but does not require it.

**Effect of the choice**, early in an asset's life, accelerated versus straight-line:

| | Accelerated (early years) | Straight-line |
| --- | --- | --- |
| Depreciation expense | Higher | Lower |
| Net income, ROA, ROE | Lower | Higher |
| Net book value / total assets | Lower | Higher |
| Asset turnover | **Higher** | Lower |
| **Cash flow** | **Identical** | **Identical** |

Later in the asset's life it reverses. Total depreciation over the life is the same under all
methods. Only the pattern differs — and **no depreciation method has any cash effect** except
through taxes (and tax depreciation is computed separately anyway).

**Changes to useful life or salvage value are changes in *estimate*** → applied **prospectively**,
over the remaining life. Extending useful lives is a classic earnings-management lever: check the
disclosed useful lives against peers and against the company's own history.

### Revaluation — an IFRS-only option

Under IFRS, PP&E and intangibles with an active market may be carried under the **revaluation model**
at fair value rather than cost. US GAAP has no such option.

- A revaluation **increase** goes to **other comprehensive income** (a revaluation surplus in equity)
  — unless it reverses a prior decrease that went through profit or loss, in which case it goes to
  profit first.
- A revaluation **decrease** goes to **profit or loss** — unless it reverses a prior surplus, in
  which case it reduces the surplus first.

> Asymmetry to memorise: **gains to OCI, losses to P&L**, each reversing the other's prior treatment
> first.

### Impairment

An asset is impaired when its carrying amount exceeds its recoverable amount.

| | **IFRS** | **US GAAP** |
| --- | --- | --- |
| Test | One step: carrying amount vs. **recoverable amount** = higher of (fair value − costs of disposal) and (value in use) | **Two steps**: (1) is carrying amount > **undiscounted** expected future cash flows? (2) if yes, write down to **fair value** |
| Loss measured as | Carrying amount − recoverable amount | Carrying amount − fair value |
| **Reversal** | **Permitted** (not for goodwill) | **Prohibited** |

The US GAAP two-step test uses **undiscounted** cash flows in the recoverability screen — which
means an asset can pass the screen and not be written down even when its discounted value is below
carrying amount. This makes US GAAP impairments **less frequent but larger** when they come.

**Effects of an impairment:**

| Line | Effect |
| --- | --- |
| Net income (year of impairment) | **Down** |
| Total assets, equity | **Down** |
| **Cash flow (CFO, CFI, total)** | **No effect** — non-cash |
| ROA, ROE in the impairment year | **Down** |
| ROA, ROE in **later** years | **Up** — smaller asset base and lower future depreciation |
| Asset turnover | **Up** (smaller denominator) |
| Debt-to-equity | **Up** |

> That "later years look better" effect is why large impairments are sometimes suspected of being a
> **big bath**: take a huge charge now, in a year already lost, and reap lower depreciation and
> higher ROA for years afterward. Flagged again in LM10.

### Derecognition

When an asset is sold, exchanged, or abandoned it is removed from the balance sheet.

```
Gain or loss on disposal = Proceeds − Carrying amount (net book value)
```

The gain or loss goes to the **income statement** (usually within continuing operations), but the
**entire proceeds** are an **investing** cash flow. This is why the gain must be reversed out of net
income when building CFO by the indirect method (LM4). Abandonment with no proceeds produces a loss
equal to the remaining net book value.

### Reading the disclosures

Required: carrying amounts by class, accumulated depreciation, depreciation methods and useful
lives, reconciliation of opening to closing carrying amounts, impairment losses and reversals,
restrictions and pledges, and contractual commitments to acquire PP&E.

Two derived measures that do real work:

```
Average age of asset base (years)   ≈ Accumulated depreciation / Annual depreciation expense
Average depreciable life (years)    ≈ Gross PP&E / Annual depreciation expense
Remaining useful life (years)       ≈ Net PP&E / Annual depreciation expense
```

An ageing asset base — average age approaching average depreciable life — signals **imminent capex**,
which matters for forecasting free cash flow. A company reporting strong FCF while quietly ageing
its asset base is borrowing from the future.

Also compare **disclosed useful lives against peers**. A company depreciating over 20 years in an
industry that uses 12 is either running better equipment or managing earnings, and the disclosure
alone will not tell you which — but it tells you to look.

---

## Formulas to know cold

```
Straight-line depreciation    = (Cost − Salvage value) / Useful life
Double-declining balance      = (2 / Useful life) × Beginning net book value   [ignores salvage in the rate]
Units of production           = (Cost − Salvage) × (Units this period / Total expected units)

Gain/loss on disposal = Proceeds − Carrying amount

IFRS impairment loss    = Carrying amount − Recoverable amount
   Recoverable amount   = max(Fair value − costs of disposal, Value in use)
US GAAP: Step 1 — impaired if Carrying amount > Undiscounted future cash flows
         Step 2 — Loss = Carrying amount − Fair value

Average age            ≈ Accumulated depreciation / Annual depreciation expense
Average depreciable life ≈ Gross PP&E / Annual depreciation expense
Remaining useful life  ≈ Net PP&E / Annual depreciation expense
```

---

## Exam traps

> **Trap 1 — Declining balance and salvage value.** Salvage is **not** subtracted in the annual
> calculation, but depreciation **stops** once book value reaches salvage. Both halves are tested.

> **Trap 2 — The US GAAP recoverability screen is undiscounted.** Step 1 uses **undiscounted** cash
> flows; step 2 measures the loss at **fair value**. Using discounted flows in step 1 gives the wrong
> conclusion about whether an impairment exists at all.

> **Trap 3 — Impairment reversals.** **IFRS permits** (except goodwill); **US GAAP prohibits**.

> **Trap 4 — Impairment and cash flow.** No effect on CFO, CFI, or total cash. It is non-cash.

> **Trap 5 — Revaluation direction.** IFRS only. **Increases → OCI; decreases → P&L**, each
> reversing the other's prior treatment first.

> **Trap 6 — Change in useful life is prospective.** It is a change in **estimate**, not policy. No
> restatement of prior periods.

> **Trap 7 — Disposal proceeds vs. gain.** The **proceeds** are the investing cash flow; the **gain**
> is the income statement effect and must be reversed out of CFO.

> **Trap 8 — Forgetting the later-years reversal.** Accelerated depreciation and impairments depress
> early results and **flatter later ones**. Questions often ask about year 4, not year 1.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** An asset costs 60,000, has a 5-year life and 10,000 salvage value. Compute year 1 and year 2 depreciation under straight-line and double-declining balance.

<details><summary>Answer</summary>

**Straight-line:** (60,000 − 10,000) / 5 = **10,000** in both years.

**Double-declining:** rate = 2/5 = 40%.
- Year 1: 40% × 60,000 = **24,000** → NBV 36,000
- Year 2: 40% × 36,000 = **14,400** → NBV 21,600

Salvage is ignored in the DDB rate but caps cumulative depreciation: the asset cannot be depreciated below 10,000.

</details>

**2.** A machine has a carrying amount of 900. Undiscounted expected future cash flows are 950; fair value is 700; value in use is 780. Determine the impairment under IFRS and under US GAAP.

<details><summary>Answer</summary>

**IFRS:** recoverable amount = max(fair value − costs of disposal, value in use) = max(700, 780) = 780. Carrying amount 900 > 780 → impairment of **120**.

**US GAAP:** Step 1 — carrying amount 900 vs. **undiscounted** cash flows 950. Since 900 < 950, the asset is **not impaired**. **No write-down at all.**

Same asset, same facts, a 120 difference in reported income — purely from the recoverability screen using undiscounted flows.

</details>

**3.** A company takes a 400 impairment on PP&E. State the effect on net income, assets, equity, CFO, asset turnover, and next year's ROA.

<details><summary>Answer</summary>

Net income **−400**; assets **−400**; equity **−400**; **CFO unchanged** (non-cash, added back in the indirect method); asset turnover **up** (same revenue over a smaller asset base); **next year's ROA up** — both because the asset base is smaller *and* because future depreciation is lower.

That last effect is the reason large discretionary impairments attract scrutiny as earnings management.

</details>

**4.** Company A depreciates its fleet over 12 years; Company B, a direct competitor, over 20. Both use straight-line. How does this distort comparison, and how do you check it?

<details><summary>Answer</summary>

B reports **lower annual depreciation** → higher operating income, higher net income, higher net book value, higher total assets. Its **ROA and ROE are flattered early**; asset turnover is lower. Over the asset's full life the totals converge, but at any snapshot B looks more profitable.

To check: compute **average depreciable life = gross PP&E / annual depreciation expense** for both and compare to the industry. Then either restate B's depreciation to A's life, or compare on an EBITDA basis (which removes depreciation entirely) while separately assessing capex intensity.

</details>

**5.** Accumulated depreciation is 4,800; annual depreciation expense is 600; gross PP&E is 9,000. What do you conclude?

<details><summary>Answer</summary>

Average age ≈ 4,800 / 600 = **8 years**. Average depreciable life ≈ 9,000 / 600 = **15 years**. Remaining useful life ≈ (9,000 − 4,800) / 600 = **7 years**.

The asset base is roughly **halfway through its life** — no immediate capex cliff, but a replacement cycle is visible on a 5–7 year horizon. If the average age were 13 against a 15-year life, you would expect a capex surge imminently and should discount current free cash flow accordingly.

</details>

**6.** Under IFRS, a building is revalued upward by 200. The following year it is revalued downward by 350. Where does each go?

<details><summary>Answer</summary>

**Year 1:** +200 to **other comprehensive income**, accumulating as a revaluation surplus in equity.

**Year 2:** the 350 decrease first **reverses the existing 200 surplus** through OCI, and the remaining **150 goes to profit or loss**.

The rule is symmetric: a decrease reverses any existing surplus for that asset before hitting P&L, and an increase reverses any prior P&L loss before going to OCI.

</details>

**7.** Why does a company that grows by acquisition tend to show lower ROA than an otherwise identical organic grower?

<details><summary>Answer</summary>

The acquirer recognises acquired intangibles and goodwill at fair value, inflating the **denominator** of ROA, and amortises the finite-lived intangibles, depressing the **numerator**. The organic grower expensed the equivalent spend (R&D, marketing) as incurred, so it carries a thinner asset base and no amortisation drag.

Neither is more profitable in economic terms — the difference is recognition. Normalise by removing goodwill and acquired intangibles from both, or by capitalising an estimate of the organic company's intangible investment.

</details>

---

## Done when

- [ ] I can compute depreciation under straight-line, double-declining balance, and units of production
- [ ] I can state the IFRS and US GAAP impairment tests and show they can give different answers on the same facts
- [ ] I can list the effects of an impairment on every statement and on next year's ratios
- [ ] I can compute average age, average depreciable life, and remaining useful life, and say what each implies for capex
- [ ] I can state the IFRS revaluation rules including the asymmetric OCI/P&L treatment
- [ ] I can explain the three origins of intangibles and why they break comparability
- [ ] I answered the self-check cold, several days after first study

---

← [LM06 Analysis of Inventories](lm-06-analysis-of-inventories.md)  ·  [Topic index](README.md)  ·  [LM08 Topics in Long-Term Liabilities and Equity](lm-08-topics-in-long-term-liabilities-and-equity.md) →
