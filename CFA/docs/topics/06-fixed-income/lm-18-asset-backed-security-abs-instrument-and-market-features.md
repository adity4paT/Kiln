# FI · LM18 — Asset-Backed Security (ABS) Instrument and Market Features

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | LM17 (securitisation structure). |
| **Where it shows up** | 1–2 questions. Covered bonds vs ABS, and the CDO structure, are the reliable targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe characteristics and risks of covered bonds and how they differ from other asset-backed securities
- describe typical credit enhancement structures used in securitizations
- describe types and characteristics of non-mortgage asset-backed securities, including the cash flows and risks of each type
- describe collateralized debt obligations, including their cash flows and risks

---

## Core concepts

### Covered bonds

**A covered bond is a debt obligation of a financial institution, secured by a segregated pool of
assets that remains ON the issuer's balance sheet.**

| | **Covered bond** | **Asset-backed security** |
| --- | --- | --- |
| **Assets** | Stay **on** the issuer's balance sheet | **Sold** to a bankruptcy-remote SPE |
| **Recourse** | **DUAL** — to the cover pool **and** to the issuer | To the **pool only** |
| **Pool composition** | **Dynamic** — the issuer must **replace** non-performing or prepaid assets | **Static** — the pool is fixed at closing |
| **Tranching** | **None** — a single class | Multiple tranches |
| **Regulation** | Governed by specific **covered bond legislation** in most jurisdictions | General securities law |
| **Credit quality** | Very high; typically AAA | Varies by tranche |
| **Prepayment risk to investor** | Low — the issuer replaces prepaid assets | Passed through to investors |

> **Dual recourse is the defining feature.** A covered bond investor has a claim on the cover pool
> **and**, if the pool is insufficient, ranks alongside senior unsecured creditors of the issuer.
> An ABS investor has recourse only to the pool. This is why covered bonds survived the financial
> crisis with essentially no defaults while many ABS structures failed.

The **dynamic pool** requirement reinforces this: the issuer must replace assets that default or
prepay, maintaining the pool's size and quality. Investors are therefore insulated from both credit
deterioration and prepayment — the issuer absorbs both.

Covered bonds are predominantly a **European** instrument (German *Pfandbriefe*, Danish and Spanish
equivalents), governed by dedicated legislation that specifies eligible assets, minimum
overcollateralisation, and the treatment of the pool in an issuer insolvency.

### Credit enhancement structures

**Internal:**

| Mechanism | How it works |
| --- | --- |
| **Subordination (credit tranching)** | Junior tranches absorb losses first |
| **Overcollateralisation** | The pool's face value **exceeds** the securities issued — the excess absorbs losses |
| **Excess spread** | The pool's interest income exceeds the securities' coupons plus fees; the surplus absorbs losses, and may be trapped in a reserve account if performance deteriorates |
| **Reserve account / cash collateral** | Cash set aside at closing |

**External:**

| Mechanism | How it works |
| --- | --- |
| **Surety bond / financial guarantee** | A third party guarantees payment |
| **Letter of credit** | A bank undertakes to cover shortfalls |
| **Cash collateral account** | Funded by a loan from a third party |

**Structural features:**

- **Waterfall** — the priority order in which collections are applied.
- **Triggers / performance tests** — if delinquencies exceed a threshold, cash flows are **redirected**
  to accelerate senior repayment, trapping cash that would otherwise flow to junior tranches. These
  are the structure's automatic defences.

### Non-mortgage ABS

| Type | Collateral | Key characteristics and risks |
| --- | --- | --- |
| **Auto loan ABS** | Car loans | **Amortising**; short weighted average life (2–4 years); collateral is a **depreciating asset** that can be repossessed. Prime, non-prime, and subprime segments. Prepayments occur but are modest and less rate-sensitive than mortgages |
| **Credit card receivable ABS** | Revolving card balances | **NON-amortising.** A **lock-out (revolving) period** during which principal collections buy **new receivables** rather than repaying investors, followed by an **amortisation period**. Includes **early amortisation triggers** if performance deteriorates |
| **Equipment / fleet lease ABS** | Leases on equipment | Amortising; residual value risk on the equipment |
| **Student loan ABS** | Education loans | Long-dated; government guarantees on some programmes; **deferment and forbearance** extend the life unpredictably |
| **Solar / consumer loan ABS** | Various consumer credit | Newer sectors; less historical loss data |

