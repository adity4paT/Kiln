# FI · LM01 — Fixed-Income Instrument Features

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 3 |
| **Prerequisites** | None. Entry point to Fixed Income. |
| **Where it shows up** | 1 question. Pure recall — but the vocabulary is used in all 19 modules. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe the features of a fixed-income security
- describe the contents of a bond indenture and contrast affirmative and negative covenants

---

## Core concepts

### The three elements of every bond

1. **Issuer** — who owes the money
2. **Maturity** — when the principal is repaid
3. **Principal and coupon** — how much, and at what rate

### Core features

| Feature | Meaning |
| --- | --- |
| **Issuer** | Sovereign, non-sovereign (state, province, municipality), quasi-government agency, supranational (World Bank, EIB), or corporate |
| **Maturity (tenor)** | Time to the final principal repayment. **Money market** = one year or less at issuance; **capital market** = more than one year. **Perpetual** bonds never mature |
| **Par value (face, principal, redemption value)** | The amount repaid at maturity. Prices are quoted as a **percentage of par**: 98.5 means 98.5% of par |
| **Coupon rate and frequency** | The annual interest rate applied to par. Usually paid semiannually; annually in much of Europe |
| **Currency denomination** | Which currency the cash flows are in. **Dual-currency** bonds pay coupons in one and principal in another |
| **Yield measures** | Discussed fully in LM6–LM8 |

**Price terminology, which is tested:**

| Term | Condition |
| --- | --- |
| **Premium** | Price **above** par — coupon rate **above** the market's required yield |
| **Par** | Price equal to par — coupon equals required yield |
| **Discount** | Price **below** par — coupon **below** required yield |

### Bond markets by currency and jurisdiction

| Type | Definition |
| --- | --- |
| **Domestic bond** | Issued in the issuer's home country, home currency, by a domestic issuer |
| **Foreign bond** | Issued in a **foreign** country's domestic market, in that country's currency, by a foreign issuer. Nicknames: **Yankee** (US), **Bulldog** (UK), **Samurai** (Japan), **Kangaroo** (Australia) |
| **Eurobond** | Issued **outside the jurisdiction of any single country**, typically unregistered and in **bearer** form. Nothing to do with the euro — a "eurodollar bond" is a USD bond issued outside the US |
| **Global bond** | Issued simultaneously in the eurobond market and in one or more domestic markets |

> **Trap:** a **eurobond** is defined by being issued outside any single country's jurisdiction, not
> by its currency. Eurobonds face **less regulation and lighter disclosure** than domestic issues,
> and historically were in bearer form (no registered owner), which had tax implications.

### Legal, regulatory, and tax considerations

- **Registered vs. bearer form** — a registered bond's owner is recorded; a bearer bond belongs to
  whoever holds it.
- **Taxation:** coupon interest is usually taxed as **ordinary income**; capital gain or loss on
  sale or redemption is taxed separately. A **discount bond** held to maturity accretes toward par,
  and that accretion may be taxed as interest income annually even though no cash is received —
  **original issue discount** treatment. A **premium bond** may permit amortisation of the premium
  against interest income.
- **Some government bonds are tax-exempt** to certain holders (US municipal bonds to US investors).

### The bond indenture (trust deed)

The **legal contract between the issuer and the bondholders**, held and enforced by a **trustee**
appointed to act on the bondholders' behalf.

**Contents:**

| Item | What it specifies |
| --- | --- |
| **Issuer and legal identity** | Including whether a **special purpose entity** is the issuer (securitisation — LM17) |
| **Source of repayment** | Cash flow from operations; a specific revenue stream; a government's taxing power |
| **Collateral / credit enhancement** | Secured vs. unsecured; guarantees; letters of credit; overcollateralisation |
| **Covenants** | Affirmative and negative undertakings |
| **Contingency provisions** | Call, put, conversion features |
| **Terms** | Maturity, coupon, frequency, currency, denomination |

