# FI · LM19 — Mortgage-Backed Security (MBS) Instrument and Market Features

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | LM13 (effective duration, negative convexity), LM17 (securitisation). |
| **Where it shows up** | 1–2 questions. Prepayment risk and the CMO tranching mechanics are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- define prepayment risk and describe time tranching structures in securitizations and their purpose
- describe fundamental features of residential mortgage loans that are securitized
- describe types and characteristics of residential mortgage-backed securities, including mortgage pass-through securities and collateralized mortgage obligations, and explain the cash flows and risks for each type
- describe characteristics and risks of commercial mortgage-backed securities

---

## Core concepts

### Features of a residential mortgage loan

| Feature | Detail |
| --- | --- |
| **Loan-to-value ratio (LTV)** | Loan amount / property value. **Lower LTV = more equity = lower default risk and better recovery** |
| **Interest rate type** | Fixed rate, adjustable (ARM), hybrid (fixed then floating), or index-referenced |
| **Amortisation** | Fully amortising, partially amortising (with a balloon), or interest-only |
| **Maturity** | Typically 15–30 years |
| **Prepayment provisions** | Whether early repayment is permitted and whether a **penalty** applies |
| **Recourse** | **Recourse** — the lender can pursue the borrower's other assets. **Non-recourse** — the lender's claim is limited to the property |

> **Recourse status drives default behaviour.** In a **non-recourse** jurisdiction, a borrower whose
> property is worth less than the loan can simply hand back the keys — **strategic default** is
> rational. In a **recourse** jurisdiction the lender can pursue other assets, so negative equity is
> far less likely to trigger default. The same loan-to-value ratio implies very different default
> risk in the two regimes, which is a genuine cross-country comparison trap.

### Prepayment risk

**Prepayment is the repayment of mortgage principal ahead of schedule** — from refinancing, home
sale, default (which the guarantor makes whole), or simply paying extra. Borrowers in most
residential markets have a **free option to prepay**, which is the source of nearly all the
complexity in MBS.

| Risk | When it bites | Consequence |
| --- | --- | --- |
| **Contraction risk** | **Rates FALL** → borrowers refinance → principal returns **early** | The investor must reinvest at the new **lower** rates, and loses the above-market coupon just as it becomes valuable |
| **Extension risk** | **Rates RISE** → refinancing stops → principal returns **late** | The investor is locked into a **below-market** coupon for longer, and cannot reinvest at the higher rates |

> **This is the worst possible combination for an investor.** You get your money back early exactly
> when reinvestment rates are poor, and late exactly when they are attractive. It is precisely the
> **negative convexity** of LM12 — upside capped, downside not — and it is why MBS yield more than
> comparable government bonds.
>
> Mechanically, the mortgage holder has **sold a call option to the homeowner**: the homeowner can
> "call" the loan at par (repay it) whenever it suits them.

**Measuring prepayment:**

```
Single monthly mortality rate (SMM) = the % of the remaining pool prepaid in a month
Conditional prepayment rate (CPR)   = the annualised prepayment rate
PSA benchmark                       = a standard prepayment ramp; 100 PSA = the benchmark path
                                      (150 PSA = 1.5x the benchmark speed)
Weighted average life (WAL)         = the average time to receipt of the principal, given
                                      an assumed prepayment speed
```

**What drives prepayment speeds:** the level of current rates **relative to the pool's coupon** (the
refinancing incentive), the **age** of the pool (seasoning — prepayments ramp up over the first few
years), **burnout** (pools that have already refinanced heavily prepay less, because the remaining
borrowers are those who cannot or will not refinance), housing turnover, and seasonality.

### Mortgage pass-through securities

The simplest structure: investors hold a **pro rata share** of all cash flows from the pool —
principal, interest, and prepayments — net of servicing and guarantee fees.

```
Pass-through coupon = Weighted average coupon of the pool − servicing fee − guarantee fee
```

Key pool measures: **weighted average coupon (WAC)**, **weighted average maturity (WAM)**, and the
weighted average life under an assumed prepayment speed.

