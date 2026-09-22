# EQ · LM06 — Discounted Cash Flow (DCF) and Growth Models

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 12 |
| **Prerequisites** | QM LM4 (Gordon growth, multistage), FSA LM5 (FCFF/FCFE), Corporate Issuers LM6 (WACC). |
| **Where it shows up** | 3 questions — the largest allocation in Equity. Gordon growth and multistage models are certainties. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- contrast the inputs used in dividend discount, free cash flow to equity (FCFE), free cash flow to the firm (FCFF), and residual income models, and explain the process for using present value models to value equity
- calculate and interpret the intrinsic value of an equity security based on present value models that assume constant cash flow growth or multistage cash flow growth
- explain the shortcomings of constant and multistage cash flow growth assumptions in present value models
- calculate the intrinsic value of a non-callable, non-convertible preferred stock and describe how contingency features affect intrinsic value

---

## Core concepts

### The four models and their matching discount rates

**Getting this pairing right decides more questions than any other single fact in Equity.**

| Model | Cash flow | Discount rate | Produces |
| --- | --- | --- | --- |
| **DDM** | Dividends | **Cost of equity (re)** | Equity value directly |
| **FCFE** | Free cash flow to equity | **Cost of equity (re)** | Equity value directly |
| **FCFF** | Free cash flow to the firm | **WACC** | **Enterprise value** — subtract net debt for equity |
| **Residual income** | Book value + PV of economic profits | **Cost of equity (re)** | Equity value directly |

```
FCFF = CFO + Interest × (1 − t) − Capex
FCFE = CFO − Capex + Net borrowing
FCFE = FCFF − Interest × (1 − t) + Net borrowing
```

**When to use which:**

| Situation | Model |
| --- | --- |
| Stable, mature, reliable dividend payer; **minority** stake | **DDM** — a minority holder actually receives dividends, not free cash flow |
| Company pays no dividend, or dividends bear no relation to earnings capacity | **FCFE** |
| Leverage is high or changing; a **control** perspective | **FCFF** — it is capital-structure independent |
| Free cash flow is persistently negative; book value is meaningful | **Residual income** |

> **The control point matters.** A minority shareholder can only extract cash the board chooses to
> distribute, so dividends are the relevant flow. An acquirer taking control can change the payout
> policy, so free cash flow is the relevant flow.

### The Gordon (constant) growth model

```
V0 = D1 / (r − g)          where D1 = D0 × (1 + g)
```

**Requirements, all of which must hold:**
- Dividends grow at a **constant rate forever**
- **`g` < `r`** — mandatory. If `g ≥ r` the formula returns a negative or infinite value
- The company is **mature and stable**

**Rearranged forms — both are directly examinable:**

```
r = D1/P0 + g          (implied required return = dividend yield + growth)
g = r − D1/P0          (implied growth the market is pricing)
```

**The sustainable growth rate:**

```
g = b × ROE          where b = retention ratio = 1 − payout ratio
```

This is the growth a company can fund **from retained earnings alone**, without issuing new equity
or increasing leverage. It is the disciplined way to estimate `g` rather than guessing.

> **Extreme sensitivity to `r − g`.** With `r` = 9% and `g` = 5%, the denominator is 4%. Move `g` to
> 6% and the denominator halves to 3% — **value rises 33%**. A one-percentage-point change in an
> unobservable perpetual growth assumption moves the answer by a third. This is why sensitivity
> analysis is not optional, and why reverse-engineering the market's implied `g` is often more
> informative than producing a point estimate.

**Hard constraint on `g`:** the perpetual growth rate cannot exceed **long-run nominal GDP growth**.
A company growing faster than the economy forever eventually becomes the whole economy.

### Multistage models

Real companies grow fast, then slow, then mature. Multistage models handle this.

**Two-stage model:**

```
V0 = Σ [Dt / (1 + r)^t]   +   [D(n+1) / (r − g_long)] / (1 + r)^n
      ─────────────────       ───────────────────────────────────
      explicit high-growth     terminal value, AS OF time n
      dividends, discounted     → discount back n periods
```

> **The single most common error in Equity:** the terminal value `D(n+1)/(r − g)` is a value **as of
> time n**, because the Gordon formula always values a stream **one period before its first cash
> flow**. Discount it back **n** periods — not n+1.

**The H-model** — growth declines **linearly** from an initial high rate `gS` to a long-run rate `gL`
over `2H` years:

