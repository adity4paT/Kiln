# FI · LM09 — The Term Structure of Interest Rates: Spot, Par, and Forward Curves

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM6 (bond pricing), QM LM4 (no-arbitrage forward rates). |
| **Where it shows up** | 2–3 questions. Forward rate calculation and the spot/par/forward relationship are near-certain. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- define spot rates and the spot curve, and calculate the price of a bond using spot rates
- define par and forward rates, and calculate par rates, forward rates from spot rates, spot rates from forward rates, and the price of a bond using forward rates
- compare the spot curve, par curve, and forward curve

---

## Core concepts

### Three curves, three questions

| Curve | Definition | Answers |
| --- | --- | --- |
| **Spot curve** (zero curve) | The yields on **zero-coupon** bonds of each maturity | "What is the rate for a single cash flow at time t?" |
| **Par curve** | The **coupon rates** at which bonds of each maturity would price **at par** | "What coupon must I offer today to issue at par?" |
| **Forward curve** | Rates for periods **beginning in the future**, implied by today's spot rates | "What rate is the market implying for a loan starting later?" |

All three are derived from the same underlying information — they are different views of one term
structure, not independent objects.

### Spot rates

A **spot rate** `z_t` is the yield on a zero-coupon bond maturing at time `t`. Because a zero has a
single cash flow, its yield is unambiguous — there is no reinvestment assumption and no coupon
timing effect.

**Pricing a bond with spot rates** — the theoretically correct method:

```
PV = C/(1+z1)¹ + C/(1+z2)² + ... + (C + F)/(1+zN)^N
```

Each cash flow is discounted at **its own** rate, reflecting the actual term structure. The **yield
to maturity** is the single rate that produces the same price — a complex weighted average of the
spot rates, dominated by the maturity where most of the value sits.

> **Why the distinction matters:** with an upward-sloping curve, a bond's YTM sits **below** the
> spot rate at its maturity, because the earlier coupons are discounted at lower short-term rates.
> Two bonds with the same maturity but different coupons will have **different YTMs** even though
> they face the identical term structure — which is why the spot curve, not the YTM curve, is the
> correct foundation for valuation.

**Bootstrapping the spot curve** from par rates: start with the shortest maturity (where the par
rate equals the spot rate) and work forward, solving each maturity's spot rate given the ones
already known.

### Par rates

A **par rate** is the coupon rate that makes a bond of that maturity price exactly at par.

```
100 = PR/(1+z1)¹ + PR/(1+z2)² + ... + (PR + 100)/(1+zN)^N
```

Solve for `PR`. Equivalently, for an N-period bond:

```
PR = [1 − 1/(1+zN)^N] / [Σ 1/(1+zt)^t]  × 100
```

**The relationships between the curves:**

| Spot curve shape | Par curve position | Forward curve position |
| --- | --- | --- |
| **Upward sloping** | **Below** the spot curve | **Above** the spot curve |
| **Flat** | Equal to the spot curve | Equal to the spot curve |
| **Downward sloping** | **Above** the spot curve | **Below** the spot curve |

> **Memorise this ordering.** With an upward-sloping curve: **forward > spot > par.** The intuition
> is that the forward rate must exceed the spot rate to pull the average up, and the par rate sits
> below the spot rate because a coupon bond's early payments are discounted at lower short rates.

### Forward rates

A **forward rate** `F(A,B)` is the rate agreed **today** for a loan of `B` periods **beginning in
`A` periods**.

**The no-arbitrage relationship** (QM LM4) — investing for the long period must equal investing
short and rolling forward:

```
(1 + z_A)^A × (1 + F(A,B))^B = (1 + z_(A+B))^(A+B)
```

Rearranged:

```
F(A,B) = [ (1 + z_(A+B))^(A+B) / (1 + z_A)^A ]^(1/B) − 1
```

**Notation warning:** the curriculum writes `F(A,B)` as the rate for a **B-period** loan beginning in
**A** periods. So `F(2,1)` is the **one-year** rate, **two years forward**. Read the question
carefully — some sources reverse the convention.

**Worked example.** `z1 = 3.0%`, `z2 = 3.8%`, `z3 = 4.3%`.

```
F(1,1) = (1.038)²/(1.030) − 1 = 1.077444/1.030 − 1 = 4.607%
F(2,1) = (1.043)³/(1.038)² − 1 = 1.134626/1.077444 − 1 = 5.307%
F(1,2) = [(1.043)³/(1.030)]^(1/2) − 1 = [1.101579]^(0.5) − 1 = 4.956%
```

**Pricing a bond with forward rates:**

```
PV = C/(1+z1) + C/[(1+z1)(1+F(1,1))] + (C+F)/[(1+z1)(1+F(1,1))(1+F(2,1))]
```

This gives **exactly the same price** as discounting at spot rates — the two are algebraically
identical, since the product of forward rates *is* the spot rate compounded.

### Interpreting the forward curve

Forward rates are **not forecasts.** They are the rates that make the market indifferent between two
investment paths — a no-arbitrage construction, not a prediction.

