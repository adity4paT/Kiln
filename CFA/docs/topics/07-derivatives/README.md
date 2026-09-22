# Derivatives

*The topic where no-arbitrage does all the work, and no forecast is ever required.*

| | |
| --- | --- |
| **Exam weight** | 5-8% — roughly 9–14 of 180 questions |
| **Study block** | Month 4, days 91–105 |
| **Budget** | 15 days · 60 hours |
| **Modules** | 10 |
| **Position in study order** | 7 of 10 |

## Why this topic sits here

Derivatives is studied **seventh**, at the start of Month 4, and it sits directly after Fixed Income
for a reason: **forwards, futures, and swaps are all no-arbitrage discounting problems**, and the
term structure machinery from Fixed Income LM9 is what prices them.

It also needs **QM LM4** (cash flow additivity and no-arbitrage), which is where the replication
argument is first introduced. If that module is shaky, LM4 here will be very hard.

At **5–8%** this is the lightest topic in the plan apart from the smaller descriptive blocks, and
its 60 hours reflect that. But do not treat it as optional: it has the highest **concept density**
of any topic. Almost every module reduces to a single idea —

> **Two portfolios with identical future cash flows must have the same price today.**

Understand that, and forwards, futures, swaps, put-call parity, and the binomial model are all the
same argument applied to different instruments. Miss it, and you are memorising six unrelated
formula sets.

**The structure:** LM1–LM3 are vocabulary and uses. **LM4 is the conceptual hinge** — do not skip it.
LM5–LM7 apply no-arbitrage to forward commitments. LM8–LM10 apply it to options.

> **LM4 is the module that makes the rest cheap.** Seven hours on arbitrage, replication, and cost of
> carry turns LM5 through LM10 from six sets of formulas into six applications of one idea. Do not
> economise on it.

## Modules

| LM | Module | Hours | Focus |
| --- | --- | --- | --- |
| 01 | [Derivative Instrument and Derivative Market Features](lm-01-derivative-instrument-and-derivative-market-features.md) | 4 | Definitions, the two families, exchange-traded vs OTC, clearinghouse mechanics. |
| 02 | [Forward Commitment and Contingent Claim Features and Instruments](lm-02-forward-commitment-and-contingent-claim-features-and-instrum.md) | 7 | **Option payoffs and profits.** Forwards, futures, swaps, options, CDS. |
| 03 | [Derivative Benefits, Risks, and Issuer and Investor Uses](lm-03-derivative-benefits-risks-and-issuer-and-investor-uses.md) | 4 | Benefits, risks, and how issuers and investors actually use derivatives. |
| 04 | [Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives](lm-04-arbitrage-replication-and-the-cost-of-carry-in-pricing-deriv.md) | 7 | **The conceptual hinge.** Arbitrage, replication, cost of carry, contango/backwardation. |
| 05 | [Pricing and Valuation of Forward Contracts and for an Underlying with Varying Maturities](lm-05-pricing-and-valuation-of-forward-contracts-and-for-an-underl.md) | 8 | **Price vs value.** Forward pricing and valuation; FRAs. Largest module. |
| 06 | [Pricing and Valuation of Futures Contracts](lm-06-pricing-and-valuation-of-futures-contracts.md) | 5 | Futures vs forwards: daily settlement, the value reset, convergence, basis. |
| 07 | [Pricing and Valuation of Interest Rate and Other Swaps](lm-07-pricing-and-valuation-of-interest-rate-and-other-swaps.md) | 6 | Swaps as a series of forwards; the swap rate as the par rate. |
| 08 | [Pricing and Valuation of Options](lm-08-pricing-and-valuation-of-options.md) | 7 | **The six option factors.** Exercise value, time value, moneyness. |
| 09 | [Option Replication Using Put-Call Parity](lm-09-option-replication-using-put-call-parity.md) | 6 | **Put-call parity** and the four synthetic positions. |
| 10 | [Valuing a Derivative Using a One-Period Binomial Model](lm-10-valuing-a-derivative-using-a-one-period-binomial-model.md) | 6 | **The binomial model** and risk-neutral valuation. The closing idea. |

## The formulas this topic lives on

Five things from this topic must be automatic.

```
1. F0 = S0(1+r)^T + FV(costs) − FV(benefits)         — cost of carry
2. Vt(long forward) = St − F0/(1+r)^(T−t)            — value during the life
3. Option payoffs and profits, all four positions, plus the breakevens
4. c0 + X/(1+r)^T = p0 + S0                          — put-call parity
5. π = [(1+r) − d]/(u − d);  c0 = [πc+ + (1−π)c−]/(1+r)
```

Plus the **six-factor table** (LM8), which must be reproducible from memory, and the one sentence
that generates the whole topic: **two portfolios with identical future cash flows must have the
same price today.**

## Topic wrap-up

Before you tick this topic complete and move to Alternative Investments:

- [ ] All 10 modules ticked, with their **Done when** lists genuinely cleared
- [ ] I can construct a cash-and-carry arbitrage in both directions and explain why F0 ≠ E(ST)
- [ ] I can compute a forward price with income and value the position mid-life
- [ ] I can compute payoff, profit, and breakeven for all four option positions
- [ ] I can reproduce the six-factor table and explain why volatility raises both calls and puts
- [ ] I can write put-call parity correctly and derive all four synthetics from it
- [ ] I can value an option on a one-period binomial tree in under two minutes
- [ ] I can explain risk-neutral valuation without saying "investors are risk neutral"
- [ ] I have completed **70+ Derivatives questions**, logged in `trackers/weak-areas.md`

**Day 105 checkpoint.** If you can state the no-arbitrage principle in one sentence and apply it to
a forward, a swap, and an option, this topic is done. If you are still memorising six separate
formula sets, go back to LM4 — the problem is there, not in the later modules.

---

[← Master study plan](../../study-plan/master-plan.md)  ·  [All topics](../)  ·  [Progress tracker](../../../trackers/progress-tracker.md)
