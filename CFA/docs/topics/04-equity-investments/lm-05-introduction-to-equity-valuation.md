# EQ · LM05 — Introduction to Equity Valuation

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | QM LM4 (discounting), Corporate Issuers LM6 (WACC). |
| **Where it shows up** | 1–2 questions. Sets up LM6 and LM7 — the model-selection LOS is the examinable part. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- contrast price and value for an equity security
- contrast the use of book value of equity, market capitalization, and enterprise value as indicators of intrinsic value
- describe major categories of equity valuation models and explain their advantages and disadvantages

---

## Core concepts

### Price and value are different things

| | **Price** | **(Intrinsic) value** |
| --- | --- | --- |
| What it is | What the market is charging today | What the security is **worth**, given its expected cash flows and risk |
| Observable? | **Yes**, continuously | **No** — it is an estimate |
| Determined by | Supply and demand right now | Fundamentals |

**The entire purpose of valuation** is to form a view of value independent of price, then compare:

```
Value > Price  →  undervalued  →  buy
Value < Price  →  overvalued   →  sell / avoid
Value = Price  →  fairly priced
```

> **The humility required:** your estimate can be wrong. A gap between your value and the market's
> price has two possible explanations — the market is mispricing the security, **or you are**. The
> analyst's job includes asking what the market knows that you do not, and what assumption you would
> need to change to reach the market's price (the implied-growth exercise in QM LM4).

**The efficient market context:** in a perfectly efficient market, price always equals value and
active analysis is worthless. Real markets are **imperfectly efficient** — which is exactly what
makes analysis worth doing and also what makes it hard. The relationship is self-correcting:
analysts searching for mispricing are the mechanism by which prices become efficient.

### Three measures of what a company is "worth"

| Measure | Formula | What it captures | Limitation |
| --- | --- | --- | --- |
| **Book value of equity** | Total assets − Total liabilities | Historical accounting net worth | Backward-looking; excludes internally generated intangibles; distorted by accounting policy and by buybacks above book |
| **Market capitalisation** | Share price × Shares outstanding | The market's view of the **equity** | Ignores debt entirely — useless for comparing companies with different leverage |
| **Enterprise value (EV)** | Market cap + Total debt − Cash and equivalents | The value of the whole **operating business**, to all capital providers | Requires care with what counts as debt (leases, pensions, minorities) |

**Why enterprise value exists.** Two companies with identical operations but different capital
structures have different market capitalisations — the more levered one has a smaller equity value
because debt has a prior claim. EV strips that out: it is what you would pay to acquire the entire
business free of its financing.

```
EV = Market capitalisation + Total debt + Preferred + Minority interest − Cash and equivalents
```

Cash is subtracted because acquiring the company gets you the cash back — you are effectively buying
the business for its price net of the cash on its balance sheet.

> **The pairing rule, which governs every multiple in LM7:** an **EV** multiple must be paired with
> a **pre-interest** measure (EBITDA, EBIT, sales), because EV belongs to all capital providers. An
> **equity** multiple must be paired with a **post-interest** measure (net income, book equity).
> **EV/net income** is meaningless — and it is the single most common multiples error.

### Categories of valuation model

**1. Present value (absolute / discounted cash flow) models**

Value = the present value of expected future cash flows.

| Model | Discounts | At |
| --- | --- | --- |
| **Dividend discount model (DDM)** | Dividends | Cost of equity |
| **Free cash flow to equity (FCFE)** | FCFE | Cost of equity |
| **Free cash flow to the firm (FCFF)** | FCFF | **WACC** (gives EV, then subtract debt) |
| **Residual income** | Book value + PV of economic profits | Cost of equity |

| Advantages | Disadvantages |
| --- | --- |
| Theoretically sound — value comes from cash flows | Highly **sensitive to inputs**, especially `r` and `g` |
| Forces explicit assumptions you must defend | Terminal value often 60–80% of the total |
| Works for non-dividend-payers (FCFE/FCFF) | DDM unusable for non-payers or erratic payers |
| Gives an absolute value, not a relative one | Requires forecasting, which is where the error lives |

**2. Relative valuation (multiples)**

Value by comparison: what are similar companies worth per unit of earnings, book value, sales, or
EBITDA?

