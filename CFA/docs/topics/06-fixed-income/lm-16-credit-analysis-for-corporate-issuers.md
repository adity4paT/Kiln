# FI · LM16 — Credit Analysis for Corporate Issuers

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | FSA LM11 (ratios), LM14 (credit risk). |
| **Where it shows up** | 2 questions. The credit ratios and the priority-of-claims application are the reliable targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe the qualitative and quantitative factors used to evaluate a corporate borrower's creditworthiness
- calculate and interpret financial ratios used in credit analysis
- describe the seniority rankings of debt, secured versus unsecured debt and the priority of claims in bankruptcy, and their impact on credit ratings

---

## Core concepts

### The four Cs of credit analysis

| C | Question | Evidence |
| --- | --- | --- |
| **Capacity** | Can the borrower **service the debt**? | Cash flow, leverage and coverage ratios, industry position |
| **Collateral** | What **assets** back the claim? | Quality, liquidity, and valuation of the asset base |
| **Covenants** | What **protections** does the lender have? | The indenture (LM1) |
| **Character** | Is management **honest and competent**? | Track record, strategy, reporting quality (FSA LM10), governance |

**Capacity is where most of the work goes**, and it has three layers:

1. **Industry structure** — Porter's five forces (Equity LM9). A structurally unprofitable industry
   constrains every participant.
2. **Industry fundamentals** — cyclicality, growth, competitive dynamics, input cost exposure.
3. **Company fundamentals** — competitive position, operating history, management strategy and
   execution, and the financial ratios below.

### The credit ratios

**Profitability and cash flow measures — the numerators:**

```
EBITDA = Operating income + Depreciation + Amortisation
FFO (funds from operations) = Net income from continuing operations + D&A + deferred taxes
                              + other non-cash items
Free cash flow after dividends = CFO − Capex − Dividends
```

> **Why FFO rather than EBITDA?** EBITDA ignores cash taxes, cash interest, and working capital.
> FFO is closer to the cash actually generated before working capital movements and capex, which is
> why rating agencies lean on it. Free cash flow **after dividends** is the most demanding measure
> — it asks what is left for debt reduction once shareholders have been paid.

**Leverage ratios — how much debt relative to earning power:**

| Ratio | Formula | Reads as |
| --- | --- | --- |
| **Debt / EBITDA** | Total debt / EBITDA | Years of EBITDA to repay all debt. **The headline leverage measure** |
| **Net debt / EBITDA** | (Total debt − Cash) / EBITDA | Same, net of cash |
| **FFO / Debt** | Funds from operations / Total debt | The agencies' preferred leverage measure. **Higher is better** |
| **Debt / Capital** | Total debt / (Total debt + Equity) | Balance sheet leverage |
| **RCF / Net debt** | (FFO − Dividends) / Net debt | Retained cash flow against net debt |

**Coverage ratios — can current earnings service the interest?**

| Ratio | Formula |
| --- | --- |
| **EBIT / Interest** | The classic interest coverage ratio |
| **EBITDA / Interest** | More generous (adds back D&A); useful for capital-intensive issuers |
| **FFO / Interest** | Cash-based |
| **(CFO + Interest + Taxes) / Interest** | Cash interest coverage (FSA LM5) |

**Rough guidance on levels** (varies enormously by industry — a utility supports far more leverage
than a semiconductor company):

| | Investment grade | High yield |
| --- | --- | --- |
| Debt / EBITDA | Below ~3× | Above ~4–5× |
| EBIT / Interest | Above ~5× | Below ~3× |
| FFO / Debt | Above ~30% | Below ~20% |

> **Compare within an industry, always.** Absolute thresholds are meaningless across sectors: a
> regulated utility with predictable cash flows and hard assets sustains 5× leverage comfortably; a
> cyclical manufacturer at 5× is in trouble. What matters is the level **relative to peers** and the
> **direction of travel**.

### Adjustments the analyst must make

Reported figures are rarely the right inputs. Standard adjustments:

