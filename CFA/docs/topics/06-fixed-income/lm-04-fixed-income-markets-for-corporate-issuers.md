# FI · LM04 — Fixed-Income Markets for Corporate Issuers

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | LM1–LM3, Corporate Issuers LM4 (short-term funding). |
| **Where it shows up** | 1–2 questions. Repos and the investment-grade/high-yield distinction are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- compare short-term funding alternatives available to corporations and financial institutions
- describe repurchase agreements (repos), their uses, and their benefits and risks
- contrast the long-term funding of investment-grade versus high-yield corporate issuers

---

## Core concepts

### Short-term funding

**For non-financial corporations:**

| Source | Detail |
| --- | --- |
| **Commercial paper (CP)** | Unsecured short-term notes, typically **under 270 days** in the US (to avoid registration). Available only to **high-quality** issuers. Issued at a **discount** |
| **Bank lines of credit** | **Uncommitted** (the bank may refuse), **committed/regular** (the bank must lend; a fee is paid), or a **revolving credit facility** (the most reliable, multi-year, and the standard CP **backstop**) |
| **Trade credit from suppliers** | Effectively free until the discount period lapses — then very expensive (Corporate Issuers LM4) |
| **Secured borrowing** | Against receivables or inventory; factoring |

> **Commercial paper is backstopped for a reason.** CP must be continually rolled over, and in a
> credit event the market can close **abruptly**. Issuers therefore maintain committed bank lines
> sufficient to repay maturing CP — a facility they hope never to draw. When the CP market froze in
> 2008, that backstop was what stood between many issuers and default.

**For banks and financial institutions:**

| Source | Detail |
| --- | --- |
| **Retail deposits** | The cheapest and stickiest funding. **Demand**, savings, and **time deposits (CDs)** |
| **Certificates of deposit** | **Non-negotiable** (held to maturity, penalty for early withdrawal) or **negotiable** (tradeable; large denominations) |
| **Central bank funds market** | Banks lend reserve balances to one another overnight |
| **Interbank market** | Unsecured lending between banks, typically short-dated |
| **Repurchase agreements** | Secured short-term borrowing — see below |

### Repurchase agreements

**A repo is a sale of a security with an agreement to repurchase it at a higher price on a later
date.** Economically it is a **collateralised loan**: the security is the collateral, and the price
difference is the interest.

```
Repo rate = (Repurchase price − Sale price) / Sale price × (360 / days)

Repo margin (haircut) = (Collateral market value − Loan amount) / Collateral market value
```

| Term | Meaning |
| --- | --- |
| **Repo** | From the **borrower's** perspective — sells the security, agrees to buy it back |
| **Reverse repo** | The same transaction from the **lender's** perspective — buys the security, agrees to sell it back |
| **Overnight repo** | One day |
| **Term repo** | Longer than one day |
| **Haircut / repo margin** | The excess of collateral value over the loan — protects the lender against a fall in collateral value |

**What determines the repo rate:**

| Factor | Effect on the repo rate |
| --- | --- |
| **Higher-quality collateral** | **Lower** rate |
| **Longer term** | Generally **higher** |
| **Collateral delivered to the lender** (rather than held by the borrower) | **Lower** rate — less risk |
| **Collateral in high demand** (a "special") | **Lower** rate — the lender wants that specific security |
| **General market interest rates** | Higher rates → higher repo rate |

**Uses of repos:**

- **Short-term financing** for dealers to carry inventory — this is the backbone of bond market
  liquidity
- **Investing surplus cash** securely (the reverse repo side)
- **Central bank operations** — open market operations to add or drain liquidity
- **Obtaining a specific security** to cover a short position

**Risks:**

| Risk | Detail |
| --- | --- |
| **Credit / counterparty risk** | The counterparty fails. Mitigated by the **haircut** and by marking to market |
| **Collateral risk** | The collateral falls in value or becomes illiquid |
| **Margin / rollover risk** | The lender demands a larger haircut, or declines to roll the repo at all |

> **Repo is where liquidity crises begin.** It is short-term, continuously rolled, and secured
> against assets whose value falls in stress. A lender who doubts the collateral raises the haircut
> or withdraws — forcing the borrower to sell assets into a falling market, which lowers collateral
> values further and prompts more haircut increases. This **feedback loop** is the mechanism behind
> most modern financial crises, and it is why repo markets are a central object of regulatory
> attention.

### Long-term funding: investment grade versus high yield

