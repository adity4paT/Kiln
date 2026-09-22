# DER · LM06 — Pricing and Valuation of Futures Contracts

## At a glance

| | |
| --- | --- |
| **Topic** | Derivatives (5-8% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM5 (forward pricing and valuation), LM1 (clearinghouse mechanics). |
| **Where it shows up** | 1-2 questions. The forward-futures price difference and the MTM valuation reset are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- compare the value and price of forward and futures contracts
- explain why forward and futures prices differ

---

## Core concepts

### The economic equivalence, and the structural difference

A futures contract is economically the same agreement as a forward — buy or sell an asset at a set
price on a set date. The **pricing formula is the same**:

```
Futures price = S0 × (1 + r)^T + FV(costs) − FV(benefits)
```

The difference is entirely **institutional**, and it is daily settlement.

| | **Forward** | **Future** |
| --- | --- | --- |
| Market | OTC, customised | **Exchange, standardised** |
| Counterparty | The other party | **The clearinghouse** |
| Settlement of gains/losses | **At maturity** | **DAILY** — mark to market |
| Margin | Collateral by agreement | **Initial, maintenance, variation margin** |
| Value between settlement dates | **Accumulates** | **Reset to ZERO each day** |
| Credit risk | Builds up over the life | **Minimal** — never more than one day's move |
| Closing a position | Requires the counterparty, or novation | **Offsetting trade** |

### Daily settlement and the valuation reset

**This is the key mechanical difference.**

A **forward's** value accumulates: if the spot price moves in your favour, your position becomes
progressively more valuable, and that value is realised only at maturity.

A **future's** gains and losses are **settled in cash every day**. At the end of each trading day:

1. The position is **marked to market** at the day's settlement price
2. The gain or loss is **paid in cash** through variation margin
3. The contract's **value resets to ZERO**

```
Value of a futures position between settlement dates
    = Current futures price − Previous day's settlement price   (times the contract size)

Value immediately AFTER daily settlement = ZERO
```

> **So a futures contract's value is zero at the end of every day**, not just at initiation. This is
> the single most examinable mechanical fact about futures.

**The consequence for credit risk:** because gains are paid out daily, no party ever owes the other
more than one day's price move. A forward, by contrast, can accumulate months of unrealised gain
before anything settles.

### Why forward and futures prices differ

In a world of **constant interest rates**, forward and futures prices would be **identical**.

They differ in practice because of an interaction between **daily settlement** and **interest rate
movements**:

| If futures prices and interest rates are... | Effect |
| --- | --- |
| **Positively correlated** | Gains are received (and reinvested) when rates are **high**; losses are funded when rates are **low**. This favours the **long**, so **futures prices exceed forward prices** |
| **Negatively correlated** | The reverse — futures prices are **below** forward prices |
| **Uncorrelated** | Futures and forward prices are **equal** |

**The mechanism, stated carefully.** A long futures holder receives cash on days the price rises. If
price rises tend to coincide with **high interest rates**, that cash is reinvested at a good rate.
On days the price falls, they must fund the loss — and if that coincides with **low** rates, funding
is cheap. Both effects favour the long, so the long is willing to pay more: the futures price sits
above the forward price.

> **In practice the difference is small** for most contracts and short maturities, and it is
> generally ignored outside of interest rate futures with long maturities, where the correlation is
> strong by construction.

**Other practical sources of divergence:** differences in **credit risk** (futures are
clearinghouse-guaranteed), **liquidity**, **transaction costs**, **margin requirements** (the
opportunity cost of posted capital), and **tax treatment**.

### The convergence property

```
As T approaches expiration, the futures price converges to the spot price:  FT → ST
```

**Why it must:** at expiration, the futures contract **is** a claim on immediate delivery — identical
to the spot. Any gap would be an instant arbitrage: buy the cheaper, sell the dearer, and settle
immediately.

The **basis** is the difference between them:

```
Basis = Spot price − Futures price
```

The basis **narrows toward zero** as expiration approaches. **Basis risk** is the risk that it does
not behave as expected during the life of the hedge — which is the main reason an exchange-traded
hedge is imperfect (LM1).

### Other futures features worth knowing

**Price limits and circuit breakers.** Exchanges impose daily limits on how far a contract price may
move. A contract that reaches the limit is **limit up** or **limit down** and may stop trading. This
prevents disorderly markets but can also **trap** a position — you cannot exit at any price, while
margin calls continue.

**Settlement.** Most futures are **cash settled** (the difference is paid) rather than physically
delivered. Where physical delivery applies, the short usually has options over **timing, grade, and
location**, which are worth something and are reflected in the price.

**Open interest** is the number of contracts outstanding. Unlike shares, futures are **created** when
a new buyer meets a new seller, so open interest rises and falls with activity. Rising open interest
alongside a price move suggests new positions are driving it; falling open interest suggests
existing positions are closing.

---

## Formulas to know cold

```
PRICING — the same formula as a forward
  Futures price = S0 × (1 + r)^T + FV(costs) − FV(benefits)

VALUATION — the key difference
  Between settlement: value = Current futures price − Previous settlement price
  IMMEDIATELY AFTER daily settlement: value = ZERO

  A forward's value ACCUMULATES until maturity.
  A future's value RESETS TO ZERO every day.

WHY FUTURES AND FORWARD PRICES DIFFER
  Futures price and interest rates POSITIVELY correlated → FUTURES price > forward price
  NEGATIVELY correlated                                   → FUTURES price < forward price
  UNCORRELATED (or constant rates)                        → the two are EQUAL

  Mechanism: the long receives cash daily. If gains arrive when rates are HIGH, reinvestment
  is favourable; if losses are funded when rates are LOW, funding is cheap. Both favour the long.

CONVERGENCE
  As T → expiration, the futures price converges to spot:  FT → ST
  BASIS = Spot − Futures,  narrowing to zero at expiration
  BASIS RISK = the basis not behaving as expected during the hedge
```

---

## Exam traps

> **Trap 1 — Forgetting the daily value reset.** A futures contract's value is **zero immediately
> after each daily settlement**, not only at initiation. Between settlements it is the change since
> the last settlement price.

> **Trap 2 — Getting the correlation effect backwards.** **Positive** correlation between futures
> prices and interest rates makes **futures prices HIGHER** than forward prices.

> **Trap 3 — Thinking the pricing formula differs.** It does **not**. The cost-of-carry formula is
> identical; only the settlement mechanics differ.

> **Trap 4 — Assuming futures have no credit risk.** They have **minimal** credit risk, not none —
> the clearinghouse itself can fail, and margin calls must be met in cash, converting credit risk
> into **liquidity** risk.

> **Trap 5 — Ignoring basis risk.** Convergence is guaranteed **at expiration**, but the basis can
> move unpredictably during the hedge. This is the main imperfection in an exchange-traded hedge.

> **Trap 6 — Overlooking price limits.** A limit move can **trap** a position: you cannot exit at
> any price while margin calls continue.

> **Trap 7 — Overstating the forward-futures price difference.** For most contracts and short
> maturities it is small and routinely ignored.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** An investor is long one futures contract. Yesterday's settlement was 102.40; today's settlement is 103.10. The contract size is 1,000 units. What happens at the end of today?

<details><summary>Answer</summary>

**The gain is 0.70 per unit × 1,000 = 700, paid in cash to the investor's margin account through variation margin.**

The sequence:
1. The position is **marked to market** at today's settlement price of 103.10
2. The gain of 700 is **credited in cash** to the investor's margin account (and debited from the short's)
3. The contract's **value resets to zero**

