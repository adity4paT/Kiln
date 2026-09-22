# DER · LM08 — Pricing and Valuation of Options

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 7 |
| **Prerequisites** | LM2 (option payoffs), LM4 (no-arbitrage). |
| **Where it shows up** | 2 questions. The factor-sensitivity table is near-certain. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain the exercise value, moneyness, and time value of an option
- contrast the use of arbitrage and replication concepts in pricing forward commitments and contingent claims
- identify the factors that determine the value of an option and describe how each factor affects the value of an option

---

## Core concepts

### The two components of an option's value

```
Option value = Exercise (intrinsic) value + Time value
```

**Exercise value** (also called intrinsic value) is what the option would be worth **if exercised
immediately**:

```
Call exercise value = max(0, S − X)
Put exercise value  = max(0, X − S)
```

It can never be negative — the holder simply would not exercise.

**Time value** is the remainder: the value of the **possibility** that the option moves further into
the money before expiration.

```
Time value = Option price − Exercise value
```

**Time value is always positive before expiration** (for a European option on a non-dividend-paying
asset) and **decays to zero at expiration**, where option value equals exercise value exactly.

> **Time decay is not linear.** It **accelerates** as expiration approaches, and it is **greatest for
> at-the-money options**, where the uncertainty about whether the option finishes in or out of the
> money is at its maximum. Deep in-the-money and deep out-of-the-money options have little time value
> to lose.

**Moneyness:**

| | **Call** | **Put** |
| --- | --- | --- |
| **In the money** | S > X | S < X |
| **At the money** | S = X | S = X |
| **Out of the money** | S < X | S > X |

### Arbitrage and replication for options versus forwards

**For a forward commitment**, replication is **static**: buy the asset, borrow the money, and hold
both to maturity. The replicating portfolio is set up once and never adjusted.

**For an option**, replication is **dynamic**: the replicating portfolio consists of a position in
the underlying plus borrowing, and the **required position changes as the underlying price moves**.
An option's sensitivity to the underlying (its **delta**) is not constant — it rises toward 1 as a
call goes deep in the money and falls toward 0 as it goes deep out of the money.

> **This is why options are harder to price.** A forward's replication is a single trade; an
> option's requires **continuous rebalancing**. The binomial model (LM10) makes this tractable by
> replicating one step at a time, and the Black–Scholes framework takes the limit as the steps
> become infinitesimal.
>
> The no-arbitrage principle is **identical** in both cases. Only the complexity of the replicating
> portfolio differs.

### Lower and upper bounds

Arbitrage imposes bounds on option prices without any model:

```
European call:  max(0, S0 − X/(1+r)^T)  ≤  c0  ≤  S0
European put:   max(0, X/(1+r)^T − S0)  ≤  p0  ≤  X/(1+r)^T
```

> **Why a call cannot be worth more than the stock:** if it were, you would sell the call, buy the
> stock, and pocket the difference with no risk — the stock covers any exercise. This is a bound
> derived purely from arbitrage, requiring no assumptions about volatility or distributions.

### The six factors that determine an option's value

**This table is the most examinable content in the module. Learn it cold.**

| Factor | Increase in the factor → | **Call value** | **Put value** |
| --- | --- | --- | --- |
| **Underlying price (S)** | | **UP** ↑ | **DOWN** ↓ |
| **Exercise price (X)** | | **DOWN** ↓ | **UP** ↑ |
| **Time to expiration (T)** | | **UP** ↑ | **UP** ↑ (usually) |
| **Volatility (σ)** | | **UP** ↑ | **UP** ↑ |
| **Risk-free rate (r)** | | **UP** ↑ | **DOWN** ↓ |
| **Income / dividends on the underlying** | | **DOWN** ↓ | **UP** ↑ |

**The reasoning behind each — derive rather than memorise:**

**Underlying price.** A call benefits from a higher price; a put from a lower one. Immediate.

**Exercise price.** A call buys at X, so a lower X is better. A put sells at X, so a higher X is
better.

**Volatility — the most important, and the one that is least intuitive.** **Higher volatility raises
BOTH call and put values.** This is because an option's payoff is **asymmetric**: greater dispersion
increases the chance of a large favourable move, while the unfavourable side is **capped at the
premium**. More uncertainty is unambiguously good for an option **buyer**, whichever direction the
option points.

> This is why **volatility is the only unobservable input** in option pricing, and why options are
> often described as instruments for trading volatility rather than direction.

**Time to expiration.** More time means more opportunity for a favourable move, so generally
**both** calls and puts are worth more. **The exception:** a deep in-the-money **European put** can
be worth **less** with more time, because exercising it delivers X, and the holder must wait longer
to receive that fixed amount — the present value of X falls with time. (American puts do not have
this problem, since they can be exercised immediately.)