> **The credit card structure is the one most often tested.** During the **lock-out period**,
> investors receive **interest only** — principal collections are reinvested in new receivables to
> keep the pool size constant, because individual card balances turn over every month. Only in the
> **amortisation period** does principal flow to investors.
>
> **Early amortisation triggers** cut the lock-out short if the pool deteriorates (excess spread
> falls below zero, or delinquencies exceed a threshold), accelerating principal repayment to
> protect investors. They are a structural defence, and their activation is a serious warning.

**Amortising versus non-amortising — the distinction that drives the cash flow profile:**

| | **Amortising** (auto, equipment, mortgages) | **Non-amortising** (credit card) |
| --- | --- | --- |
| Principal | Repaid gradually over the life | No scheduled principal during the lock-out |
| Pool | Shrinks | Replenished with new receivables |
| Prepayment | Shortens the life | Absorbed by the revolving structure |

### Collateralised debt obligations

**A CDO is a securitisation whose collateral is itself a portfolio of debt instruments** — bonds,
loans, or other structured securities — rather than a pool of consumer or commercial loans.

| Type | Collateral |
| --- | --- |
| **CLO (collateralised loan obligation)** | **Leveraged loans** — floating-rate senior secured corporate bank debt |
| **CBO (collateralised bond obligation)** | Corporate bonds |
| **Structured finance CDO** | **Other ABS and MBS tranches** — a securitisation of securitisations |
| **Synthetic CDO** | **Credit default swaps** rather than cash assets — exposure without owning the underlying |

**The structure:** senior, mezzanine, and equity tranches, with an **actively managed** collateral
pool. A **collateral manager** buys and sells the underlying debt during a reinvestment period,
subject to portfolio quality tests.

**The economics:**

```
CDO arbitrage = Interest earned on the collateral pool
              − Interest paid to the senior and mezzanine tranches
              − Management fees
              = Residual to the EQUITY tranche
```

The equity tranche is a **leveraged bet on the collateral's default rate**. If defaults stay low it
earns a very high return; if they rise it is wiped out first.

**Risks:**

| Risk | Detail |
| --- | --- |
| **Default correlation** | The **dominant** risk. If the underlying credits default **together**, the diversification the structure assumes disappears and senior tranches take losses |
| **Manager risk** | Performance depends on the collateral manager's selection and trading |
| **Leverage** | The equity tranche is highly levered and can be wiped out by a modest rise in defaults |
| **Model risk** | Ratings depend on **correlation assumptions** that cannot be observed directly and were badly wrong in 2008 |
| **Liquidity** | Thin secondary markets, especially in stress |
| **Complexity** | Structured finance CDOs — CDOs of ABS tranches — are extremely difficult to analyse from the outside |

> **Default correlation is the whole game.** Tranching a pool of 100 credits produces a safe senior
> tranche **only if** the credits default **independently**. If they are driven by a common factor —
> a recession, a housing downturn, a sector shock — they default **together**, the subordination is
> overwhelmed, and the senior tranche suffers.
>
> This is a direct application of the conditional correlation point from **QM LM6**: correlations
> converge toward 1 in stress, exactly when the diversification is needed. The 2008 failure of
> structured finance CDOs was fundamentally a **correlation assumption** failure, not a failure of
> the tranching mathematics.

---

## Formulas to know cold