Tomorrow's gain or loss will be measured from **103.10**, not from the original entry price.

**Contrast with a forward:** the same 0.70 move would have increased the forward's **value** by the discounted equivalent, with **no cash changing hands** until maturity. The gain would accumulate as an unrealised claim on the counterparty — which is exactly the credit exposure daily settlement eliminates.

**The practical cost:** the short must **fund** the 700 in cash today. In a large, fast-moving position this is a real liquidity demand, and it has caused problems for otherwise solvent hedgers.

</details>

**2.** Why are futures prices on interest rate contracts typically above the equivalent forward prices?

<details><summary>Answer</summary>

Because **interest rate futures prices and interest rates are, by construction, correlated** — and the direction of that correlation favours the long.

**The mechanism:** the long futures holder receives cash on days the futures price **rises** and must fund losses on days it falls. For a contract whose price is **positively correlated** with interest rates:

- Gains arrive when rates are **high** → the cash is reinvested at a **favourable** rate
- Losses must be funded when rates are **low** → funding the loss is **cheap**

Both effects work in the long's favour, over and above the contract's economics. The long is therefore willing to pay more for the futures than for the equivalent forward, and the **futures price sits above the forward price**.

**If the correlation were negative**, the reverse: gains would arrive when reinvestment is poor and losses would be funded when borrowing is expensive, so futures would price **below** forwards.