| | **Investment grade** (BBB−/Baa3 and above) | **High yield** (below BBB−/Baa3) |
| --- | --- | --- |
| **Instruments** | Public bonds, medium-term notes, CP for short-term | Public bonds, **bank loans (leveraged loans)**, private placements, PIK notes |
| **Security** | Usually **unsecured** | Often **secured**, and structurally subordinated layers |
| **Covenants** | **Lighter** — the issuer's quality is the protection | **Tighter** and more numerous — maintenance covenants, restricted payments |
| **Call features** | Often **make-whole** calls (expensive to exercise) | **Hard call protection** for a period, then a declining call price schedule |
| **Maturities** | Wide range, out to 30 years and beyond | Typically **shorter** — 5 to 10 years |
| **Investor base** | Pensions, insurers, index funds — **mandate-constrained** | Dedicated high-yield funds, CLOs, hedge funds |
| **Pricing driver** | Mostly **interest rate risk** — spreads are narrow and stable | Mostly **credit risk** — spread dominates, and behaves more like equity |
| **Documentation** | Standardised | Heavily negotiated |

**Additional instruments across the spectrum:**

- **Medium-term notes (MTNs)** — issued continuously off a shelf programme rather than in a single
  large offering, allowing an issuer to tailor size, maturity, and structure to investor demand.
- **Leveraged loans** — floating-rate senior secured bank debt, syndicated to institutional
  investors, and the principal collateral for **CLOs**.
- **Bridge financing** — temporary funding pending a permanent issue.

> **Why the investment-grade boundary matters so much:** many institutional mandates and regulatory
> capital rules prohibit holding below investment grade. A downgrade across the boundary forces
> mandate-constrained holders to sell **regardless of price**, producing a price fall far larger than
> the change in default probability alone justifies. Such issuers are called **fallen angels**, and
> the forced-selling dynamic is a recurring source of opportunity for unconstrained investors.

---

## Formulas to know cold

```
REPURCHASE AGREEMENT
  Repo rate = [(Repurchase price − Sale price) / Sale price] × (360 / days)
  Dollar interest = Sale price × Repo rate × (days / 360)

  Repo margin (haircut) = (Collateral value − Loan amount) / Collateral value

  REPO         = the BORROWER's side (sells now, buys back later)
  REVERSE REPO = the LENDER's side  (buys now, sells back later)

  Repo rate is LOWER when:  collateral quality is higher · collateral is delivered to the lender
                            · the collateral is in special demand · the term is shorter

COMMERCIAL PAPER
  Unsecured, typically < 270 days (US), issued at a DISCOUNT, high-quality issuers only,
  ALWAYS backstopped by committed bank lines because the market can close abruptly.

INVESTMENT GRADE / HIGH YIELD BOUNDARY:  BBB− / Baa3
  Crossing it forces mandate-constrained selling — a "FALLEN ANGEL"
```

---

## Exam traps

> **Trap 1 — Repo vs reverse repo.** **Repo is the borrower's side** (sell now, buy back later);
> **reverse repo is the lender's side**. The same transaction, named from opposite ends.

> **Trap 2 — Thinking higher-quality collateral means a higher repo rate.** It means a **lower**
> rate — less risk to the lender, so less compensation required.

> **Trap 3 — Missing the "special" effect.** Collateral in high demand commands a **lower** repo
> rate, because the lender wants that particular security and will accept less interest to get it.

> **Trap 4 — Treating commercial paper as low risk because it is short.** It carries **rollover
> risk**: the market can close abruptly. This is why committed backstop lines are mandatory.

> **Trap 5 — Haircut direction.** The haircut **protects the lender**: collateral value exceeds the
> loan. A larger haircut means less credit extended per unit of collateral.

> **Trap 6 — Assuming high-yield bonds have weaker covenants.** The reverse: **high-yield covenants
> are tighter and more numerous**, because the issuer's quality provides less protection.

> **Trap 7 — Underestimating the investment-grade boundary.** Forced selling by mandate-constrained
> holders makes the price move far larger than the change in fundamentals alone.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A dealer sells 10m of government bonds under a 7-day repo at a repo rate of 4.2%, with a 2% haircut. Compute the loan amount and the interest paid.

<details><summary>Answer</summary>

**Loan amount:** the haircut means the lender advances less than the collateral's market value.
Loan = 10,000,000 × (1 − 0.02) = **9,800,000**

**Interest** (money-market convention, 360-day year):
Interest = 9,800,000 × 4.2% × (7/360) = 9,800,000 × 0.042 × 0.019444 = **8,003**

**Repurchase price** = 9,800,000 + 8,003 = **9,808,003**