**Agency vs non-agency:**

| | **Agency MBS** | **Non-agency MBS** |
| --- | --- | --- |
| Issuer | Government agencies or government-sponsored enterprises | Private financial institutions |
| Credit risk | **Minimal** — guaranteed | **Present** — requires credit enhancement |
| Underlying loans | Must meet **conforming** standards (size, LTV, documentation) | Non-conforming: jumbo, subprime, alt-A |
| Main risk | **Prepayment risk** | Prepayment **and credit** risk |

> **For agency MBS, the analysis is almost entirely about prepayment.** Credit risk is guaranteed
> away, so the whole question is how fast principal comes back and under what rate conditions.

### Collateralised mortgage obligations

**A CMO redistributes prepayment risk among tranches** by directing principal repayments in a
specified order. This is **time tranching** — distinct from the **credit tranching** of LM17.

> **The purpose:** different investors have different tolerances for prepayment uncertainty. A
> pension fund matching a 20-year liability wants a long, stable life; a money market fund wants a
> short one. A pass-through offers neither — every investor gets the same uncertain profile. A CMO
> creates tranches with **different** prepayment profiles from the **same** pool, so each investor
> can buy the profile they want.
>
> Total prepayment risk is **unchanged** — as with credit tranching, it is redistributed.

**Sequential-pay CMO:** all principal goes to **tranche A** until it is fully retired, then to
tranche B, then C. Tranche A has the shortest, most certain life and absorbs the most contraction
risk; the last tranche has the longest life and the most extension risk.

**Planned amortisation class (PAC) and support tranches** — the most examinable structure:

| Tranche | Behaviour |
| --- | --- |
| **PAC** | Has a **scheduled principal repayment plan** that is honoured as long as prepayments fall within a specified band (the "PAC collar", e.g. 100–300 PSA). Prepayment risk is **greatly reduced** |
| **Support (companion)** | **Absorbs the variability** — receives the excess when prepayments are fast, and is starved when they are slow |

The support tranche makes the PAC's stability possible by taking on **amplified** prepayment risk.
It is paid a higher yield for doing so. If prepayments move **outside** the collar for long enough,
the support tranche is exhausted and the PAC's schedule **breaks** — at which point the PAC behaves
like an ordinary sequential tranche.

**Other CMO tranche types:** **floating-rate** tranches (created from fixed-rate collateral, paired
with an **inverse floater**), **accrual (Z) tranches** (accrue interest rather than receiving it,
which accelerates repayment of earlier tranches), and **interest-only (IO)** and **principal-only
(PO)** strips.

> **IO and PO strips behave in opposite and extreme ways.** A **PO** strip is bought at a deep
> discount and receives only principal — **fast prepayments are good** (the principal arrives
> sooner), so its price **rises sharply** when rates fall. An **IO** strip receives only interest —
> **fast prepayments are disastrous** (the balance on which interest is paid disappears), so its
> price **falls** when rates fall. An IO has **negative duration**: it rises in value when rates
> rise, which makes it a hedging instrument for portfolios of other MBS.

### Commercial mortgage-backed securities

Backed by mortgages on **income-producing commercial property** — office, retail, industrial,
multifamily, hotel.

**The fundamental difference from residential: CMBS loans are typically NON-RECOURSE to the
borrower.** The lender's claim is limited to the property, so **credit analysis is about the
property's cash flow**, not the borrower's.

**The two key metrics:**

```
Debt service coverage ratio (DSCR) = Net operating income / Annual debt service
    Higher is better. Below 1.0 means the property does not cover its own debt service.

Loan-to-value ratio (LTV) = Loan amount / Property value
    Lower is better.
```

**Call protection — the defining structural difference from residential MBS:**

Commercial mortgages generally **restrict prepayment**, which largely removes the prepayment risk
that dominates residential MBS:

| Mechanism | Effect |
| --- | --- |
| **Prepayment lockout** | Prepayment **prohibited** for a period |
| **Defeasance** | The borrower substitutes government securities producing identical cash flows, rather than repaying |
| **Yield maintenance charge** | A penalty making the lender whole for lost interest |
| **Prepayment penalty points** | A declining percentage penalty (e.g. 5-4-3-2-1) |

