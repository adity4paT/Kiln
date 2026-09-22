# Equity Investments

*The topic where FSA, Quants, and Corporate Issuers all pay off at once.*

| | |
| --- | --- |
| **Exam weight** | 11-14% — roughly 19–25 of 180 questions |
| **Study block** | Month 2, days 43–60 |
| **Budget** | 18 days · 72 hours |
| **Modules** | 12 |
| **Position in study order** | 4 of 10 |

## Why this topic sits here

Equity is studied **fourth**, immediately after Corporate Issuers, and it is the point where the
first three blocks converge.

LM6 (DCF) needs the discounting from **QM LM4** and the free cash flow definitions from **FSA LM5**.
LM8 (forecasting) is **FSA LM12** applied to a valuation. LM7 (multiples) needs enterprise value and
the pairing rule. LM12 (CAPM) needs the portfolio mathematics from **QM LM8** and the regression from
**QM LM10**. LM10's central test — ROIC versus WACC — comes straight from **Corporate Issuers LM5
and LM6**.

None of this is accidental. Studying Equity fourth means every prerequisite is in place, and the
topic consolidates rather than introduces. Studying it first, as some plans do, means learning five
things at once.

At **11–14%** it is joint-heaviest with FSA and Fixed Income. The 72 hours are concentrated in
LM6 and LM7 — 22 of them — because the valuation modules carry most of the exam weight and almost
all of the reusable technique.

> **LM6 and LM7 are the topic.** If time runs short, protect those two and LM12 at the expense of
> LM2, LM9, and LM11 — which are descriptive and can be covered at a skim in an evening.

## Modules

| LM | Module | Hours | Focus |
| --- | --- | --- | --- |
| 01 | [Equity Instrument Features](lm-01-equity-instrument-features.md) | 4 | Share types, preference share features, depository receipts. Pure recall. |
| 02 | [Equity Jurisdictions, Classes, and the Voting Process](lm-02-equity-jurisdictions-classes-and-the-voting-process.md) | 4 | Economic vs voting rights, cumulative voting, the proxy process. |
| 03 | [Equity Issuance and Trading](lm-03-equity-issuance-and-trading.md) | 6 | Markets, order types, float and liquidity measures, index types. |
| 04 | [Sources of Equity Returns](lm-04-sources-of-equity-returns.md) | 6 | **Dividend chronology** and buyback effects on EPS and BVPS. |
| 05 | [Introduction to Equity Valuation](lm-05-introduction-to-equity-valuation.md) | 5 | Price vs value, enterprise value, the **pairing rule**, model selection. |
| 06 | [Discounted Cash Flow (DCF) and Growth Models](lm-06-discounted-cash-flow-dcf-and-growth-models.md) | 12 | **The core module.** DDM, FCFE, FCFF, Gordon growth, multistage, H-model. |
| 07 | [Relative Value Equity Valuation Approaches](lm-07-relative-value-equity-valuation-approaches.md) | 10 | **Justified multiples** from fundamentals; EV/EBITDA; peer group construction. |
| 08 | [Financial Statement Forecasting in Equity Valuation](lm-08-financial-statement-forecasting-in-equity-valuation.md) | 5 | Building a forecast model; the equity value bridge. Consolidates FSA LM12. |
| 09 | [Industry and Competitive Analysis](lm-09-industry-and-competitive-analysis.md) | 6 | Industry analysis, lifecycle, Porter, PESTLE, HHI. |
| 10 | [Company Analysis: Past, Present, and Future](lm-10-company-analysis-past-present-and-future.md) | 5 | Competitive strategy, pricing power, ROIC vs WACC. Consolidates Corporate Issuers. |
| 11 | [Equity Analyst Research Reports](lm-11-equity-analyst-research-reports.md) | 3 | Research reports and why valuations differ. Overlaps Ethics Standard V. |
| 12 | [The Capital Asset Pricing Model, Market Model, and Other Factor-Based Equity Models](lm-12-the-capital-asset-pricing-model-market-model-and-other-facto.md) | 6 | **CAPM**, the SML, APT, and multi-factor models. Previews Portfolio Management. |

## The formulas this topic lives on

Six things from this topic must be automatic.

```
1. MODEL–RATE PAIRING:  DDM & FCFE → re;  FCFF → WACC → EV (− net debt = equity)
2. Gordon:  V0 = D1/(r − g);  r = D1/P0 + g;  g = r − D1/P0;  g = b × ROE
3. Multistage terminal value D(n+1)/(r−g) is AS OF time n → discount n periods
4. Justified P/E = payout/(r − g);  Justified P/B = (ROE − g)/(r − g)  [P/B > 1 ⟺ ROE > r]
5. EV = Mkt cap + Debt + Pref + Minorities − Cash;  EV pairs with PRE-interest flows only
6. CAPM:  E(Ri) = Rf + βi[E(RM) − Rf];  βi = Cov(Ri,RM)/Var(RM) = ρ σi/σM
```

## Topic wrap-up

Before you tick this topic complete and move to Portfolio Management:

- [ ] All 12 modules ticked, with their **Done when** lists genuinely cleared
- [ ] I can value a share three ways — DDM, multiples, and a DCF — and explain why they differ
- [ ] I can build a two-stage DDM and discount the terminal value by the right number of periods
- [ ] I can derive the justified P/E and P/B from the Gordon model, from memory
- [ ] I can state the pairing rule and never write EV/net income
- [ ] I can compute a required return with CAPM and place a security relative to the SML
- [ ] I can reverse-engineer the growth rate the market is pricing, and say whether it is plausible
- [ ] I have completed **100+ Equity questions**, logged in `trackers/weak-areas.md`

**Day 60 checkpoint — the halfway mark on exam weight.** FSA, QM (first block), Corporate Issuers,
and Equity together account for roughly a third of the exam, and every remaining topic borrows from
them. If LM6 or LM7 is shaky, fix it now: Fixed Income (day 71) is the same discounting applied to
bonds, and Portfolio Management (day 61) begins with CAPM.

---

[← Master study plan](../../study-plan/master-plan.md)  ·  [All topics](../)  ·  [Progress tracker](../../../trackers/progress-tracker.md)