Economically: the dealer has borrowed 9.8m for a week against 10m of collateral, paying 8,003 in interest. The 200,000 haircut protects the lender if the bonds fall in value before the repo unwinds.

</details>

**2.** Explain how the repo market can transmit a shock into a full liquidity crisis.

<details><summary>Answer</summary>

Through a **self-reinforcing feedback loop**:

1. **A shock reduces confidence** in a class of collateral — say mortgage-backed securities.
2. **Lenders raise haircuts.** A borrower who could finance 98% of collateral value can now finance only 85%. The same collateral supports far less borrowing.
3. **Borrowers must find cash** to replace the lost financing. Since repo is overnight or short-term, this happens **within days**.
4. **They sell assets** — and in stress, they sell the most liquid assets first, then the impaired ones, into a market with few buyers.
5. **Forced selling lowers prices**, which reduces collateral values further, which triggers **more haircut increases and margin calls**.
6. **Some lenders withdraw entirely**, refusing to roll at any haircut.

**Why repo specifically:** it is (a) **short-term and continuously rolled**, so refusal to roll is immediate rather than gradual; (b) **secured against assets whose value falls in stress**, so the collateral and the confidence deteriorate together; and (c) **enormous in size** and central to dealer inventory financing, so a repo freeze removes market-making capacity exactly when liquidity is needed.

This mechanism is why central banks intervene directly in repo markets during crises, and why post-crisis regulation focused heavily on funding stability.

</details>

**3.** Contrast the covenant packages typical of investment-grade and high-yield bonds, and explain why they differ.

<details><summary>Answer</summary>

**Investment grade: lighter covenants.** Often only an affirmative reporting obligation, a negative pledge, and limits on merger or change of control. Few or no **maintenance** covenants (ratios tested each period).

**High yield: tighter and more numerous.** Restrictions on additional indebtedness (often a fixed-charge coverage test before new debt), **restricted payments** baskets limiting dividends and buybacks, limits on asset sales and on the use of proceeds, change-of-control put options, and frequently maintenance covenants in the accompanying bank loans.

**Why they differ:** covenants substitute for issuer quality. An investment-grade issuer has a strong balance sheet, diversified funding access, and a reputation it needs to preserve for future issuance — its **own incentives** largely protect creditors. A high-yield issuer has none of that cushion, so the creditor's protection must be written into the contract.

**The practical consequence for an analyst:** covenant strength should be priced. **Covenant-lite** high-yield debt — increasingly common in strong markets — offers the spread of a high-yield credit with materially less protection, and recovery rates on such debt have historically been lower.

</details>

**4.** Why does a bond downgraded from BBB− to BB+ often fall in price by far more than the change in default probability justifies?

<details><summary>Answer</summary>

Because of **forced selling across the investment-grade boundary**.

Many institutional mandates — insurance company portfolios, pension funds, and index-tracking funds benchmarked to investment-grade indexes — **prohibit holding below investment grade**. Bank regulatory capital rules also penalise sub-investment-grade holdings heavily.

When the downgrade occurs, those holders must sell **regardless of price**, often within a specified window. Simultaneously, the natural buyers — dedicated high-yield funds — have limited capacity to absorb a large investment-grade issue at short notice, and they know the sellers are constrained.

The result is a price fall driven by a **supply-demand imbalance in the holder base**, not by fundamentals. The issuer is called a **fallen angel**.

**The opportunity:** unconstrained investors who can buy fallen angels at the forced-selling price have historically earned attractive returns, since the rating change typically reflects information already partly in the price. The risk is obvious — the downgrade is usually deserved, and some fallen angels keep falling.

</details>

---

## Done when

- [ ] I can compare short-term funding sources for corporations and for banks
- [ ] I can explain why commercial paper requires a committed backstop line
- [ ] I can compute a repo rate, the interest, and the effect of a haircut
- [ ] I can distinguish repo from reverse repo and state what makes the repo rate lower
- [ ] I can explain the repo feedback loop that turns a shock into a liquidity crisis
- [ ] I can contrast investment-grade and high-yield funding on six dimensions
- [ ] I can explain the fallen angel dynamic and why the price move exceeds the fundamental change
- [ ] I answered the self-check cold, several days after first study

---

← [LM03 Fixed-Income Issuance and Trading](lm-03-fixed-income-issuance-and-trading.md)  ·  [Topic index](README.md)  ·  [LM05 Fixed-Income Markets for Government Issuers](lm-05-fixed-income-markets-for-government-issuers.md) →