> **So CMBS analysis is credit analysis, while agency RMBS analysis is prepayment analysis.** This
> is the cleanest contrast in the module and a favourite exam point.

**CMBS risks:**

- **Balloon risk** — most commercial mortgages are **partially amortising** with a large balloon
  payment at maturity, requiring **refinancing**. If credit conditions have tightened or property
  values have fallen, refinancing may be unavailable. Failure to refinance is **extension risk** in
  its most severe form, and often results in default.
- **Property-type and geographic concentration**
- **Tenant concentration** and lease expiry schedules — a single anchor tenant leaving can destroy a
  retail property's cash flow
- **Cyclicality** of commercial property values and rents

---

## Formulas to know cold

```
PREPAYMENT RISK
  CONTRACTION risk — rates FALL → refinancing → principal back EARLY → reinvest at LOW rates
  EXTENSION risk   — rates RISE → refinancing stops → principal back LATE → stuck at a LOW coupon
  ⇒ NEGATIVE CONVEXITY (LM12). The investor has SOLD a call option to the homeowner.

PREPAYMENT MEASURES
  SMM = % of the remaining pool prepaid in a month
  CPR = annualised prepayment rate
  PSA = standard prepayment benchmark; 100 PSA = benchmark, 150 PSA = 1.5x that speed
  WAL = weighted average life, given an assumed prepayment speed

PASS-THROUGH
  Pass-through coupon = Pool WAC − servicing fee − guarantee fee
  Pool measures: WAC (weighted average coupon), WAM (weighted average maturity)

CMO — TIME TRANCHING (redistributes PREPAYMENT risk; credit tranching redistributes DEFAULT risk)
  Sequential-pay: principal to tranche A until retired, then B, then C
  PAC:     a scheduled repayment plan, honoured within a prepayment COLLAR
  Support: absorbs the variability; higher yield; if exhausted, the PAC schedule BREAKS
  PO strip: fast prepayments GOOD → price RISES when rates fall
  IO strip: fast prepayments BAD  → price FALLS when rates fall → NEGATIVE duration

CMBS — the loans are NON-RECOURSE ⇒ analysis is CREDIT, not prepayment
  DSCR = Net operating income / Annual debt service      (higher is better; > 1.0 required)
  LTV  = Loan amount / Property value                    (lower is better)
  Call protection: lockout · defeasance · yield maintenance · penalty points
  BALLOON RISK: partially amortising loans need REFINANCING at maturity
```

---

## Exam traps

> **Trap 1 — Contraction vs extension risk.** **Rates FALL → contraction** (early repayment, reinvest
> low). **Rates RISE → extension** (late repayment, stuck low). Both hurt. Inverting these is the
> most common MBS error.

> **Trap 2 — Credit tranching vs time tranching.** **Credit** tranching redistributes **default**
> risk (LM17). **Time** tranching redistributes **prepayment** risk.

> **Trap 3 — Assuming a PAC has no prepayment risk.** It has **greatly reduced** risk **within its
> collar**. Outside the collar, once the support tranche is exhausted, the schedule **breaks**.

> **Trap 4 — IO and PO strip directions.** **PO: fast prepayments GOOD** — price rises when rates
> fall. **IO: fast prepayments BAD** — price falls when rates fall, giving it **negative duration**.

> **Trap 5 — Applying residential prepayment analysis to CMBS.** Commercial mortgages have **call
> protection** (lockout, defeasance, yield maintenance). CMBS analysis is **credit** analysis.

> **Trap 6 — Missing balloon risk.** Most commercial mortgages are **partially amortising** and must
> be **refinanced** at maturity. Failure to refinance is the dominant CMBS risk.

> **Trap 7 — Using modified duration for an MBS.** Cash flows change with rates. Use **effective**
> duration (LM13), computed by Monte Carlo across many rate paths.

