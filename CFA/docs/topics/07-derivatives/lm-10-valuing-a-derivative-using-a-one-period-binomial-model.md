# DER · LM10 — Valuing a Derivative Using a One-Period Binomial Model

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM4 (replication), LM8 (option factors), LM9 (parity). |
| **Where it shows up** | 2 questions. The binomial calculation and risk-neutral pricing are the closing ideas of the topic. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain how to value a derivative using a one-period binomial model
- describe the concept of risk neutrality in derivatives pricing

---

## Core concepts

### The setup

The one-period binomial model assumes the underlying can take exactly **two** values at the end of
the period:

```
                    S+ = S0 × u        (up move)
         S0  <
                    S− = S0 × d        (down move)

where  u = the up factor (> 1)
       d = the down factor (< 1), often set to 1/u
```

The option's payoffs at the two nodes are known:

```
c+ = max(0, S+ − X)        c− = max(0, S− − X)       [for a call]
p+ = max(0, X − S+)        p− = max(0, X − S−)       [for a put]
```

### Method 1 — replication (the conceptual route)

Construct a portfolio of **h units of the underlying** plus **borrowing or lending** that reproduces
the option's payoffs in both states. By no-arbitrage, the option must cost what the portfolio costs.

**The hedge ratio (delta):**

```
h = (c+ − c−) / (S+ − S−)
```

This is the number of units of the underlying needed per option. It is the **slope** of the option's
payoff against the underlying's — the option's **delta**.

The replicating portfolio is then valued, and the option's price follows. This is the method that
makes the logic transparent, but it is slower to compute.

### Method 2 — risk-neutral valuation (the route to use on the exam)

**The risk-neutral probability:**

```
π = [(1 + r) − d] / (u − d)
```

**The option value:**

```
c0 = [ π × c+ + (1 − π) × c− ] / (1 + r)
```

> **Compute `π` first, then apply it to the payoffs, then discount at the risk-free rate.** This is
> a three-step mechanical procedure and it is considerably faster than replication. Use it.

### Risk neutrality — what it means and what it does not

This is the conceptual heart of the module, and it is widely misunderstood.

> **`π` is NOT the real probability of an up move.** It is a **mathematical construction** — the
> probability that would make investors indifferent to risk, i.e. that would make the underlying's
> expected return equal the risk-free rate.

**The remarkable fact: the option's value does not depend on the real probabilities at all.**

Consider two investors who completely disagree about the stock's prospects — one thinks an up move
is 80% likely, the other 30%. **They will still agree on the option's price.** Why?

Because the option can be **replicated** by a portfolio of the stock and borrowing. The replicating
portfolio's cost depends only on `S0`, `u`, `d`, `r`, and `X` — **none of which is a probability**.
If the option traded at any other price, both investors could arbitrage it, regardless of their
views.

> **The real probabilities are already embedded in the current stock price `S0`.** An investor who
> is more optimistic about the stock has already bid `S0` up. Once `S0` is given, the option's price
> follows mechanically — there is no room for a second, independent opinion about the same
> uncertainty.

**Why it is called "risk-neutral":** the formula prices the option **as if** investors were
indifferent to risk — as if the expected return on everything were the risk-free rate. This is a
**computational device**, not a claim about investor psychology. We are not assuming anyone is risk
neutral; we are using the fact that the answer is the same either way.

> **This is the deepest idea in Derivatives, and it is the payoff of LM4.** Arbitrage pricing needs
> no forecast, and therefore needs no probabilities. Every pricing result in this topic — forwards,
> futures, swaps, parity, and the binomial model — is the same principle applied to a different
> instrument.

### Worked example

A stock trades at 50. In one year it will be either 60 (u = 1.2) or 42 (d = 0.84). The one-year
risk-free rate is 4%. Value a one-year European call with exercise price 52.

**Step 1 — the payoffs:**
```
c+ = max(0, 60 − 52) = 8
c− = max(0, 42 − 52) = 0
```

**Step 2 — the risk-neutral probability:**
```
π = [(1 + 0.04) − 0.84] / (1.2 − 0.84) = (1.04 − 0.84)/0.36 = 0.20/0.36 = 0.5556
```

**Step 3 — discount the expected payoff:**
```
c0 = [0.5556 × 8 + 0.4444 × 0] / 1.04 = 4.4444/1.04 = 4.27
```

**Cross-check with replication:**
```
h = (8 − 0)/(60 − 42) = 8/18 = 0.4444
Portfolio: buy 0.4444 shares, borrow B, where the portfolio replicates the call.
At the down node: 0.4444 × 42 − B × 1.04 = 0  →  B = 18.667/1.04 = 17.95
Cost today = 0.4444 × 50 − 17.95 = 22.22 − 17.95 = 4.27  ✓
```