| Adjustment | Why |
| --- | --- |
| **Add operating lease obligations to debt** | Under IFRS 16 they are already on balance sheet; under US GAAP operating leases they are too, but the EBITDA treatment differs (FSA LM8) |
| **Add net pension underfunding to debt** | An economically debt-like fixed claim (FSA LM8) |
| **Deduct excess cash** | But only cash genuinely available, not working cash or trapped foreign cash |
| **Treat hybrid securities appropriately** | Part debt, part equity by agency methodology |
| **Adjust for non-recurring items** | Normalise EBITDA before computing leverage |
| **Add back operating lease interest to EBIT** | For comparability |

### Seniority and the priority of claims

```
1. Secured creditors              — up to the value of their collateral
2. Senior unsecured
3. Senior subordinated
4. Subordinated
5. Junior subordinated
6. Preference shareholders
7. Common shareholders
```

**Secured versus unsecured:**

| | **Secured** | **Unsecured** |
| --- | --- | --- |
| Backed by | Specific **collateral** | The general credit of the issuer |
| Recovery | **Higher** — first claim on the pledged assets | Lower |
| Yield | **Lower** | Higher |
| Rating | Notched **up** from the issuer rating | At or near the issuer rating |

**Doctrines that matter:**

- **Absolute priority rule** — each class paid in full before the next. **Frequently violated** in
  negotiated reorganisations, where senior creditors concede value to junior classes and equity to
  avoid protracted litigation and preserve going-concern value.
- **Pari passu** — equal-ranking claims treated equally.
- **Structural subordination** — holding-company debt is effectively junior to operating-subsidiary
  debt (LM14). Check the **guarantee structure**: an upstream guarantee from the opco mitigates it.

**Notching.** Rating agencies assign an **issuer rating** (applying to senior unsecured debt), then
**notch** individual issues up or down:

- **Up** for secured debt with good collateral
- **Down** for subordinated debt and for structurally subordinated holdco debt
- The amount of notching typically widens the **lower** the issuer rating, because recovery
  differences matter more when default is more likely

### Qualitative factors

| Factor | What to look for |
| --- | --- |
| **Industry structure** | Five forces; is the industry structurally profitable? |
| **Competitive position** | Market share, cost position, pricing power (Equity LM10) |
| **Management strategy** | Growth ambitions, appetite for debt-funded M&A, stated leverage targets |
| **Financial policy** | Dividend and buyback behaviour; historical leverage discipline; response to prior downturns |
| **Governance** | Board independence, related-party transactions, reporting quality (FSA LM10) |
| **Ownership** | Private equity ownership usually means higher leverage and a shorter horizon |
| **Country and currency risk** | Where the assets and cash flows sit versus where the debt sits |

> **Financial policy is the qualitative factor that most often decides the outcome.** Two companies
> with identical ratios can have very different trajectories if one has a stated commitment to a
> leverage target and a history of honouring it, while the other has repeatedly levered up for
> acquisitions or shareholder distributions. **What management has done before is the best available
> evidence of what it will do next.**

---

## Formulas to know cold

```
THE FOUR Cs
  Capacity · Collateral · Covenants · Character

CASH FLOW MEASURES
  EBITDA = Operating income + D + A
  FFO    = Net income from continuing ops + D&A + deferred taxes + other non-cash items
  Free cash flow after dividends = CFO − Capex − Dividends

LEVERAGE (lower is better, except FFO/Debt where HIGHER is better)
  Debt / EBITDA            Net debt / EBITDA
  FFO / Debt               ← the agencies' preferred measure; HIGHER is better
  Debt / Capital = Debt/(Debt + Equity)
  RCF / Net debt = (FFO − Dividends) / Net debt

COVERAGE (higher is better)
  EBIT / Interest          EBITDA / Interest          FFO / Interest
  Cash interest coverage = (CFO + Interest paid + Taxes paid) / Interest paid

ROUGH THRESHOLDS (industry-dependent — always compare within a sector)
  Investment grade:  Debt/EBITDA < ~3x | EBIT/Interest > ~5x | FFO/Debt > ~30%
  High yield:        Debt/EBITDA > ~4-5x | EBIT/Interest < ~3x | FFO/Debt < ~20%

STANDARD ADJUSTMENTS
  + operating lease obligations to debt
  + net pension underfunding to debt
  − genuinely excess cash
  normalise EBITDA for non-recurring items
```

