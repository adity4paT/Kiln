# FSA · LM03 — Analyzing Balance Sheets

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM1–LM2. The accounting equation, and the capitalise/expense logic from LM2. |
| **Where it shows up** | 2–3 questions. Goodwill and financial-instrument classification are perennial favourites. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the financial reporting and disclosures related to intangible assets
- explain the financial reporting and disclosures related to goodwill
- explain the financial reporting and disclosures related to financial instruments
- explain the financial reporting and disclosures related to non-current liabilities
- calculate and interpret common-size balance sheets and related financial ratios

---

## Core concepts

### What a balance sheet is, and isn't

`Assets = Liabilities + Equity`, at a **single moment**. Two limitations drive most of the analysis:

1. **Mixed measurement.** Some items are at historical cost, some at amortised cost, some at fair
   value. The total is therefore not "the value of the company" in any economic sense.
2. **Omitted assets.** Internally generated brands, customer relationships, and human capital are
   largely absent, while the *same* assets acquired in a business combination appear on the balance
   sheet. This is the deepest comparability problem in FSA.

Balance sheets are presented either as **classified** (current vs. non-current, the norm under both
frameworks) or in **liquidity order** (permitted under IFRS where more relevant, e.g. banks).
Current means expected to be realised or settled within one year or one operating cycle, whichever
is longer.

### Intangible assets

| Origin | IFRS | US GAAP |
| --- | --- | --- |
| **Purchased separately** | Capitalise at cost | Capitalise at cost |
| **Acquired in a business combination** | Capitalise at fair value | Capitalise at fair value |
| **Internally generated — research** | **Expense** | **Expense** |
| **Internally generated — development** | **Capitalise** once technical and commercial feasibility criteria are met | **Expense** (except software, once technological feasibility is reached) |
| **Internally generated brands, mastheads, customer lists, goodwill** | **Never capitalise** | **Never capitalise** |

Subsequent measurement depends on life:

- **Finite-lived** (patents, licences, customer relationships) → **amortise** over useful life;
  test for impairment when indicators arise.
- **Indefinite-lived** (some brands, broadcast licences) → **do not amortise**; test for impairment
  **at least annually**.

> The analyst's normalisation: a company that grew by **acquisition** carries recognised intangibles
> and amortises them; an identical company that grew **organically** expensed the same economics as
> R&D and marketing. The acquirer shows more assets and lower ROA; the organic grower shows higher
> ROA on a thinner asset base. Neither is "better" — they are differently recognised. Comparing them
> without adjustment is the error.

### Goodwill

**Goodwill = purchase price − fair value of identifiable net assets acquired.** It arises **only**
in a business combination. It is the residual: what you paid over and above everything you could
identify and value separately.

| Property | Treatment |
| --- | --- |
| Recognition | Only on acquisition; never internally generated |
| Amortisation | **None**, under both frameworks |
| Impairment testing | **At least annually**, and whenever indicators arise |
| Reversal of impairment | **Prohibited** under both IFRS and US GAAP |
| Tested at | IFRS: cash-generating unit (CGU). US GAAP: reporting unit |

**Impairment mechanics differ:**

- **IFRS (one step):** compare the CGU's carrying amount to its **recoverable amount**
  (higher of fair value less costs of disposal, and value in use). The shortfall is the impairment;
  it is allocated **first to goodwill**, then pro rata to other assets.
- **US GAAP (current, simplified one step):** compare the reporting unit's **carrying amount** to
  its **fair value**; the excess is the goodwill impairment, capped at the goodwill carried.

**Analyst treatment.** For comparability — especially in ratio and multiple work — many analysts
**remove goodwill from assets and from equity** before computing leverage and return ratios, because
goodwill is neither separable nor independently cash-generating. A goodwill impairment is a
**non-cash** charge: it reduces net income and equity but does not touch cash or CFO. It is, however,
an informative signal — it is management conceding the acquisition underperformed.

> **Trap:** "Goodwill is amortised over no more than 40 years." False under both current frameworks.
> Goodwill is **never amortised** — it is tested for impairment.

### Financial instruments

Classification drives where value changes go. Learn the three buckets and the two destinations.

| Classification | Measured at | Unrealised gains/losses go to |
| --- | --- | --- |
| **Amortised cost** (held to collect contractual cash flows) | Amortised cost | Nowhere — not remeasured |
| **FVOCI** — fair value through other comprehensive income | Fair value | **Other comprehensive income** (equity) |
| **FVPL** — fair value through profit or loss | Fair value | **Net income** |

Points that get tested:

- Debt held **to collect contractual cash flows** → amortised cost. Held **to collect and to sell**
  → FVOCI. Held **for trading** → FVPL.
- **Equity investments** are generally FVPL; IFRS permits an irrevocable election to present
  non-trading equity investments at **FVOCI** (with, under IFRS, **no recycling** of gains to profit
  or loss on disposal).
