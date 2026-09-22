# QM · LM06 — Statistical Distributions for Financial Asset Prices and Returns

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 14 |
| **Prerequisites** | LM5 (mean, variance, covariance). Studied in Month 5 — the assets and portfolios now have meaning. |
| **Where it shows up** | 2–3 questions. The normal distribution, lognormal prices, and Bayes are all reliable. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate, interpret, and evaluate unconditional expected values for mean, variance, and covariance
- calculate, interpret, and evaluate the principal moments of key statistical distributions used in finance
- calculate, interpret, and evaluate conditional expectations, variances, and covariances
- formulate investment problems through Bayesian updating

---

## Core concepts

### Probability vocabulary, precisely

| Term | Meaning |
| --- | --- |
| **Random variable** | A quantity whose outcome is uncertain |
| **Outcome** | One possible realisation |
| **Event** | A set of one or more outcomes |
| **Mutually exclusive** | Cannot both occur |
| **Exhaustive** | Cover every possibility (probabilities sum to 1) |
| **Independent** | `P(A\|B) = P(A)` — knowing B tells you nothing about A |
| **Unconditional (marginal) probability** | `P(A)` — the probability of A, full stop |
| **Conditional probability** | `P(A\|B)` — the probability of A **given that** B has occurred |
| **Joint probability** | `P(AB)` — the probability that both occur |

The two rules everything is built from:

```
Multiplication rule:  P(AB) = P(A|B) × P(B)
Addition rule:        P(A or B) = P(A) + P(B) − P(AB)

If independent:       P(AB) = P(A) × P(B)
If mutually exclusive: P(AB) = 0, so P(A or B) = P(A) + P(B)
```

> **Trap:** mutually exclusive and independent are **not** the same thing — they are near opposites.
> If two events are mutually exclusive and both have positive probability, then knowing one occurred
> tells you the other did **not**, so they are maximally *dependent*.

### The total probability rule — unconditional from conditional

An unconditional expected value is the probability-weighted average of the conditional ones across
a mutually exclusive and exhaustive set of scenarios:

```
P(A) = Σ P(A | Si) × P(Si)

E(X) = Σ E(X | Si) × P(Si)
```

**Example.** A stock returns 25% in an expansion (probability 0.30), 8% in normal conditions (0.50),
and −15% in a recession (0.20).

```
E(R) = 0.30(25%) + 0.50(8%) + 0.20(−15%) = 7.5% + 4.0% − 3.0% = 8.5%
```

**Variance** from the same scenarios:

```
σ² = Σ P(Si) × [R_i − E(R)]²
   = 0.30(25 − 8.5)² + 0.50(8 − 8.5)² + 0.20(−15 − 8.5)²
   = 0.30(272.25) + 0.50(0.25) + 0.20(552.25)
   = 81.675 + 0.125 + 110.45 = 192.25
σ = √192.25 = 13.87%
```

**Covariance** between two assets across scenarios:

```
Cov(A,B) = Σ P(Si) × [R_A,i − E(R_A)] × [R_B,i − E(R_B)]
```

### Bayes' formula — updating on new information

This is the module's conceptual centrepiece, and it is directly examinable.

```
P(Event | Information) = [ P(Information | Event) × P(Event) ] / P(Information)
```

Read as: **posterior = (likelihood × prior) / evidence.** You start with a prior belief, observe
something, and revise.

The denominator is almost always computed with the total probability rule:

```
P(Information) = P(Info | Event) × P(Event) + P(Info | not Event) × P(not Event)
```

**Worked example.** 20% of firms in a sector beat earnings estimates. Of those that beat, 70% had
raised guidance beforehand. Of those that missed, 25% had raised guidance. A firm has raised
guidance. What is the probability it beats?

```
P(Beat) = 0.20            P(Guidance | Beat) = 0.70
P(Miss) = 0.80            P(Guidance | Miss) = 0.25

P(Guidance) = 0.70(0.20) + 0.25(0.80) = 0.14 + 0.20 = 0.34

P(Beat | Guidance) = 0.14 / 0.34 = 41.2%
```