| Advantages | Disadvantages |
| --- | --- |
| Quick, transparent, and widely understood | Only tells you what the peer group is worth — if the **whole sector is mispriced**, the multiple carries the error |
| Reflects current market sentiment | Comparability is often poor (accounting policy, growth, risk, capital structure) |
| Fewer assumptions to defend | Denominators can be negative or meaningless (loss-making companies) |
| Good for cross-sectional screening | Backward-looking if trailing figures are used |

**3. Asset-based valuation**

Value = the market value of assets less the market value of liabilities.

Appropriate for **asset-intensive businesses**, financial institutions, natural resource companies,
holding companies, and **liquidation** scenarios. It fails badly for businesses whose value is in
intangibles, brands, people, or growth options — precisely the assets that are not on the balance
sheet (FSA LM3).

### Choosing a model

| Situation | Model |
| --- | --- |
| Mature, stable, reliable dividend payer | **DDM** |
| Non-dividend-payer, or dividends unrelated to earnings capacity | **FCFE** or **FCFF** |
| High and changing leverage, or a control perspective | **FCFF** (capital-structure independent) |
| Minority stake in a dividend-paying company | **DDM** — a minority holder receives dividends, not free cash flow |
| Asset-heavy, financial, or resource company | **Asset-based**, or a book-value multiple |
| Screening a large universe quickly | **Multiples** |
| Loss-making or early stage | **EV/sales**, or a scenario-based DCF |
| Cyclical company at a cycle extreme | **Normalised** earnings multiples, or a DCF spanning a full cycle |

> **Best practice is to use more than one.** A DCF and a multiples check answer different questions,
> and their disagreement is informative: if your DCF says 80 and the peer group implies 50, either
> your growth assumption is aggressive or the market is pricing in something you have not modelled.
> Either way, you have learned where the argument is.

---

## Formulas to know cold

```
Enterprise value
  EV = Market cap + Total debt + Preferred + Minority interest − Cash and equivalents

Book value of equity = Total assets − Total liabilities
Market capitalisation = Share price × Shares outstanding

THE PAIRING RULE (governs every multiple in LM7)
  EV multiples     ↔  PRE-interest flows:   EBITDA, EBIT, Sales, FCFF
  Equity multiples ↔  POST-interest flows:  Net income, EPS, Book equity, FCFE
  EV/Net income is MEANINGLESS — never use it.

MODEL SELECTION
  Dividend-paying, stable, minority stake      →  DDM        (discount at cost of equity)
  Non-payer / dividends ≠ capacity              →  FCFE       (discount at cost of equity)
  Changing leverage, control perspective        →  FCFF       (discount at WACC → EV)
  Asset-heavy, financial, resource, liquidation →  Asset-based
  Quick screen, or loss-making                  →  Multiples
```

---

## Exam traps

> **Trap 1 — Confusing price with value.** Price is observable; value is estimated. The whole
> exercise is comparing them — and accepting that your estimate may be the wrong one.

> **Trap 2 — Mismatching the multiple.** **EV pairs with pre-interest** measures (EBITDA, EBIT,
> sales). **Equity value pairs with post-interest** measures (net income, book equity). EV/net income
> is the classic error.

> **Trap 3 — Forgetting to subtract cash in EV.** Cash is **subtracted**; debt is added.

> **Trap 4 — Using the DDM for a non-dividend-payer.** It cannot work. Use FCFE or FCFF.

> **Trap 5 — Discounting FCFF at the cost of equity.** **FCFF pairs with WACC** and yields enterprise
> value (subtract net debt for equity value). **FCFE pairs with the cost of equity** and yields
> equity value directly.

> **Trap 6 — Believing multiples are assumption-free.** Using a peer multiple assumes the peer group
> is correctly priced and genuinely comparable. If the whole sector is mispriced, the multiple
> inherits the error in full.

> **Trap 7 — Applying asset-based valuation to an intangible-heavy business.** The most valuable
> assets — brands, R&D, customer relationships, people — are largely absent from the balance sheet.

> **Trap 8 — Trusting book value as a value indicator.** It is historical, policy-dependent, and can
> even be **negative** for a highly profitable company that has repurchased shares above book.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company has a market cap of 4,200m, total debt of 1,800m, and cash of 350m. Compute enterprise value and explain when you would use it instead of market cap.

<details><summary>Answer</summary>

EV = 4,200 + 1,800 − 350 = **5,650m**

