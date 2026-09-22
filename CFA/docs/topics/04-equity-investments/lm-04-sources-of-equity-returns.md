# EQ · LM04 — Sources of Equity Returns

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM1, FSA LM2 (EPS). |
| **Where it shows up** | 2 questions. Dividend chronology and the effect of buybacks are reliable calculations. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe features and uses of dividends, share repurchases, stock splits, and reverse stock splits
- describe dividend payment chronology
- calculate price and total return for equity securities

---

## Core concepts

### Forms of shareholder distribution

| Form | Effect on the company | Effect on the shareholder |
| --- | --- | --- |
| **Cash dividend** | **Cash out**; assets and equity fall | Cash received; share price falls by roughly the dividend |
| **Stock (share) dividend** | **No cash movement**; a transfer within equity | More shares, each worth proportionally less. **Total value unchanged** |
| **Stock split** | No cash; par value adjusted | More shares at a lower price. **Total value unchanged** |
| **Reverse split** | No cash | Fewer shares at a higher price. **Total value unchanged** |
| **Share repurchase (buyback)** | **Cash out**; shares retired or held as treasury | Fewer shares outstanding; the remaining holders own a larger fraction |

### Stock dividends, splits, and reverse splits

None of these change the value of the company or of a shareholder's stake. They are **cosmetic** —
but they carry signalling content.

**A 3-for-1 split:** a holder of 100 shares at 150 now holds 300 shares at 50. Value: 15,000 before,
15,000 after.

**Why companies split:** to bring the share price into a range perceived as accessible, improve
liquidity and round-lot tradability, and — more honestly — to signal management's confidence that
the price will keep rising.

**Reverse splits** go the other way, typically to **regain compliance** with an exchange's minimum
price requirement. Because of that context, a reverse split is generally read as a **negative
signal**: it is what a company does when its share price has collapsed.

> **The EPS consequence** (FSA LM2): splits and stock dividends are applied **retroactively** to the
> beginning of the earliest period presented when computing weighted average shares. They are **not**
> time-weighted.

### Share repurchases

**The four motivations:**

1. **Signalling** — management believes the shares are undervalued, and is willing to spend real
   cash to back that view.
2. **Flexibility** — a buyback is discretionary and carries no ongoing commitment, unlike a
   dividend, which the market punishes a company for cutting.
3. **Tax efficiency** — where capital gains are taxed more lightly than dividends, or where the
   shareholder can choose when to realise the gain.
4. **Offsetting dilution** from employee share-based compensation.

**The effect on EPS depends entirely on one comparison:**

```
If the after-tax cost of funds used  <  the earnings yield (E/P),  EPS RISES
If the after-tax cost of funds used  >  the earnings yield (E/P),  EPS FALLS
```

Buying back shares with cash forgoes the after-tax interest that cash was earning; buying back with
borrowed money incurs after-tax interest. Either way, you compare that cost to the earnings per
share you are retiring.

**The effect on book value per share:**

```
If the repurchase price > book value per share,  BVPS FALLS
If the repurchase price < book value per share,  BVPS RISES
```

> **Crucially: a buyback that raises EPS does not necessarily create value.** EPS rises whenever the
> funding cost is below the earnings yield — which says nothing about whether the shares were
> actually cheap. Repurchasing overvalued shares transfers value **from** continuing shareholders
> **to** the selling ones. The right question is not "does EPS rise?" but **"is the share price below
> intrinsic value?"**
>
> This is also why compensating management on EPS growth (Corporate Issuers LM3) invites buybacks
> regardless of whether they create value.

**A buyback is equivalent to a cash dividend of the same size** in its effect on shareholder wealth,
assuming no taxes and that shares are repurchased at fair value. What differs is the **form** (some
shareholders receive cash, the rest receive a larger ownership fraction) and the **tax treatment**.

### Dividend payment chronology

Four dates, in order. This sequence is tested directly.

| Date | What happens |
| --- | --- |
| **Declaration date** | The board announces the dividend. A liability is created |
| **Ex-dividend date** | The **first day the share trades WITHOUT** the right to the dividend. **Buy on or after this date and you do not receive it.** The price typically drops by roughly the dividend amount at the open |
| **Record date** | The company determines who is on the register and therefore entitled. Usually **one business day after** the ex-date under modern (T+1) settlement |
| **Payment date** | Cash is actually distributed |

