# QM · LM03 — Benchmarking Returns

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 8 |
| **Prerequisites** | LM2 (geometric mean, chaining returns). BA II Plus IRR function. |
| **Where it shows up** | 2 questions. MWR vs TWR is one of the most predictable Level I items. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate and compare money-weighted and time-weighted rates of return
- describe the choices and the implications of the different weighting methods used in index construction and management, and calculate, interpret, and explain the value and the returns of an index

---

## Core concepts

### Two ways to measure a portfolio's return, and they disagree

| | **Money-weighted return (MWR)** | **Time-weighted return (TWR)** |
| --- | --- | --- |
| Also called | Internal rate of return (IRR) | Geometric mean of sub-period returns |
| Measures | The **investor's** actual experience | The **manager's** skill |
| Affected by cash flow timing? | **Yes, heavily** | **No** |
| Use when | The investor controls the timing of contributions and withdrawals | Comparing managers, or reporting fund performance |
| Industry standard for reporting | No | **Yes** (GIPS requires TWR) |

The reason they differ is simple: MWR gives more weight to periods when more money was invested.
If an investor adds a large sum just before a bad quarter, MWR drops sharply even though the
manager did nothing differently — so MWR penalises the manager for the investor's timing.

### Computing money-weighted return

MWR is the discount rate that sets the net present value of all cash flows to zero.

```
Σ CFt / (1 + MWR)^t = 0
```

Treat it exactly like an IRR problem. **Sign convention is everything:**

- Cash **into** the portfolio (purchases, contributions) → **negative** (outflow from the investor)
- Cash **out** of the portfolio (dividends received, sales, withdrawals) → **positive**
- The **ending value** counts as a final positive inflow (as if liquidated)

**Worked example.** Buy 1 share at 100. At the end of year 1 it pays a 5 dividend and you buy a
second share for 110. At the end of year 2 both pay 5 each and you sell both at 120.

```
t=0:  −100                                       (buy the first share)
t=1:  +5 − 110 = −105                            (dividend received, second share bought)
t=2:  +10 + 240 = +250                           (two dividends, sell two shares at 120)

Solve:  −100 − 105/(1+r) + 250/(1+r)² = 0   →   r ≈ 16.1%
```

On the BA II Plus: `CF` → CF0 = −100, C01 = −105, F01 = 1, C02 = 250, F02 = 1 → `IRR` `CPT`.

### Computing time-weighted return

Break the period at **every external cash flow**, compute the HPR for each sub-period, and chain
them geometrically. External cash flows never enter the return calculation — that is exactly how
their effect is removed.

```
TWR = [(1 + R1)(1 + R2)...(1 + Rn)]^(1/years) − 1
```

**Same example.**

```
Year 1:  R1 = (110 + 5 − 100) / 100 = 15.0%
Year 2:  R2 = (120 + 5 − 110) / 110 = 13.64%

TWR = [(1.15)(1.1364)]^(1/2) − 1 = (1.30686)^0.5 − 1 = 14.32%
```

**MWR 16.1% vs. TWR 14.32%.** The investor did better than the manager's per-unit performance,
because they added money before the second year. Had year 2 been the weak year, MWR would have
fallen below TWR.

> **The rule to internalise:** if money is added **before a strong period**, MWR > TWR. If money is
> added **before a weak period**, MWR < TWR. Questions frequently describe the timing and ask which
> is higher without requiring any calculation at all.

### Index construction — the three weighting methods

An index is a portfolio. How you weight it determines what it measures.

| Method | Weight of each constituent | Implied strategy | Bias |
| --- | --- | --- | --- |
| **Price-weighted** | Price / Σ prices | Buy **one share** of each | Toward **high-priced** shares; distorted by stock splits |
| **Equal-weighted** | 1 / n | Equal money in each | Toward **small caps**; requires frequent rebalancing |
| **Market-cap-weighted** | Market cap / Σ market caps | Hold the whole market in proportion | Toward **large caps**; momentum — winners grow their weight |

**Price-weighted index** (e.g. the Dow Jones Industrial Average, Nikkei 225):

```
Index value = Σ Prices / Divisor
```

The **divisor** starts at the number of constituents and is adjusted for stock splits, constituent
changes, and spin-offs so the index value does not jump for a non-economic reason. A 2-for-1 split
halves a share's price and therefore halves its weight — a purely mechanical change in what the
index measures. This is the central weakness of price weighting.

**Equal-weighted index:**

```
Index return = Simple arithmetic average of constituent returns
```

