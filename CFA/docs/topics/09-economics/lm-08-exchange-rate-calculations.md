# ECON · LM08 — Exchange Rate Calculations

## At a glance

| | |
| --- | --- |
| **Topic** | Economics (6-9% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM7 (quote conventions), QM LM4 (no-arbitrage), Derivatives LM4 (cost of carry). |
| **Where it shows up** | 2 questions. Cross-rates and forward points are among the most reliable calculations on the exam. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate and interpret currency cross-rates
- explain the arbitrage relationship between spot and forward exchange rates and interest rates, calculate a forward rate using points or in percentage terms, and interpret a forward discount or premium

---

## Core concepts

### Cross-rates

A **cross-rate** is an exchange rate between two currencies derived from each one's rate against a
third — usually the US dollar.

**The method: arrange the quotes so the common currency cancels.**

```
If you have   A/B  and  B/C,   then   A/C = (A/B) × (B/C)
```

**Worked example.** USD/EUR = 1.10 and JPY/USD = 150. Find JPY/EUR.

```
JPY/EUR = (JPY/USD) × (USD/EUR) = 150 × 1.10 = 165
```

Check the cancellation: `(JPY/USD) × (USD/EUR)` — the USD terms cancel, leaving JPY/EUR. One euro
costs 165 yen.

**When the common currency is in the wrong position, invert one quote first.**

**Worked example.** USD/EUR = 1.10 and USD/GBP = 1.28. Find EUR/GBP.

```
Both have USD as the PRICE currency, so they will not cancel directly.
Invert the first:  EUR/USD = 1/1.10 = 0.9091

EUR/GBP = (EUR/USD) × (USD/GBP) = 0.9091 × 1.28 = 1.1636
```

One pound costs 1.1636 euros.

> **The reliable method: write the quotes as fractions and check that the unwanted currency cancels
> diagonally.** If it does not, invert one of them. Never try to do this in your head — write it
> down, every time.

**With bid-ask spreads:** to buy the base currency of the cross, you use the **ask** side of each
constituent leg. Multiply the **bids** together for the cross bid, and the **asks** together for the
cross ask. The cross spread is always **wider** than either constituent spread.

### Forward exchange rates and covered interest rate parity

**The no-arbitrage relationship** (QM LM4, Derivatives LM4):

```
F(P/B) = S(P/B) × (1 + r_price × days/360) / (1 + r_base × days/360)
```

Or, for annual periods:

```
F = S × (1 + r_price) / (1 + r_base)
```

> **The mnemonic: the PRICE currency's rate goes on TOP.** The forward rate adjusts the spot rate by
> the **ratio of the two interest rates**, with the price currency's rate in the numerator.

**Why it must hold — the arbitrage.** Two routes to holding the price currency in one year:

1. **Invest domestically:** hold the price currency and earn `r_price`
2. **Convert, invest abroad, convert back:** convert to the base currency at S, earn `r_base`, and
   convert back at the forward rate F agreed today

Both are **riskless** (the forward rate is locked in today). They must therefore produce identical
returns, or an arbitrage exists. Rearranging gives the formula.

> **This is exactly the cash-and-carry argument from Derivatives LM4**, applied to currencies. If F
> is too high, borrow the base currency, convert to price, invest, and sell forward — a riskless
> profit. Arbitrage forces F back to the parity level.

### Forward premium and discount

```
Forward premium/discount (in points) = F − S
Forward premium/discount (%)         = (F − S) / S
```

> **The rule that follows directly from the formula:**
>
> **The currency with the HIGHER interest rate trades at a FORWARD DISCOUNT.**
> **The currency with the LOWER interest rate trades at a FORWARD PREMIUM.**
>
> **Why:** if it were otherwise, you could borrow the low-rate currency, invest in the high-rate one,
> and lock in the conversion back with a forward — capturing the rate differential with no risk.
> The forward rate must move to eliminate exactly that opportunity.

**Applying it to the quote.** In a P/B quote, `F > S` means it takes **more** price currency to buy
one base currency forward — so the **base currency is at a forward premium** and the **price currency
is at a forward discount**.

Since the price currency's rate is in the **numerator**, a **higher price-currency rate raises F**
— putting the price currency at a discount. Consistent, as it must be.

### Forward points

Forward rates are quoted in **points** rather than as outright rates. The points must be **scaled**
before being added to the spot rate, and the scaling depends on the quote's decimal convention.

```
Forward rate = Spot rate + (Forward points / Scaling factor)
```

| Currency pair type | Typical decimals | Scaling factor |
| --- | --- | --- |
| Most pairs (e.g. USD/EUR = 1.1050) | 4 decimals | **10,000** |
| JPY pairs (e.g. JPY/USD = 150.25) | 2 decimals | **100** |

**Worked example.** Spot USD/EUR = 1.1050 and the 3-month forward points are **+85**.

```
Forward rate = 1.1050 + 85/10,000 = 1.1050 + 0.0085 = 1.1135
```

The EUR (base) is at a **forward premium** of 85 points — so EUR interest rates must be **lower**
than USD rates.

**Worked example with negative points.** Spot JPY/USD = 150.00 and the 6-month points are **−120**.

```
Forward rate = 150.00 + (−120/100) = 150.00 − 1.20 = 148.80
```

The USD (base) is at a **forward discount** — so USD rates are **higher** than JPY rates.

> **The scaling factor is where marks are lost.** Match the points to the **decimal convention of
> the quote**: 4-decimal quotes scale by 10,000; JPY quotes, normally quoted to 2 decimals, scale by
> 100. Getting this wrong gives an answer that is out by a factor of 100.

### Uncovered interest rate parity — and why it fails

**Covered** interest rate parity (above) involves a **forward contract**, so it is riskless and holds
by arbitrage.

**Uncovered** interest rate parity makes the same prediction without the forward — that the
**expected** change in the spot rate equals the interest differential:

```
Expected % change in the spot rate ≈ r_price − r_base
```

> **Uncovered parity does NOT reliably hold.** Empirically, high-interest-rate currencies have
> tended to **appreciate**, or at least to depreciate by **less** than the interest differential —
> which is the opposite of the prediction. This is the **forward rate bias**, and it is the basis of
> the **carry trade**: borrowing in a low-rate currency and investing in a high-rate one, capturing
> the differential.
>
> The carry trade is **not arbitrage** — it is an unhedged position exposed to currency risk. It
> produces **steady small gains punctuated by occasional large losses** when the funding currency
> appreciates sharply, which is the negatively skewed, option-like payoff of QM LM5 and Alternative
> Investments LM6.

---

## Formulas to know cold

```
CROSS-RATES — arrange so the common currency CANCELS
  Given A/B and B/C:   A/C = (A/B) × (B/C)
  If the common currency is in the wrong position, INVERT one quote first.
  WRITE IT DOWN — never do this in your head.

  With bid-ask: multiply the BIDS for the cross bid, the ASKS for the cross ask.
  The cross spread is always WIDER than either constituent spread.

COVERED INTEREST RATE PARITY
  F(P/B) = S(P/B) × (1 + r_price × days/360) / (1 + r_base × days/360)
  Annual:  F = S × (1 + r_price) / (1 + r_base)

  MNEMONIC: the PRICE currency's rate goes on TOP.

FORWARD PREMIUM / DISCOUNT
  Points:  F − S          Percent:  (F − S)/S

  THE CURRENCY WITH THE HIGHER INTEREST RATE TRADES AT A FORWARD DISCOUNT.
  The currency with the LOWER rate trades at a forward PREMIUM.
  (Otherwise you could borrow low, invest high, and lock the conversion back — riskless profit.)

FORWARD POINTS — scaling is where marks are lost
  Forward rate = Spot + (Points / Scaling factor)
     4-decimal quotes (most pairs)  → divide by 10,000
     JPY quotes (2 decimals)        → divide by 100

  e.g. Spot USD/EUR 1.1050, points +85  →  1.1050 + 85/10,000 = 1.1135
       Spot JPY/USD 150.00, points −120 →  150.00 − 120/100  = 148.80

UNCOVERED interest rate parity (NO forward contract) does NOT reliably hold.
  Expected % change in spot ≈ r_price − r_base
  Empirically high-rate currencies have APPRECIATED → the FORWARD RATE BIAS
  → the basis of the CARRY TRADE, which is NOT arbitrage and carries currency risk.
```

---

## Exam traps

> **Trap 1 — Misidentifying the base currency.** In **P/B**, the base is the **second** currency.
> Establish this before any calculation.

> **Trap 2 — Cross-rate multiplication without checking cancellation.** **Write the quotes as
> fractions** and verify the unwanted currency cancels. If it does not, invert one first.

> **Trap 3 — Forward points scaling.** Divide by **10,000** for 4-decimal quotes and by **100** for
> JPY. Getting this wrong is out by a factor of 100.

> **Trap 4 — Inverting the parity formula.** The **PRICE currency's rate goes on TOP**.

> **Trap 5 — Forward premium/discount direction.** The **HIGHER-rate currency trades at a
> DISCOUNT**. Candidates routinely assume the opposite.

> **Trap 6 — Ignoring day-count.** For periods under a year use `× days/360`. Applying the annual
> formula to a 90-day forward overstates the adjustment fourfold.

> **Trap 7 — Confusing covered and uncovered parity.** **Covered** involves a forward and holds by
> **arbitrage**. **Uncovered** has no forward and does **not** reliably hold.

> **Trap 8 — Treating the carry trade as arbitrage.** It is an **unhedged** position with real
> currency risk and a negatively skewed payoff.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Given USD/EUR = 1.0850 and USD/CHF = 0.8920, compute the CHF/EUR cross-rate.

<details><summary>Answer</summary>

Both quotes have **USD as the price currency**, so they will not cancel directly. Invert one.

Invert the second: **CHF/USD** = 1/0.8920 = **1.12108**

Now the USD cancels:
```
CHF/EUR = (CHF/USD) × (USD/EUR) = 1.12108 × 1.0850 = 1.2164
```

**One euro costs 1.2164 Swiss francs.**

**Check the cancellation explicitly:** (CHF/USD) × (USD/EUR) — the USD appears once in the denominator and once in the numerator, so it cancels, leaving CHF/EUR. ✓

**The method that always works:** write both quotes as fractions, identify which currency must cancel, and invert whichever quote has it in the wrong position. Then multiply.

</details>

**2.** Spot USD/GBP = 1.2600. US rates are 5.2% and UK rates are 4.4%, both annual. Compute the 6-month forward rate and state which currency is at a premium.

<details><summary>Answer</summary>

**GBP is the base; USD is the price.** The price currency's rate goes on top.

For 6 months, use `× 180/360 = 0.5`:

```
F = 1.2600 × [1 + 0.052 × 0.5] / [1 + 0.044 × 0.5]
  = 1.2600 × (1.0260) / (1.0220)
  = 1.2600 × 1.003914
  = 1.2649
```

**F (1.2649) > S (1.2600)**, so it takes **more** dollars to buy a pound forward.

- **GBP (the base) is at a forward PREMIUM** — 49 points, or (1.2649 − 1.2600)/1.2600 = **+0.39%**
- **USD (the price) is at a forward DISCOUNT**

**Consistency check:** the **USD has the HIGHER rate** (5.2% vs 4.4%), and the higher-rate currency trades at a **forward discount**. ✓

The intuition: you earn more interest holding dollars, so the forward market must make dollars cheaper to buy forward — otherwise you could borrow pounds, invest in dollars, and lock in the conversion back for a riskless profit.

</details>

**3.** Spot JPY/USD = 148.50 and the 3-month forward points are −95. Compute the forward rate and say which currency has higher interest rates.

<details><summary>Answer</summary>

**JPY quotes are conventionally to 2 decimals, so the scaling factor is 100** (not 10,000).

```
Forward rate = 148.50 + (−95/100) = 148.50 − 0.95 = 147.55
```

**F (147.55) < S (148.50)**, so it takes **fewer** yen to buy a dollar forward.

- **USD (the base) is at a forward DISCOUNT**
- **JPY (the price) is at a forward PREMIUM**

**Therefore USD interest rates are HIGHER than JPY rates** — the higher-rate currency trades at a forward discount.

**Why the scaling factor matters:** dividing by 10,000 instead of 100 would give 148.4905 — barely different from spot, and wrong by a factor of 100 in the adjustment. **Always match the scaling to the quote's decimal convention.**

</details>

**4.** Explain why covered interest rate parity holds but uncovered parity does not.

<details><summary>Answer</summary>

**Covered interest rate parity holds because it is enforced by ARBITRAGE.**

The 'covered' element is the **forward contract**, which locks in the future conversion rate **today**. This makes both investment routes completely riskless:
1. Invest domestically at `r_price`
2. Convert at spot, invest abroad at `r_base`, convert back at the **agreed** forward rate F

Both outcomes are known with certainty at the outset. If they differed, a trader could borrow in one currency, invest in the other, and lock in the conversion back — capturing the difference with **no capital at risk and no uncertainty**. Arbitrageurs would execute this until the prices converged.

This is the **cash-and-carry argument of Derivatives LM4** applied to currencies. It holds tightly in practice, with deviations limited to transaction costs and, in stressed markets, to funding constraints.

**Uncovered parity does NOT hold because there is no arbitrage to enforce it.**

Uncovered parity predicts that the **expected** spot change equals the interest differential:
```
Expected % change in spot ≈ r_price − r_base
```

There is **no forward contract** — the position is unhedged. If the prediction fails, there is no riskless trade to correct it, only a **speculative position with genuine currency risk**. Nothing forces the relationship to hold.

**And empirically it fails in a specific direction:** high-interest-rate currencies have tended to **appreciate**, or to depreciate by **less** than the differential. This is the **forward rate bias**, and it is the basis of the **carry trade**.

**Why the carry trade is not free money:** it produces steady small gains punctuated by **occasional large losses** when the funding currency appreciates sharply in a risk-off episode. The payoff is negatively skewed and option-like (QM LM5) — the return is compensation for bearing crash risk, not an arbitrage.

</details>

---

## Done when

- [ ] I can compute any cross-rate by writing the quotes as fractions and checking cancellation
- [ ] I can compute cross bid-ask from constituent bid-ask quotes
- [ ] I can apply covered interest rate parity with the price currency's rate on top
- [ ] I can state and explain why the higher-rate currency trades at a forward discount
- [ ] I can compute a forward rate from points with the correct scaling factor for any pair
- [ ] I can handle day-count adjustment for periods under a year
- [ ] I can explain why covered parity holds and uncovered parity does not
- [ ] I can explain the carry trade and why it is not arbitrage
- [ ] I answered the self-check cold, several days after first study

---

← [LM07 Capital Flows and the FX Market](lm-07-capital-flows-and-the-fx-market.md)  ·  [Topic index](README.md)
