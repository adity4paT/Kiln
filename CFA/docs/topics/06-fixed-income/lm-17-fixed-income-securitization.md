# FI · LM17 — Fixed-Income Securitization

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 3 |
| **Prerequisites** | LM1 (indentures), LM14 (credit risk). |
| **Where it shows up** | 1 question. Descriptive; the SPE and bankruptcy-remoteness concepts are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- explain benefits of securitization for issuers, investors, economies, and financial markets
- describe securitization, including the parties and the roles they play

---

## Core concepts

### What securitisation is

**Securitisation pools illiquid financial assets — loans, leases, receivables — and issues
securities backed by the cash flows from that pool.** The assets are sold to a separate legal
entity, so the securities depend on the **pool's** performance rather than on the originator's
credit.

```
Borrowers → pay → Loan pool → SOLD to → Special Purpose Entity → issues → Securities → Investors
                                              ↑
                              (bankruptcy remote from the originator)
```

### The parties

| Party | Role |
| --- | --- |
| **Seller / originator** | Originated the loans and sells them to the SPE (a bank, a finance company, a retailer) |
| **Special purpose entity (SPE / SPV / issuer)** | Buys the assets and issues the securities. **Bankruptcy remote** from the originator |
| **Servicer** | Collects payments from the underlying borrowers, handles delinquencies and recoveries, remits to the trustee. Often the originator continues in this role |
| **Trustee** | Holds the assets for investors, oversees the waterfall, enforces the documents |
| **Underwriter** | Structures and distributes the securities |
| **Rating agencies** | Rate the tranches |
| **Credit enhancement providers** | Guarantors, insurers, providers of letters of credit |
| **Investors** | Buy the tranches |

### Bankruptcy remoteness — the concept that makes it work

**The true sale of the assets to the SPE means that if the originator goes bankrupt, the pooled
assets are NOT part of its bankruptcy estate.** Investors' claims are on the pool alone.

This is why an SPE's securities can be rated **higher than the originator itself**. A BB-rated
finance company can issue AAA-rated ABS, because the rating reflects the **pool's** credit quality
and the **structural protections**, not the originator's.

> **The requirement is a genuine "true sale".** If a court later determines the transfer was not a
> true sale — that the originator retained too much control or too much risk — the assets can be
> pulled back into the bankruptcy estate, and the entire structure fails. This is why securitisation
> documentation is so voluminous, and why legal opinions on true sale are central to the rating.

### Tranching and the waterfall

The SPE issues **tranches** with different priorities of claim on the pool's cash flows.

```
Pool cash flows
      ↓
  SENIOR tranche      — paid FIRST, lowest yield, highest rating (often AAA)
      ↓
  MEZZANINE tranches  — paid next
      ↓
  SUBORDINATED /      — paid LAST, absorbs losses FIRST, highest yield
  EQUITY tranche         (often retained by the originator)
```

**Losses flow in the opposite direction from cash:** the **subordinated tranche absorbs losses
first**, protecting the tranches above it. This is **credit tranching** — redistributing credit risk
without changing the total.

**Time tranching** is a separate mechanism (LM19): redistributing **prepayment** risk by directing
principal repayments to tranches in a specified sequence.

> **The critical insight:** tranching does **not** reduce the total risk of the pool. It
> **redistributes** it, concentrating credit risk in the junior tranches so the senior tranches can
> be rated highly. The total risk is unchanged; its distribution across investors is transformed.
>
> This is also the structure's failure mode. If the **pool's** loss experience exceeds what the
> subordination was sized for — as with subprime mortgages in 2007–08 — losses reach the senior
> tranches, and a security rated AAA on a model of pool behaviour suffers losses no AAA corporate
> bond would.

### Credit enhancement