Conceptually the cleanest, but it **requires periodic rebalancing** back to equal weights, which in
practice means selling winners and buying losers, with transaction costs. Without rebalancing the
weights drift and it ceases to be equal-weighted.

**Market-capitalisation-weighted index** (S&P 500, FTSE 100, MSCI World):

```
Index value = Σ (Price × Shares outstanding) / Divisor
```

**Float-adjusted** market-cap weighting — the modern standard — counts only shares actually
available to public investors, excluding government, founder, and strategic holdings. It gives a
more investable index.

Cap weighting is **self-rebalancing**: as a price rises, so does its weight, with no trading
required. Its drawback is concentration — a market-cap index can become dominated by a handful of
names, and it mechanically holds more of whatever has already risen most.

### Index returns

```
Price return   = (Index value_end − Index value_begin) / Index value_begin
Total return   = (Index value_end − Index value_begin + Income) / Index value_begin
```

**Total return indexes assume dividends are reinvested.** The gap between a price index and its
total return version compounds substantially over decades — for a broad equity index it is typically
2–4 percentage points a year, which dominates the comparison over any long horizon.

**Rebalancing** restores target weights (essential for equal weighting, automatic for cap weighting).
**Reconstitution** changes which securities are *in* the index, and causes real price pressure as
index funds are forced to trade.

### Types of indexes

Beyond broad market equity indexes: sector, style (value/growth), size, geographic, fixed income
(where constructing an index is harder — bonds are less liquid, mature, and are often
issuance-weighted, which perversely gives the largest weight to the biggest *borrowers*),
commodity, real estate, and hedge fund indexes.

Two biases worth knowing for the Alternative Investments topic: hedge fund indexes suffer from
**survivorship bias** (failed funds disappear from the history) and **backfill bias** (a fund joining
an index brings its good past record with it). Both inflate reported index returns.

---

## Formulas to know cold

```
MONEY-WEIGHTED RETURN (= IRR)
    Σ CFt / (1 + MWR)^t = 0
    Sign convention: cash INTO the portfolio negative; cash OUT and ending value positive
    BA II Plus: CF worksheet → IRR → CPT

TIME-WEIGHTED RETURN
    Break at every external cash flow; compute each sub-period HPR:
        R_sub = (Ending value + Income − Beginning value) / Beginning value
    TWR = [(1+R1)(1+R2)...(1+Rn)]^(1/years) − 1

INDEX WEIGHTING
    Price-weighted:      w_i = P_i / Σ P     ;  Index = Σ P / Divisor
    Equal-weighted:      w_i = 1 / n         ;  Return = arithmetic mean of returns
    Cap-weighted:        w_i = (P_i × Q_i) / Σ (P × Q)
    Float-adjusted cap:  uses only publicly available shares

INDEX RETURNS
    Price return = (V_end − V_begin) / V_begin
    Total return = (V_end − V_begin + Income) / V_begin
```

---

## Exam traps

> **Trap 1 — Which return for which purpose.** **TWR judges the manager** (cash flow timing removed);
> **MWR judges the investor's experience** (timing included). GIPS requires TWR for exactly this
> reason.

> **Trap 2 — MWR sign convention.** Cash **into** the portfolio is **negative**. Getting this
> backwards gives an IRR of the wrong sign or an `Error 5` on the calculator.

> **Trap 3 — Forgetting the ending value in MWR.** The terminal portfolio value is a final positive
> cash flow, as if liquidated. Omitting it is the most common MWR error.

> **Trap 4 — Chaining sub-period returns arithmetically.** TWR chains **geometrically**:
> `(1+R1)(1+R2)`, then take the n-th root if annualising.

> **Trap 5 — Price-weighted indexes and splits.** A split changes a constituent's weight without any
> economic event. The divisor is adjusted so the index level does not jump, but the **weight**
> genuinely changes.

> **Trap 6 — Price return vs. total return.** Total return includes reinvested income. The
> difference compounds enormously over long horizons; comparing one index's price return to
> another's total return is meaningless.

> **Trap 7 — Which index is biased which way.** Price-weighted → high-**priced** shares (not large
> companies — a 400 share of a small company outweighs a 20 share of a giant). Cap-weighted → large
> companies. Equal-weighted → small companies.

> **Trap 8 — Assuming equal weighting needs no maintenance.** It requires the most rebalancing of
> the three; cap weighting requires essentially none.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** An investor buys one share at 60. At the end of year 1 it pays a 2 dividend and they buy a second share at 72. At the end of year 2 each share pays 2 and both are sold at 66. Compute the MWR and TWR, and explain the difference.

<details><summary>Answer</summary>

