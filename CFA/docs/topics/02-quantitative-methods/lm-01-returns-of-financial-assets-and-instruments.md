# QM · LM01 — Returns of Financial Assets and Instruments

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | Basic algebra. No prior finance assumed. |
| **Where it shows up** | 1–2 questions directly, but the vocabulary underpins Equity, Fixed Income, and Portfolio Management. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe, compare, and interpret returns
- describe, compare, and interpret required rates of return, risk-free rates, risk premia, and inflation

---

## Core concepts

### Returns — the vocabulary you will use for the next five months

Get these distinctions precise now. Almost every later topic assumes them.

| Term | Meaning |
| --- | --- |
| **Holding period return (HPR)** | Total return over one period: price change plus income, as a fraction of the starting price |
| **Realised return** | What actually happened. Backward-looking, observable |
| **Expected return** | The probability-weighted mean of possible outcomes. Forward-looking, unobservable |
| **Required return** | The **minimum** return an investor demands to take the risk. A hurdle, not a forecast |
| **Nominal return** | Return in money terms, before adjusting for inflation |
| **Real return** | Return in purchasing-power terms, after inflation |
| **Gross return** | Before management fees and expenses (but usually after trading costs) |
| **Net return** | After all fees and expenses. What the investor actually keeps |
| **Pre-tax / after-tax return** | Before / after the investor's tax liability |
| **Leveraged return** | Return on the investor's own capital when part of the position is financed with borrowing |

Two pairings the exam tests directly:

- **Required vs. expected.** If the *expected* return exceeds the *required* return, the asset is
  attractive — it is priced to deliver more than the risk demands. If expected < required, it is
  overpriced. This comparison is the engine of every valuation model you will meet.
- **Gross vs. net.** The difference is fees, and over long horizons the gap is enormous. A 2% annual
  fee on a portfolio compounding at 8% gross consumes roughly a third of the terminal wealth over
  30 years.

### Building the required return

The required return is a **stack**:

```
Required return = Real risk-free rate
                + Expected inflation
                + Risk premium
```

Equivalently, since the nominal risk-free rate already contains the first two:

```
Required return = Nominal risk-free rate + Risk premium
```

Each layer, precisely:

- **Real risk-free rate** — the compensation for deferring consumption, with no default risk and no
  inflation. This is a *theoretical* construct; it cannot be observed directly. It is driven by
  society's time preference and the productivity of capital.
- **Expected inflation premium** — compensation for the expected erosion of purchasing power over
  the holding period. Note: **expected**, not realised.
- **Nominal risk-free rate** — what you actually observe (a short-term government bill).
  Approximately the real rate plus expected inflation; exactly, `(1+r_real)(1+π) − 1`.
- **Risk premium** — the additional return demanded for bearing risk. Decomposes into:

| Premium | Compensates for |
| --- | --- |
| **Default risk premium** | The possibility the borrower fails to pay |
| **Liquidity premium** | The cost and difficulty of converting to cash quickly at fair value |
| **Maturity risk premium** | Greater price sensitivity to interest rate changes at longer maturities |
| **Equity risk premium** | Bearing the residual, unprotected claim of an equity holder |

> **A no-arbitrage check you can apply constantly:** two assets with identical risk must offer the
> same required return. If they do not, one is mispriced. This intuition drives Fixed Income spreads
> and Derivatives pricing alike.

### Real vs. nominal — the Fisher relation

```
(1 + Nominal) = (1 + Real) × (1 + Inflation)

Exactly:      Real = (1 + Nominal) / (1 + Inflation) − 1
Approximately: Real ≈ Nominal − Inflation
```

The approximation is fine at low rates and breaks down badly at high ones. At 3% nominal and 2%
inflation the approximation gives 1.0% against an exact 0.98% — immaterial. At 40% nominal and 35%
inflation it gives 5% against an exact **3.70%** — a quarter of the answer wrong.

> **Trap:** the exam picks high-inflation numbers precisely to punish the approximation. Use the
> exact form unless the question says otherwise.

### Risk aversion, and what it implies

Investors are assumed **risk averse**: for a given expected return they prefer less risk, and they
will only accept more risk if compensated with a higher expected return. Three logical consequences:

1. **The risk premium is positive.** Risky assets must offer more than the risk-free rate, or nobody
   would hold them.
2. **Required return rises with risk.** This is the security market line (Portfolio Management LM2).
3. **Diversification has value.** If risk can be reduced without sacrificing expected return, a
   risk-averse investor takes that trade every time. This is the entire basis of portfolio theory.

Risk aversion is a *preference*, not a fact about the world — but it is the assumption that makes
finance work, and the exam treats it as given.

### What moves the risk-free rate

Level I expects you to link the components to observable conditions:

- **Higher expected inflation** raises the nominal risk-free rate one-for-one (approximately).
- **Stronger expected economic growth** raises the real rate — capital is more productive, so it
  commands more.
- **Central bank policy** moves short rates directly and long rates through expectations.
- **Greater uncertainty** widens risk premia without necessarily moving the risk-free rate — and in
  a flight to quality it can push the risk-free rate *down* while every risky yield rises.

That last case is worth holding onto: in a crisis, government yields fall while corporate spreads
widen. Both happen because the risk premium, not the risk-free rate, is doing the moving.