```
V0 = [D0 × (1 + gL) + D0 × H × (gS − gL)] / (r − gL)

    = normal-growth value  +  value of the excess growth
```

`H` is **half** the length of the high-growth period. The H-model is more realistic than an abrupt
two-stage drop, because growth rates in practice decay rather than fall off a cliff.

**Three-stage models** add a transition phase between high growth and maturity — growth constant and
high, then declining, then constant and low.

### Shortcomings of the growth assumptions

The LOS asks for these explicitly.

**Constant growth (Gordon):**
- Requires perpetual constant growth, which no real company delivers
- **Breaks entirely when `g ≥ r`**
- Hypersensitive to `r` and `g` — small changes produce large value swings
- Unusable for non-dividend-payers, and misleading for erratic payers
- Assumes a stable payout ratio and stable risk forever

**Multistage:**
- The **transition is arbitrary** — why does high growth end in year 5 rather than year 7? A
  two-stage model imposes an implausible discontinuity
- The **terminal value dominates**, typically 60–80% of total value, so the model is mostly a
  statement about `g_long` and `r` regardless of the effort spent on the explicit years
- More stages means more assumptions, each one a new place to be wrong; the extra precision is
  often false
- Still assumes a constant `r` throughout, when a maturing company's risk should be falling

> **The honest framing:** these models do not produce an answer. They produce a **disciplined
> statement of what you must believe** for a given price to be justified. Used that way — to
> reverse-engineer the market's assumptions and ask whether they are plausible — they are extremely
> useful. Used as a value calculator, they are a machine for dressing up a growth guess as a number.

### Valuing preferred stock

**Non-callable, non-convertible, perpetual preferred** — a level perpetuity:

```
V0 = Dp / r
```

**Preferred with a maturity date** — an annuity plus a redemption value:

```
V0 = Σ [Dp / (1 + r)^t] + Face / (1 + r)^n
```

**How contingency features affect value** — the principle is the same as callable/putable common
stock (LM1): **whoever holds the option pays for it.**

| Feature | Who holds the option | Effect on value to the investor |
| --- | --- | --- |
| **Callable** | **Issuer** | **Lower** — the issuer redeems when rates fall, capping the investor's gain |
| **Putable** | **Investor** | **Higher** — a price floor |
| **Convertible** | **Investor** | **Higher** — participation in equity upside |
| **Cumulative** | **Investor** | **Higher** — missed dividends accrue and must be paid |
| **Participating** | **Investor** | **Higher** — shares in profits above the fixed dividend |

```
Value of callable preferred    = Straight preferred value − Value of the call option
Value of putable preferred     = Straight preferred value + Value of the put option
Value of convertible preferred = Straight preferred value + Value of the conversion option
```

---

## Formulas to know cold

```
MODEL–RATE PAIRING  (the highest-value fact in Equity)
  DDM              → discount at re      → equity value
  FCFE             → discount at re      → equity value
  FCFF             → discount at WACC    → ENTERPRISE value (− net debt = equity)
  Residual income  → discount at re      → equity value

  FCFF = CFO + Interest(1−t) − Capex
  FCFE = CFO − Capex + Net borrowing = FCFF − Interest(1−t) + Net borrowing

GORDON GROWTH
  V0 = D1/(r − g),   D1 = D0(1+g),   REQUIRES g < r
  r  = D1/P0 + g
  g  = r − D1/P0
  Sustainable growth:  g = b × ROE,  b = retention ratio = 1 − payout ratio
  Hard cap: g ≤ long-run nominal GDP growth

TWO-STAGE
  V0 = Σ Dt/(1+r)^t + [D(n+1)/(r − gL)] / (1+r)^n
                       └ terminal value is AS OF time n → discount n periods, not n+1

H-MODEL  (growth declines LINEARLY from gS to gL over 2H years)
  V0 = [D0(1 + gL) + D0 × H × (gS − gL)] / (r − gL)
       └ normal growth ┘  └ excess growth ┘      H = HALF the high-growth period

PREFERRED STOCK
  Perpetual:  V0 = Dp / r
  Maturity:   V0 = Σ Dp/(1+r)^t + Face/(1+r)^n
  Callable    = straight − call option value    (worth LESS)
  Putable     = straight + put option value     (worth MORE)
  Convertible = straight + conversion value     (worth MORE)
```