**When to use EV instead of market cap:**
- **Comparing companies with different leverage.** A company funded 70% with debt has a small equity value relative to its operations; market cap would make it look cheap on any earnings multiple when it is simply levered.
- **Acquisition analysis.** An acquirer buys the whole business and assumes its debt — EV is closer to what must actually be paid.
- **Operating multiples.** EV/EBITDA and EV/Sales compare the value of the *operations* to the *operating* result, independent of financing.

Cash is subtracted because acquiring the company delivers the cash back to the buyer — the effective price of the business is net of it.

</details>

**2.** Why is EV/EBITDA a legitimate multiple while EV/net income is not?

<details><summary>Answer</summary>

Because of the **pairing rule**: the numerator and denominator must belong to the **same claimants**.

**Enterprise value** is the value of the whole business to **all** capital providers — debt and equity together.

**EBITDA** is earnings **before** interest, so it is the operating result available to **all** those providers. Numerator and denominator match.

**Net income** is **after** interest — it belongs to **equity holders alone**. Dividing enterprise value by an equity-only flow compares a claim covering everyone to a flow covering only shareholders. The multiple has no coherent interpretation, and it moves with leverage for no economic reason.

The correct equity pairing for net income is **market cap / net income** — the P/E ratio.

</details>

**3.** A technology company pays no dividend and has negative earnings but is growing revenue at 45% a year. Which valuation approaches can you use, and what are their limitations?

<details><summary>Answer</summary>

**Not usable:** the DDM (no dividends) and any P/E-based multiple (negative denominator).

**Usable:**

**(1) FCFE or FCFF DCF.** The theoretically right approach — value the cash flows once the business matures. **Limitation:** almost all the value sits in a terminal value built on assumptions about a profitability level the company has never demonstrated. Extremely sensitive to the margin and growth assumptions, so present it as a range with explicit scenarios.

**(2) EV/Sales.** Works with negative earnings. **Limitation:** it implicitly assumes an eventual margin. EV/Sales of 8× is only meaningful alongside a view on what margin the business will reach — two companies at the same EV/Sales with different terminal margins are not comparably priced.

**(3) Multiples of a forward, normalised metric** — EV/EBITDA on a year when the company is expected to be profitable, or a price/gross profit measure.

**(4) Business-model-specific metrics** (Corporate Issuers LM7) — value per subscriber, EV/annual recurring revenue, with LTV/CAC as a sanity check on unit economics.

Use several. Their disagreement tells you which assumption the valuation actually rests on.

</details>

**4.** Your DCF gives a value of 92 for a share trading at 61. What should you do before recommending a purchase?

<details><summary>Answer</summary>

**Interrogate your own model first.** A 50% gap is more often an error in the analysis than a market mispricing.

1. **Reverse-engineer the market's assumptions.** What growth rate, margin, or discount rate would produce 61? (The implied-growth exercise from QM LM4.) If the market is pricing 2% growth and you are assuming 7%, the disagreement is now specific and arguable rather than a bare number.
2. **Check the terminal value share.** If it is 80% of your total, the valuation is really a statement about `g` and `r`, not about the explicit forecast.
3. **Sanity-check against multiples.** What P/E and EV/EBITDA does your 92 imply? If it implies 40× in a sector trading at 14×, say why this company deserves it.
4. **Sensitivity-test** the two or three assumptions that drive the answer, and present a range.
5. **Ask what the market knows that you do not** — a pending regulatory decision, customer concentration, a covenant issue, an accounting concern (FSA LM10).

Then recommend, stating the assumptions the thesis depends on and what would falsify it.

</details>

---

## Done when

- [ ] I can contrast price and value and state what a gap between them implies
- [ ] I can compute enterprise value with the right signs on debt and cash
- [ ] I can state the pairing rule and explain why EV/net income is meaningless
- [ ] I can name the four present value models and the correct discount rate for each
- [ ] I can list the advantages and disadvantages of DCF, multiples, and asset-based approaches
- [ ] I can select an appropriate model from a described situation and justify it
- [ ] I can explain why book value is a weak indicator of intrinsic value
- [ ] I answered the self-check cold, several days after first study

---

← [LM04 Sources of Equity Returns](lm-04-sources-of-equity-returns.md)  ·  [Topic index](README.md)  ·  [LM06 Discounted Cash Flow (DCF) and Growth Models](lm-06-discounted-cash-flow-dcf-and-growth-models.md) →
