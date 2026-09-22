# EQ · LM07 — Relative Value Equity Valuation Approaches

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 10 |
| **Prerequisites** | LM5 (the pairing rule, enterprise value), LM6 (Gordon growth, for the justified multiple derivation). |
| **Where it shows up** | 2–3 questions. Justified P/E and the peer-group selection logic are the reliable targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the process for using multiples to value equity based on the method of comparables and the method of forecasted fundamentals
- calculate and interpret price and enterprise value multiples, and describe their appropriate uses
- determine a potential peer group for multiples-based equity valuation based on a company's industry classification or specific drivers of expected return
- describe the use of multiples based on past, current, and projected future values in estimating equity value

---

## Core concepts

### Two ways to use a multiple

| Method | How it works | The assumption |
| --- | --- | --- |
| **Method of comparables** | Compare the company's multiple to peers, the sector, or its own history | **The comparison set is correctly priced** |
| **Method of forecasted fundamentals** | Derive the multiple the company *should* trade at from its fundamentals (growth, payout, risk) | Your fundamental estimates are right |

The second is usually called the **justified multiple**, and it is the one that requires derivation.

### Price multiples

| Multiple | Formula | Best for | Watch out for |
| --- | --- | --- | --- |
| **P/E** | Price / EPS | Profitable, stable companies | **Meaningless if earnings are negative**; distorted by accounting policy and one-offs |
| **P/B** | Price / Book value per share | **Financial institutions**; asset-heavy businesses | Book value ignores intangibles; distorted by buybacks above book |
| **P/S** | Price / Sales per share | Loss-making and early-stage companies; cyclicals at a trough | **Ignores profitability entirely** and ignores leverage |
| **P/CF** | Price / Cash flow per share | Where earnings quality is doubtful | Definition of "cash flow" varies |
| **Dividend yield** | D / P | Income-focused comparison; mature payers | Useless for non-payers; a high yield may signal distress |

**Trailing vs. forward:**

```
Trailing P/E = Current price / EPS over the last 12 months    ← actual, but backward-looking
Forward P/E  = Current price / Expected EPS next 12 months    ← relevant, but depends on forecasts
```

> Prices reflect **expectations**, so forward multiples are generally more informative. The cost is
> that they depend on someone's forecast — often a consensus that is systematically optimistic. When
> comparing companies, **use the same basis for all of them**; comparing one company's forward P/E to
> another's trailing P/E is meaningless.

**Normalised earnings** for cyclicals: use mid-cycle or average earnings rather than the current
year. A cyclical at the peak shows a **low** P/E (peak earnings in the denominator) and a cyclical at
the trough shows a **high** one — the opposite of what naive reading suggests. This inversion is a
classic value trap and a favourite exam item.

### Enterprise value multiples

| Multiple | Formula | Why it is used |
| --- | --- | --- |
| **EV/EBITDA** | EV / EBITDA | **Capital-structure neutral**; ignores depreciation policy differences; works for loss-making companies at the net level |
| **EV/EBIT** | EV / EBIT | Like EV/EBITDA but retains the capital-intensity signal that depreciation carries |
| **EV/Sales** | EV / Revenue | For loss-making companies; least sensitive to accounting |
| **EV/FCFF** | EV / Free cash flow to firm | Closest to a cash-based economic measure |

**Why EV/EBITDA is the workhorse in practice:**

- **Neutral to capital structure** — comparable across differently levered companies, and across
  jurisdictions with different tax rates
- **Neutral to depreciation policy** — removes an area of wide accounting discretion (FSA LM7)
- **Usable when net income is negative** but EBITDA is positive

**Its weaknesses, which the exam expects you to know:**

- **Ignores capital intensity entirely.** A company needing heavy maintenance capex and one needing
  almost none look identical on EBITDA. Charlie Munger's objection — "think about EBITDA as
  bullshit earnings" — is precisely that depreciation is a real cost.
- **Ignores working capital requirements** and therefore cash conversion.
- **Ignores differences in tax** position.
- EBITDA is a **non-GAAP measure** and its definition varies (FSA LM10) — "adjusted EBITDA"
  especially.

> **The pairing rule, again** (LM5): **EV multiples pair with pre-interest flows** (EBITDA, EBIT,
> sales); **equity multiples pair with post-interest flows** (EPS, book equity). Mixing them is the
> most common multiples error.