**Asset-backed and collateral terminology:** **collateral trust bonds** (secured on financial
assets), **equipment trust certificates** (secured on physical equipment — common for rolling stock
and aircraft), **mortgage-backed securities** (LM19), and **covered bonds** (LM18), where the
underlying pool stays on the issuer's balance sheet and investors have **dual recourse** — to the
pool *and* to the issuer.

### Covenants — affirmative and negative

**Covenants are the lender's substitute for control rights** (Corporate Issuers LM2). Because
debtholders have no vote, covenants are how they constrain behaviour that would transfer value to
shareholders.

| | **Affirmative covenants** | **Negative covenants** |
| --- | --- | --- |
| Nature | What the issuer **must do** | What the issuer **must not do** |
| Typical cost | Generally **low cost** to the issuer | **Restrict operating and financing flexibility** |

**Affirmative covenant examples:**
- Make timely payments of principal and interest
- Maintain the corporate existence and its properties
- Comply with applicable laws and regulations
- Pay taxes and other claims when due
- Provide **financial statements and reports** on schedule
- Maintain **specified financial ratios** — e.g. interest coverage above 3.0×, debt/EBITDA below 4.0×

**Negative covenant examples:**
- **Restrictions on additional debt** — a limit on further borrowing or on leverage
- **Negative pledge** — cannot grant security to other lenders without granting it equally here
- **Restricted payments** — limits on dividends and share buybacks
- **Restrictions on asset sales** or on the disposal of collateral
- Restrictions on mergers, acquisitions, and changes of control
- Limits on **sale-and-leaseback** transactions

> **Why negative covenants matter more to the analyst:** they directly prevent the actions that
> transfer value from creditors to shareholders — levering up, paying a large special dividend,
> selling the assets that back the debt. A bond with weak negative covenants ("covenant-lite") offers
> materially less protection, and the yield should reflect that.
>
> Covenants are also where **default** usually begins. A covenant breach is a **technical default**
> that can accelerate the debt long before the issuer actually misses a payment — which is precisely
> the point: it gives lenders a seat at the table while there is still something to negotiate over.

---

## Formulas to know cold

```
PRICE vs PAR (memorise the direction — it recurs in every valuation module)
  Coupon rate > required yield  →  PREMIUM  (price above par)
  Coupon rate = required yield  →  PAR
  Coupon rate < required yield  →  DISCOUNT (price below par)
  And ALWAYS: price moves INVERSELY to yield.

Prices are quoted as a PERCENTAGE OF PAR:  98.5 means 98.5% of par value.

BOND MARKET CLASSIFICATION
  Domestic — home country, home currency, domestic issuer
  Foreign  — foreign issuer, in that country's domestic market and currency
             (Yankee / Bulldog / Samurai / Kangaroo)
  Eurobond — issued OUTSIDE any single country's jurisdiction; often bearer form;
             NOT defined by currency
  Global   — eurobond market AND one or more domestic markets simultaneously

COVENANTS
  AFFIRMATIVE = what the issuer MUST DO      (pay, report, maintain ratios)
  NEGATIVE    = what the issuer MUST NOT DO  (additional debt, dividends, asset sales,
                                              negative pledge)
```

---

## Exam traps

> **Trap 1 — Eurobonds and the euro.** A **eurobond** is issued outside the jurisdiction of any
> single country. It has **nothing to do with the euro currency** — a eurodollar bond is a USD bond
> issued outside the US.

> **Trap 2 — Affirmative vs negative covenants.** **Affirmative = must do.** **Negative = must not
> do.** Maintaining a ratio is affirmative; a limit on additional debt is negative.

> **Trap 3 — Premium and discount direction.** A **premium** bond has a coupon **above** the required
> yield. Reversing this cascades into every valuation question.

> **Trap 4 — Forgetting that a covenant breach is a default.** Technical default can accelerate the
> debt before any payment is missed.

