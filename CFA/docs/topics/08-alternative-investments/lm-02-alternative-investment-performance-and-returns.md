# AI · LM02 — Alternative Investment Performance and Returns

## At a glance

| | |
| --- | --- |
| **Topic** | Alternative Investments (7-10% of the exam) |
| **Hours budgeted** | 10 |
| **Prerequisites** | LM1 (fee structures), QM LM3 (MWR vs TWR). |
| **Where it shows up** | 2-3 questions. Fee calculations and the biases in reported returns are near-certain. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe the performance appraisal of alternative investments
- calculate and interpret alternative investment returns both before and after fees

---

## Core concepts

### Why performance appraisal is harder here

| Problem | Consequence |
| --- | --- |
| **Illiquidity and infrequent pricing** | Returns are **appraisal-based**, not market-based |
| **Smoothing** | Appraisals anchor on prior values → reported volatility and correlation are **understated** |
| **Non-normal return distributions** | Skewed and leptokurtic → mean and standard deviation are inadequate (QM LM5) |
| **Short track records** | Insufficient data for statistical confidence |
| **Selection and survivorship biases** | Reported index returns are inflated |
| **Complex, layered fees** | Gross and net returns differ substantially |
| **Cash flow timing controlled by the GP** | IRR is affected by when capital is called and returned |

### The biases in reported alternative returns

**All of these inflate reported performance**, and the exam asks about them directly:

| Bias | Mechanism |
| --- | --- |
| **Survivorship bias** | Failed funds **stop reporting** and disappear from the index. The survivors look better than the original population |
| **Backfill (instant history) bias** | A fund joining a database brings its **past track record** with it — and funds only join after a good run |
| **Self-selection / reporting bias** | Reporting is **voluntary**. Funds with poor performance simply stop |
| **Smoothing (appraisal) bias** | Infrequent, appraisal-based valuations anchor on prior marks, **understating volatility and correlation** |
| **Stale pricing** | Illiquid positions are marked at old prices, so the return series lags reality |

> **The combined effect is large.** Studies have estimated that survivorship and backfill biases
> together overstate hedge fund index returns by **several percentage points a year**, and smoothing
> can halve the apparent volatility. Any comparison of an alternatives index to a public equity
> index without adjusting for these is misleading.

### Return measurement: MWR versus TWR

> **For private capital funds, the money-weighted return (IRR) is the standard**, not the
> time-weighted return.

**Why the departure from the usual rule?** Because the **GP controls the timing** of capital calls
and distributions. The LP cannot choose when money goes in or comes out. Since the GP's timing
decisions are part of what the LP is paying for, the return measure should **include** their effect
— which is exactly what MWR does and TWR strips out (QM LM3).

This is the mirror image of public markets, where TWR is used precisely **because** the investor
controls the timing and the manager should not be judged on it.

### The private capital performance measures

| Measure | Formula | What it tells you |
| --- | --- | --- |
| **IRR** | The discount rate setting the NPV of all cash flows to zero | The annualised money-weighted return. **The headline measure** |
| **PIC (paid-in capital)** | Called capital / Committed capital | How much of the commitment has been drawn |
| **DPI (distributions to paid-in)** | Cumulative distributions / Paid-in capital | **Realised** return. The "cash-on-cash" multiple |
| **RVPI (residual value to paid-in)** | Current NAV / Paid-in capital | **Unrealised** value still in the fund |
| **TVPI (total value to paid-in)** | (Distributions + NAV) / Paid-in capital = **DPI + RVPI** | The **total** multiple. The headline multiple measure |
| **MOIC (multiple on invested capital)** | Total value / Invested capital | Similar to TVPI, measured on invested rather than paid-in capital |

> **DPI versus RVPI is the quality test.** A fund reporting a TVPI of 1.8× made entirely of **RVPI**
> (unrealised NAV, valued by the GP) is a very different proposition from one where most of it is
> **DPI** — cash actually returned. Late in a fund's life, a high RVPI share is a warning: the
> remaining assets are the ones that could not be sold.