---

## Exam traps

> **Trap 1 — Discounting FCFF at the cost of equity.** **FCFF pairs with WACC**; FCFE and dividends
> pair with `re`. And FCFF gives **enterprise** value — subtract net debt to reach equity value.

> **Trap 2 — Terminal value discounting.** `D(n+1)/(r−g)` is a value **at time n**. Discount **n**
> periods. This is the most common single error in the module.

> **Trap 3 — D0 instead of D1.** The Gordon numerator is **next** period's dividend:
> `D1 = D0 × (1 + g)`.

> **Trap 4 — `g ≥ r`.** Mathematically invalid. It signals a bad assumption, not an enormous value.

> **Trap 5 — H-model's `H`.** `H` is **half** the high-growth period. A 10-year decline means
> **H = 5**.

> **Trap 6 — Sustainable growth.** `g = b × ROE`, where `b` is the **retention** ratio (1 − payout),
> not the payout ratio.

> **Trap 7 — Using the DDM on a non-payer, or on a controlling stake.** No dividends means no DDM.
> And a **control** perspective calls for FCFF — an acquirer can change the payout policy.

> **Trap 8 — Callable preferred.** The call benefits the **issuer**, so callable preferred is worth
> **less** than otherwise identical straight preferred.

> **Trap 9 — Treating the output as an answer.** These models state what you must believe. Always
> compute the implied `g` at the market price and ask whether it is plausible.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company just paid a dividend of 2.20. Dividends are expected to grow 4.5% forever. The required return is 10%. Compute the value per share, and the implied growth if it trades at 45.

<details><summary>Answer</summary>

D1 = 2.20 × 1.045 = 2.299

V0 = 2.299 / (0.10 − 0.045) = 2.299 / 0.055 = **41.80**

Implied growth at a price of 45:
g = r − D1/P0 = 0.10 − 2.299/45 = 0.10 − 0.0511 = **4.89%**

So at 45 the market prices 4.89% perpetual growth against your 4.5%. The disagreement is 39 basis points of perpetual growth — a specific, arguable difference rather than a bare 'it's overvalued by 7%'. Ask which of you has the better case on long-run growth before acting.

</details>

**2.** Dividends will be 1.50, 1.95, and 2.34 in years 1–3, then grow at 4% forever. The required return is 11%. Compute the value today.

<details><summary>Answer</summary>

**Explicit dividends, discounted:**
```
1.50 / 1.11    = 1.3514
1.95 / 1.11²   = 1.5827
2.34 / 1.11³   = 1.7108
                 ------
                  4.6449
```
**Terminal value at time 3:**
D4 = 2.34 × 1.04 = 2.4336
TV3 = 2.4336 / (0.11 − 0.04) = 2.4336 / 0.07 = **34.766**

Discount **3** periods: 34.766 / 1.11³ = **25.418**

**V0 = 4.645 + 25.418 = 30.06**

Note: the terminal value is **85%** of the total. Whatever care went into the year-2 dividend, this valuation is overwhelmingly a statement about the 4% perpetual growth rate and the 11% required return.

</details>

**3.** A company has ROE of 15% and pays out 40% of earnings. Estimate its sustainable growth rate and explain what the estimate assumes.

<details><summary>Answer</summary>

Retention ratio b = 1 − 0.40 = 0.60

g = b × ROE = 0.60 × 0.15 = **9.0%**

**What it assumes:**
- ROE stays at 15% on the **newly retained** capital, not just on the existing base — often optimistic, since the best projects are usually taken first
- The **payout ratio stays at 40%**
- **No new equity issuance** and **constant leverage** — growth is funded entirely from retained earnings
- Net margin and asset turnover are stable (ROE is itself a DuPont product — FSA LM11)

**The important caveat:** 9% is not sustainable **in perpetuity**. It exceeds long-run nominal GDP growth, so it can only be a **near-term** growth rate. For a terminal value you must step down to something at or below nominal GDP growth — which is exactly why multistage models exist.

</details>

**4.** Explain why the terminal value typically accounts for most of a DCF's total value, and what follows from it.

<details><summary>Answer</summary>

Two compounding reasons.

**(1) The terminal value captures an infinite stream**, while the explicit period captures only 3–10 years. Even discounted, a perpetuity is large relative to a decade of cash flows.

