# QM · LM09 — Simulation of Financial Asset Prices and Returns

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 10 |
| **Prerequisites** | LM6 (distributions), LM7 (sampling and resampling). |
| **Where it shows up** | 1–2 questions. Entirely conceptual — no calculations. Know what each method assumes. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe historical simulation and explain how it can be used in investment applications
- describe bootstrap resampling, and explain how it can be used in investment applications
- describe Monte Carlo simulation and explain how it can be used in investment applications

---

## Core concepts

### Why simulate at all

Analytical formulas require assumptions — usually normality, constant volatility, and a tractable
payoff. Simulation is what you use when those assumptions fail:

- The payoff is **path-dependent** (the outcome depends on the whole route, not just the endpoint)
- There are **many interacting random variables** with a complex dependence structure
- You need the **whole distribution** of outcomes, not just a mean and a variance
- The analytical solution simply does not exist

All three methods below produce a **distribution of outcomes** rather than a point estimate. That is
their common value: they replace "the expected value is 8%" with "here is the full range, and here
is the 5th percentile".

### Historical simulation

**What it is.** Re-run the portfolio or strategy over **actual historical returns**, in the order
they occurred, and observe the distribution of results.

| | |
| --- | --- |
| **Assumes** | The past is representative of the future |
| **Keeps** | The real distribution — actual skew, actual fat tails, actual correlations, actual sequences |
| **Requires** | No distributional assumption at all |

**Advantages:**
- Uses **real** data, so the fat tails and skew are genuine rather than assumed
- Preserves the actual **correlation structure** between assets, including how it behaved in stress
- Simple to implement and easy to explain

**Limitations:**
- **Limited by the sample.** You only observe events that actually happened. A crisis not in your
  window is not in your distribution.
- **Assumes the past repeats**, which fails after structural change — a regime shift, a new
  regulatory environment, an instrument with no history.
- **The number of scenarios is fixed** by the length of your data. You cannot generate more.
- Sensitive to the **period chosen** (time-period bias).

**Uses:** Value at Risk, stress testing, strategy backtesting, assessing drawdown behaviour.

### Bootstrap resampling

**What it is.** Draw observations **with replacement** from your historical sample, many times over,
to construct a distribution of whatever statistic you care about.

The key difference from historical simulation: **historical simulation replays the sequence as it
happened; the bootstrap reshuffles it** — drawing repeatedly, with replacement, so the same
observation can appear several times in one resample and not at all in another.

| | |
| --- | --- |
| **Assumes** | Observations are **independent and identically distributed** |
| **Generates** | As many resamples as you like from a fixed dataset |
| **Answers** | "What is the sampling distribution of this statistic?" |

**Advantages:**
- **No distributional assumption** required
- Works when the **analytical standard error is unknown or intractable** — its most common
  professional use
- Generates **unlimited** resamples from a finite dataset
- Naturally produces **confidence intervals** for statistics with no closed-form solution
  (the median, the Sharpe ratio, a maximum drawdown)

**Limitations:**
- Still bounded by the original sample — it cannot create information that was not there
- **Destroys time-series structure.** Because it samples randomly, it breaks autocorrelation,
  volatility clustering, and momentum. For serially dependent financial data this is a real problem,
  and the reason **block bootstrap** methods (resampling contiguous blocks rather than single
  observations) exist.
- The i.i.d. assumption is often violated by financial returns

**Uses:** confidence intervals for complex statistics, standard errors for estimators with no
formula, testing the significance of a backtest result.

### Monte Carlo simulation

**What it is.** **Specify a probability distribution** for each risk factor, then draw random values
from those distributions thousands of times, computing the outcome each time.

| | |
| --- | --- |
| **Assumes** | The distributions you specify are correct |
| **Generates** | Scenarios that have **never occurred** — this is its unique strength |
| **Requires** | Explicit modelling choices for every input |

**The procedure:**

1. Specify the **variables** and the **quantity** to be estimated
2. Specify a **distribution** for each variable, and the **dependence** between them (correlations)
3. Draw a random value for each variable
4. Compute the outcome for that draw
5. **Repeat thousands of times**
6. Summarise the resulting distribution — mean, percentiles, probability of falling short of a target

**Advantages:**
- Not limited to what has happened — can explore **any** scenario, including unprecedented ones
- Handles **complex, path-dependent** payoffs where no analytical formula exists
- Handles **many interacting variables** with specified dependence
- Ideal for **long-horizon planning** where you need the probability of reaching a goal

**Limitations:**
- **Garbage in, garbage out.** The output is only as good as the input distributions and
  correlations. It "answers precisely the question you asked, which may not be the right question."
