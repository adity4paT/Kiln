# Portfolio Management

*Where the whole curriculum stops being about securities and starts being about portfolios.*

| | |
| --- | --- |
| **Exam weight** | 8-12% — roughly 14–21 of 180 questions |
| **Study block** | Month 3, days 61–70 |
| **Budget** | 10 days · 40 hours |
| **Modules** | 6 |
| **Position in study order** | 5 of 10 |

## Why this topic sits here

Portfolio Management is studied **fifth**, at the start of Month 3, and it sits at a deliberate
hinge point.

Everything before it — FSA, QM, Corporate Issuers, Equity — analyses **individual securities and
companies**. This topic changes the unit of analysis to the **portfolio**, and with it the definition
of risk: what matters is no longer a security's own volatility but its **contribution** to the
portfolio, which is a statement about covariance.

It also sits immediately before Fixed Income for a reason. LM1 and LM2 establish the risk framework
— systematic versus diversifiable, the efficient frontier, CAPM — that Fixed Income's duration and
credit work then applies to bonds. And it consolidates CAPM, which you first met in Equity LM12.

**Note the deliberate double coverage.** QM LM8 (Month 5) covers the same portfolio mathematics from
the quantitative side. That is not redundancy — it is the **spacing schedule** working as designed.
You meet the efficient frontier here in Month 3, then again in Month 5 as consolidation, which is
exactly the retrieval interval that builds durable recall.

At **8–12%** this is the third-heaviest topic on the exam, and at 40 hours it has the best
weight-to-hours ratio in the entire plan.

## Modules

| LM | Module | Hours | Focus |
| --- | --- | --- | --- |
| 01 | [Portfolio Risk and Return: Part I](lm-01-portfolio-risk-and-return-part-i.md) | 9 | Portfolio math, correlation, the efficient frontier, utility. Heavy calculation. |
| 02 | [Portfolio Risk and Return: Part II](lm-02-portfolio-risk-and-return-part-ii.md) | 11 | **The core module.** CAPM, SML, CML, and the four performance ratios. |
| 03 | [Portfolio Management: An Overview](lm-03-portfolio-management-an-overview.md) | 5 | Investor types, DB vs DC, pooled vehicles. Pure recall. |
| 04 | [Basics of Portfolio Planning and Construction](lm-04-basics-of-portfolio-planning-and-construction.md) | 7 | **The IPS**, willingness vs ability, the five constraints. |
| 05 | [The Behavioral Biases of Individuals](lm-05-the-behavioral-biases-of-individuals.md) | 4 | Cognitive vs emotional biases. Classification is what is tested. |
| 06 | [Introduction to Risk Management](lm-06-introduction-to-risk-management.md) | 4 | Risk governance, risk budgeting, VaR. Descriptive. |

## The formulas this topic lives on

Five things from this topic must be automatic.

```
1. σp² = w1²σ1² + w2²σ2² + 2w1w2ρ12σ1σ2        — and σp < weighted average whenever ρ < 1
2. CAPM:  E(Ri) = Rf + βi[E(RM) − Rf]           — and the SML's above/below reading
3. βi = Cov(Ri,RM)/Var(RM) = ρ(i,M) σi/σM       — βp IS a weighted average
4. Sharpe = (Rp − Rf)/σp   vs   Treynor = (Rp − Rf)/βp   — know WHICH to use WHEN
5. U = E(R) − ½Aσ²                               — higher A = more risk averse
```

Plus two distinctions that decide questions on their own:
- **CML: total risk (σ), efficient portfolios. SML: systematic risk (β), any asset.**
- **Ability vs willingness to take risk: take the LOWER.**

## Topic wrap-up

Before you tick this topic complete and move to Fixed Income:

- [ ] All 6 modules ticked, with their **Done when** lists genuinely cleared
- [ ] I can compute portfolio standard deviation for two assets without hesitating over the formula
- [ ] I can state the CML/SML distinction on axis, domain, and slope
- [ ] I can compute all four performance measures and choose correctly between Sharpe and Treynor
- [ ] I can explain why non-systematic risk earns no premium, from first principles
- [ ] I can list the IPS components and the five constraints (L-T-T-L-U) from memory
- [ ] I can classify any described behavioural bias as cognitive or emotional
- [ ] I have completed **60+ Portfolio Management questions**, logged in `trackers/weak-areas.md`

**Day 70 checkpoint.** LM1 and LM2 are 20 of this topic's 40 hours and carry most of its exam
weight. They also return twice more — in QM LM8 (Month 5) and throughout Alternative Investments.
Getting them solid now pays three times.

---

[← Master study plan](../../study-plan/master-plan.md)  ·  [All topics](../)  ·  [Progress tracker](../../../trackers/progress-tracker.md)