**(2) The `1/(r − g)` multiplier is large.** With r = 9% and g = 4%, the terminal cash flow is multiplied by 20. Small changes in either input move it enormously: raising g to 5% makes the multiplier 25 — a **25% increase in terminal value** from one percentage point of an unobservable perpetual assumption.

**What follows:**
- **Allocate effort accordingly.** Spending four weeks on the explicit forecast and ten minutes on `g` misallocates attention by an order of magnitude.
- **Always sensitivity-test `g` and `r`** and present a range, not a point.
- **Cross-check the terminal value** against an exit multiple: what EV/EBITDA does your terminal value imply? If it implies 22× in a sector where mature companies trade at 9×, the assumption is wrong however carefully you derived it.
- **Cap `g` at long-run nominal GDP growth**, always.

</details>

**5.** Compute the value of a share using the H-model: D0 = 3.00, current growth 18% declining linearly to 5% over 12 years, required return 11%.

<details><summary>Answer</summary>

H = 12/2 = **6** (H is half the decline period).

V0 = [D0(1 + gL) + D0 × H × (gS − gL)] / (r − gL)
   = [3.00(1.05) + 3.00 × 6 × (0.18 − 0.05)] / (0.11 − 0.05)
   = [3.15 + 3.00 × 6 × 0.13] / 0.06
   = [3.15 + 2.34] / 0.06
   = 5.49 / 0.06
   = **91.50**

Reading the decomposition: 3.15/0.06 = **52.50** is the value if the company grew at only 5% forever; 2.34/0.06 = **39.00** is the value of the **excess growth** during the decline. The excess growth is 43% of the total — and that share is the part of the valuation most at risk if growth decays faster than assumed.

</details>

**6.** Why would an acquirer taking control value a company with FCFF while a minority investor uses the DDM?

<details><summary>Answer</summary>

Because **what each party can actually extract differs**.

A **minority shareholder** has no influence over the payout policy. They receive only what the board chooses to distribute — **dividends**. Valuing them on free cash flow they cannot access would overstate what the stake is worth to them.

An **acquirer taking control** can change the dividend policy, alter the capital structure, and redirect the cash. The relevant flow is the **free cash flow of the business**, not the historical distribution. **FCFF** is the right measure because it is **capital-structure independent** — the acquirer may refinance entirely, so valuing the operations before financing decisions is correct.

This is also why control stakes trade at a **control premium** over the minority price: the controlling holder has access to a cash flow stream the minority does not. The two valuations are both correct for their respective perspectives.

</details>

**7.** A preferred share pays a fixed dividend of 4.50 and the required return is 7.5%. Value it. Then explain how a call feature at 55 would change your answer.

<details><summary>Answer</summary>

**Straight perpetual preferred:** V0 = 4.50 / 0.075 = **60.00**

**With a call feature at 55:** the value is **lower than 60**.

The issuer will call when it is advantageous to them — specifically when required returns **fall**, making the 4.50 dividend expensive relative to what they could issue at now. That is precisely when the straight value would have risen above 60, so the call **caps the investor's upside** at around 55 plus accrued.

```
Callable value = Straight value − Call option value = 60.00 − (option value)
```

The investor is short a call option to the issuer and must be compensated for it, so callable preferred trades at a lower price and a **higher yield** than otherwise identical straight preferred.

The symmetric point: a **putable** feature (investor's option) or a **conversion** feature (investor's option) would make it worth **more** than 60. The rule throughout: whoever holds the option pays for it.

</details>

---

## Done when

- [ ] I can state the four models with their correct discount rates and what each produces
- [ ] I can apply the Gordon growth model and rearrange it for implied return and implied growth
- [ ] I can compute the sustainable growth rate and state what it assumes
- [ ] I can build a two-stage model and discount the terminal value the right number of periods
- [ ] I can apply the H-model with H as half the decline period
- [ ] I can state the shortcomings of both constant and multistage growth assumptions
- [ ] I can value perpetual and finite-maturity preferred stock
- [ ] I can state how each contingency feature moves preferred value, and why
- [ ] I can explain why a control perspective calls for FCFF and a minority perspective for the DDM
- [ ] I answered the self-check cold, several days after first study

---

← [LM05 Introduction to Equity Valuation](lm-05-introduction-to-equity-valuation.md)  ·  [Topic index](README.md)  ·  [LM07 Relative Value Equity Valuation Approaches](lm-07-relative-value-equity-valuation-approaches.md) →