- It is **not forecasting** — it explores the consequences of assumptions, it does not predict
- Can produce **false confidence**: thousands of runs from a wrong model yield a beautifully smooth,
  entirely misleading distribution
- Computationally intensive; requires care with the random number generator

**Uses:** retirement and goal-based planning (probability of running out of money), pricing
path-dependent and exotic options, portfolio stress testing, capital adequacy, pension liability
modelling.

### Choosing between them

| Question | Method |
| --- | --- |
| How would this portfolio have behaved in the last 20 years, including the actual crises? | **Historical simulation** |
| What is the confidence interval for this Sharpe ratio, given no formula exists for it? | **Bootstrap** |
| What is the probability of running out of money over a 30-year retirement? | **Monte Carlo** |
| How do I price a path-dependent option? | **Monte Carlo** |
| Is this backtest result statistically distinguishable from luck? | **Bootstrap** |
| What is the 1-day 99% VaR, without assuming normality? | **Historical simulation** (or Monte Carlo) |

> **The distinction the exam tests most often:** historical simulation and bootstrap are both
> **bounded by observed data**; Monte Carlo is **not**, because it generates from specified
> distributions. That freedom is Monte Carlo's advantage and its central danger.

### A caution that applies to all three

None of these methods is a forecast. They are **structured explorations of assumptions**. A
simulation reports what follows *if* your inputs are right; it contains no information about whether
they are. The most dangerous output in finance is a precise-looking number derived from an
unexamined assumption, and simulation is very good at producing exactly that.

---

## Formulas to know cold

This module has no formulas to memorise. What must be memorised is the comparison table:

```
                      HISTORICAL          BOOTSTRAP           MONTE CARLO
Data source           Actual history      Resample history    Generated from
                      in sequence         with replacement    specified distributions
Distributional        None                None                REQUIRED (you specify)
  assumption
Can produce           NO                  NO                  YES
  unseen scenarios
Number of scenarios   Fixed by data       Unlimited           Unlimited
Preserves time-       YES                 NO (unless block    Only if modelled
  series structure                        bootstrap)
Main use              VaR, backtesting    Confidence          Goal planning,
                                          intervals, SEs      exotic options
Main weakness         Sample-limited      i.i.d. assumption;  Garbage in,
                                          breaks serial       garbage out
                                          dependence
```

---

## Exam traps

> **Trap 1 — Confusing historical simulation with bootstrap.** Historical simulation **replays the
> actual sequence**; the bootstrap **resamples with replacement**, reshuffling and repeating
> observations.

> **Trap 2 — Thinking Monte Carlo predicts.** It does not forecast. It explores the consequences of
> assumptions you supplied. Its precision says nothing about its accuracy.

> **Trap 3 — Believing Monte Carlo needs no assumptions.** It requires the **most** assumptions of
> the three — a distribution for every variable plus the dependence structure between them.

> **Trap 4 — Forgetting the bootstrap's i.i.d. requirement.** Financial returns exhibit volatility
> clustering and autocorrelation. A naive bootstrap destroys both, which is why block bootstrap
> methods exist.

> **Trap 5 — Assuming historical simulation covers the tails.** It covers only the tails that
> **occurred in your window**. A crisis outside the sample simply does not exist in the output.

> **Trap 6 — More iterations means more accuracy.** More iterations reduce *simulation* error, not
> *model* error. A million runs of a wrong model is still wrong, just more smoothly.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Distinguish historical simulation from bootstrap resampling.

<details><summary>Answer</summary>

**Historical simulation** re-runs the strategy over the **actual historical sequence** of returns, in the order they occurred. It preserves the real time-series structure — volatility clustering, momentum, the actual path through a crisis — and produces exactly as many scenarios as your data has periods.

**Bootstrap resampling** draws observations **randomly with replacement** from the historical sample, many times over. An observation can appear several times in one resample and not at all in another. It can generate unlimited resamples, but it **destroys the time-series ordering**, so autocorrelation and volatility clustering are lost.

Different purposes: historical simulation asks 'how would this have performed?'; the bootstrap asks 'what is the sampling distribution of this statistic?'

</details>

**2.** Why can Monte Carlo simulation explore scenarios that have never occurred, and why is that both its strength and its danger?

<details><summary>Answer</summary>

Monte Carlo draws from **specified probability distributions** rather than from observed data. A normal distribution with σ = 20% will occasionally generate a −60% year even if no such year appears in the historical sample, because the distribution assigns it positive probability.

**Strength:** it is the only method that can assess exposure to events outside your data window — essential for stress testing, for long-horizon planning where the future need not resemble the past, and for pricing instruments with no history.