**The J-curve.** Private capital funds show **negative returns in early years** — management fees
are charged from day one while investments are held at cost and have not yet appreciated, and early
write-offs surface before successes mature. Returns turn positive as investments mature and exit.
Judging a fund on its year-2 IRR is meaningless.

### Fees and the gross-to-net calculation

**The mechanics, in order:**

```
1. Compute the GROSS return
2. Deduct the MANAGEMENT fee (on committed capital, invested capital, or NAV — check which)
3. Check the HURDLE — has it been cleared? Hard or soft?
4. Check the HIGH WATER MARK — is the fund above its previous peak?
5. Deduct the PERFORMANCE fee
6. The result is the NET return to the investor
```

**Worked example.** A fund with 200m of capital returns 18% gross. Fees are 1.5% on beginning-of-year
assets and 20% performance with a 6% **hard** hurdle and a high water mark that has been cleared.

```
Beginning value            = 200.0m
Gross return 18%           = +36.0m  →  236.0m
Management fee 1.5% × 200  = −3.0m
                              -------
                              233.0m

Hurdle = 6% × 200          = 12.0m
Profit above the hurdle    = 36.0 − 12.0 = 24.0m
Performance fee 20% × 24   = −4.8m
                              -------
Ending value                 228.2m

Net return = (228.2 − 200)/200 = 14.1%
```

**Total fees = 7.8m = 3.9% of assets**, converting an 18% gross return into **14.1% net** — the
investor keeps 78% of the gross return.

> **Fund-of-funds double the problem.** A second layer of, say, 1% and 10% on top means the investor
> might keep only around 65% of the gross return. Over a decade the compounding difference is
> enormous, and it is the main reason fund-of-funds structures have come under pressure.

### Risk-adjusted measures and their limits

The standard measures (Portfolio Management LM2) **understate risk** for alternatives:

- **Sharpe ratio** uses standard deviation, which is **understated by smoothing** and which is the
  wrong risk measure for **skewed** distributions
- **Beta and CAPM** assume the market model holds, which it does not for strategies with option-like
  payoffs

**Better-suited measures:**

| Measure | Why it helps |
| --- | --- |
| **Sortino ratio** | Uses **downside deviation** instead of standard deviation (QM LM5) |
| **Maximum drawdown** | The worst peak-to-trough loss — captures the tail directly |
| **Calmar ratio** | Return divided by maximum drawdown |
| **Value at Risk / conditional VaR** | Explicit tail measures (Portfolio Management LM6) |
| **Skewness and kurtosis** | Reported alongside the mean, to show the distribution's shape |

> **The general principle:** any strategy with an **option-like payoff** — selling volatility,
> merger arbitrage, carry trades, credit strategies — produces steady small gains punctuated by
> occasional large losses. Its Sharpe ratio looks excellent right up until the loss arrives, because
> standard deviation cannot distinguish a smooth series from a safe one.

---

## Formulas to know cold

```
PRIVATE CAPITAL MULTIPLES
  PIC  = Called capital / Committed capital
  DPI  = Cumulative distributions / Paid-in capital      ← REALISED  ("cash on cash")
  RVPI = Current NAV / Paid-in capital                   ← UNREALISED
  TVPI = (Distributions + NAV) / Paid-in capital = DPI + RVPI    ← TOTAL

  IRR is the standard return measure — MONEY-weighted, because the GP controls timing.

FEE CALCULATION — in order
  1. Gross return
  2. − Management fee (on committed / invested / NAV — CHECK WHICH)
  3. Check hurdle (HARD: fee on the excess only | SOFT: fee on all returns once cleared)
  4. Check HIGH WATER MARK
  5. − Performance fee
  6. = Net return

BIASES IN REPORTED RETURNS — all INFLATE performance
  SURVIVORSHIP  — failed funds stop reporting
  BACKFILL      — new entrants bring their good past record
  SELF-SELECTION— reporting is voluntary
  SMOOTHING     — appraisal-based valuations UNDERSTATE volatility AND correlation
  STALE PRICING — marks lag reality

THE J-CURVE: negative early returns (fees from day one, investments at cost), positive later.

RISK MEASURES BETTER SUITED TO ALTERNATIVES
  Sortino (downside deviation) · Maximum drawdown · Calmar · VaR / CVaR · skew and kurtosis
```

