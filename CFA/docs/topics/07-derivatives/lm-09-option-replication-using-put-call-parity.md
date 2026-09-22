# DER · LM09 — Option Replication Using Put-Call Parity

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM8 (option factors), LM4 (replication). |
| **Where it shows up** | 2 questions. Put-call parity is one of the most reliably tested relationships on the exam. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain put-call parity for European options
- explain put-call forward parity for European options

---

## Core concepts

### Put-call parity

**The relationship:**

```
c0 + X/(1 + r)^T  =  p0 + S0
```

| Left side — the **fiduciary call** | Right side — the **protective put** |
| --- | --- |
| A **long call** plus a **risk-free bond** with face value X | A **long put** plus the **underlying asset** |

**Why they must be equal: they have identical payoffs in every state of the world.**

| At expiration | **Fiduciary call** (c + bond) | **Protective put** (p + stock) |
| --- | --- | --- |
| **ST > X** | Call worth `ST − X`, bond worth X → **ST** | Put worthless, stock worth ST → **ST** |
| **ST < X** | Call worthless, bond worth X → **X** | Put worth `X − ST`, stock worth ST → **X** |
| **ST = X** | **X** | **X** |

Identical payoffs in every state → **identical value today**, by the law of one price (LM4). If they
were not equal, you would buy the cheaper package, sell the dearer, and lock in a riskless profit.

> **Note what the equality means economically:** both packages guarantee a **minimum value of X**
> with **unlimited upside above X**. They are two different ways of constructing the same insured
> position — one by buying a call and setting aside the cash, the other by buying the asset and
> insuring it.

### Rearranging parity — the four synthetic positions

Parity can be rearranged to synthesise any of the four instruments from the other three. **This is
the most examinable use of the relationship.**

```
Synthetic CALL:   c0 = p0 + S0 − X/(1+r)^T
                       long put + long stock + borrow PV(X)

Synthetic PUT:    p0 = c0 − S0 + X/(1+r)^T
                       long call + short stock + lend PV(X)

Synthetic STOCK:  S0 = c0 − p0 + X/(1+r)^T
                       long call + short put + lend PV(X)

Synthetic BOND:   X/(1+r)^T = p0 + S0 − c0
                       long put + long stock + short call
```

> **The synthetic bond is worth noticing.** A long put, a long stock, and a short call — with the
> same exercise price and expiry — is a **riskless position** that must earn the risk-free rate. A
> deviation from that is an arbitrage, and it is the basis of the **conversion** and **reversal**
> trades that market makers run continuously.

**Using parity to detect arbitrage.** Compute both sides. If `c0 + PV(X) > p0 + S0`, the fiduciary
call is overpriced: **sell** the call, **borrow** PV(X), **buy** the put, **buy** the stock. The
profit is the difference, locked in today with no risk.

### Put-call forward parity

The same relationship expressed using a **forward** on the asset instead of the asset itself.

Since the forward price satisfies `F0 = S0 × (1+r)^T`, we can substitute `S0 = F0/(1+r)^T`:

```
c0 + X/(1 + r)^T  =  p0 + F0/(1 + r)^T
```

Or, multiplying through by `(1+r)^T`:

```
c0 × (1+r)^T + X  =  p0 × (1+r)^T + F0

equivalently:   c0 − p0 = (F0 − X) / (1 + r)^T
```

**Why it is useful:** it prices options on assets where the **spot is not directly investable** —
commodities that cannot be cheaply stored, or assets subject to short-sale constraints. If you
cannot buy and hold the asset, you cannot construct the protective put directly, but you **can**
take a long forward position. Forward parity replaces the spot position with a forward one.

> **A neat consequence:** if `F0 = X`, then `c0 = p0`. A call and a put struck **at the forward
> price**, with the same expiry, have **equal value**. This is why option traders quote strikes
> relative to the forward rather than the spot — the at-the-money-forward strike is the natural
> symmetry point.

### What parity tells you about the option factors

Put-call parity **derives** several rows of the LM8 factor table rather than requiring them to be
memorised separately:

- **Risk-free rate.** `c0 = p0 + S0 − X/(1+r)^T`. A higher `r` **reduces** `X/(1+r)^T`, so `c0`
  **rises**. And `p0 = c0 − S0 + X/(1+r)^T`, so `p0` **falls**. This is the LM8 explanation in one
  line.
- **Exercise price.** A higher X raises `X/(1+r)^T`, lowering `c0` and raising `p0`.
- **Volatility.** Parity says nothing about it — volatility affects `c0` and `p0` **equally**, so
  the relationship is preserved. This is consistent with LM8: higher volatility raises **both**.