---

## Formulas to know cold

```
Holding period return:   HPR = (P1 − P0 + Income) / P0
                         HPR = (P1 + D1) / P0 − 1

Required return = Real risk-free rate + Expected inflation + Risk premium
                = Nominal risk-free rate + Risk premium

Fisher relation (exact):
    (1 + Nominal) = (1 + Real) × (1 + Inflation)
    Real = (1 + Nominal) / (1 + Inflation) − 1

Fisher relation (approximation, low rates only):
    Real ≈ Nominal − Inflation

Risk premium components:
    default risk + liquidity + maturity risk  (+ equity risk premium for equities)
```

---

## Exam traps

> **Trap 1 — Required vs. expected return.** **Required** is the hurdle the risk demands;
> **expected** is what you forecast. The asset is attractive when expected > required.

> **Trap 2 — The Fisher approximation at high rates.** Use `(1+n)/(1+π) − 1`. Subtraction is only
> acceptable at low rates, and the exam deliberately supplies high ones.

> **Trap 3 — Expected vs. realised inflation.** The premium embedded in rates is for **expected**
> inflation. Realised inflation differing from expectations is precisely what creates unexpected
> real gains and losses on nominal bonds.

> **Trap 4 — Gross vs. net return.** Net is after **all** fees. Comparing one manager's gross return
> to another's net return is meaningless and is a standard trick.

> **Trap 5 — Assuming the risk-free rate and risk premia move together.** In a flight to quality the
> risk-free rate **falls** while risk premia **widen**.

> **Trap 6 — Treating the real risk-free rate as observable.** It is a theoretical construct. What
> you observe is a nominal short-term government rate.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** An investor buys a share at 80, receives a dividend of 3.20, and sells at 86.50. Compute the holding period return.

<details><summary>Answer</summary>

HPR = (86.50 − 80 + 3.20) / 80 = 9.70 / 80 = **0.12125 = 12.13%**

Note that income and capital gain are both in the numerator — HPR is a **total** return measure.

</details>

**2.** The nominal return is 24% and inflation is 18%. Compute the real return exactly and by approximation. Comment on the difference.

<details><summary>Answer</summary>

Exact: (1.24 / 1.18) − 1 = 1.05085 − 1 = **5.085%**
Approximate: 24% − 18% = **6%**

The approximation overstates by about 0.9 percentage points — nearly 18% of the true answer. At these inflation levels the approximation is not acceptable. Use the exact form whenever inflation is above a few percent.

</details>

**3.** Distinguish the required return from the expected return, and say what it means when they differ.

<details><summary>Answer</summary>

**Required return** is the minimum an investor demands given the asset's risk — a hurdle derived from the risk-free rate plus appropriate risk premia. **Expected return** is the probability-weighted mean outcome you forecast for the asset.

If **expected > required**, the asset offers more than its risk demands → it is **undervalued** and attractive.
If **expected < required**, it offers less than the risk demands → **overvalued**.
If they are equal, the asset is fairly priced.

Every valuation model in the curriculum is ultimately a machine for making this comparison.

</details>

**4.** Name the four components of a risk premium and give an example of a security where each dominates.

<details><summary>Answer</summary>

**Default risk premium** — a high-yield corporate bond; the dominant concern is whether the issuer pays.
**Liquidity premium** — a thinly traded private placement or small-cap stock; the concern is exiting at fair value.
**Maturity risk premium** — a 30-year government bond; there is no default risk, but enormous price sensitivity to rate changes.
**Equity risk premium** — a common share; the holder has the residual, unprotected claim after every other claimant.

</details>

**5.** Government bond yields fall sharply while corporate bond yields rise. Explain what is happening in terms of the required return components.

<details><summary>Answer</summary>

A **flight to quality**. Investors are moving out of risky assets and into government securities.

- Demand for governments rises → their prices rise → the **risk-free rate falls**.
- Perceived default and liquidity risk on corporates rises → **risk premia widen** — by more than the risk-free rate fell.

Required return = risk-free + premium. For corporates the premium term dominates, so their required return (and yield) rises even as the risk-free component falls. This is why credit spreads widen most sharply in exactly the periods when government yields are falling.

</details>

**6.** Why does risk aversion imply that diversification has value?

<details><summary>Answer</summary>

A risk-averse investor prefers less risk at any given expected return. Diversification reduces portfolio risk **without** reducing expected return, because the expected return of a portfolio is the weighted average of component expected returns, while its risk is *less* than the weighted average whenever the components are imperfectly correlated.

That is a strictly favourable trade — the same expected return at lower risk — so a risk-averse investor always takes it. This single observation is the foundation of everything in Portfolio Management.

</details>

---

## Done when

- [ ] I can define and distinguish HPR, realised, expected, and required return
- [ ] I can build the required return from real risk-free rate, inflation, and risk premia
- [ ] I can apply the exact Fisher relation and say when the approximation fails
- [ ] I can name the four risk premium components with an example of each
- [ ] I can explain why a flight to quality moves the risk-free rate and risk premia in opposite directions
- [ ] I can state what risk aversion implies for the risk premium and for diversification
- [ ] I answered the self-check cold, several days after first study

---

[Topic index](README.md)  ·  [LM02 Types of Financial Returns](lm-02-types-of-financial-returns.md) →
