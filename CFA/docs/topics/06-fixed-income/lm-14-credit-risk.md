# FI · LM14 — Credit Risk

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | LM7 (spread measures). |
| **Where it shows up** | 1–2 questions. Expected loss and the spread decomposition are the calculable parts. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe credit risk and its components, probability of default and loss given default
- describe the uses of ratings from credit rating agencies and their limitations
- describe macroeconomic, market, and issuer-specific factors that influence the level and volatility of yield spreads

---

## Core concepts

### The components of credit risk

**Credit risk is the risk of loss from a borrower failing to make promised payments.** It decomposes
into two independent questions:

| Component | Question | Determined by |
| --- | --- | --- |
| **Probability of default (PD)** | **How likely** is a failure to pay? | Business risk, leverage, liquidity, management, industry |
| **Loss given default (LGD)** | **How much** is lost if it happens? | Seniority, collateral, the recovery environment |

```
Expected loss = Probability of default × Loss given default × Exposure at default

Recovery rate = 1 − Loss given default (as a percentage)
```

> **The two components are genuinely independent.** A senior secured bond from a weak issuer may
> have a **high PD and a low LGD** — default is likely, but recovery is good. A subordinated bond
> from a strong issuer has the reverse. Two bonds with identical expected loss can have very
> different risk profiles, and investors who cannot tolerate a default event at all care about PD
> even when LGD is low.

**Related terms:**

| Term | Meaning |
| --- | --- |
| **Default risk** | The probability of failing to pay |
| **Loss severity** | The same as LGD — the portion of value lost |
| **Spread risk** | The risk that the **spread widens** without any default. This is what actually causes most credit losses in practice |
| **Credit migration (downgrade) risk** | The risk of a rating downgrade, which widens the spread |
| **Market liquidity risk** | The risk that the bid-ask spread widens, raising the cost of exit |

> **Most credit losses in a portfolio come from spread widening and downgrades, not from actual
> defaults.** A diversified investment-grade portfolio may experience no defaults at all in a bad
> year and still lose materially from spread widening. This distinction matters for how credit risk
> is measured and hedged.

### Seniority and the priority of claims

In liquidation, claims are paid in strict order:

```
1. Secured creditors (up to the value of their collateral)
2. Senior unsecured creditors
3. Senior subordinated
4. Subordinated
5. Junior subordinated
6. Preference shareholders
7. Common shareholders   ← the residual claim (Corporate Issuers LM2)
```

**Key doctrines:**

- **Absolute priority rule** — each class is paid in full before the next receives anything. **In
  practice it is frequently violated** in negotiated reorganisations, where junior classes extract
  value to avoid protracted litigation.
- **Pari passu** — claims of equal ranking are treated equally.
- **Structural subordination** — debt at a **holding company** is effectively junior to debt at an
  **operating subsidiary**, because the operating company's creditors have first claim on its assets;
  the holding company is only an equity holder in the subsidiary. This is an easy risk to miss when
  reading a group's consolidated accounts.

**Recovery rates vary systematically:** by seniority (secured recovers most), by industry (asset-rich
industries recover more), and **by the point in the cycle** — recoveries are **lowest in recessions**,
precisely when defaults are highest. PD and LGD are therefore **positively correlated**, which makes
credit losses fatter-tailed than an independence assumption would suggest.

### Credit ratings

| Category | Moody's | S&P / Fitch |
| --- | --- | --- |
| **Investment grade** | Aaa, Aa, A, Baa | AAA, AA, A, BBB |
| **High yield / speculative** | Ba, B, Caa, Ca, C | BB, B, CCC, CC, C |
| **Default** | — | D |

The boundary is **Baa3 / BBB−**, and crossing it matters enormously (LM4 — fallen angels).

**Issuer rating versus issue rating:**

- An **issuer (corporate family) rating** applies to the entity's senior unsecured debt.
- An **issue rating** applies to a specific security and is **notched** up or down from the issuer
  rating to reflect that issue's seniority, collateral, and structural position.

**Uses of ratings:** a low-cost credit opinion, a common language across markets, a basis for
investment mandates and regulatory capital rules, and a trigger for covenants and collateral
provisions.

**Limitations — the LOS asks for these explicitly:**

| Limitation | Detail |
| --- | --- |
| **Ratings lag the market** | Spreads move first; rating changes follow, often by months |
| **Ratings are through-the-cycle** | Deliberately stable, so they under-react to genuine deterioration |
| **They measure PD better than LGD** | Two bonds with the same rating can have very different recovery prospects |
| **Issuer-pays conflict of interest** | The rated entity pays for the rating |
| **Poor performance on structured products** | Systematically over-rated before 2008 |
| **They say nothing about spread or liquidity risk** | Which is where most losses come from |
| **Mechanical reliance creates cliff effects** | Mandate-driven forced selling at the investment-grade boundary amplifies price moves |

> **Ratings are a starting point, not a conclusion.** An analyst who stops at the rating has
> outsourced the analysis to an agency that is paid by the issuer, updates slowly by design, and
> measures only one of the two components of credit risk.