### Assumptions and limitations

Put-call parity holds exactly only under:

| Assumption | Why it matters |
| --- | --- |
| **European options** | American early exercise breaks the payoff equivalence. For American options only an **inequality** holds |
| **Same underlying, exercise price, and expiration** | All three must match |
| **No dividends** (or an adjustment) | With dividends: `c0 + X/(1+r)^T = p0 + S0 − PV(dividends)` |
| **No transaction costs or short-sale constraints** | Otherwise the arbitrage is not executable |
| **Borrowing and lending at the risk-free rate** | Required to construct the bond leg |

**With dividends,** the protective put side is reduced by the present value of the dividends the
stock will pay before expiry, because the option holder does not receive them:

```
c0 + X/(1 + r)^T  =  p0 + S0 − PV(dividends)
```

---

## Formulas to know cold

```
PUT-CALL PARITY (European options, same underlying, X, and expiry)
  c0 + X/(1+r)^T  =  p0 + S0
  └ fiduciary call ┘   └ protective put ┘

  Both guarantee a MINIMUM of X with UNLIMITED upside above X.

THE FOUR SYNTHETICS — rearrangements of the same equation
  Synthetic CALL:   c0 = p0 + S0 − X/(1+r)^T
  Synthetic PUT:    p0 = c0 − S0 + X/(1+r)^T
  Synthetic STOCK:  S0 = c0 − p0 + X/(1+r)^T
  Synthetic BOND:   X/(1+r)^T = p0 + S0 − c0      ← a RISKLESS position

WITH DIVIDENDS
  c0 + X/(1+r)^T = p0 + S0 − PV(dividends)

PUT-CALL FORWARD PARITY
  c0 + X/(1+r)^T = p0 + F0/(1+r)^T
  c0 − p0 = (F0 − X)/(1+r)^T

  If F0 = X  →  c0 = p0   (a call and put struck AT THE FORWARD have equal value)

  Useful when the SPOT is not investable (commodities, short-sale constraints).

ASSUMPTIONS
  EUROPEAN options · same underlying/X/expiry · dividends adjusted
  · no transaction costs or short-sale constraints · borrowing and lending at r
```

---

## Exam traps

> **Trap 1 — Which side has which instrument.** **Fiduciary call = call + bond.** **Protective put =
> put + stock.** Writing it as "call + stock = put + bond" is wrong and produces nonsense.

> **Trap 2 — Forgetting to discount X.** It is `X/(1+r)^T`, the **present value** of the exercise
> price — not X itself.

> **Trap 3 — Applying parity to American options.** It holds **exactly** only for **European**
> options. Early exercise breaks the payoff equivalence; only an inequality holds for Americans.

> **Trap 4 — Ignoring dividends.** With dividends, subtract **PV(dividends)** from the stock on the
> protective put side.

> **Trap 5 — Sign errors when rearranging.** Derive each synthetic from the base equation rather
> than memorising four separate formulas. Move one term at a time.

> **Trap 6 — Thinking volatility appears in parity.** It does not — it affects `c0` and `p0`
> **equally**, preserving the relationship. Parity is a **model-free** arbitrage relationship, which
> is why it holds regardless of any assumption about the price distribution.

> **Trap 7 — Missing the forward parity insight.** When **F0 = X**, a call and a put have **equal
> value**. This is why traders quote strikes relative to the forward.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A stock trades at 84. A 6-month European call with exercise price 80 trades at 8.20, and the equivalent put at 2.90. The annual risk-free rate is 5%. Is there an arbitrage?

<details><summary>Answer</summary>

**Fiduciary call** = c0 + X/(1+r)^T = 8.20 + 80/(1.05)^0.5 = 8.20 + 80/1.02470 = 8.20 + 78.07 = **86.27**

**Protective put** = p0 + S0 = 2.90 + 84 = **86.90**

**They are not equal — the protective put is overpriced by 0.63.** An arbitrage exists.

**The trade:**
1. **Sell** the protective put package: sell the put (+2.90) and short the stock (+84) → receive **86.90**
2. **Buy** the fiduciary call package: buy the call (−8.20) and lend 78.07 at 5% → pay **86.27**
3. **Net inflow today: 0.63**, with no capital committed

**At expiry both packages are worth exactly the same** (max(ST, 80)), so the positions offset perfectly and the 0.63 is kept regardless of where the stock ends.

In practice, transaction costs and the cost of borrowing the stock to short would likely consume 0.63 — which is why such discrepancies are small and fleeting.