| Type | Mechanism |
| --- | --- |
| **Internal — subordination** | Junior tranches absorb losses first |
| **Internal — overcollateralisation** | The pool's face value **exceeds** the securities issued |
| **Internal — excess spread** | The pool's interest income exceeds the securities' coupons plus fees; the surplus absorbs losses |
| **Internal — reserve account** | Cash set aside at closing |
| **External — guarantee / surety bond** | A third party guarantees payment (introduces that party's credit risk) |
| **External — letter of credit** | A bank undertakes to cover shortfalls |

**Internal enhancement is preferred** because external enhancement introduces the guarantor's credit
risk — if the guarantor is downgraded, so is the security. This dependency was a significant channel
of contagion in 2008, when monoline insurers were downgraded.

### Benefits of securitisation

**For the originator (issuer):**

- **Funding diversification** — access to capital markets beyond deposits and corporate debt
- **Lower funding cost** — the securities can be rated above the originator
- **Balance sheet and regulatory capital relief** — the assets are removed from the balance sheet
- **Liquidity** — converts illiquid loans into cash that can be re-lent
- **Risk transfer** — credit risk moves to investors

**For investors:**

- **Access to asset classes** otherwise unavailable — consumer credit, mortgages, auto loans
- **A choice of risk/return profiles** through tranching, from AAA to equity
- **Diversification** — pool exposure rather than single-name exposure
- **Often better risk-adjusted yields** than similarly rated corporate bonds

**For the economy and financial markets:**

- **Lower borrowing costs** for end borrowers (homeowners, car buyers, small businesses), because
  capital market funding is cheaper than balance sheet funding
- **Greater credit availability**, because capital recycles rather than sitting on bank balance
  sheets
- **More efficient risk allocation** — risk is held by those best placed to bear it
- **Disintermediation** — borrowers can access capital markets without a bank intermediary

> **The counter-argument, which the curriculum does not ignore:** the **originate-to-distribute**
> model weakens the originator's incentive to underwrite carefully, because it does not retain the
> risk. This misalignment contributed materially to the 2008 crisis, and post-crisis regulation
> responded with **risk retention rules** requiring originators to keep a slice (typically 5%) of
> the credit risk — "skin in the game".

---

## Formulas to know cold

```
THE STRUCTURE
  Borrowers → Loan pool → SOLD (true sale) → SPE → issues tranches → Investors
                                              ↑ BANKRUPTCY REMOTE from the originator

  ⇒ tranches can be rated HIGHER than the originator itself

TRANCHING — cash flows DOWN, losses UP
  Senior       — paid FIRST, lowest yield, highest rating
  Mezzanine    — paid next
  Subordinated — paid LAST, absorbs losses FIRST, highest yield

  Tranching REDISTRIBUTES risk; it does NOT reduce total pool risk.

CREDIT ENHANCEMENT
  INTERNAL (preferred): subordination · overcollateralisation · excess spread · reserve account
  EXTERNAL: guarantee / surety bond · letter of credit
            ← introduces the GUARANTOR'S credit risk

PARTIES
  Seller/originator · SPE (issuer) · Servicer · Trustee · Underwriter
  · Rating agencies · Credit enhancement providers · Investors
```

---

## Exam traps

> **Trap 1 — Thinking tranching reduces risk.** It **redistributes** it. Total pool risk is
> unchanged; the senior tranches are protected by the junior ones absorbing losses first.

> **Trap 2 — Missing why an ABS can be rated above its originator.** The **true sale** to a
> **bankruptcy-remote** SPE means investors' claims are on the **pool**, not on the originator.

> **Trap 3 — Assuming external enhancement is stronger.** It introduces the **guarantor's credit
> risk**. Internal enhancement (subordination, overcollateralisation) is generally preferred.

> **Trap 4 — Confusing credit tranching with time tranching.** **Credit** tranching redistributes
> **default** risk; **time** tranching redistributes **prepayment** risk (LM19).

> **Trap 5 — Forgetting the servicer.** The servicer collects the payments, and its competence and
> solvency matter. Servicer failure disrupts cash flow even when the underlying loans are performing.

> **Trap 6 — Overlooking the originate-to-distribute incentive problem.** An originator that retains
> no risk has weak incentives to underwrite carefully — which is why risk retention rules exist.

> **Trap 7 — Assuming a AAA ABS behaves like a AAA corporate bond.** Its rating rests on a **model
> of pool behaviour**. If the model's loss assumptions are wrong, the rating is wrong.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** How can a BB-rated finance company issue AAA-rated securities?

<details><summary>Answer</summary>

Through **true sale to a bankruptcy-remote special purpose entity**, combined with **credit enhancement**.

**The mechanism:**
1. The finance company **sells** the loan pool to an SPE in a transaction structured as a genuine **true sale** — not a secured borrowing.
2. The SPE is **bankruptcy remote**: if the originator fails, the pooled assets are **not part of its bankruptcy estate**. Investors' claims are on the pool alone.
3. The SPE issues **tranches**. The senior tranche is protected by **subordination** — junior tranches absorb losses first — plus overcollateralisation, excess spread, and reserve accounts.
4. Rating agencies size the enhancement so that the senior tranche survives loss scenarios consistent with a AAA rating.

**So the rating reflects the pool's credit quality and the structural protections, not the originator's own creditworthiness.**

**What makes it fragile:** the rating depends entirely on (a) the true sale holding up legally — if a court recharacterises the transfer, the assets return to the bankruptcy estate and the structure fails — and (b) the **loss model** being right. A AAA rating on modelled pool behaviour is a different object from a AAA rating on a sovereign or a blue-chip corporate, as 2008 demonstrated.

</details>

**2.** A securitisation has a 78% senior tranche, a 15% mezzanine tranche, and a 7% subordinated tranche. Pool losses reach 11%. Who bears them?

<details><summary>Answer</summary>

Losses are absorbed **from the bottom up**:

- **Subordinated tranche (7%): wiped out entirely.** It absorbs the first 7% of losses.
- **Mezzanine tranche (15%): absorbs the next 4%** (11% − 7%), leaving it with 11 of its 15 percentage points intact — a loss of about **27% of its principal**.
- **Senior tranche (78%): untouched.** Losses would have to exceed 22% (7% + 15%) before it took any loss.

**This is credit tranching working as designed.** The subordination of 22% below the senior tranche is what supports its high rating.

**The failure mode:** if pool losses reach, say, 30% — as happened with subprime mortgage pools in 2008 — the senior tranche takes an 8% loss. A security rated AAA suffers a loss no AAA corporate bond ever has. The rating was never wrong about the *structure*; it was wrong about the **loss distribution of the pool**.

</details>

**3.** Why is internal credit enhancement generally preferred to external?

<details><summary>Answer</summary>

Because **external enhancement introduces the guarantor's credit risk**, creating a dependency the structure was designed to avoid.

**Internal enhancement** — subordination, overcollateralisation, excess spread, reserve accounts — is **self-contained within the structure**. It depends only on the pool's own cash flows and the agreed priority of claims. No third party can fail.

**External enhancement** — a guarantee, surety bond, or letter of credit — makes the security's rating dependent on the **guarantor's** rating. The security can be no stronger than the entity standing behind it.

**This dependency was a major contagion channel in 2008.** Monoline bond insurers had guaranteed vast volumes of structured securities. When the insurers were downgraded, **every security they had wrapped was downgraded simultaneously**, regardless of how the underlying pools were performing. A single counterparty's deterioration propagated across thousands of otherwise unrelated securities.

**The general principle:** internal enhancement converts a credit problem into a structural one, which can be analysed from the pool's own data. External enhancement converts it into a counterparty problem, which imports a risk from outside the structure entirely.

</details>

**4.** What is the originate-to-distribute problem, and how did regulation respond?

<details><summary>Answer</summary>

**The problem is an incentive misalignment.** In a traditional lending model the bank keeps the loan on its balance sheet and bears the loss if the borrower defaults — so it has a strong incentive to underwrite carefully.

In an **originate-to-distribute** model the originator sells the loans into a securitisation and retains none of the credit risk. Its compensation depends on **origination volume**, not on loan performance. Underwriting standards therefore deteriorate: less documentation, higher loan-to-value ratios, and borrowers who could not service the loan under any realistic scenario.

The risk passes to investors who cannot observe the underwriting quality directly and rely on ratings — which are themselves based on models calibrated to historical loss data from an era when underwriting was tighter. **The historical data no longer describes the loans being made.**

This dynamic contributed materially to the 2008 crisis.

**The regulatory response: risk retention rules** — 'skin in the game'. Originators are generally required to retain a slice (typically **5%**) of the credit risk of securitisations they sponsor, either as a vertical slice of every tranche or as a horizontal slice of the first-loss piece. The intent is to restore the incentive to underwrite well by ensuring the originator suffers alongside investors.

Whether 5% is sufficient is contested, but the principle — that risk transfer without risk retention corrupts underwriting — is well established.

</details>

---

## Done when

- [ ] I can draw the securitisation structure and name all the parties and their roles
- [ ] I can explain bankruptcy remoteness and why it lets an ABS be rated above its originator
- [ ] I can explain tranching and state that it redistributes rather than reduces risk
- [ ] I can name four internal and two external credit enhancements and say why internal is preferred
- [ ] I can list the benefits to issuers, investors, and the economy
- [ ] I can explain the originate-to-distribute problem and the risk retention response
- [ ] I answered the self-check cold, several days after first study

---

← [LM16 Credit Analysis for Corporate Issuers](lm-16-credit-analysis-for-corporate-issuers.md)  ·  [Topic index](README.md)  ·  [LM18 Asset-Backed Security (ABS) Instrument and Market Features](lm-18-asset-backed-security-abs-instrument-and-market-features.md) →