**Risk-free rate.** A **call** is a deferred purchase: the holder pays X later rather than now, and a
higher rate makes that deferral more valuable → **call value rises**. A **put** is a deferred sale:
the holder receives X later, and a higher rate makes that delayed receipt less valuable → **put
value falls**.

**Income on the underlying.** Dividends **reduce the underlying's price** on the ex-date without
compensating the option holder (who does not own the shares). That lowers calls and raises puts.

### American versus European

An **American** option can be exercised at any time, so it is worth **at least as much** as an
otherwise identical **European** option:

```
American option value ≥ European option value
```

**When early exercise matters:**

- **American call on a non-dividend-paying stock:** early exercise is **never optimal**. You would
  give up the remaining time value and pay X earlier than necessary. Its value therefore equals the
  European call's.
- **American call on a dividend-paying stock:** early exercise can be optimal just before a large
  ex-dividend date, to capture the dividend.
- **American put:** early exercise **can** be optimal, particularly when deep in the money — the
  holder receives X immediately and can invest it, rather than waiting.

---

## Formulas to know cold

```
OPTION VALUE = EXERCISE VALUE + TIME VALUE
  Call exercise value = max(0, S − X)
  Put exercise value  = max(0, X − S)
  Time value = Option price − Exercise value;  decays to ZERO at expiration
  Time decay ACCELERATES near expiry and is GREATEST for at-the-money options

ARBITRAGE BOUNDS
  European call:  max(0, S0 − X/(1+r)^T)  ≤  c0  ≤  S0
  European put:   max(0, X/(1+r)^T − S0)  ≤  p0  ≤  X/(1+r)^T

THE SIX FACTORS — the most examinable table in the module
  Factor increases →            Call      Put
  Underlying price (S)           UP       DOWN
  Exercise price (X)            DOWN       UP
  Time to expiration (T)         UP        UP (usually)
  VOLATILITY (σ)                 UP        UP     ← BOTH rise. The key counter-intuitive one.
  Risk-free rate (r)             UP       DOWN
  Income / dividends            DOWN       UP

REPLICATION
  FORWARD commitment → STATIC replication (set up once)
  OPTION             → DYNAMIC replication (rebalance as the price moves)
  The no-arbitrage PRINCIPLE is identical; only the complexity differs.

AMERICAN vs EUROPEAN
  American ≥ European
  American CALL on a NON-dividend stock: early exercise NEVER optimal → equals European
  American PUT: early exercise CAN be optimal, especially deep in the money
```

---

## Exam traps

> **Trap 1 — Volatility's effect on puts.** **Higher volatility raises BOTH calls and puts.** The
> payoff is asymmetric: more dispersion increases the favourable tail while the loss stays capped at
> the premium. Candidates routinely say volatility helps calls and hurts puts.

> **Trap 2 — The risk-free rate's effect on puts.** A higher rate **lowers** put values (the delayed
> receipt of X is worth less) and **raises** call values (the deferred payment of X is worth more).

> **Trap 3 — Assuming more time always helps.** It usually does, but a deep in-the-money **European
> put** can be worth **less** with more time, because the fixed X arrives later.

> **Trap 4 — Thinking time decay is linear.** It **accelerates** near expiry and is **largest for
> at-the-money** options.

> **Trap 5 — Believing exercise value can be negative.** It cannot: `max(0, ...)`. The holder would
> simply not exercise.

> **Trap 6 — Assuming American options should be exercised early.** An American **call on a
> non-dividend-paying stock** should **never** be exercised early — you forfeit time value and pay X
> sooner than necessary.

> **Trap 7 — Confusing static and dynamic replication.** A forward is replicated **once**; an option
> requires **continuous rebalancing** because its delta changes.

> **Trap 8 — Dividends' direction.** Dividends **lower calls** and **raise puts**, because the option
> holder does not receive them but suffers the ex-date price drop.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A stock trades at 72. A call with exercise price 65 costs 9.40. Compute the exercise value and time value. What happens to each as expiration approaches?

<details><summary>Answer</summary>

**Exercise value** = max(0, 72 − 65) = **7.00**
**Time value** = 9.40 − 7.00 = **2.40**

The option is **in the money** by 7.00, and the market is paying an additional 2.40 for the possibility that the stock rises further before expiry.

**As expiration approaches:**
- **Exercise value** changes only with the stock price — it is max(0, S − 65) at any moment, with no time component
- **Time value decays toward zero**, and the decay **accelerates** near expiry
- **At expiration**, time value is exactly **zero** and the option is worth precisely its exercise value

So if the stock is still at 72 on the expiry date, the option is worth exactly **7.00** — the 2.40 of time value has been entirely consumed. The option seller collects that decay; the buyer pays it. This is why option buyers need the underlying to move, not merely to stay put.

</details>