The prior of 20% rose to 41.2% — a real update, but far below the 70% that intuition suggests. That
gap is **base rate neglect**, and it is one of the most robust findings in behavioural research.
Most people answer near 70% because they focus on the likelihood and ignore the prior.

### Discrete distributions

**Uniform (discrete).** Every outcome equally likely. `P(x) = 1/n`.

**Bernoulli.** A single trial with two outcomes: success with probability `p`, failure with `1 − p`.
Mean `p`, variance `p(1 − p)`.

**Binomial.** The number of successes in `n` independent Bernoulli trials.

```
P(X = x) = C(n,x) × p^x × (1 − p)^(n−x)     where C(n,x) = n! / [x!(n − x)!]

Mean = np          Variance = np(1 − p)
```

Requires: fixed `n`, only two outcomes per trial, constant `p`, and **independent** trials.

### Continuous distributions

**Continuous uniform** over [a, b]:

```
P(x1 ≤ X ≤ x2) = (x2 − x1) / (b − a)
Mean = (a + b)/2      Variance = (b − a)²/12
```

**Normal.** The workhorse. Fully described by just two parameters, **μ and σ²**.

Properties: symmetric (skew = 0), kurtosis 3 (excess kurtosis 0), bell-shaped, tails extend to
±∞, and — critically — **a linear combination of normally distributed variables is itself normally
distributed**. That last property is why portfolio theory can assume normality and stay tractable.

```
Approximately:  68% within ±1σ     95% within ±2σ (precisely 1.96)     99% within ±3σ (precisely 2.58)
```

**Standard normal (Z).** Mean 0, standard deviation 1.

```
Z = (X − μ) / σ
```

Standardising lets you use one table for every normal distribution. Learn the critical values cold:
**1.65 (90%), 1.96 (95%), 2.58 (99%)** — two-tailed.

**Lognormal.** X is lognormal if `ln(X)` is normal.

| Property | Consequence |
| --- | --- |
| Bounded below by **zero** | Prices cannot go negative — this is why lognormal fits **prices** |
| **Right-skewed** | Unlimited upside, limited downside |

> **The distinction that is tested every time:** **continuously compounded returns are modelled as
> normal; asset prices are then lognormal.** If `r = ln(P1/P0)` is normal, then `P1 = P0 × e^r` is
> lognormal. The logic: a return can be any real number, but a price cannot fall below zero.

**Student's t.** Symmetric and bell-shaped like the normal, but with **fatter tails**, governed by
degrees of freedom. As `df → ∞` it converges to the normal. Used when the population variance is
unknown and the sample is small — which in practice is most of the time (LM7).

**Chi-square** — for tests about a single variance. Asymmetric and bounded below at zero.
**F-distribution** — the ratio of two chi-square variables; for comparing two variances and for the
ANOVA F-test in regression (LM10).

### Conditional expectations and variances

```
E(X | S) = Σ x × P(x | S)
```

The expected value **given** that scenario S has occurred. Conditional expectations are how scenario
analysis works: you condition on an economic state and recompute.

A tree diagram is the standard tool — each branch is a conditional probability, each path's joint
probability is the product along the branch, and the unconditional expectation is the
probability-weighted sum across all paths.

> Practical note: conditional **variance** can be very different from unconditional variance.
> Conditioning on "a recession has begun" typically raises both the conditional variance of returns
> *and* the conditional correlations between assets — which is precisely why diversification
> disappoints exactly when it is needed. This point returns in Portfolio Management.

---

## Formulas to know cold