### Justified multiples from fundamentals

Start from the Gordon growth model and divide through.

**Justified leading (forward) P/E** — divide `P0 = D1/(r − g)` by `E1`:

```
P0/E1 = (D1/E1) / (r − g) = payout ratio / (r − g)
```

**Justified trailing P/E** — divide by `E0`:

```
P0/E0 = [payout ratio × (1 + g)] / (r − g)
```

**Justified P/B** — from the residual income relationship:

```
P0/B0 = (ROE − g) / (r − g)
```

Read this one carefully: **P/B exceeds 1 precisely when ROE > r.** A company earning more on its
book equity than the return investors require is worth more than its book value. A company earning
less is worth less. This is the ROIC-versus-WACC test (Corporate Issuers LM5) expressed as a
multiple.

**Justified P/S:**

```
P0/S0 = [net profit margin × payout ratio × (1 + g)] / (r − g)
```

> **What the justified multiples teach:** a multiple is **not** an arbitrary market convention. It is
> a compressed statement about **growth, profitability, payout, and risk**. A company deserves a
> higher P/E if it has higher `g`, higher payout for a given `g`, or lower `r`. When you see a P/E
> of 30 against a sector at 15, the justified formula tells you exactly which of those four must
> differ — and by how much.

### Selecting a peer group

The weakest link in relative valuation. A multiple is only as good as the comparison set.

**Start with an industry classification** — GICS, ICB, or a similar scheme — then **refine by the
drivers of expected return**:

| Refine on | Why |
| --- | --- |
| **Growth rate** | A 20%-growth company does not belong with a 2%-growth peer |
| **Profitability (margins, ROE/ROIC)** | Drives the justified multiple directly |
| **Risk and capital structure** | Affects `r`, and therefore the denominator |
| **Business model** | Subscription vs transactional; asset-light vs asset-heavy |
| **Size and market position** | Scale economics, bargaining power |
| **Geography and end markets** | Different growth and regulatory environments |
| **Accounting policy** | LIFO/FIFO, depreciation lives, IFRS/US GAAP (FSA) |
| **Cycle position** | Compare like for like within the cycle |

**The problems, stated plainly:**

- **Few true comparables exist.** Conglomerates and diversified companies have none.
- **If the whole sector is mispriced, the multiple inherits the error in full.** Relative valuation
  tells you whether a company is cheap **relative to its peers**, not whether it is cheap.
- **Accounting differences** distort every earnings- and book-based multiple unless adjusted.
- A **small peer group** is dominated by one or two outliers — use the **median**, not the mean.

### Past, current, and projected multiples

| Basis | Use | Limitation |
| --- | --- | --- |
| **Historical (own history)** | Is the company cheap **relative to itself**? | The business may have changed fundamentally; long-run mean reversion may not apply |
| **Current (trailing)** | Actual, verifiable numbers | Backward-looking; includes one-off items |
| **Forward (projected)** | What the market is paying for **expected** earnings | Depends on forecasts, which are systematically optimistic |

**A company's own historical multiple range** is a genuinely useful anchor — but only if the
business is fundamentally unchanged. A company that has shifted from a low-growth hardware model to
a high-growth subscription model should **not** revert to its historical P/E, and arguing that it
should is a common error.

> **Best practice:** use multiples as a **cross-check on a DCF**, not as a substitute for one. When
> they disagree, the disagreement is the most informative output you have — it localises exactly
> which assumption the valuation depends on.

---

## Formulas to know cold

```
PRICE MULTIPLES
  P/E = Price / EPS          P/B = Price / Book value per share
  P/S = Price / Sales/share  P/CF = Price / Cash flow per share
  Dividend yield = D / P

ENTERPRISE VALUE MULTIPLES   (EV = Mkt cap + Debt + Pref + Minorities − Cash)
  EV/EBITDA    EV/EBIT    EV/Sales    EV/FCFF

PAIRING RULE
  EV  ↔ pre-interest:  EBITDA, EBIT, Sales, FCFF
  Equity ↔ post-interest: EPS, Book equity, FCFE

JUSTIFIED MULTIPLES (derived from the Gordon growth model)
  Leading P/E   P0/E1 = payout ratio / (r − g)
  Trailing P/E  P0/E0 = [payout × (1 + g)] / (r − g)
  P/B           P0/B0 = (ROE − g) / (r − g)      ← P/B > 1 exactly when ROE > r
  P/S           P0/S0 = [net margin × payout × (1 + g)] / (r − g)

PEER GROUP: start with industry classification, then refine on
  growth · profitability · risk & capital structure · business model
  · size · geography · accounting policy · cycle position
  Use the MEDIAN, not the mean, in small peer groups.
```

