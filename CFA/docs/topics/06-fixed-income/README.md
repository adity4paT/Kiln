# Fixed Income

*The largest topic in the curriculum, and the one where the mathematics of Quants finally does real work.*

| | |
| --- | --- |
| **Exam weight** | 11-14% — roughly 19–25 of 180 questions |
| **Study block** | Month 3, days 71–90 |
| **Budget** | 20 days · 80 hours |
| **Modules** | 19 |
| **Position in study order** | 6 of 10 |

## Why this topic sits here

Fixed Income is studied **sixth**, in the second half of Month 3, and it is the single largest block
in the plan: **19 modules, 80 hours, 20 days.**

It sits here for two reasons. First, it needs **QM LM4** (discounting and no-arbitrage forward
rates) and **FSA LM11** (the ratios that credit analysis is built on) to already be solid — this is
the most prerequisite-dependent topic in the curriculum. Second, it needs the **risk framework from
Portfolio Management** (systematic risk, the price of risk) that you complete on day 70, one day
before this block starts.

At **11–14%** it is joint-heaviest with FSA and Equity. But its real weight is larger than that,
because the discounting mechanics here carry directly into **Derivatives** (forwards, futures, and
swaps are all no-arbitrage discounting problems) and the credit analysis carries into
**Alternative Investments** (private debt).

**The structure of the block:** LM1–LM5 are descriptive vocabulary. LM6–LM9 are valuation. LM10–LM13
are interest rate risk — the mathematical core. LM14–LM16 are credit. LM17–LM19 are structured
products. Each group builds on the last.

> **LM10–LM13 are the heart of the topic.** Duration, convexity, and their curve-based extensions
> account for 20 of the 80 hours and a disproportionate share of the exam questions. If the block
> runs long, compress LM1–LM5 (which are recall) and protect LM10–LM13.

## Modules

| LM | Module | Hours | Focus |
| --- | --- | --- | --- |
| 01 | [Fixed-Income Instrument Features](lm-01-fixed-income-instrument-features.md) | 3 | Bond features, indentures, and covenants. Vocabulary for all 19 modules. |
| 02 | [Fixed-Income Cash Flows and Types](lm-02-fixed-income-cash-flows-and-types.md) | 3 | Cash flow structures and **contingency provisions** — who holds the option. |
| 03 | [Fixed-Income Issuance and Trading](lm-03-fixed-income-issuance-and-trading.md) | 3 | Markets, issuance, trading, and why bond liquidity is structurally low. |
| 04 | [Fixed-Income Markets for Corporate Issuers](lm-04-fixed-income-markets-for-corporate-issuers.md) | 4 | Short-term funding and **repos**; investment grade vs high yield. |
| 05 | [Fixed-Income Markets for Government Issuers](lm-05-fixed-income-markets-for-government-issuers.md) | 3 | Sovereign, non-sovereign, and supranational issuers. Short module. |
| 06 | [Fixed-Income Bond Valuation: Prices and Yields](lm-06-fixed-income-bond-valuation-prices-and-yields.md) | 6 | **Bond pricing** and the five price-yield relationships. Calculator-heavy. |
| 07 | [Yield and Yield Spread Measures for Fixed-Rate Bonds](lm-07-yield-and-yield-spread-measures-for-fixed-rate-bonds.md) | 5 | Periodicity conversion; YTM, YTC, YTW; **G-, Z-, and option-adjusted spreads**. |
| 08 | [Yield and Yield Spread Measures for Floating-Rate Instruments](lm-08-yield-and-yield-spread-measures-for-floating-rate-instrument.md) | 4 | Discount margin for FRNs; **money market yield conventions**. |
| 09 | [The Term Structure of Interest Rates: Spot, Par, and Forward Curves](lm-09-the-term-structure-of-interest-rates-spot-par-and-forward-cu.md) | 6 | **Spot, par, and forward curves.** No-arbitrage forward rates. |
| 10 | [Interest Rate Risk and Return](lm-10-interest-rate-risk-and-return.md) | 5 | Sources of return and the **duration gap** — the topic's conceptual centrepiece. |
| 11 | [Yield-Based Bond Duration Measures and Properties](lm-11-yield-based-bond-duration-measures-and-properties.md) | 5 | **Modified duration**, money duration, PVBP. Heavy calculation. |
| 12 | [Yield-Based Bond Convexity and Portfolio Properties](lm-12-yield-based-bond-convexity-and-portfolio-properties.md) | 5 | **Convexity** and the duration-plus-convexity price estimate. |
| 13 | [Curve-Based and Empirical Fixed-Income Risk Measures](lm-13-curve-based-and-empirical-fixed-income-risk-measures.md) | 5 | **Effective duration** for option-embedded bonds; key rate duration. |
| 14 | [Credit Risk](lm-14-credit-risk.md) | 4 | Credit risk: PD, LGD, expected loss, ratings and their limits. |
| 15 | [Credit Analysis for Government Issuers](lm-15-credit-analysis-for-government-issuers.md) | 3 | Sovereign credit analysis. Short module. |
| 16 | [Credit Analysis for Corporate Issuers](lm-16-credit-analysis-for-corporate-issuers.md) | 5 | **Corporate credit ratios** and the adjustments that matter. |
| 17 | [Fixed-Income Securitization](lm-17-fixed-income-securitization.md) | 3 | Securitisation structure, SPEs, and bankruptcy remoteness. |
| 18 | [Asset-Backed Security (ABS) Instrument and Market Features](lm-18-asset-backed-security-abs-instrument-and-market-features.md) | 4 | Covered bonds, non-mortgage ABS, and CDOs. |
| 19 | [Mortgage-Backed Security (MBS) Instrument and Market Features](lm-19-mortgage-backed-security-mbs-instrument-and-market-features.md) | 4 | **Prepayment risk**, CMO time tranching, and CMBS. |