**2.** Explain why higher volatility increases the value of BOTH calls and puts.

<details><summary>Answer</summary>

Because an option's payoff is **asymmetric**: the downside is **capped at the premium** while the upside is not.

**For a call:** higher volatility widens the distribution of possible prices at expiry. The chance of a very large favourable move (deep in the money) increases substantially. The chance of a very large **un**favourable move also increases — but it does not matter, because the option simply expires worthless either way. Losing by 5 and losing by 50 produce the **identical** outcome for the holder: zero payoff, premium lost.

**So the favourable tail gets fatter while the unfavourable tail is truncated.** The expected payoff rises, and so does the value.

**For a put:** the identical logic runs in the other direction. Higher volatility increases the chance of a very large **fall** (deep in the money), while an equally large rise makes no difference — the put expires worthless regardless.

**The general statement:** volatility increases the value of **optionality** itself, in whichever direction the option points. Only the holder of a **symmetric** position (a forward, or the underlying) is indifferent to which tail fattens.

**Why it matters practically:** volatility is the **only input to option pricing that cannot be observed** — S, X, T, r, and dividends are all known. Option trading is therefore fundamentally about views on volatility, and the market's **implied volatility** is the price it is putting on future uncertainty.

</details>

**3.** Why would an American call on a non-dividend-paying stock never be exercised early?

<details><summary>Answer</summary>

**Two reasons, both about giving up value for nothing.**

**(1) You forfeit the time value.** Exercising delivers only the **exercise value** — max(0, S − X). But the option is worth **exercise value plus time value** in the market. Selling the option instead always yields more than exercising it. Exercising early throws away the time value.

**(2) You pay X earlier than necessary.** Exercising means paying the exercise price now rather than at expiration. That money could have been earning the risk-free rate in the meantime. Deferring the payment is strictly better.

**Both effects run the same way, so early exercise is never optimal.**

**The consequence:** an American call on a non-dividend-paying stock has **exactly the same value as the equivalent European call**. The early exercise right is worthless because it would never be used.

**The exceptions:**
- **Dividends.** Exercising just before a large ex-dividend date can be optimal — you capture the dividend, which the option holder otherwise misses while suffering the ex-date price drop.
- **American puts.** Early exercise **can** be optimal. Exercising a deep in-the-money put delivers **X in cash immediately**, which can be invested at the risk-free rate. Here, receiving money sooner is better, so the calculus reverses.

</details>

**4.** Construct the six-factor table from memory and explain the risk-free rate row.

<details><summary>Answer</summary>

| Factor increases → | **Call** | **Put** |
| --- | --- | --- |
| Underlying price (S) | **UP** | **DOWN** |
| Exercise price (X) | **DOWN** | **UP** |
| Time to expiration (T) | **UP** | **UP** (usually) |
| Volatility (σ) | **UP** | **UP** |
| Risk-free rate (r) | **UP** | **DOWN** |
| Income / dividends | **DOWN** | **UP** |

**The risk-free rate row, explained:**

A **call** is a **deferred purchase**. The holder has locked in the right to buy at X, but does not pay X until exercise. The money that would otherwise be tied up in the stock can earn the risk-free rate in the meantime. A **higher** rate makes that deferral **more valuable** → the call is worth **more**.

Equivalently, from put-call parity (LM9): `c0 = p0 + S0 − X/(1+r)^T`. A higher r **reduces** the present value of X, which **raises** c0.

A **put** is a **deferred sale**. The holder has locked in the right to sell at X, but will not receive X until exercise. A **higher** rate makes that delayed receipt **less valuable** → the put is worth **less**.

From parity: `p0 = c0 − S0 + X/(1+r)^T`. A higher r reduces the present value of X, which **lowers** p0.

**The mnemonic:** think about **when the exercise price changes hands**. The call holder **pays** it later (good when rates are high); the put holder **receives** it later (bad when rates are high).

</details>

---

## Done when

- [ ] I can decompose an option's value into exercise value and time value
- [ ] I can explain why time decay accelerates and is largest at the money
- [ ] I can state the arbitrage bounds for European calls and puts
- [ ] I can reproduce the six-factor table from memory and derive every row
- [ ] I can explain why higher volatility raises both call and put values
- [ ] I can explain the risk-free rate's opposite effects using the timing of the exercise price
- [ ] I can explain why an American call on a non-dividend stock is never exercised early
- [ ] I can contrast static replication of a forward with dynamic replication of an option
- [ ] I answered the self-check cold, several days after first study

---

← [LM07 Pricing and Valuation of Interest Rate and Other Swaps](lm-07-pricing-and-valuation-of-interest-rate-and-other-swaps.md)  ·  [Topic index](README.md)  ·  [LM09 Option Replication Using Put-Call Parity](lm-09-option-replication-using-put-call-parity.md) →