> **Trap 8 — Ignoring recourse status.** In a **non-recourse** jurisdiction, **strategic default** on
> a residential mortgage in negative equity is rational. The same LTV implies different risk across
> regimes.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Interest rates fall 200bp. Explain what happens to an investor in a mortgage pass-through security.

<details><summary>Answer</summary>

**Prepayments accelerate sharply.** Homeowners refinance into new mortgages at the lower rate, repaying the existing loans at par.

**Consequences for the investor:**
1. **Principal returns early** — much sooner than the scheduled amortisation implied.
2. **It must be reinvested at the new, lower rates** — this is **contraction risk**.
3. **The above-market coupon is lost precisely when it became most valuable.** An ordinary bond would have appreciated substantially on a 200bp rally; the MBS does not, because it is being repaid at par.
4. **The price is therefore compressed** — it rises far less than a comparable-duration government bond would.

**This is negative convexity in action** (LM12): the investor's upside is capped while the downside is not. If rates had risen 200bp instead, prepayments would have **slowed** (extension risk), the investor would be locked into a below-market coupon for longer, and the price would have fallen like any other bond.

**Economically:** the MBS investor has **sold a call option** to the homeowner, who can repay at par whenever it suits them. The extra yield MBS offer over Treasuries is the premium for writing that option.

</details>

**2.** How does a PAC tranche achieve stable cash flows, and what breaks it?

<details><summary>Answer</summary>

**The mechanism: a support (companion) tranche absorbs the prepayment variability.**

The PAC has a **scheduled principal repayment plan**, calculated to be achievable across a **band of prepayment speeds** — the **PAC collar**, say 100–300 PSA.