Both methods agree, as they must.

### Extending the model

**Multi-period binomial models** simply repeat the one-period calculation at each node, working
**backward from expiration**. More periods give a finer approximation of the price distribution.

**American options** require checking at **every node** whether immediate exercise exceeds the
continuation value, and taking the larger. This is why American options must be valued on a tree —
there is no closed-form solution.

**Black–Scholes–Merton** is the limit of the binomial model as the number of periods goes to
infinity and each period becomes infinitesimally short. Its assumptions — continuous trading,
constant volatility, lognormally distributed prices (QM LM6), European exercise, no transaction
costs — are the binomial assumptions taken to their limit.

### Key insights to carry forward

| Insight | Why it matters |
| --- | --- |
| **The hedge ratio `h` is the option's delta** | It is the number of shares needed to hedge one option — the basis of dynamic hedging |
| **Delta changes as the price moves** | Which is why option replication is **dynamic**, not static (LM8) |
| **Real probabilities never appear** | The option's value depends on `S0`, `u`, `d`, `r`, `X` — not on anyone's view |
| **Volatility enters through `u` and `d`** | Larger `u` and smaller `d` mean higher volatility, which raises option value (LM8) |

---

## Formulas to know cold

```
THE SETUP
  S+ = S0 × u  (up)        S− = S0 × d  (down)        often d = 1/u
  c+ = max(0, S+ − X)      c− = max(0, S− − X)

METHOD 1 — REPLICATION
  Hedge ratio (DELTA):  h = (c+ − c−) / (S+ − S−)
  Build a portfolio of h units of the underlying plus borrowing that matches both payoffs.

METHOD 2 — RISK-NEUTRAL VALUATION  ← USE THIS ON THE EXAM
  Step 1:  π = [(1 + r) − d] / (u − d)
  Step 2:  Expected payoff = π × c+ + (1 − π) × c−
  Step 3:  c0 = Expected payoff / (1 + r)

RISK NEUTRALITY
  π is NOT the real probability of an up move. It is a mathematical construction.
  The option's value does NOT depend on real probabilities at all —
  because the option can be REPLICATED, and the replicating portfolio's cost
  depends only on S0, u, d, r, and X.
  The real probabilities are ALREADY EMBEDDED in S0.

EXTENSIONS
  Multi-period: repeat at each node, working BACKWARD from expiration
  American:     at every node, take max(immediate exercise, continuation value)
  Black-Scholes: the limit as the number of periods → ∞
```

---

## Exam traps

> **Trap 1 — Thinking π is a real probability.** It is a **mathematical construction** used for
> pricing. It carries no information about what anyone actually expects.

> **Trap 2 — Using real probabilities in the formula.** They do **not** enter. Two investors with
> completely different views agree on the option's price.

> **Trap 3 — The risk-neutral probability formula.** `π = [(1+r) − d]/(u − d)`. Note it is
> `(1 + r)`, not `r`, in the numerator.

> **Trap 4 — Forgetting to discount.** The expected payoff under π must be **discounted at the
> risk-free rate** to get today's value.

> **Trap 5 — Hedge ratio numerator order.** `h = (c+ − c−)/(S+ − S−)` — the **up-state values
> first** in both. Reversing gives a negative delta for a call.

> **Trap 6 — Valuing an American option like a European one.** At **every node** you must compare
> immediate exercise to the continuation value and take the larger.

> **Trap 7 — Missing where volatility enters.** It is embedded in **u and d**. A wider spread between
> them means higher volatility and a higher option value.

> **Trap 8 — Thinking the two methods can disagree.** Replication and risk-neutral valuation are
> algebraically identical and always give the same answer. Use whichever is faster — usually
> risk-neutral.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A stock trades at 40. In one period it moves to 48 or 34. The risk-free rate is 3%. Value a European put with exercise price 42.

<details><summary>Answer</summary>

**Step 1 — the factors and payoffs:**
u = 48/40 = 1.20, d = 34/40 = 0.85
p+ = max(0, 42 − 48) = **0**
p− = max(0, 42 − 34) = **8**

**Step 2 — the risk-neutral probability:**
π = [(1 + 0.03) − 0.85] / (1.20 − 0.85) = (1.03 − 0.85)/0.35 = 0.18/0.35 = **0.5143**

**Step 3 — discount the expected payoff:**
p0 = [0.5143 × 0 + 0.4857 × 8] / 1.03 = 3.8857/1.03 = **3.77**

**Cross-check via the hedge ratio:**
h = (p+ − p−)/(S+ − S−) = (0 − 8)/(48 − 34) = **−0.5714**