> **The ex-date is the one that matters economically**, and it is the one the exam asks about. To
> receive the dividend you must buy **before** the ex-dividend date. The record date is an
> administrative consequence of the settlement cycle, not the decision point.

### Computing returns

```
Price return  = (P1 − P0) / P0

Income (dividend) yield = D1 / P0

Total return  = (P1 − P0 + D1) / P0  = Price return + Dividend yield
```

**Multi-period compounding:**

```
Total return over n periods:  (1 + R1)(1 + R2)...(1 + Rn) − 1
```

**Real and after-tax variants:**

```
Real return      = (1 + Nominal) / (1 + Inflation) − 1
After-tax return = accounts for the different rates on dividends and capital gains
```

> **The difference between price return and total return is not a technicality.** Over a 30-year
> horizon, reinvested dividends typically account for more than half the terminal wealth of a broad
> equity index (QM LM3). Comparing a price index to a total return index, or quoting one when you
> mean the other, misstates equity performance by a very large margin.

---

## Formulas to know cold

```
RETURNS
  Price return    = (P1 − P0)/P0
  Dividend yield  = D1 / P0
  Total return    = (P1 − P0 + D1)/P0 = Price return + Dividend yield
  Multi-period    = (1+R1)(1+R2)...(1+Rn) − 1
  Real return     = (1 + Nominal)/(1 + Inflation) − 1

SPLITS
  n-for-1 split:  shares × n,  price ÷ n,  total value UNCHANGED
  Applied RETROACTIVELY in weighted average share calculations (FSA LM2)

BUYBACKS
  EPS effect:  after-tax cost of funds  <  earnings yield (E/P)  →  EPS RISES
               after-tax cost of funds  >  earnings yield (E/P)  →  EPS FALLS
  BVPS effect: repurchase price > BVPS  →  BVPS FALLS
               repurchase price < BVPS  →  BVPS RISES

DIVIDEND CHRONOLOGY (in order)
  Declaration  →  EX-DIVIDEND  →  Record  →  Payment
                  ↑ buy BEFORE this date to receive the dividend
```

---

## Exam traps

> **Trap 1 — The ex-dividend date.** You must buy **before** the ex-date to receive the dividend.
> Buying on the ex-date means you do **not** get it. The record date is not the decision point.

> **Trap 2 — Believing splits create value.** A split changes nothing. Value, ownership fraction,
> and market capitalisation are all unchanged.

> **Trap 3 — Assuming a buyback that raises EPS creates value.** EPS rises whenever the funding cost
> is below the earnings yield — regardless of whether the shares are cheap. Value is created only if
> the repurchase price is **below intrinsic value**.

> **Trap 4 — Getting the buyback EPS condition backwards.** EPS **rises** when the after-tax cost of
> funds is **below** the earnings yield (E/P).

> **Trap 5 — Getting the BVPS effect backwards.** Repurchasing **above** book value **reduces** BVPS.

> **Trap 6 — Time-weighting a split.** Splits and stock dividends are applied **retroactively** to
> the start of the earliest period presented, not weighted for months outstanding.

> **Trap 7 — Confusing price return with total return.** Total return includes dividends. Over long
> horizons the difference dominates.

> **Trap 8 — Reading a reverse split as neutral.** Mechanically it is, but it is usually a **negative
> signal** — a company restoring compliance with a minimum price requirement after a collapse.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A share trades at 48 on 10 March. The dividend of 1.20 has a declaration date of 5 March, ex-date of 14 March, record date of 15 March, and payment date of 2 April. An investor buys on 14 March. Do they receive the dividend?

<details><summary>Answer</summary>

**No.** The **ex-dividend date is 14 March** — that is the first day the share trades **without** the right to the dividend. To receive it, the investor must buy **on or before 13 March**.

The investor buying on 14 March should expect to pay roughly 1.20 less per share at the open, since the share no longer carries the entitlement. They are not worse off — they simply bought the share without the dividend attached, at a correspondingly lower price.

</details>

**2.** A company with 20m shares and net income of 60m repurchases 2m shares at 45 each using cash that was earning 4% after tax. Compute EPS before and after, and explain the result.