Under the **pure expectations hypothesis**, forward rates *would* equal expected future spot rates.
In practice they are widely observed to **exceed** expected future rates, because they embed a
**term premium** — compensation for the greater price risk of longer maturities.

> **The practical implication:** an upward-sloping curve implying forward rates well above current
> spots does **not** necessarily mean the market expects rates to rise that much. It may simply mean
> investors demand a premium for duration. Reading the forward curve as a rate forecast is a
> standard error.

**A useful trading intuition:** if you believe future spot rates will be **lower** than today's
forward rates imply, long-dated bonds are attractive — you are being paid a forward rate you do not
expect to materialise. The reverse if you expect rates above the forwards.

### Yield curve shapes and their names

| Shape | Description | Common interpretation |
| --- | --- | --- |
| **Upward sloping (normal)** | Long rates above short | Expected growth, or a term premium, or both |
| **Flat** | Similar across maturities | Transition |
| **Inverted** | Short rates **above** long | Historically associated with expectations of monetary easing, often preceding recessions |
| **Humped** | Rises then falls | Mixed expectations |

**Swap curve.** In many markets the **swap rate curve** rather than the government curve is used as
the benchmark for pricing corporate and derivative cash flows — it is available at more maturities,
is not distorted by government supply and demand or regulatory buying, and reflects bank credit. The
**swap spread** (swap rate minus government yield of the same maturity) is itself a widely watched
indicator of credit and liquidity conditions.

---

## Formulas to know cold

```
SPOT RATES — pricing a bond
  PV = C/(1+z1)¹ + C/(1+z2)² + ... + (C+F)/(1+zN)^N
  Each cash flow discounted at ITS OWN rate. YTM is the single rate giving the same price.

PAR RATE — the coupon that prices the bond at par
  100 = PR/(1+z1)¹ + ... + (PR + 100)/(1+zN)^N   → solve for PR

FORWARD RATES — the no-arbitrage relationship
  (1 + z_A)^A × (1 + F(A,B))^B = (1 + z_(A+B))^(A+B)

  F(A,B) = [ (1 + z_(A+B))^(A+B) / (1 + z_A)^A ]^(1/B) − 1

  NOTATION: F(A,B) = the B-PERIOD rate beginning in A periods.
            F(2,1) = the ONE-year rate, TWO years forward.

PRICING WITH FORWARD RATES (identical result to spot rates)
  PV = C/(1+z1) + C/[(1+z1)(1+F(1,1))] + (C+F)/[(1+z1)(1+F(1,1))(1+F(2,1))]

CURVE ORDERING
  Upward-sloping spot curve:   FORWARD  >  SPOT  >  PAR
  Flat:                        all three equal
  Downward-sloping:            FORWARD  <  SPOT  <  PAR
```

---

## Exam traps

> **Trap 1 — Forward rate notation.** `F(A,B)` is the **B-period** rate beginning in **A** periods.
> `F(2,1)` is the one-year rate two years forward, **not** the two-year rate one year forward. Read
> the question.

> **Trap 2 — Inverting the no-arbitrage relationship.** `(1+z_A)^A × (1+F)^B = (1+z_(A+B))^(A+B)`.
> The **longer** spot rate is on the right, compounded over the **total** period.

> **Trap 3 — Treating forward rates as forecasts.** They are **no-arbitrage** constructions that
> embed a **term premium**. Forwards systematically exceed realised future spot rates.

> **Trap 4 — The curve ordering.** With an **upward-sloping** curve: **forward > spot > par**.
> Getting this backwards is common and costs qualitative questions.

> **Trap 5 — Confusing YTM with the spot rate at that maturity.** With an upward-sloping curve a
> coupon bond's YTM is **below** the spot rate at its maturity, because earlier coupons are
> discounted at lower rates.

> **Trap 6 — Forgetting that two bonds of the same maturity can have different YTMs.** Different
> coupons mean different weightings across the spot curve. This is why the spot curve, not a YTM
> curve, is the correct valuation foundation.

> **Trap 7 — Taking the B-th root.** `F(A,B)` requires `^(1/B)`. Omitting it when B > 1 gives a
> compounded rate rather than an annualised one.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Spot rates are z1 = 2.4%, z2 = 3.1%, z3 = 3.6%. Compute F(1,1), F(2,1), and F(1,2).

<details><summary>Answer</summary>

**F(1,1)** — the one-year rate, one year forward:
(1.031)²/(1.024) − 1 = 1.062961/1.024 − 1 = 1.038048 − 1 = **3.805%**

**F(2,1)** — the one-year rate, two years forward:
(1.036)³/(1.031)² − 1 = 1.111934/1.062961 − 1 = 1.046072 − 1 = **4.607%**

**F(1,2)** — the **two**-year rate, one year forward:
[(1.036)³/(1.024)]^(1/2) − 1 = [1.085873]^(0.5) − 1 = 1.042052 − 1 = **4.205%**

Note the `^(1/2)` in the last one — F(1,2) covers **two** periods, so the B-th root is required to annualise it. Omitting it is the standard error.