---

## Exam traps

> **Trap 1 — Using TWR for private capital.** **MWR (IRR) is the standard**, because the **GP
> controls the timing** of calls and distributions. This reverses the public-market rule.

> **Trap 2 — Reading TVPI without splitting it.** **DPI is realised cash; RVPI is the GP's own
> valuation.** A high TVPI made mostly of RVPI late in a fund's life is a warning, not a result.

> **Trap 3 — Management fee base.** It may be on **committed**, **invested**, or **NAV** capital.
> They give very different answers. Read the question.

> **Trap 4 — Forgetting the hurdle and high water mark.** Both can eliminate the performance fee
> entirely in a given year.

> **Trap 5 — Comparing an alternatives index to a public index directly.** Survivorship, backfill,
> self-selection, and smoothing biases all **inflate** the alternatives figure.

> **Trap 6 — Trusting reported volatility and correlation.** **Smoothing understates both**, making
> the diversification benefit look larger than it is.

> **Trap 7 — Judging a fund on early-year returns.** The **J-curve** makes early IRRs meaningless.

> **Trap 8 — Relying on the Sharpe ratio.** It uses standard deviation, which is understated by
> smoothing and is the wrong measure for skewed, option-like payoffs.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A hedge fund with 500m returns 22% gross. Fees are 2% of beginning assets and 20% performance with a 5% soft hurdle and no high water mark issue. Compute the net return to investors.

<details><summary>Answer</summary>

```
Beginning value                 = 500.0m
Gross return 22%                = +110.0m  →  610.0m
Management fee 2% × 500         = −10.0m
                                   --------
                                    600.0m
```
**Hurdle check:** 22% > 5%, so the hurdle is cleared. It is a **SOFT** hurdle, so the performance fee applies to the **full** gross profit, not just the excess.

```
Performance fee 20% × 110.0     = −22.0m
                                   --------
Ending value                       578.0m
```

**Net return = (578 − 500)/500 = 15.6%**

**Total fees = 32.0m = 6.4% of beginning assets.** The investor keeps 15.6 of a 22% gross return — about **71%**.

Had the hurdle been **hard**, the performance fee would be 20% × (110 − 25) = 17.0m, giving a net return of **16.6%** — a full percentage point better.

</details>

**2.** A private equity fund reports a TVPI of 2.1x. DPI is 0.4x. What does this tell you, and what would you want to know?

<details><summary>Answer</summary>

**RVPI = TVPI − DPI = 2.1 − 0.4 = 1.7×**

So **81% of the reported value is unrealised** — it is the GP's own valuation of assets still held, not cash returned to investors. Only 0.4× of paid-in capital has actually come back.

**What I would want to know:**

**(1) The fund's vintage and age.** For a 3-year-old fund this split is entirely normal — investments have not matured. For a **9-year-old** fund approaching the end of its life, it is a serious concern: the remaining assets are the ones that **could not be sold**, and a 1.7× mark on them deserves scrutiny.

**(2) How the NAV is determined.** Comparable-company multiples? A DCF? A recent funding round? Who validated it — an independent valuer, or the GP alone?

**(3) The composition of the residual.** Is it a handful of large positions or a diversified tail? Is it concentrated in one sector that has since repriced?

**(4) Realised versus unrealised IRR.** The IRR on exited deals alone tells you what the GP has actually delivered.

**(5) Marks versus public comparables.** If public peers have derated 40% and the GP's marks are unchanged, the NAV is stale.