## The formulas this topic lives on

Six things from this topic must be automatic.

```
1. Bond pricing on the BA II Plus, with correct periodicity  (N×2, I/Y÷2, PMT÷2, double the I/Y)
2. Forward rates:  (1 + z_A)^A × (1 + F(A,B))^B = (1 + z_(A+B))^(A+B)
3. ModDur = MacDur/(1+r);  %ΔP ≈ −ModDur × ΔY
4. %ΔP ≈ (−ModDur × ΔY) + (½ × Convexity × ΔY²)
5. EffDur = (PV− − PV+)/(2 × ΔCurve × PV0)   — for anything with an embedded option
6. Expected loss = PD × LGD × Exposure
```

Plus three relationships that decide questions on their own:
- **MacDur > horizon → price risk dominates → rising rates hurt** (LM10)
- **Callable: OAS = Z-spread − option cost, so OAS < Z-spread** (LM7)
- **Rates fall → contraction risk; rates rise → extension risk** (LM19)

## Topic wrap-up

Before you tick this topic complete and move to Derivatives:

- [ ] All 19 modules ticked, with their **Done when** lists genuinely cleared
- [ ] I can price a bond and solve for YTM in under 30 seconds each, with correct periodicity
- [ ] I can compute a forward rate from two spot rates, including the B-th root
- [ ] I can state the duration gap relationship in all three cases, with the right direction
- [ ] I can apply the duration-plus-convexity estimate without forgetting the ½ or the square
- [ ] I can say why effective duration is required for a callable bond or an MBS
- [ ] I can compute expected loss and the main credit ratios, with the standard adjustments
- [ ] I can explain contraction and extension risk and why they produce negative convexity
- [ ] I have completed **120+ Fixed Income questions**, logged in `trackers/weak-areas.md`

**Day 90 checkpoint — the end of Month 3 and the largest block in the plan.** You are now past FSA,
QM's first half, Corporate Issuers, Equity, Portfolio Management, and Fixed Income: roughly
**60% of the exam's weight**. Take the Month 3 review day seriously, and run a 60-question mixed
set across all six topics before starting Derivatives.

---

[← Master study plan](../../study-plan/master-plan.md)  ·  [All topics](../)  ·  [Progress tracker](../../../trackers/progress-tracker.md)