```
COVERED BOND vs ABS
  Assets:    ON the issuer's balance sheet    vs  SOLD to a bankruptcy-remote SPE
  Recourse:  DUAL (pool AND issuer)           vs  Pool ONLY
  Pool:      DYNAMIC (issuer replaces assets) vs  STATIC
  Tranching: NONE, single class               vs  Multiple tranches

CREDIT ENHANCEMENT
  INTERNAL: subordination · overcollateralisation · excess spread · reserve account
  EXTERNAL: surety bond / guarantee · letter of credit · cash collateral account
  STRUCTURAL: waterfall · performance triggers (redirect cash flow if the pool deteriorates)

NON-MORTGAGE ABS
  AMORTISING (auto, equipment): principal repaid gradually; pool shrinks
  NON-AMORTISING (credit card): LOCK-OUT period (interest only, principal buys new receivables)
                                → AMORTISATION period (principal flows to investors)
                                + EARLY AMORTISATION TRIGGERS if the pool deteriorates

CDO
  CDO arbitrage = collateral interest − senior/mezz interest − fees = EQUITY tranche residual
  CLO = leveraged loans | CBO = corporate bonds
  Structured finance CDO = other ABS/MBS tranches | Synthetic CDO = credit default swaps

  DOMINANT RISK: DEFAULT CORRELATION. Tranching produces a safe senior tranche ONLY IF
  the underlying credits default INDEPENDENTLY.
```

---

## Exam traps

> **Trap 1 — Covered bond recourse.** **Dual recourse** — to the cover pool **and** to the issuer.
> An ABS investor has recourse to the **pool only**. This is the defining difference.

> **Trap 2 — Covered bond pools are static.** They are **dynamic**: the issuer must **replace**
> non-performing and prepaid assets, which insulates investors from both credit and prepayment risk.

> **Trap 3 — Credit card ABS cash flows.** During the **lock-out period** investors receive
> **interest only**; principal collections buy **new receivables**. Principal flows only in the
> amortisation period.

> **Trap 4 — Missing early amortisation triggers.** They accelerate principal repayment to protect
> investors when the pool deteriorates. Their activation is a serious warning signal.

> **Trap 5 — Treating a CDO as diversified by construction.** Its safety depends entirely on
> **default correlation**. Correlated defaults overwhelm the subordination.

> **Trap 6 — Confusing a CLO with a CBO.** **CLO = leveraged loans**; **CBO = corporate bonds**.

> **Trap 7 — Thinking a synthetic CDO holds assets.** It holds **credit default swaps** — exposure
> without ownership of the underlying.

> **Trap 8 — Assuming external enhancement is stronger.** It imports the guarantor's credit risk.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Why did covered bonds survive the financial crisis with essentially no defaults while many ABS structures failed?

<details><summary>Answer</summary>

**Three structural features, working together:**

**(1) Dual recourse.** A covered bond investor has a claim on the **cover pool** *and*, if the pool proves insufficient, ranks alongside the issuer's **senior unsecured creditors**. An ABS investor has recourse to the pool alone — if the pool fails, there is nothing else.

**(2) The dynamic pool.** The issuer is **obliged to replace** assets that default or prepay, maintaining the pool's size and quality. Credit deterioration in the pool is therefore absorbed by the **issuer**, not passed to investors. An ABS pool is **static** — losses flow straight through.

**(3) Dedicated legislation.** Most European jurisdictions govern covered bonds by specific statute, setting eligible asset types, minimum overcollateralisation, and the treatment of the pool in an issuer insolvency. That legal certainty is far stronger than the contractual protections in an ABS.

**Plus a fourth factor:** covered bonds are issued by **regulated banks** with their own capital and supervision, against **conservatively underwritten** mortgages with low loan-to-value limits set by the legislation. The assets were better to begin with.

**The trade-off:** covered bonds yield materially less than comparable ABS. Investors pay for the dual recourse and the dynamic pool.

</details>

**2.** Describe the cash flows to an investor in a credit card ABS through its life.

<details><summary>Answer</summary>

**Lock-out (revolving) period — typically 18–36 months:**
The investor receives **interest only**. Principal collections from cardholders are **reinvested in new receivables** rather than repaid, keeping the pool size constant. This is necessary because individual card balances turn over almost entirely every month — without replenishment the pool would disappear within a year, making a multi-year security impossible.

**Amortisation period:**
Principal collections now flow **to investors**, repaying the securities. This can be structured as a **controlled amortisation** (scheduled repayments over a set period) or a **bullet/accumulation** structure (collections accumulate in an account and are paid as a single sum).