---

## Exam traps

> **Trap 1 — FFO/Debt direction.** **Higher is better** — it is cash flow over debt, the inverse of
> a leverage ratio. Debt/EBITDA is the one where lower is better.

> **Trap 2 — Comparing leverage across industries.** A utility at 5× Debt/EBITDA may be
> investment-grade; a cyclical manufacturer at 5× is not. **Compare within a sector.**

> **Trap 3 — Interest coverage numerator.** **EBIT**, not net income. Interest is deducted in
> arriving at net income, which makes the ratio circular.

> **Trap 4 — Forgetting the adjustments.** Add **pension underfunding** and **lease obligations** to
> debt; normalise EBITDA for non-recurring items. Reported leverage understates true leverage.

> **Trap 5 — Deducting all cash.** Only **genuinely excess** cash. Working cash and cash trapped in
> foreign subsidiaries (repatriation would trigger tax) are not available for debt reduction.

> **Trap 6 — Assuming the absolute priority rule holds.** It is **frequently violated** in
> negotiated reorganisations.

> **Trap 7 — Missing structural subordination.** Holdco debt is junior to opco debt unless there is
> an upstream guarantee. Check the guarantee structure, not just the label.

> **Trap 8 — Ignoring financial policy.** A company with strong current ratios and a history of
> debt-funded acquisitions is a different credit from one with the same ratios and a stated,
> honoured leverage target.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** EBITDA is 850, total debt 3,400, cash 400, EBIT 620, interest expense 145, FFO 690. Compute the main credit ratios and assess.

<details><summary>Answer</summary>

**Leverage:**
Debt/EBITDA = 3,400/850 = **4.00×**
Net debt/EBITDA = (3,400 − 400)/850 = 3,000/850 = **3.53×**
FFO/Debt = 690/3,400 = **20.3%**

**Coverage:**
EBIT/Interest = 620/145 = **4.28×**
EBITDA/Interest = 850/145 = **5.86×**
FFO/Interest = 690/145 = **4.76×**

**Assessment: borderline investment grade — most likely BB+/BBB−.** Debt/EBITDA of 4.0× is above the usual investment-grade threshold of ~3×; FFO/Debt of 20% sits at the boundary; EBIT/Interest of 4.3× is adequate but not strong.

**What would settle it:** the **industry** (a utility at these ratios is comfortably investment grade; a cyclical manufacturer is not), the **trend** over three years, the **maturity profile**, and whether pension and lease adjustments would push leverage higher. Also the **financial policy** — is management committed to de-levering?

</details>

**2.** Why do rating agencies prefer FFO/Debt to Debt/EBITDA?

<details><summary>Answer</summary>

Because **EBITDA overstates the cash available to service debt**.

EBITDA is earnings before interest, tax, depreciation and amortisation. It therefore **ignores**:
- **Cash taxes**, which are a genuine, non-discretionary outflow
- **Cash interest**, though that is partly the point of the measure
- **Working capital** movements, which can consume substantial cash in a growing business
- **Maintenance capital expenditure**, which is the cost of keeping the earnings stream intact

**FFO** starts from net income from continuing operations and adds back D&A, deferred taxes, and other non-cash items. It is therefore **after cash taxes and after cash interest** — much closer to the cash genuinely generated before working capital and capex.

**FFO/Debt is also a flow-over-stock ratio in the intuitive direction:** higher is better, and it reads as 'what fraction of the debt could be repaid from one year's cash generation?'

**The practical difference:** two companies with identical Debt/EBITDA of 4× can have FFO/Debt of 25% and 12% if one faces a much higher cash tax rate and interest burden. The second is materially weaker, and only FFO/Debt reveals it.

</details>

**3.** A company's reported Debt/EBITDA is 2.8×. It has 400 of net pension underfunding and 600 of operating lease obligations not in reported debt, and EBITDA includes a 90 one-off gain. Reported debt is 1,680 and EBITDA 600. Recompute.

<details><summary>Answer</summary>