### What drives yield spreads

**Macroeconomic factors:**

| Factor | Effect on spreads |
| --- | --- |
| **Economic slowdown or recession** | **Wider** — default expectations rise |
| Strong growth | Narrower |
| **Rising expected default rates** | Wider |
| Monetary tightening | Generally wider (funding costs rise) |

**Market factors:**

| Factor | Effect on spreads |
| --- | --- |
| **Flight to quality** | **Wider** — and government yields **fall** simultaneously |
| **Falling market liquidity** | Wider |
| **Heavy new issuance supply** | Wider |
| Strong demand for yield ("reach for yield") | Narrower |
| Rising volatility / risk aversion | Wider |

**Issuer-specific factors:**

| Factor | Effect |
| --- | --- |
| Deteriorating financial performance | Wider |
| Rising leverage; a debt-funded acquisition | Wider |
| Large shareholder distributions | Wider |
| A downgrade, or being placed on negative watch | Wider |
| Covenant strength | Stronger covenants → narrower |
| Issue size and liquidity | Larger, more liquid issues → narrower |

**The asymmetry worth knowing:** spreads **widen much faster than they narrow**. Credit spread
series are strongly **negatively skewed** — long periods of gradual tightening punctuated by violent
widening. That shape is why credit returns have a fat left tail and why selling credit protection
resembles selling insurance: steady premium income, occasional large losses (QM LM5).

### Estimating the price impact of a spread change

```
%ΔPrice ≈ −(Modified duration × ΔSpread) + (½ × Convexity × ΔSpread²)
```

This is the same formula as for a benchmark yield change (LM12) — a spread widening moves the price
exactly as a yield rise does, because the required return has risen either way.

---

## Formulas to know cold

```
CREDIT RISK COMPONENTS
  Expected loss = Probability of default × Loss given default × Exposure at default
  Recovery rate = 1 − Loss given default

  PD  → how LIKELY   (business risk, leverage, liquidity, management)
  LGD → how MUCH     (seniority, collateral, recovery environment)
  The two are POSITIVELY correlated — recoveries are worst in recessions.

PRIORITY OF CLAIMS (absolute priority rule; often violated in practice)
  Secured → Senior unsecured → Senior subordinated → Subordinated
  → Junior subordinated → Preference shares → Common shares

  STRUCTURAL SUBORDINATION: holding-company debt is effectively junior to
  operating-subsidiary debt.

PRICE IMPACT OF A SPREAD CHANGE
  %ΔPrice ≈ −(ModDur × ΔSpread) + (½ × Convexity × ΔSpread²)

RATING BOUNDARY
  Investment grade / high yield:  Baa3 (Moody's)  =  BBB− (S&P, Fitch)
```

---

## Exam traps

> **Trap 1 — Conflating PD and LGD.** They are **independent** components. A bond can have a high PD
> and a low LGD (senior secured, weak issuer) or the reverse.

> **Trap 2 — Thinking defaults drive credit losses.** **Spread widening and downgrades** cause most
> credit portfolio losses. A year with no defaults can still be a bad year.

> **Trap 3 — Missing structural subordination.** **Holding-company debt is junior** to
> **operating-subsidiary** debt, because the opco's creditors have first claim on its assets. This
> is invisible in consolidated accounts.

> **Trap 4 — Assuming the absolute priority rule always holds.** It is **frequently violated** in
> negotiated reorganisations.

> **Trap 5 — Treating PD and LGD as independent in a portfolio model.** They are **positively
> correlated**: recoveries are lowest exactly when defaults are highest, which fattens the loss tail.

> **Trap 6 — Relying on ratings.** They **lag**, they are deliberately **through-the-cycle**, they
> measure **PD better than LGD**, and the **issuer pays** for them.

> **Trap 7 — Assuming spreads and government yields move together.** In a flight to quality,
> government yields **fall** while spreads **widen** (LM7, QM LM1).

> **Trap 8 — Treating spread changes as symmetric.** Spreads **widen far faster than they narrow** —
> the series is strongly negatively skewed.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A bond has a probability of default of 3.5% and an expected recovery rate of 42%. Compute the expected loss as a percentage of exposure.

<details><summary>Answer</summary>

Loss given default = 1 − Recovery rate = 1 − 0.42 = **58%**

Expected loss = PD × LGD = 0.035 × 0.58 = **2.03%** of exposure.

So on a 10m position, the expected loss is about **203,000**.

Note what this figure hides: it is an **expectation**, not an outcome. The actual result is either no loss (96.5% of the time) or a 58% loss (3.5% of the time). An investor who cannot tolerate the latter outcome cares about the **PD** independently of the expected loss — which is why regulatory and mandate constraints are usually written on ratings (a PD proxy) rather than on expected loss.

</details>

**2.** Explain structural subordination with an example, and say why it is easy to miss.

<details><summary>Answer</summary>

**Structural subordination** arises when debt is issued at a **holding company** while the operating assets and cash flows sit in **subsidiaries**.