**MWR (IRR):**
```
t=0:  −60
t=1:  +2 − 72 = −70
t=2:  +4 + 132 = +136
```
Solve −60 − 70/(1+r) + 136/(1+r)² = 0 → **r ≈ 3.24%**

**TWR:**
Year 1: (72 + 2 − 60)/60 = 23.33%
Year 2: (66 + 2 − 72)/72 = −5.56%
TWR = [(1.2333)(0.9444)]^(1/2) − 1 = (1.16478)^0.5 − 1 = **7.93%**

**MWR (3.24%) < TWR (7.93%)** because the investor doubled their position **just before the weak year**. More money was exposed to the −5.56% period than to the +23.33% period. The manager's per-unit performance was 7.93%; the investor earned 3.24% because of their own timing.

</details>

**2.** An investor makes a large contribution immediately before a strong quarter. Without calculating, which is higher — MWR or TWR?

<details><summary>Answer</summary>

**MWR is higher.** MWR weights periods by the amount of money invested, so a large balance during a strong period lifts it. TWR strips out cash-flow timing entirely and is unaffected.

The general rule: money added **before a strong period → MWR > TWR**; money added **before a weak period → MWR < TWR**. Many exam questions test only this relationship and require no arithmetic.

</details>

**3.** A price-weighted index contains three shares priced at 20, 45, and 135. What is each weight? One share undergoes a 3-for-1 split. What happens?

<details><summary>Answer</summary>

Σ prices = 200. Weights: 20/200 = **10%**, 45/200 = **22.5%**, 135/200 = **67.5%**.

If the 135 share splits 3-for-1, its price becomes 45. New Σ = 20 + 45 + 45 = 110. Its weight falls from 67.5% to 45/110 = **40.9%** — with no change in the company's size or value.

The **divisor is adjusted** so the index *level* does not jump, but the **composition of what the index measures has genuinely changed**. This is the structural flaw in price weighting: a purely cosmetic corporate action reallocates the index.

</details>

**4.** Why is a market-cap-weighted index self-rebalancing while an equal-weighted index is not?

<details><summary>Answer</summary>

In a cap-weighted index, each weight **is** the constituent's share of total market value. When a price rises, both its market cap and the index total rise together, and the weight adjusts automatically — a buy-and-hold portfolio stays correctly weighted with **no trading**.

An equal-weighted index requires every holding to be 1/n of the portfolio. As soon as prices move, the weights drift away from 1/n, so the index must **periodically sell winners and buy losers** to restore equality. That means real turnover and real transaction costs, which is why equal-weighted funds carry higher expenses.

</details>

**5.** Over 30 years an index's price return averaged 6.1% a year while its total return averaged 9.0%. How much of the ending wealth comes from dividends?

<details><summary>Answer</summary>

Price-only: 1.061^30 = **5.92×**
Total return: 1.090^30 = **13.27×**

Dividends and their reinvestment account for **13.27 − 5.92 = 7.35× the original investment** — more than half of the total ending wealth (55%).

This is why quoting a price index return as 'the market's return' materially misrepresents equity performance over long horizons, and why total return is always the correct basis for comparison.

</details>

**6.** Why is constructing a fixed-income index harder than an equity index, and what problem does issuance weighting create?

<details><summary>Answer</summary>

Bonds are far less liquid than equities, many do not trade for days, pricing often relies on matrix or model estimates rather than transactions, and the universe **turns over constantly** as bonds mature and new issues arrive. The number of distinct bonds vastly exceeds the number of listed equities.

**Issuance (market-value) weighting** gives the largest weight to the **largest borrowers** — i.e. the index is most exposed to whoever has issued the most debt. That is perverse from a credit standpoint: the weighting scheme systematically tilts toward the most indebted issuers, which is the opposite of what a credit-conscious investor would choose.

</details>

---

## Done when

- [ ] I can compute MWR using the BA II Plus cash flow worksheet with the correct sign convention
- [ ] I can compute TWR by breaking at each cash flow and chaining geometrically
- [ ] I can predict which of MWR and TWR is higher from cash-flow timing alone, without calculating
- [ ] I can state why GIPS requires TWR for performance reporting
- [ ] I can compute weights under all three index methods and say which bias each carries
- [ ] I can explain the divisor and what a stock split does to a price-weighted index
- [ ] I can explain why cap weighting self-rebalances and equal weighting does not
- [ ] I answered the self-check cold, several days after first study

---

← [LM02 Types of Financial Returns](lm-02-types-of-financial-returns.md)  ·  [Topic index](README.md)  ·  [LM04 The Time Value of Money in Finance](lm-04-the-time-value-of-money-in-finance.md) →