</details>

**2.** Explain why the par curve lies below the spot curve when the spot curve is upward sloping.

<details><summary>Answer</summary>

A **par bond** pays coupons throughout its life, not just at maturity. Those earlier coupons are discounted at the **shorter, lower** spot rates.

The par rate is the single coupon rate that makes the bond price at 100. Because a meaningful share of the bond's cash flows is discounted at rates **below** the maturity spot rate, the coupon needed to reach par is **less than** the maturity spot rate.

**Contrast with a zero-coupon bond:** all of its value sits at maturity, discounted entirely at `zN`. Its yield *is* `zN`.

So with an upward-sloping curve: **par < spot**. And the forward rate must sit **above** the spot rate, because the spot rate is a geometric average of the forwards along the way and an average can only rise if later terms exceed it.

**Full ordering, upward-sloping curve: forward > spot > par.** With a downward-sloping curve every inequality reverses. With a flat curve all three coincide.

</details>

**3.** The 5-year spot rate is 4.2%. The forward curve implies the one-year rate five years forward is 5.6%. Does the market expect the one-year rate to be 5.6% in five years?

<details><summary>Answer</summary>

**Not necessarily — and probably not.**

The forward rate is a **no-arbitrage** construction: it is the rate that makes an investor indifferent between (a) investing for six years at the six-year spot rate and (b) investing for five years and rolling into a one-year investment. It is derived entirely from today's spot curve, with no forecasting content of its own.

Under the **pure expectations hypothesis**, forwards would equal expected future spot rates. But empirically, forward rates **systematically exceed** realised future spot rates, because they embed a **term premium** — compensation investors demand for the greater price risk of holding longer maturities.

So a forward of 5.6% might decompose into, say, an expected future spot of 4.9% plus a 70bp term premium.

**The practical implication:** an upward-sloping curve does not mean the market is forecasting large rate rises. It may mean investors want paying for duration. Reading forwards as forecasts is one of the more consequential errors in fixed income, and it leads directly to the conclusion that the curve is 'wrong' when it is doing something else entirely.

</details>

**4.** Price a 3-year 5% annual-coupon bond (face 100) using spot rates z1 = 2.4%, z2 = 3.1%, z3 = 3.6%. Then state what its YTM would be relative to z3.

<details><summary>Answer</summary>

```
5 / 1.024          = 4.8828
5 / (1.031)²       = 5 / 1.062961 = 4.7038
105 / (1.036)³     = 105 / 1.111934 = 94.4297
                     --------
Price                104.0163
```
**Price = 104.02.**

**YTM relative to z3:** the YTM will be **below 3.6%**.

Why: the bond's first two coupons are discounted at 2.4% and 3.1% — rates **below** z3. The YTM is the single rate that reproduces this price, so it must be a weighted average of the three spot rates, pulled below 3.6% by the earlier, lower ones.

(Solving: N=3, PV=−104.0163, PMT=5, FV=100 → I/Y ≈ **3.56%**, just below z3 = 3.6%, as expected. The gap is small here because most of the value sits in the final cash flow.)

</details>

**5.** Why is the swap curve often preferred to the government curve as a pricing benchmark?

<details><summary>Answer</summary>

Several reasons, all practical:

**(1) Availability at more maturities.** Swap rates are quoted continuously across a dense grid of maturities. Government curves have gaps where no bond has been issued, requiring interpolation.

**(2) Not distorted by supply and demand for specific issues.** Government bonds are subject to **special** demand (LM4), regulatory buying by banks and insurers, central bank purchases, and on-the-run/off-the-run liquidity effects (LM3). These push individual government yields away from the underlying term structure. Swaps have no fixed supply.

**(3) Reflects bank credit rather than sovereign credit**, which is closer to the funding cost of most market participants and therefore a more natural discounting basis for corporate and derivative cash flows.

**(4) Comparable across countries** where government bond markets differ in depth and structure.

**The swap spread** — swap rate minus the government yield at the same maturity — is itself watched closely as an indicator of bank credit and liquidity conditions. It widens in stress.

</details>

---

## Done when

- [ ] I can define spot, par, and forward rates and say what question each answers
- [ ] I can price a bond with spot rates and explain why its YTM differs from the maturity spot rate
- [ ] I can compute any forward rate from spot rates, including the B-th root when B > 1
- [ ] I can state the forward > spot > par ordering for an upward-sloping curve and explain why
- [ ] I can explain why forward rates are not forecasts and what a term premium is
- [ ] I can price a bond with forward rates and show it equals the spot-rate price
- [ ] I can explain why the swap curve is often preferred as a benchmark
- [ ] I answered the self-check cold, several days after first study

---

← [LM08 Yield and Yield Spread Measures for Floating-Rate Instruments](lm-08-yield-and-yield-spread-measures-for-floating-rate-instrument.md)  ·  [Topic index](README.md)  ·  [LM10 Interest Rate Risk and Return](lm-10-interest-rate-risk-and-return.md) →