- **Impairment** uses an **expected credit loss** model — losses are provided for before they occur.
- **Financial liabilities** are usually at amortised cost, except derivatives and liabilities held
  for trading, which are FVPL.

**Why it matters analytically:** two companies holding identical securities can report very different
net income purely through classification. FVPL routes volatility through earnings; FVOCI parks it in
equity. When comparing, look at **comprehensive income**, not net income — it captures both.

### Non-current liabilities

- **Long-term debt.** Carried at **amortised cost** using the effective interest method. The carrying
  amount converges to face value at maturity. Disclosures to read: the **maturity schedule** (how
  much comes due when — refinancing risk), interest rates, currency, and **covenants**.
- **Deferred tax liabilities.** Temporary differences between accounting and tax bases (LM9).
- **Lease liabilities.** Under IFRS 16, essentially **all** leases go on-balance-sheet as a
  right-of-use asset and a lease liability. Under US GAAP, both finance and operating leases are
  recognised on the balance sheet, but the **income statement pattern differs**: a finance lease
  splits into amortisation plus interest (front-loaded total expense), whereas a US GAAP operating
  lease reports a **single straight-line** lease expense. Covered in LM8.
- **Pension obligations.** Defined benefit plans report the **funded status** — plan assets minus
  the benefit obligation — as a net asset or liability (LM8).
- **Provisions/contingent liabilities.** Recognise when an outflow is probable and reliably
  estimable; otherwise disclose. IFRS measures a provision at the **best estimate**; US GAAP uses
  the **low end** of a range when no point in the range is better than any other — a real difference.

### Common-size balance sheets and ratios

**Vertical common-size balance sheet:** every line as a **percentage of total assets**. This makes
capital structure and asset composition comparable across companies of any size, and makes drift
visible: inventory rising from 12% to 19% of assets over three years is a working-capital problem
you can see before any ratio confirms it.

**Liquidity ratios** — can it meet near-term obligations?

| Ratio | Formula | Note |
| --- | --- | --- |
| Current | Current assets / Current liabilities | Broadest |
| Quick (acid test) | (Cash + Short-term investments + Receivables) / Current liabilities | Excludes inventory |
| Cash | (Cash + Short-term investments) / Current liabilities | Most conservative |

**Solvency ratios** — can it survive its debt?

| Ratio | Formula |
| --- | --- |
| Debt-to-assets | Total debt / Total assets |
| Debt-to-capital | Total debt / (Total debt + Total equity) |
| Debt-to-equity | Total debt / Total equity |
| Financial leverage | Average total assets / Average total equity |

> Interpretation discipline: a ratio is meaningless in isolation. Always compare against (a) the
> company's own history, (b) close peers, and (c) covenant thresholds. A current ratio of 1.4 is
> comfortable for a supermarket and alarming for a capital-goods manufacturer.

---

## Formulas to know cold

```
Goodwill = Purchase price − Fair value of identifiable net assets acquired

Current ratio = Current assets / Current liabilities
Quick ratio   = (Cash + Short-term marketable securities + Receivables) / Current liabilities
Cash ratio    = (Cash + Short-term marketable securities) / Current liabilities

Debt-to-assets    = Total debt / Total assets
Debt-to-capital   = Total debt / (Total debt + Total equity)
Debt-to-equity    = Total debt / Total equity
Financial leverage = Average total assets / Average total equity

Common-size balance sheet line = Line item / Total assets
```

---

## Exam traps

> **Trap 1 — Goodwill is never amortised.** Under both IFRS and US GAAP it is tested for impairment
> at least annually. Any answer mentioning goodwill amortisation is wrong.

> **Trap 2 — Goodwill impairment cannot be reversed.** Under IFRS, impairments of *other* assets may
> be reversed; goodwill impairment never can. Under US GAAP no impairment reversal is permitted.

> **Trap 3 — Internally generated vs. acquired intangibles.** Internally generated brands and
> goodwill are **never** capitalised. The identical economics, acquired, *are*. This asymmetry is the
> point of the LOS.

> **Trap 4 — FVOCI vs. FVPL.** FVOCI unrealised gains go to **other comprehensive income (equity)**,
> not net income. Two companies with identical holdings can show different net income solely because
> of this. Compare **comprehensive income** instead.

> **Trap 5 — Research vs. development.** Research is *always* expensed under both frameworks.
> Development may be capitalised **under IFRS only** (once criteria are met). US GAAP expenses it,
> except software after technological feasibility.

> **Trap 6 — Impairment is non-cash.** It reduces net income, assets, and equity. It does **not**
> reduce cash or CFO. Questions about the cash-flow impact of an impairment are testing this.

> **Trap 7 — Provision measurement.** IFRS uses the **best estimate** within a range; US GAAP uses
> the **low end** when no amount in the range is more likely than another.