**Danger:** the output is entirely determined by the input distributions and correlations, which are chosen by the modeller and are usually wrong in the tails. If you specify normal returns, you will never generate the fat-tailed crash that real markets produce. The simulation will report a smooth, precise, confident answer — and it will be a picture of your assumptions, not of the world.

</details>

**3.** An analyst wants a confidence interval for a portfolio's maximum drawdown statistic, for which no analytical standard error formula exists. Which method, and why?

<details><summary>Answer</summary>

**Bootstrap resampling.**

There is no closed-form sampling distribution for maximum drawdown, so the usual `estimate ± t × SE` approach is unavailable. The bootstrap sidesteps this entirely: resample the return series with replacement thousands of times, compute the maximum drawdown for each resample, and read the empirical 2.5th and 97.5th percentiles of that distribution as the 95% confidence interval.

This is the bootstrap's most valuable professional application — producing standard errors and confidence intervals for statistics with no analytical solution.

**Caveat:** maximum drawdown is inherently **path-dependent**, and a naive bootstrap destroys the sequencing that creates drawdowns. A **block bootstrap** — resampling contiguous blocks of returns — is the appropriate variant here.

</details>

**4.** A client asks for the probability that their retirement savings last 30 years. Which method, and what must you be careful about?

<details><summary>Answer</summary>

**Monte Carlo simulation.** The question requires a full distribution of long-horizon outcomes across many interacting uncertain variables — returns, inflation, longevity, spending — over a horizon far longer than any clean historical sample.

What to be careful about:
- **Return distribution assumptions.** Normal returns will understate the probability of a severe sequence of bad years, because real returns are leptokurtic.
- **Sequence-of-returns risk.** Poor returns *early* in retirement are far more damaging than the same returns late, because withdrawals compound the loss. The model must be path-dependent, not average-based.
- **Correlation between inflation and returns** — modelling them independently understates the risk of the worst case (high inflation with poor real returns).
- **False precision.** '87.3% probability of success' invites more confidence than the inputs justify. Report a range and the sensitivity to key assumptions.

</details>

**5.** Why does running a Monte Carlo simulation 1,000,000 times instead of 10,000 not necessarily make the answer better?

<details><summary>Answer</summary>

More iterations reduce **simulation error** — the noise from having drawn a finite number of random samples. That error shrinks with the number of runs and is usually negligible after a few thousand iterations.

It does **nothing** to reduce **model error** — the error from having specified the wrong distributions, the wrong correlations, or the wrong structure. That error is fixed by the model, not by the sample size.

So a million runs of a model that assumes normal returns produces a very smooth, very precise estimate of what a world with normal returns would look like. If real returns have fat tails, the answer is wrong, and the extra precision makes it **more** persuasive and therefore **more** dangerous.

</details>

**6.** Historical simulation of a portfolio over 2010–2024 shows a worst annual loss of 18%. What is wrong with treating that as the worst case?

<details><summary>Answer</summary>

The window **excludes the events that would define a true worst case**. 2010–2024 contains no 2008-scale financial crisis and no 1970s-style inflation shock. Historical simulation can only produce outcomes that occurred in the sample, so the '18% worst case' is a statement about the last 15 years, not about the tail.

Additional problems: **time-period bias** (the window was largely a bull market with unusually accommodative monetary policy); **structural change** (the portfolio's current holdings may not have existed or behaved the same way across the window); and the sample provides only 15 annual observations, far too few to say anything about a 1-in-50-year event.

Remedies: lengthen the window to include multiple crises, supplement with **Monte Carlo** using fat-tailed distributions, and run explicit **scenario analysis** on historical stress episodes even if they predate the sample.

</details>

---

## Done when

- [ ] I can reproduce the three-way comparison table from memory
- [ ] I can state the precise difference between historical simulation and bootstrap resampling
- [ ] I can explain why Monte Carlo can generate unprecedented scenarios and the other two cannot
- [ ] I can say which method requires the most assumptions, and why that is Monte Carlo
- [ ] I can explain the i.i.d. assumption in the bootstrap and why block bootstrap exists
- [ ] I can match each method to an appropriate investment application
- [ ] I can explain why more iterations reduce simulation error but not model error
- [ ] I answered the self-check cold, several days after first study

---

← [LM08 The Return and Risk of a Financial Portfolio](lm-08-the-return-and-risk-of-a-financial-portfolio.md)  ·  [Topic index](README.md)  ·  [LM10 Applications of Simple Linear Regression in Finance](lm-10-applications-of-simple-linear-regression-in-finance.md) →