</details>

**2.** Show how to construct a synthetic long stock position using options and a bond.

<details><summary>Answer</summary>

Rearrange put-call parity to isolate S0:

```
c0 + X/(1+r)^T = p0 + S0
           S0   = c0 − p0 + X/(1+r)^T
```

**The position: long a call, short a put, and lend the present value of X** — all with the same exercise price and expiry.

**Why it works, checked at expiry:**

| | ST > X | ST < X |
| --- | --- | --- |
| Long call | ST − X | 0 |
| Short put | 0 | −(X − ST) = ST − X |
| Bond matures | X | X |
| **Total** | **ST** | **ST** |

In **both** states the package is worth exactly **ST** — identical to owning the stock.

**Why anyone would do this:**
- **Short-sale constraints** — if the stock cannot be borrowed, a synthetic short (the reverse: short call, long put, borrow PV(X)) achieves the exposure
- **Capital efficiency** — the options require less capital than buying the stock outright
- **Market access** — where direct ownership is restricted by regulation or mandate
- **The combination `long call + short put` is known as a synthetic forward**, and it is how traders express directional views without the underlying

</details>

**3.** Explain put-call forward parity and why it is useful.

<details><summary>Answer</summary>

**The relationship:** substituting `S0 = F0/(1+r)^T` into standard parity gives

```
c0 + X/(1+r)^T = p0 + F0/(1+r)^T

or equivalently:  c0 − p0 = (F0 − X)/(1+r)^T
```

**Why it is useful — three reasons:**

**(1) The spot may not be investable.** Standard parity requires constructing a **protective put** — buying and holding the underlying. For many assets that is impossible or prohibitively expensive: commodities with high storage costs, electricity, or assets subject to short-sale restrictions. You cannot buy and store a barrel of oil to replicate a protective put, but you **can** take a long forward position. Forward parity substitutes the forward for the spot.

**(2) It isolates the forward price.** The relationship `c0 − p0 = (F0 − X)/(1+r)^T` lets you back out an implied forward price from observed option prices, which is useful where the forward market is less liquid than the options market.

**(3) The symmetry insight.** If **F0 = X**, then `c0 = p0` — a call and a put struck **at the forward price** have **equal value**. This is why option traders quote strikes relative to the **forward** rather than the spot: the at-the-money-forward strike is the natural centre of the volatility smile, and it is where the call and put are symmetric.

**Note:** parity in either form is **model-free**. It requires no assumption about volatility or the price distribution — only no-arbitrage. That is what makes it so reliable, and why violations are immediately traded away.

</details>

**4.** Why does put-call parity hold exactly only for European options?

<details><summary>Answer</summary>

Because **American early exercise breaks the payoff equivalence** on which the argument rests.

The parity argument depends on the two packages having **identical payoffs at a single point in time** — expiration. The table:

| At expiry | Fiduciary call | Protective put |
| --- | --- | --- |
| ST > X | ST | ST |
| ST < X | X | X |

With **American** options, either side can be **exercised early**, which terminates that leg at a different time and a different value. The two packages no longer produce identical cash flows at a common date, so the equality cannot be enforced by arbitrage.

**What holds instead** is an **inequality**. For American options on a non-dividend-paying stock:

```
S0 − X  ≤  C0 − P0  ≤  S0 − X/(1+r)^T
```

**The practical reason early exercise matters here:** an American **put** may rationally be exercised early when deep in the money, to receive X immediately and invest it (LM8). That possibility gives the American put extra value the European put does not have, breaking the exact relationship.

An American **call** on a **non-dividend-paying** stock is never exercised early, so it equals its European counterpart — and parity effectively holds if the put is also European.

</details>

---

## Done when

- [ ] I can write put-call parity correctly, with the call on the bond side
- [ ] I can prove it with a payoff table in both states
- [ ] I can derive all four synthetic positions by rearrangement
- [ ] I can detect an arbitrage from mispriced parity and specify the trade
- [ ] I can state the dividend adjustment
- [ ] I can write put-call forward parity and explain when it is needed
- [ ] I can explain why c0 = p0 when F0 = X
- [ ] I can state why parity holds exactly only for European options
- [ ] I answered the self-check cold, several days after first study

---

← [LM08 Pricing and Valuation of Options](lm-08-pricing-and-valuation-of-options.md)  ·  [Topic index](README.md)  ·  [LM10 Valuing a Derivative Using a One-Period Binomial Model](lm-10-valuing-a-derivative-using-a-one-period-binomial-model.md) →