> **Trap 8 — Averages.** Ratios mixing a balance-sheet item with an income-statement item use the
> **average** balance. Pure balance-sheet ratios (current, quick, debt-to-equity) use period-end.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Company A buys Company B for 500m. The fair value of B's identifiable net assets is 380m, of which 60m is a customer-relationship intangible not previously on B's books. How much goodwill is recognised?

<details><summary>Answer</summary>

Goodwill = 500 − 380 = **120m**.

The 60m customer relationship is part of the 380m of *identifiable* net assets — it is recognised separately at fair value and is **not** goodwill. Identifying more intangibles reduces goodwill and creates future amortisation, which is why the allocation is scrutinised.

</details>

**2.** Two companies have identical operations. One grew organically; the other by acquisition. How will their balance sheets and ROA differ, and what should you do about it?

<details><summary>Answer</summary>

The **acquirer** capitalises acquired intangibles and goodwill, so it reports **larger total assets, more equity, and ongoing amortisation** → **lower ROA** and a lower asset turnover. The **organic grower** expensed the equivalent spend as R&D and marketing, so it shows a **thinner asset base and higher ROA**.

To compare: either strip goodwill and acquired intangibles from both, or capitalise-and-amortise an estimate of the organic company's intangible spend. Comparing the reported figures directly is the error.

</details>

**3.** A company classifies a bond portfolio as FVOCI instead of FVPL. Fair value rises 10m during the year. What is the effect on net income, comprehensive income, and equity?

<details><summary>Answer</summary>

**Net income: no effect.** **Other comprehensive income: +10m.** **Comprehensive income: +10m.** **Equity: +10m** (via accumulated OCI).

The classification moves *where* the gain is reported, not whether it is reported. This is exactly why comprehensive income is the comparable measure across companies with different classification choices.

</details>

**4.** Current assets are 4,200 (cash 600, short-term investments 300, receivables 1,400, inventory 1,700, prepaid 200). Current liabilities are 2,800. Compute the current, quick, and cash ratios.

<details><summary>Answer</summary>

Current = 4,200 / 2,800 = **1.50**
Quick = (600 + 300 + 1,400) / 2,800 = 2,300 / 2,800 = **0.82**
Cash = (600 + 300) / 2,800 = 900 / 2,800 = **0.32**

The gap between the current and quick ratios is almost entirely inventory — 1,700 of 4,200 current assets. For this company, liquidity depends heavily on how fast inventory converts.

</details>

**5.** A company records a 200m goodwill impairment. State the effect on net income, total assets, equity, CFO, and debt-to-equity.

<details><summary>Answer</summary>

Net income **−200m**; total assets **−200m**; equity **−200m**; **CFO unchanged** (non-cash charge — it is added back in the indirect method); debt-to-equity **rises**, because debt is unchanged while equity falls.

It is also a signal: management is conceding the acquisition did not deliver.

</details>

**6.** Under IFRS, which intangibles are amortised and which are not?

<details><summary>Answer</summary>

**Finite-lived** intangibles (patents, licences with expiry, customer relationships) are **amortised** over useful life and tested for impairment when indicators arise. **Indefinite-lived** intangibles and **goodwill** are **not amortised** and must be tested for impairment **at least annually**.

</details>

**7.** Why might an analyst deduct goodwill from both assets and equity before computing leverage ratios?

<details><summary>Answer</summary>

Goodwill is not separable, cannot be sold independently, generates no cash flows of its own, and in distress has effectively no realisable value. Leaving it in overstates the asset and equity base and therefore **understates** leverage. Removing it from both sides gives a tangible-equity view that is more comparable across acquisitive and organic companies, and closer to what a lender would underwrite.

</details>

**8.** On a vertical common-size balance sheet, inventory rises from 12% to 19% of total assets over three years while revenue grows 4% a year. What do you suspect?

<details><summary>Answer</summary>

Inventory is growing far faster than sales — the classic signature of **slowing demand, obsolescence building, or a deliberate build-up that has not been sold through**. It ties up cash (CFO deteriorates), raises the risk of future write-downs, and will show up as a lengthening days-of-inventory-on-hand. Check DOH, the inventory note for write-downs, and whether receivables are also stretching.

</details>

---

## Done when

- [ ] I can define goodwill and compute it from a purchase price and identifiable net assets
- [ ] I can state the treatment of goodwill: no amortisation, annual impairment test, no reversal
- [ ] I can explain why acquisitive and organic growers are not directly comparable, and what to adjust
- [ ] I can classify a financial instrument into amortised cost / FVOCI / FVPL and say where gains land
- [ ] I can compute current, quick, cash, and the four solvency ratios from a balance sheet
- [ ] I can build a vertical common-size balance sheet and read a composition shift from it
- [ ] I answered the self-check cold, several days after first study

---

← [LM02 Analyzing Income Statements](lm-02-analyzing-income-statements.md)  ·  [Topic index](README.md)  ·  [LM04 Analyzing Statements of Cash Flows I](lm-04-analyzing-statements-of-cash-flows-i.md) →