**Early amortisation:**
If the pool deteriorates — **excess spread falls below zero**, delinquencies or charge-offs breach a threshold, or the seller becomes insolvent — an **early amortisation trigger** fires. The lock-out ends immediately and all principal collections are directed to investors, rapidly de-leveraging the structure.

**For the investor, early amortisation means:** the security repays much sooner than expected (reinvestment risk), *and* it signals that the pool is performing badly. It is a protective mechanism, but its activation is a serious warning about the collateral.

</details>

**3.** Why is default correlation the dominant risk in a CDO?

<details><summary>Answer</summary>

Because **tranching produces a safe senior tranche only if the underlying credits default independently**.

**The logic of the structure:** take 100 credits each with a 5% default probability. If defaults are **independent**, the probability that more than 20% default is vanishingly small — so a senior tranche with 20% subordination beneath it is genuinely safe, and a AAA rating is justified.

**If the credits are correlated**, that calculation collapses. Correlated credits default **together**, driven by a common factor — a recession, a sector shock, a housing downturn. The realistic outcomes become bimodal: either very few defaults, or very many. The 'safe' senior tranche now faces a real probability of losses that the independence assumption said was effectively zero.

**Why it was catastrophic in 2008:** structured finance CDOs held tranches of **subprime mortgage** securitisations. The models assumed modest correlation between regional housing markets — reasonable on historical data covering a period with no national house price decline. When house prices fell **nationally**, every pool deteriorated simultaneously. Correlation went to nearly 1, subordination was overwhelmed, and AAA-rated tranches took severe losses.

**The general principle** (QM LM6): **conditional correlations rise toward 1 in stress**, exactly when the diversification is needed. Any structure whose safety rests on an assumed correlation is fragile in precisely the state it was built to survive.

</details>

**4.** Contrast an auto loan ABS with a credit card ABS on cash flow structure and risks.

<details><summary>Answer</summary>

**Auto loan ABS — amortising:**
- Underlying loans have **fixed schedules** with level payments of principal and interest
- The pool **shrinks** over time; principal flows to investors from the start
- **Short weighted average life** — typically 2–4 years
- Collateral is a **depreciating asset** that can be repossessed, so recoveries are meaningful but decline over the loan's life
- **Prepayments** occur (early payoff, trade-in, insurance write-off) but are modest and **less rate-sensitive** than mortgages — nobody refinances a car loan to save 50bp
- Segmented by borrower quality: prime, non-prime, subprime, with very different loss expectations

**Credit card ABS — non-amortising:**
- Underlying balances **revolve** — there is no fixed schedule, and individual balances turn over monthly
- **Lock-out period**: interest only to investors; principal collections buy **new receivables**
- Then an **amortisation period** when principal flows to investors
- **Early amortisation triggers** protect investors if the pool deteriorates
- Collateral is **unsecured** — no repossession, so recoveries are low
- Performance is highly sensitive to **unemployment**, the key driver of card charge-offs

**The core difference:** the auto pool self-liquidates on a known schedule; the card pool must be actively replenished, which is why the structure needs a lock-out period and trigger-based defences.

</details>

---

## Done when

- [ ] I can contrast covered bonds and ABS on recourse, pool dynamics, and tranching
- [ ] I can explain why covered bonds performed so well through the crisis
- [ ] I can name four internal and three external credit enhancements plus structural triggers
- [ ] I can describe the credit card ABS lock-out and amortisation periods and early amortisation triggers
- [ ] I can contrast amortising and non-amortising ABS structures
- [ ] I can describe CDO tranching, the arbitrage economics, and the role of the collateral manager
- [ ] I can explain why default correlation is the dominant CDO risk, and connect it to QM LM6
- [ ] I answered the self-check cold, several days after first study

---

← [LM17 Fixed-Income Securitization](lm-17-fixed-income-securitization.md)  ·  [Topic index](README.md)  ·  [LM19 Mortgage-Backed Security (MBS) Instrument and Market Features](lm-19-mortgage-backed-security-mbs-instrument-and-market-features.md) →