**Example:** HoldCo owns 100% of OpCo. OpCo has the factories, the receivables, and all the revenue, and has borrowed 500m directly. HoldCo has separately issued 300m of bonds.

In a bankruptcy, **OpCo's creditors are paid from OpCo's assets first**. Only what remains after they are paid in full flows up to HoldCo as an equity distribution — and HoldCo's bondholders are paid from that residual. HoldCo debt is therefore **effectively junior** to OpCo debt, even though both may be labelled 'senior unsecured'.

**Why it is easy to miss:** the **consolidated** financial statements show a single balance sheet with total debt of 800m and total assets of the group. Nothing in the consolidated accounts reveals **where** the debt sits relative to **where** the assets sit.

**Where to look:** the debt note's breakdown by issuing entity, the guarantee structure (does OpCo guarantee HoldCo's debt? if so, subordination is mitigated), and the offering memorandum's structure diagram. Rating agencies notch holding-company debt down for exactly this reason.

</details>

**3.** Why do most credit portfolio losses come from spread widening rather than defaults?

<details><summary>Answer</summary>

Because of **frequency and breadth**.

**Defaults are rare and idiosyncratic.** In a diversified investment-grade portfolio, the annual default rate is measured in tens of basis points. A portfolio of 200 names might experience no defaults at all in a given year.

**Spread widening affects every holding simultaneously.** When credit conditions deteriorate, spreads widen **across the whole portfolio** — every bond is marked down at once. A 100bp widening on a portfolio with a duration of 5 costs roughly **5%** of value immediately, with no defaults at all.

**Plus the mechanisms that amplify it:**
- **Downgrade (migration) risk** — a downgrade widens the spread mechanically, and a downgrade across the investment-grade boundary triggers forced selling (LM4)
- **Liquidity risk** — bid-ask spreads widen in stress, so exiting costs more precisely when you want to
- **Mark-to-market** — the loss is recognised immediately even if the bond ultimately pays in full

**The practical consequence:** credit risk management focuses on spread duration and rating migration, not only on default probability. And it explains why a credit portfolio can have a terrible year with a zero default rate.

</details>

**4.** List four limitations of credit ratings that an analyst must work around.

<details><summary>Answer</summary>

**(1) They lag the market.** Spreads move first, sometimes by months. By the time a downgrade arrives, the price has already adjusted — so trading on rating changes is trading on stale information.

**(2) They are deliberately through-the-cycle.** Agencies aim for **stability**, smoothing through cyclical variation. That is useful for regulatory purposes but means ratings systematically **under-react** to genuine deterioration in real time.

**(3) They measure PD better than LGD.** Two bonds with the same rating can have very different **recovery** prospects depending on seniority, collateral, and the asset base. The rating compresses both components into one symbol.

**(4) The issuer-pays conflict of interest.** The rated entity selects and pays the agency. The structural incentive toward rating inflation is well documented, most catastrophically in structured products before 2008.

**Also:** ratings say nothing about **spread risk or liquidity risk**, which is where most losses come from; and **mechanical reliance** in mandates and capital rules creates cliff effects at the investment-grade boundary that amplify price moves beyond what the fundamentals justify.

**How to work around them:** treat the rating as a **screening input**, do independent ratio and covenant analysis (LM16), watch market-implied measures (spreads, CDS), and read the agency's **rationale and outlook** rather than just the symbol.

</details>

**5.** A bond has a modified duration of 6.4 and convexity of 58. Its spread widens by 120bp with no change in the benchmark yield. Estimate the price change.

<details><summary>Answer</summary>

A spread widening moves the price exactly as a yield rise does — the required return has increased either way.

```
Duration term    = −6.4 × 0.0120             = −7.680%
Convexity adjust = 0.5 × 58 × (0.0120)²      = 0.5 × 58 × 0.000144 = +0.042%
                                                 ─────────
Estimated %ΔPrice                              = −7.638%
```

The bond falls approximately **7.64%** with **no default, no downgrade to junk, and no change in government yields**. This is the spread risk that dominates credit portfolio losses.

Note the convexity adjustment is small here (4bp) because the move is modest and convexity is low. For a longer-duration bond in a 400bp widening it would be far more significant.

</details>

---

## Done when

- [ ] I can define PD and LGD and compute expected loss and the recovery rate
- [ ] I can state the priority of claims and explain structural subordination
- [ ] I can explain why PD and LGD are positively correlated and what that does to the loss distribution
- [ ] I can explain why spread widening rather than default drives most credit portfolio losses
- [ ] I can name the rating categories and the investment-grade boundary in both scales
- [ ] I can list four limitations of ratings and say how to work around them
- [ ] I can name macroeconomic, market, and issuer-specific spread drivers
- [ ] I can estimate a price change from a spread move using duration and convexity
- [ ] I answered the self-check cold, several days after first study

---

← [LM13 Curve-Based and Empirical Fixed-Income Risk Measures](lm-13-curve-based-and-empirical-fixed-income-risk-measures.md)  ·  [Topic index](README.md)  ·  [LM15 Credit Analysis for Government Issuers](lm-15-credit-analysis-for-government-issuers.md) →