The negative delta is correct for a put — hedging a long put requires a **long** position in the stock (or, equivalently, replicating the put requires **shorting** the stock).

</details>

**2.** Explain why two investors who strongly disagree about a stock's prospects will nonetheless agree on the value of an option on it.

<details><summary>Answer</summary>

Because the option's value is determined by **replication and arbitrage**, and neither of those depends on anyone's opinion.

**The argument:** the option's payoffs can be reproduced exactly by a portfolio of the **stock** and **borrowing** — h shares plus a loan, where `h = (c+ − c−)/(S+ − S−)`. The cost of assembling that portfolio depends only on:

**S0, u, d, r, and X** — and **not one of these is a probability**.

If the option traded at any price other than the replicating portfolio's cost, **either** investor could arbitrage it: buy the cheap one, sell the expensive one, lock in a riskless profit. Their disagreement about the stock's direction is irrelevant to that trade, because the position is hedged in **both** states.

**Where did the disagreement go?** It is **already embedded in S0**. The optimistic investor has already bid the stock up; the pessimist has sold. The current price reflects the market's aggregate view. Once S0 is given, the option's price follows mechanically — there is no room for a second, independent opinion about the same uncertainty.

**This is the deepest idea in the topic**, and it is what LM4 was building toward. Arbitrage pricing needs no forecast, and therefore needs no probabilities.

</details>

**3.** What does 'risk-neutral' actually mean in risk-neutral valuation?

<details><summary>Answer</summary>

It is a **computational device**, not an assumption about investor psychology.

**What π is:** the probability that would make the underlying's **expected return equal the risk-free rate** — that is, the probability an investor indifferent to risk would assign. Formally:

```
π × u + (1 − π) × d = (1 + r)     →    π = [(1 + r) − d]/(u − d)
```

**What the technique does:** it prices the option **as if** everyone were risk neutral, then discounts at the risk-free rate. The answer is correct **even though nobody is risk neutral**.

**Why it works:** because the option is **perfectly replicable**, its price is pinned by arbitrage regardless of risk preferences. Since the answer does not depend on risk preferences, we are free to compute it under **whichever** preference assumption is most convenient — and risk neutrality is by far the most convenient, because it lets us discount at the risk-free rate rather than at some unknown risk-adjusted rate.

**The crucial clarification:** we are **not** assuming investors are risk neutral. We are exploiting the fact that the answer is the **same either way**, and choosing the easy route.

**What we have avoided:** without this device, you would need to know the option's **risk-adjusted discount rate** — which depends on the option's risk, which depends on its value, which is what you are trying to find. The risk-neutral approach cuts that circularity.

</details>

**4.** How does the binomial model handle an American option, and why can't a closed-form solution be used?

<details><summary>Answer</summary>

**The method:** at **every node** in the tree, compare two values and take the larger:

```
Value at node = max( immediate exercise value , continuation value )

  where  immediate exercise = max(0, S − X) for a call, max(0, X − S) for a put
         continuation value = the risk-neutral discounted value of holding on
```

Work **backward from expiration**. At the final nodes, value is simply the exercise value. At each earlier node, compute the continuation value from the two nodes ahead, compare it to immediate exercise, and record the maximum. Repeat back to today.

**Why no closed-form solution exists:** the early exercise decision is **path-dependent in a way that has no analytical expression**. Whether exercising at node X is optimal depends on the values at all subsequent nodes, which in turn depend on their own exercise decisions. There is no formula that collapses this recursion.

**Black–Scholes** solves the **European** case analytically because there is exactly **one** decision point — expiration. Adding the option to exercise at any of infinitely many intermediate moments destroys that tractability.

**The practical consequence:** American options are valued **numerically** — on binomial or trinomial trees, by finite difference methods, or by Monte Carlo with regression methods. More tree steps give a better approximation at the cost of computation.

**Where it matters most:** American **puts**, where early exercise is genuinely often optimal (LM8). An American call on a non-dividend-paying stock never exercises early, so Black–Scholes prices it exactly.

</details>

---

## Done when

- [ ] I can compute u, d, and the payoffs at both nodes
- [ ] I can compute the risk-neutral probability with the correct (1+r) in the numerator
- [ ] I can value a call or put in three steps and cross-check with the hedge ratio
- [ ] I can compute the hedge ratio and interpret its sign for a call and a put
- [ ] I can explain why real probabilities do not enter the valuation
- [ ] I can explain what 'risk-neutral' means as a computational device, not a psychological claim
- [ ] I can explain how American options are handled and why no closed form exists
- [ ] I answered the self-check cold, several days after first study

---

← [LM09 Option Replication Using Put-Call Parity](lm-09-option-replication-using-put-call-parity.md)  ·  [Topic index](README.md)