**Adjusted debt:**
1,680 + 400 (pension underfunding) + 600 (lease obligations) = **2,680**

**Adjusted EBITDA:**
600 − 90 (one-off gain) = **510**

(Strictly, capitalised leases would also add an implied depreciation and interest split, which would raise EBITDA somewhat — but the exam convention here is the simple addition to debt.)

**Adjusted Debt/EBITDA = 2,680 / 510 = 5.25×**

The reported 2.8× understates leverage by nearly **half**. On the reported figure this looks comfortably investment grade; on the adjusted figure it is firmly high yield.

**This is the single highest-value exercise in credit analysis.** Reported leverage is almost always understated, and the gap is largest for companies with large lease commitments (retailers, airlines) and legacy pension obligations (industrials).

</details>

**4.** Explain notching and why it widens at lower rating levels.

<details><summary>Answer</summary>

**Notching** is the adjustment of an individual **issue** rating up or down from the **issuer** rating, to reflect that issue's expected **recovery** in a default.

The issuer rating applies to senior unsecured debt and reflects **probability of default**. But two bonds from the same issuer have the **same PD** and can have very different **LGD** (LM14):
- **Secured** debt with good collateral → notched **up**
- **Subordinated** debt → notched **down**
- **Structurally subordinated** holdco debt → notched **down**

**Why notching widens at lower rating levels:** for a AAA issuer, default is so unlikely that the difference in recovery between a secured and a subordinated bond is almost irrelevant to expected loss — you multiply a large LGD difference by a tiny PD. Both issues get essentially the issuer rating.

For a **B** or **CCC** issuer, default is a live possibility. Recovery differences now dominate expected loss: the secured bondholder might recover 80% and the subordinated holder 10%, and that difference is what the investor actually experiences. Agencies therefore notch by two or three levels rather than one.

**The general principle: PD dominates at high ratings; LGD dominates at low ratings.**

</details>

**5.** Two companies have identical credit ratios. One is owned by a private equity sponsor; the other is family-controlled with a stated 2.5x leverage target it has held for a decade. How does this affect your view?

<details><summary>Answer</summary>

**Financial policy is the qualitative factor that most often decides the outcome**, and these two have opposite policies.

**The private-equity-owned company:** PE sponsors have a **3–7 year horizon** and are rewarded on equity returns, which leverage amplifies. Expect: a **dividend recapitalisation** (borrowing to pay the sponsor a distribution), debt-funded bolt-on acquisitions, and cost-cutting that may impair long-term competitiveness. Current ratios are a snapshot of a position the owner **intends to change**, in the direction that harms creditors. Covenants are the only real protection, and PE-sponsored deals are frequently **covenant-lite**.

**The family-controlled company:** a **stated leverage target honoured for a decade** is strong evidence of intent, and family owners typically have a multi-generational horizon and reputational stake in the business surviving. Expect ratios to be **maintained or improved**. The risk is different — succession, and the possibility of a large acquisition or a generational buyout.

**What to check:** the **covenant package** (what actually prevents a dividend recap?), the **change-of-control** provisions, and each owner's **track record**. What management has done before is the best available evidence of what it will do next.

**Conclusion:** identical ratios, materially different credits. The PE-owned bond should trade at a wider spread, and the difference is not mispricing.

</details>

---

## Done when

- [ ] I can state the four Cs and explain what evidence supports each
- [ ] I can compute the full set of leverage and coverage ratios and state which direction is good
- [ ] I can make the standard adjustments for leases, pensions, excess cash, and non-recurring items
- [ ] I can explain why agencies prefer FFO/Debt to Debt/EBITDA
- [ ] I can state the priority of claims and explain notching
- [ ] I can explain why notching widens at lower rating levels
- [ ] I can explain why financial policy and ownership change the credit view at identical ratios
- [ ] I answered the self-check cold, several days after first study

---

← [LM15 Credit Analysis for Government Issuers](lm-15-credit-analysis-for-government-issuers.md)  ·  [Topic index](README.md)  ·  [LM17 Fixed-Income Securitization](lm-17-fixed-income-securitization.md) →