---

## Exam traps

> **Trap 1 — Mismatching numerator and denominator.** **EV/net income** is meaningless. EV pairs with
> pre-interest flows; equity value pairs with post-interest flows.

> **Trap 2 — Cyclical P/E inversion.** A cyclical at the **peak** shows a **low** P/E (inflated
> earnings) and at the **trough** a **high** one. Naive reading buys the peak and avoids the trough —
> exactly backwards. Use **normalised** earnings.

> **Trap 3 — Mixing trailing and forward bases.** Compare all companies on the **same** basis.

> **Trap 4 — Assuming the peer group is correctly priced.** Relative valuation says whether a company
> is cheap **relative to its peers**, not whether it is cheap. A whole mispriced sector carries the
> error through in full.

> **Trap 5 — P/E with negative earnings.** Undefined and uninterpretable. Use EV/Sales, P/B, or a
> forward multiple on a profitable year.

> **Trap 6 — Treating EBITDA as cash flow.** It ignores capex, working capital, interest, and tax.
> For a capital-intensive business it overstates economic earnings substantially.

> **Trap 7 — Misreading the justified P/B condition.** **P/B > 1 requires ROE > r**, not ROE > g.

> **Trap 8 — Assuming reversion to a historical multiple.** Only valid if the business is
> fundamentally unchanged. A genuine model shift breaks the anchor.

> **Trap 9 — Using the mean of a small peer group.** One outlier dominates. Use the **median**.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company has a payout ratio of 45%, a required return of 10%, and expected growth of 4%. Compute the justified leading and trailing P/E.

<details><summary>Answer</summary>

**Leading P/E** = payout / (r − g) = 0.45 / (0.10 − 0.04) = 0.45 / 0.06 = **7.5×**

**Trailing P/E** = [payout × (1 + g)] / (r − g) = [0.45 × 1.04] / 0.06 = 0.468 / 0.06 = **7.8×**

The trailing multiple is higher because the denominator is **last** year's earnings, which are smaller by a factor of (1+g).

If the shares actually trade at 14× leading earnings, the market is assuming higher growth, a lower required return, or a higher payout than you are. Solve for the implied `g`: 0.45/(0.10 − g) = 14 → g = 6.8%. The disagreement is now a specific, arguable 2.8 percentage points of perpetual growth.

</details>

**2.** Why does a justified P/B above 1 require ROE > r?

<details><summary>Answer</summary>

From the residual income relationship, `P0/B0 = (ROE − g)/(r − g)`.

For this to exceed 1: `(ROE − g) > (r − g)`, which simplifies to **ROE > r**.

**The economics:** book value is the capital shareholders have put in. If the company earns a return on that capital **above** what investors require (`ROE > r`), it is creating value with every unit of equity it holds — so the market rationally pays **more** than book value for it.

If `ROE < r`, the company is **destroying** value: the capital would be worth more returned to shareholders than retained. The market pays **less** than book, and the discount widens the more capital the company retains.

This is the **ROIC versus WACC** test (Corporate Issuers LM5) expressed as a multiple. It also explains why persistently sub-1 P/B companies are often correctly priced rather than cheap: a low ROE justifies a low P/B.

</details>

**3.** A cyclical steel producer trades at a P/E of 5 at the top of the cycle and 40 at the bottom. Explain and say what to do.

<details><summary>Answer</summary>

**The P/E inverts for cyclicals** because earnings are far more volatile than price.

**At the peak:** earnings are at a cyclical maximum. The denominator is inflated, so the P/E looks **low** — the stock appears cheap. But those earnings are unsustainable, and the market knows it, which is why the price has not risen proportionally.

**At the trough:** earnings are depressed or negative. The denominator collapses, so the P/E looks **high** — the stock appears expensive. But the market is looking through to recovery.

**Naive P/E screening therefore buys cyclicals at the peak and avoids them at the trough** — precisely the wrong times.