```
PROBABILITY RULES
  P(AB) = P(A|B) × P(B)                    [multiplication]
  P(A or B) = P(A) + P(B) − P(AB)          [addition]
  Independent:  P(AB) = P(A)P(B)
  Total probability:  P(A) = Σ P(A|Si) P(Si)

EXPECTED VALUE, VARIANCE, COVARIANCE (from scenarios)
  E(X)     = Σ P(Si) × Xi
  Var(X)   = Σ P(Si) × [Xi − E(X)]²
  Cov(A,B) = Σ P(Si) × [RA,i − E(RA)] × [RB,i − E(RB)]

BAYES' FORMULA
  P(Event | Info) = P(Info | Event) × P(Event) / P(Info)
  P(Info) = P(Info|Event)P(Event) + P(Info|not Event)P(not Event)

BINOMIAL
  P(X=x) = C(n,x) p^x (1−p)^(n−x),   C(n,x) = n!/[x!(n−x)!]
  Mean = np      Variance = np(1−p)

CONTINUOUS UNIFORM on [a,b]
  P(x1 ≤ X ≤ x2) = (x2 − x1)/(b − a)
  Mean = (a+b)/2      Variance = (b−a)²/12

NORMAL
  Z = (X − μ)/σ
  Critical values (two-tailed):  90% → 1.65 | 95% → 1.96 | 99% → 2.58
  Roughly: 68% within ±1σ, 95% within ±2σ, 99% within ±3σ

LOGNORMAL
  X lognormal  ⟺  ln(X) normal.  Bounded at 0, right-skewed.
  Continuously compounded returns → NORMAL;  prices → LOGNORMAL
```

---

## Exam traps

> **Trap 1 — Mutually exclusive vs. independent.** Not the same. Mutually exclusive events with
> positive probability are maximally **dependent**: if one happens, the other cannot.

> **Trap 2 — Base rate neglect in Bayes.** The posterior is driven by the **prior** as much as by the
> likelihood. A rare event with strong evidence is often still unlikely. Compute; do not intuit.

> **Trap 3 — Normal vs. lognormal.** **Returns** (continuously compounded) are modelled as normal;
> **prices** are lognormal. Reversing this is the single most common error in the module.

> **Trap 4 — Variance from scenarios uses squared deviations from the *expected* value**, weighted by
> probability — not the sample formula with n − 1.

> **Trap 5 — Binomial independence.** The binomial requires **independent** trials with constant p.
> Sampling without replacement from a small population violates both.

> **Trap 6 — Critical values.** 1.96 is **95% two-tailed**; 1.65 is 90% two-tailed (and 95%
> one-tailed). Mixing them up is a standing source of errors through LM7 and LM10.

> **Trap 7 — Conditional variance equals unconditional variance.** It usually does not. Conditioning
> on a stressed state raises both variances and correlations.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A stock returns 30% in a boom (p = 0.25), 10% in normal conditions (p = 0.55), and −20% in a recession (p = 0.20). Compute the expected return and standard deviation.

<details><summary>Answer</summary>

E(R) = 0.25(30) + 0.55(10) + 0.20(−20) = 7.5 + 5.5 − 4.0 = **9.0%**

Variance:
0.25(30 − 9)² = 0.25(441) = 110.25
0.55(10 − 9)² = 0.55(1) = 0.55
0.20(−20 − 9)² = 0.20(841) = 168.20
σ² = **279.0**

σ = √279.0 = **16.70%**

</details>

**2.** 30% of companies in a sector are 'high quality'. 80% of high-quality companies have an ROE above 15%; only 20% of the rest do. A company has ROE above 15%. What is the probability it is high quality?

<details><summary>Answer</summary>

```
P(HQ) = 0.30                P(ROE>15 | HQ)     = 0.80
P(not HQ) = 0.70            P(ROE>15 | not HQ) = 0.20

P(ROE>15) = 0.80(0.30) + 0.20(0.70) = 0.24 + 0.14 = 0.38

P(HQ | ROE>15) = 0.24 / 0.38 = 63.2%
```
The prior of 30% rises to **63.2%**. Notice it is well below the 80% likelihood — because high-quality companies are only 30% of the population to begin with. Ignoring that prior is base rate neglect.

</details>

**3.** Why are asset prices modelled as lognormal while continuously compounded returns are modelled as normal?

<details><summary>Answer</summary>

A **price cannot be negative**. The normal distribution extends to −∞, so it cannot describe a price — it would assign positive probability to impossible outcomes.