> **Trap 5 — Covered bonds vs asset-backed securities.** A **covered bond** pool stays **on** the
> issuer's balance sheet and investors have **dual recourse**. An ABS pool is sold to an SPE and
> investors have recourse only to the pool (LM17–LM18).

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A Japanese company issues a bond denominated in US dollars, sold to investors in the US market under US regulations. What type of bond is it?

<details><summary>Answer</summary>

A **foreign bond** — specifically a **Yankee bond**.

The defining features: a **foreign issuer** (Japanese), issuing in **another country's domestic market** (the US), in **that country's currency** (USD), subject to **that country's regulation** (SEC registration and disclosure).

Contrast with a **eurobond**: if the same Japanese company issued a USD bond **outside** US jurisdiction — sold to international investors through a syndicate in London, not registered with the SEC — it would be a **eurodollar bond** (a type of eurobond), with lighter regulation and disclosure.

</details>

**2.** Classify each as affirmative or negative: (a) maintain interest coverage above 2.5x, (b) do not pledge assets to other lenders, (c) file audited financial statements within 90 days, (d) limit dividends to 50% of net income.

<details><summary>Answer</summary>

**(a) Affirmative** — the issuer *must do* something: maintain a specified ratio.
**(b) Negative** — a **negative pledge**; the issuer *must not* grant security to others.
**(c) Affirmative** — must provide reports.
**(d) Negative** — a **restricted payments** covenant; the issuer must not exceed a distribution limit.

The test is simply the grammar of the obligation: does it require action (affirmative) or forbid it (negative)?

</details>

**3.** Why do negative covenants matter more to a credit analyst than affirmative ones?

<details><summary>Answer</summary>

Because **negative covenants prevent the specific actions that transfer value from creditors to shareholders** — which is the structural conflict at the heart of debt investing (Corporate Issuers LM2).

Shareholders hold a residual claim that behaves like a call option, so they benefit from actions that raise risk or extract cash: levering up, paying a large special dividend, buying back stock, selling the assets that back the debt, or granting a prior claim to a new lender. None of these is prevented by an affirmative covenant.

**Negative covenants block them directly:** limits on additional debt, restricted payments, negative pledge, restrictions on asset sales and on change of control.

Affirmative covenants are largely things a solvent issuer would do anyway — pay on time, file accounts, maintain the business. They matter mainly as an **early warning mechanism**: a missed reporting deadline or a breached maintenance ratio signals trouble and can accelerate the debt while there is still value to negotiate over.

The practical consequence: **covenant-lite** debt offers materially less protection, and the spread should compensate for it.

</details>

**4.** What is the role of the trustee under a bond indenture?

<details><summary>Answer</summary>

The trustee is appointed to **act on behalf of the bondholders** as a collective, because bondholders are dispersed and cannot practically coordinate.

The trustee's functions:
- **Holds the indenture** and represents bondholders' interests under it
- **Monitors compliance** with the covenants
- **Enforces the terms** on default — declaring a default, accelerating the debt, and pursuing remedies including claims on collateral
- **Administers payments** in some structures, and communicates with bondholders
- **Coordinates collective action** in a restructuring, where individual bondholders acting alone would be unable to negotiate

The trustee is normally a bank or trust company. Note it acts for bondholders, **not** for the issuer, despite being appointed and paid by the issuer — a structural tension the exam does not dwell on but which is worth noticing.

</details>

---

## Done when

- [ ] I can name the three elements of every bond and describe six core features
- [ ] I can state the premium/par/discount conditions and the inverse price-yield relationship
- [ ] I can distinguish domestic, foreign, eurobond, and global bonds, and explain what a eurobond actually is
- [ ] I can classify any covenant as affirmative or negative
- [ ] I can explain why negative covenants matter most to a credit analyst
- [ ] I can describe the contents of an indenture and the trustee's role
- [ ] I answered the self-check cold, several days after first study

---

[Topic index](README.md)  ·  [LM02 Fixed-Income Cash Flows and Types](lm-02-fixed-income-cash-flows-and-types.md) →