**What to do:** use **normalised (mid-cycle) earnings** — average margins and volumes across a full historical cycle — as the denominator. Or use **P/B**, which is far more stable for asset-heavy cyclicals, or **EV/Sales**. Or run a DCF spanning a full cycle (FSA LM12).

</details>

**4.** Two companies in the same industry have identical EV/EBITDA of 9×. One requires maintenance capex of 3% of sales, the other 12%. Are they equally valued?

<details><summary>Answer</summary>

**No — the capital-intensive one is far more expensive.**

EBITDA is **before depreciation**, so it treats a business that must continually reinvest to stand still exactly like one that need not. But maintenance capex is a **real, unavoidable cash outflow** — it is the cost of preserving the earnings stream.

The company spending 12% of sales on maintenance capex converts far less of its EBITDA into cash available to investors. On **EV/(EBITDA − maintenance capex)**, or on **EV/FCFF**, the two would look very different.

**This is the central criticism of EV/EBITDA:** it ignores capital intensity. The correct response is to use EV/EBIT (which retains depreciation as a proxy for capital consumption), EV/FCFF, or to adjust EBITDA explicitly for maintenance capex when comparing businesses of different capital intensity.

</details>

**5.** How would you construct a peer group for a mid-cap European speciality chemicals company?

<details><summary>Answer</summary>

**Start** with the industry classification (GICS: Materials → Chemicals → Speciality Chemicals), then **refine on the drivers of expected return**:

- **Business mix** — speciality (formulated, higher margin, stickier) versus commodity chemicals. These have completely different margin profiles and cyclicality and should not be pooled.
- **Growth rate** — comparable end-market exposure and historical growth.
- **Profitability** — EBITDA margin and ROIC in a similar band.
- **Size** — mid-cap peers; large caps carry scale advantages and often a liquidity premium.
- **Geography and end markets** — European regulatory and energy cost environment; exposure to automotive versus construction versus pharma end markets.
- **Capital structure** — similar leverage, or use EV multiples to neutralise it.
- **Accounting** — IFRS reporters (avoid mixing with US GAAP LIFO reporters without adjustment).

**Then:** use the **median** multiple, not the mean — speciality chemicals peer groups are small and one outlier distorts the average. Show the **range** as well as the median, and explain where in the range this company belongs and why.

**Finally:** cross-check against a DCF. If the peer median implies a value well below your DCF, work out which assumption is doing the work.

</details>

**6.** Explain the difference between the method of comparables and the method of forecasted fundamentals.

<details><summary>Answer</summary>

**Method of comparables:** compare the company's actual multiple to those of peers, the sector, or its own history, and conclude it is cheap or expensive relative to them. It requires almost no modelling, and its critical assumption is that **the comparison set is correctly priced**. If the whole sector is in a bubble, every member looks fairly valued.

**Method of forecasted fundamentals (justified multiple):** derive the multiple the company **should** trade at from its own fundamentals — `P/E = payout/(r − g)`, `P/B = (ROE − g)/(r − g)`. It requires you to estimate growth, payout, profitability, and the required return, but it produces an **absolute** standard independent of what anyone else is priced at.

**Use both.** The comparables method tells you where the market sits; the fundamentals method tells you where it should sit. When a company trades at 22× against a justified 12×, either your `g` is too low or the market's is too high — and reverse-engineering the market's implied `g` turns a vague disagreement into a specific, testable claim.

</details>

---

## Done when

- [ ] I can compute and interpret P/E, P/B, P/S, EV/EBITDA, EV/EBIT, and EV/Sales
- [ ] I can state the pairing rule and apply it without thinking
- [ ] I can derive all four justified multiples from the Gordon growth model
- [ ] I can explain why P/B > 1 requires ROE > r and connect it to ROIC vs WACC
- [ ] I can explain the cyclical P/E inversion and what to use instead
- [ ] I can list the weaknesses of EV/EBITDA, especially capital intensity
- [ ] I can construct a peer group by refining an industry classification on return drivers
- [ ] I can distinguish the method of comparables from the method of forecasted fundamentals
- [ ] I answered the self-check cold, several days after first study

---

← [LM06 Discounted Cash Flow (DCF) and Growth Models](lm-06-discounted-cash-flow-dcf-and-growth-models.md)  ·  [Topic index](README.md)  ·  [LM08 Financial Statement Forecasting in Equity Valuation](lm-08-financial-statement-forecasting-in-equity-valuation.md) →