<details><summary>Answer</summary>

**Before:** EPS = 60m / 20m = **3.00**

**Cost of the repurchase:** 2m × 45 = 90m. Forgone after-tax interest = 90m × 4% = **3.6m**.

**After:** Net income = 60 − 3.6 = 56.4m; shares = 18m.
EPS = 56.4 / 18 = **3.133**

**EPS rises.** The test: earnings yield = E/P = 3.00/45 = **6.67%**, versus an after-tax funding cost of **4%**. Since 4% < 6.67%, EPS rises.

**But** this says nothing about value creation. EPS would rise on exactly this arithmetic whether the shares were worth 30 or 70. Value is created only if 45 is **below intrinsic value** — buying overvalued shares transfers wealth from continuing shareholders to sellers, however flattering the EPS line looks.

</details>

**3.** A share was bought at 62, paid dividends of 1.10 and 1.25 over two years, and was sold at 71. Compute the total return over the holding period and the annualised figure.

<details><summary>Answer</summary>

Total gain = (71 − 62) + 1.10 + 1.25 = 9 + 2.35 = 11.35
Holding period total return = 11.35 / 62 = **18.31%**

Annualised (geometric): (1.1831)^(1/2) − 1 = **8.77%** per year.

By way of contrast, the **price return** alone was (71 − 62)/62 = **14.52%** — the dividends contributed 3.79 percentage points, or about 21% of the total return over just two years. Over decades that share compounds into the majority of terminal wealth.

</details>

**4.** A company repurchases shares at 38 when book value per share is 52. What happens to BVPS, and how do you interpret it?

<details><summary>Answer</summary>

The repurchase price (38) is **below** book value per share (52), so **BVPS rises**.

Mechanically: the company pays out 38 of book value per share retired but removes 52 of book value's worth of claim, so the remaining shareholders' book value per share increases.

**Interpretation:** the shares trade below book value, which means the market is pricing the company's assets at less than their carrying amount. Two readings:
- The market believes the assets are **impaired or will earn below their cost of capital** — in which case repurchasing is not obviously wise, and the accretion to BVPS is an accounting artefact.
- The shares are **genuinely undervalued**, in which case the repurchase creates real value for continuing shareholders.

Distinguishing the two requires the valuation work in LM6 and LM7. The BVPS accretion alone proves nothing.

</details>

**5.** Explain why a share repurchase is economically equivalent to a cash dividend of the same amount, and what differs in practice.

<details><summary>Answer</summary>

**Why equivalent:** both distribute the same amount of cash from the company to shareholders, and both reduce the company's assets and equity by that amount. Assuming no taxes and repurchase at fair value, total shareholder wealth is identical under either route.

With a dividend, every shareholder receives cash and retains the same ownership fraction of a smaller company. With a buyback, the selling shareholders receive cash and exit, while the remaining shareholders hold a **larger fraction of a smaller company** — the same value, arrived at differently.

**What differs in practice:**
- **Taxes.** Dividends are typically taxed on receipt; buybacks let the shareholder choose when to realise a gain, and capital gains rates may be lower.
- **Flexibility.** Cutting a dividend is heavily punished by the market; a buyback programme can be slowed or stopped without signal.
- **Signalling.** A buyback signals that management believes the shares are cheap.
- **The fair value assumption.** Repurchasing **above** intrinsic value destroys value for continuing shareholders — a dividend cannot do this. The equivalence holds only at fair value.

</details>

---

## Done when

- [ ] I can list the four dividend dates in order and say which one determines entitlement
- [ ] I can explain why splits, stock dividends, and reverse splits change nothing in value
- [ ] I can state the EPS test for a buyback and apply it with the correct direction
- [ ] I can state the BVPS test for a buyback and apply it
- [ ] I can explain why a buyback that raises EPS does not necessarily create value
- [ ] I can compute price return, dividend yield, and total return, and annualise a multi-period return
- [ ] I can explain the equivalence of buybacks and dividends and where it breaks down
- [ ] I answered the self-check cold, several days after first study

---

← [LM03 Equity Issuance and Trading](lm-03-equity-issuance-and-trading.md)  ·  [Topic index](README.md)  ·  [LM05 Introduction to Equity Valuation](lm-05-introduction-to-equity-valuation.md) →