**If rates were constant** — or uncorrelated with the futures price — the daily settlement timing would have no value either way, and the two prices would be **identical**.

**In practice** the difference is small for short maturities but becomes meaningful for long-dated interest rate futures, where the correlation is strong and the effect compounds. This is why long-dated Eurodollar-style futures require a **convexity adjustment** when used to infer forward rates.

</details>

**3.** Explain convergence and basis risk, and why basis risk makes an exchange-traded hedge imperfect.

<details><summary>Answer</summary>

**Convergence:** as a futures contract approaches expiration, its price must converge to the spot price. At expiry the contract **is** a claim on immediate delivery, identical to the spot asset. Any gap would be an instant, riskless arbitrage — buy the cheaper, sell the dearer, settle immediately — so arbitrageurs close it.

**Basis** = Spot price − Futures price. It narrows toward **zero** at expiration.

**Basis risk** is the risk that the basis **does not behave as expected during the life of the hedge**. It arises when:
- The **hedge expiry does not match** the exposure date, so the position must be closed before convergence
- The **hedged asset differs** from the contract's deliverable (hedging jet fuel with crude oil futures, or a specific bond with a Treasury future)
- **Supply and demand** conditions move spot and futures differently — storage constraints, deliverable scarcity, or a squeeze

**Why it makes the hedge imperfect:** the hedger is protected against changes in the **futures price**, but their actual exposure is to the **spot price**. The residual — the change in the basis — is unhedged. A hedge that eliminates price risk therefore **converts it into basis risk**, which is usually much smaller but is not zero.

**The practical implication:** basis risk is the price of standardisation. It is the main reason a corporate treasurer with a precise, dated exposure prefers a **customised forward** (LM1), accepting counterparty risk to eliminate basis risk.

</details>

**4.** A trader holds a large short futures position when the contract goes limit down for three consecutive days. What is the problem?

<details><summary>Answer</summary>

Wait — a **short** position **gains** when the price falls, so limit down is favourable for them. Let me restate the dangerous case: a trader holding a **long** position when the contract goes **limit down** is trapped.

**The problem with a limit move against you:**

**(1) You cannot exit.** When the contract hits its daily price limit, trading effectively stops at that price. There are no buyers at the limit price — everyone wants out in the same direction. The position cannot be closed **at any price**.

**(2) Margin calls continue.** The position is still marked to market at the limit price each day, and **variation margin must be paid in cash**. The trader is funding losses on a position they cannot exit.

**(3) The true loss may be larger than the marks show.** If the market would have fallen 15% but the limit is 5%, the position is being marked at an artificially favourable price. The remaining loss arrives on subsequent days, one limit at a time.

**(4) Liquidity, not solvency, is what kills.** A trader who could survive the eventual loss may still fail because they cannot fund three consecutive days of margin calls. This is the mechanism by which **credit risk becomes liquidity risk** in cleared markets (LM1).

**The lesson:** price limits protect the *market* from disorderly trading, not individual participants from loss. They can turn a bad position into a fatal one by removing the exit while keeping the cash demands.

</details>

---

## Done when

- [ ] I can state that futures and forwards share the same pricing formula
- [ ] I can explain the daily value reset and compute a futures position's value between settlements
- [ ] I can state the correlation effect and get the direction right
- [ ] I can explain why futures and forward prices are equal under constant rates
- [ ] I can define convergence, basis, and basis risk, and explain why hedges are imperfect
- [ ] I can explain how price limits can trap a position
- [ ] I can reproduce the forward-vs-futures comparison table
- [ ] I answered the self-check cold, several days after first study

---

← [LM05 Pricing and Valuation of Forward Contracts and for an Underlying with Varying Maturities](lm-05-pricing-and-valuation-of-forward-contracts-and-for-an-underl.md)  ·  [Topic index](README.md)  ·  [LM07 Pricing and Valuation of Interest Rate and Other Swaps](lm-07-pricing-and-valuation-of-interest-rate-and-other-swaps.md) →