**The general principle: DPI is a fact; RVPI is an opinion.** A track record built on unrealised marks has not been tested.

</details>

**3.** Explain the four biases that inflate reported hedge fund index returns.

<details><summary>Answer</summary>

**(1) Survivorship bias.** Funds that perform badly **close and stop reporting**, disappearing from the index — often with their historical data removed entirely. The index therefore reflects only the **survivors**, which is not the population an investor could have selected from ex ante.

**(2) Backfill (instant history) bias.** When a fund joins a database, it typically brings its **entire past track record** with it. But funds only join **after** a period of good performance — nobody registers a database entry to showcase two bad years. So the historical returns added to the index are systematically **better than average**.

**(3) Self-selection / reporting bias.** Reporting is entirely **voluntary**. Funds with poor performance simply stop submitting data. Notably, so do some **very successful** funds that are closed to new capital and have no marketing need — which cuts the other way, but the net effect is upward.

**(4) Smoothing (appraisal) bias.** Illiquid positions are marked by **appraisal**, which anchors on the prior valuation and adjusts only partially toward current conditions. The return series is therefore artificially **smooth**, **understating both volatility and correlation** with public markets (Portfolio Management LM1).

**The combined effect:** studies estimate survivorship and backfill together overstate hedge fund index returns by **several percentage points a year**, and smoothing can roughly **halve** apparent volatility. A reported Sharpe ratio of 1.2 might be 0.5 on adjusted figures.

**The practical response:** discount reported index returns, un-smooth the return series before using it in an optimisation, and treat any correlation estimate from appraisal-based data with suspicion.

</details>

**4.** Why is the money-weighted return used for private capital when the time-weighted return is standard elsewhere?

<details><summary>Answer</summary>

Because **the manager controls the timing of the cash flows**, which reverses the logic that makes TWR standard in public markets.

**The public-market rule** (QM LM3): TWR is used to evaluate a manager **precisely because** it strips out the effect of cash flow timing. The **investor** decides when to add or withdraw money, and the manager should not be rewarded or penalised for decisions they did not make.

**In private capital the roles are reversed.** The **GP** decides:
- **When to call capital** — and holding an LP's committed capital idle while waiting for deals is a cost
- **When to deploy it** into investments
- **When to exit** and return proceeds

Those timing decisions are **part of what the LP is paying the GP for**. A GP who calls capital early and deploys it slowly destroys value; one who times entries and exits well creates it. Stripping that out with TWR would remove a central component of the GP's performance.

**So MWR (IRR) is correct here** — it captures both the investment selection **and** the timing, which together are the GP's contribution.

**The caveats, which matter:**
- IRR can be **manipulated** by using subscription credit lines to delay capital calls, which mechanically boosts the reported IRR without improving the LP's actual outcome
- IRR assumes **reinvestment at the IRR** (Corporate Issuers LM5), which is unrealistic for high-IRR funds
- This is why **IRR should always be read alongside the multiples (TVPI, DPI)**, which are immune to timing manipulation. A 30% IRR with a 1.3× TVPI is a fast small win; a 20% IRR with a 2.5× TVPI is far more money.

</details>

---

## Done when

- [ ] I can name and explain the five biases that inflate reported alternative returns
- [ ] I can explain why MWR is used for private capital and name the caveats on IRR
- [ ] I can compute PIC, DPI, RVPI, and TVPI and explain why the DPI/RVPI split matters
- [ ] I can compute a net return from a gross return through the full fee sequence
- [ ] I can explain the J-curve and why early-year returns are meaningless
- [ ] I can explain why the Sharpe ratio is inadequate for alternatives and name better measures
- [ ] I answered the self-check cold, several days after first study

---

← [LM01 Alternative Investment Features, Methods, and Structures](lm-01-alternative-investment-features-methods-and-structures.md)  ·  [Topic index](README.md)  ·  [LM03 Investments in Private Capital: Equity and Debt](lm-03-investments-in-private-capital-equity-and-debt.md) →