A **continuously compounded return** can take any real value: r = ln(P1/P0) goes to −∞ as the price approaches zero, and is unbounded above. So the normal is a natural fit.

The two are linked: if `r = ln(P1/P0)` is normal, then `P1 = P0 × e^r` is **lognormal** by definition — bounded below at zero and right-skewed, with unlimited upside and limited downside. That shape matches observed price behaviour, which is why it underpins the Black–Scholes framework in Derivatives.

</details>

**4.** A portfolio manager beats the benchmark with probability 0.55 in any quarter, independently. What is the probability of beating it in exactly 3 of 4 quarters? And in at least 3?

<details><summary>Answer</summary>

Binomial with n = 4, p = 0.55.

**Exactly 3:** C(4,3) × 0.55³ × 0.45¹ = 4 × 0.166375 × 0.45 = **0.2995**

**Exactly 4:** C(4,4) × 0.55⁴ = 1 × 0.09150 = **0.0915**

**At least 3:** 0.2995 + 0.0915 = **0.3910**

Worth noting: a manager with a genuine 55% edge still fails to beat the benchmark in 3 of 4 quarters about 61% of the time. Short-run track records contain very little information about skill.

</details>

**5.** Returns are normally distributed with mean 9% and standard deviation 14%. What is the probability of a return below −5%?

<details><summary>Answer</summary>

Z = (−5 − 9)/14 = −14/14 = **−1.00**

P(Z < −1.00) ≈ **15.87%**

Using the rule of thumb: about 68% of observations fall within ±1σ, leaving 32% in the two tails, so roughly 16% in each. The exact table value is 0.1587.

Caveat worth stating: real return distributions are **leptokurtic** (LM5), so the true probability of a loss this size is typically somewhat *higher* than the normal model says.

</details>

**6.** Distinguish mutually exclusive from independent events with a concrete example.

<details><summary>Answer</summary>

**Mutually exclusive:** a company's earnings cannot both beat and miss estimates in the same quarter. P(beat and miss) = 0. Knowing it beat tells you with **certainty** it did not miss — these events are maximally *dependent*.

**Independent:** the outcome of a fair coin flip and tomorrow's return on a stock. P(heads | stock rises) = P(heads) = 0.5. Knowing one tells you **nothing** about the other, and P(both) = P(A)P(B).

The two concepts are close to opposites. Two events with positive probability cannot be both mutually exclusive and independent.

</details>

**7.** Why does conditioning on a recession typically raise both conditional variance and conditional correlations, and why does that matter?

<details><summary>Answer</summary>

In stressed markets, common factors — liquidity, risk appetite, funding conditions — come to dominate asset-specific drivers. Assets that normally move for idiosyncratic reasons all start responding to the same systemic pressure, so they move **together** and they move **more**.

Why it matters: portfolio risk estimates built on unconditional (full-sample) correlations **understate** risk in exactly the states where losses matter most. Diversification benefits computed in calm periods partly evaporate in a crisis — the correlations you relied on are not the ones you get.

This is the statistical basis for stress-testing with conditional rather than unconditional inputs, and it recurs throughout Portfolio Management and Alternative Investments.

</details>

---

## Done when

- [ ] I can apply the multiplication, addition, and total probability rules and distinguish independence from mutual exclusivity
- [ ] I can compute expected value, variance, and covariance from a scenario table
- [ ] I can apply Bayes' formula and explain base rate neglect
- [ ] I can compute binomial probabilities and state the distribution's requirements
- [ ] I can standardise to Z and recall 1.65 / 1.96 / 2.58 cold
- [ ] I can explain precisely why returns are normal and prices are lognormal
- [ ] I can explain why conditional correlations rise in stress and what that does to risk estimates
- [ ] I answered the self-check cold, several days after first study

---

← [LM05 Statistical Characteristics of Asset Returns](lm-05-statistical-characteristics-of-asset-returns.md)  ·  [Topic index](README.md)  ·  [LM07 Estimation and Hypothesis Testing](lm-07-estimation-and-hypothesis-testing.md) →