- **If prepayments are FAST** (above the collar's midpoint), the PAC receives its scheduled amount and the **excess principal goes to the support tranche**, retiring it faster.
- **If prepayments are SLOW**, the PAC still receives its scheduled amount and the **support tranche receives nothing**, waiting.

The support tranche therefore experiences **amplified** prepayment variability — far more than the underlying pool — which is exactly what makes the PAC stable. It is compensated with a **higher yield**.

**What breaks it:**

**Prepayments outside the collar, sustained.** If prepayments run **very fast** for long enough, the support tranche is **completely retired**. With no support left to absorb the excess, further prepayments flow to the PAC and its schedule **breaks** — it becomes a 'broken PAC' and behaves like an ordinary sequential tranche.

Similarly, if prepayments are **very slow** for long enough, the support tranche is starved and the PAC's schedule cannot be met.

**The practical lesson:** a PAC's protection **erodes over time** as the support tranche amortises. An older PAC with a thin remaining support tranche offers much less protection than its collar suggests. Always check the **remaining support balance**, not just the stated collar.

</details>

**3.** Why does an interest-only (IO) strip have negative duration?

<details><summary>Answer</summary>

Because its value depends on the **outstanding principal balance** surviving, and prepayments destroy that balance.

An **IO strip receives only the interest payments** from the mortgage pool. Interest is calculated on the **remaining principal**. So the IO's total cash flow depends entirely on how long the principal stays outstanding.

**When rates FALL:**
- Prepayments **accelerate** — borrowers refinance
- The principal balance **shrinks rapidly**
- There is **less and less principal to pay interest on**
- The IO's cash flows **collapse** → its **price FALLS**

**When rates RISE:**
- Prepayments **slow** — nobody refinances
- Principal stays outstanding **longer**
- Interest is paid on a larger balance for more periods
- The IO's cash flows **increase** → its **price RISES**

**A security whose price rises when rates rise has NEGATIVE duration.** This is genuinely unusual — almost every fixed-income instrument has positive duration.

**Why it matters practically:** IOs are used as **hedging instruments** for portfolios of other MBS. A portfolio of pass-throughs loses value when rates rise; adding IOs, which gain, offsets it. The IO's negative duration is precisely the property that makes it useful.

**The mirror image:** a **PO strip** receives only principal, bought at a deep discount. Fast prepayments mean the discounted principal arrives **sooner** — good. So a PO's price **rises sharply** when rates fall, giving it very **high positive duration**.

</details>

**4.** Why is CMBS analysis fundamentally credit analysis while agency RMBS analysis is prepayment analysis?

<details><summary>Answer</summary>

**Two structural differences, and they reverse the priorities:**

**(1) Call protection.** Commercial mortgages **restrict prepayment** through lockout periods, **defeasance** (substituting government securities rather than repaying), **yield maintenance** charges, and declining **penalty points**. These largely eliminate the prepayment optionality that dominates residential MBS. The homeowner's free prepayment option simply does not exist in commercial lending.

**(2) Credit risk.** **Agency** RMBS carry a guarantee against default — credit risk is guaranteed away, leaving prepayment as the only meaningful variable. **CMBS carry full credit risk**, and the loans are typically **non-recourse**: the lender's claim is limited to the property, so the analysis is entirely about whether the **property's own cash flow** services the debt.

**So CMBS analysis is property-level credit analysis:**
- **DSCR** = net operating income / annual debt service — does the property cover its debt?
- **LTV** = loan / property value — how much equity cushion is there?
- **Tenant concentration and lease expiry schedules** — an anchor tenant leaving can destroy a retail property
- **Property type and geographic concentration**
- **Balloon risk** — most commercial loans are partially amortising and must be **refinanced** at maturity. If values have fallen or credit has tightened, refinancing may be unavailable, and that is the dominant cause of CMBS losses

**And agency RMBS analysis is prepayment modelling:** CPR and PSA speeds, seasoning, burnout, the refinancing incentive relative to the pool WAC, and the resulting weighted average life and effective duration.

</details>

**5.** A residential mortgage market is non-recourse. How does this change default behaviour compared to a recourse market?

<details><summary>Answer</summary>

**It makes strategic default rational.**

In a **non-recourse** market, the lender's claim is limited to the **property**. If the borrower stops paying, the lender forecloses and takes the house — and that is the end of the matter. The borrower's other assets and future income are untouchable.

So when the property is worth **less than the loan** (negative equity), the borrower holds what amounts to a **put option**: they can 'sell' the house to the lender at the loan balance simply by walking away. A borrower with 200,000 of debt on a house worth 150,000 is 50,000 better off defaulting, regardless of their ability to pay.

In a **recourse** market, the lender can pursue the borrower's **other assets and future income** for the shortfall. Walking away does not extinguish the debt. Negative equity is therefore far less likely to trigger default — the borrower keeps paying because defaulting does not help them.

**Implications for MBS analysis:**
- **The same LTV implies very different default risk** in the two regimes. Cross-country comparison of mortgage pools on LTV alone is misleading.
- In non-recourse markets, **default becomes highly sensitive to house prices** — a price decline of 20% can trigger a wave of strategic defaults from borrowers who could perfectly well afford to pay.
- This creates **correlation** between defaults (they all respond to the same house price index), which is exactly the assumption failure that broke structured finance CDOs in 2008 (LM18).
- Recourse markets show more stable default behaviour through a housing downturn, which is one reason mortgage losses varied so much across countries in the crisis.

</details>

---

## Done when

- [ ] I can define contraction and extension risk and state which rate move causes each
- [ ] I can explain why prepayment risk creates negative convexity and what option the investor has sold
- [ ] I can define SMM, CPR, PSA, and WAL and name the drivers of prepayment speed
- [ ] I can describe a pass-through and distinguish agency from non-agency MBS
- [ ] I can explain how a PAC/support structure works and what breaks a PAC
- [ ] I can state the price behaviour of IO and PO strips and explain the IO's negative duration
- [ ] I can explain why CMBS analysis is credit analysis, and compute DSCR and LTV
- [ ] I can explain balloon risk and why it dominates CMBS losses
- [ ] I can explain how recourse status changes residential default behaviour
- [ ] I answered the self-check cold, several days after first study

---

← [LM18 Asset-Backed Security (ABS) Instrument and Market Features](lm-18-asset-backed-security-abs-instrument-and-market-features.md)  ·  [Topic index](README.md)
