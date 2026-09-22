# FI · LM02 — Fixed-Income Cash Flows and Types

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 3 |
| **Prerequisites** | LM1. |
| **Where it shows up** | 1–2 questions. The contingency provisions (call/put/conversion) are the reliable target. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe common cash flow structures of fixed-income instruments and contrast cash flow contingency provisions that benefit issuers and investors
- describe how legal, regulatory, and tax considerations affect the issuance and trading of fixed-income securities

---

## Core concepts

### Principal repayment structures

| Structure | How principal is repaid |
| --- | --- |
| **Bullet** | **Entire principal at maturity.** Coupons only until then. The standard structure |
| **Fully amortising** | Principal repaid **gradually** with each payment; the balance is zero at maturity. Each payment is level, with a rising principal and falling interest share (mortgages, car loans) |
| **Partially amortising** | Some principal amortised, with a **balloon payment** of the remainder at maturity |
| **Sinking fund** | The issuer must **retire a specified portion each year**, by open-market purchase or by redeeming bonds selected by lot |

> **Sinking fund provisions reduce credit risk** (the issuer retires debt gradually rather than
> facing a single large repayment) but introduce **reinvestment risk** for the investor, who may
> have their bond redeemed early — typically at par — when rates have fallen.

### Coupon structures

| Structure | Coupon behaviour |
| --- | --- |
| **Fixed rate** | Constant for the life of the bond |
| **Floating rate (FRN)** | **Reference rate + quoted margin**, reset periodically. Reference rates now include SOFR, SONIA, €STR, and EURIBOR |
| **Zero coupon** | No coupons; issued at a **discount** and redeemed at par. The entire return is price accretion |
| **Step-up** | Coupon **rises** on a schedule, or on a credit rating downgrade |
| **Credit-linked** | Coupon changes with the issuer's **credit rating** |
| **Payment-in-kind (PIK)** | The issuer may pay coupons **in more bonds** rather than cash. High-yield; a significant credit warning |
| **Deferred / split coupon** | No coupon for an initial period, then a higher one |
| **Index-linked** | Principal and/or coupon linked to **inflation** or another index |

**Floating-rate note mechanics:**

```
Coupon = Reference rate + Quoted margin
```

An FRN's price stays **close to par** because the coupon resets to the market rate. Its price
sensitivity to interest rates is therefore very low — duration is roughly the time to the **next
reset**, not to maturity (LM8). It retains full **credit** risk, however: if the issuer's credit
deteriorates, the required margin rises above the quoted margin and the price falls below par.

**Caps and floors** on an FRN: a **cap** benefits the **issuer** (limits how high the coupon can go);
a **floor** benefits the **investor** (limits how low). A **collar** has both.

**Inflation-linked bonds** (TIPS, index-linked gilts) come in several forms:

| Type | Mechanism |
| --- | --- |
| **Capital-indexed** | The **principal** is adjusted for inflation; a fixed coupon rate is applied to the adjusted principal. The most common form (TIPS) |
| **Interest-indexed** | Principal fixed; only the **coupon** is adjusted |
| **Zero-coupon indexed** | A single inflation-adjusted payment at maturity |
| **Indexed-annuity** | A level payment stream adjusted for inflation |

### Contingency provisions — who holds the option

**The governing principle, which recurs throughout Fixed Income and Derivatives: whoever holds the
option pays for it.**

| Provision | Option holder | Effect on the bond's price | Effect on the yield |
| --- | --- | --- | --- |
| **Callable** | **Issuer** | **Lower** than an otherwise identical straight bond | **Higher** |
| **Putable** | **Investor** | **Higher** | **Lower** |
| **Convertible** | **Investor** | **Higher** | **Lower** |

```
Value of a callable bond   = Value of a straight bond − Value of the call option
Value of a putable bond    = Value of a straight bond + Value of the put option
Value of a convertible     = Value of a straight bond + Value of the conversion option
```

**Call provisions in detail:**

- **Why issuers call:** when interest rates **fall**, the issuer can refinance at a lower cost —
  which is exactly when the bond would otherwise be most valuable to the investor. The call
  therefore **caps the investor's upside**.
- **Call protection** — a period during which the bond cannot be called. **American style** =
  callable any time after the protection period; **European style** = callable only on one date;
  **Bermudan style** = callable on specified dates.
- **Call price schedule** — usually starts above par and declines toward par over time.
- **Make-whole call** — the issuer must pay the present value of the remaining cash flows at a
  small spread over the government curve, which makes calling expensive and largely protects the
  investor.

**Put provisions** let the investor sell the bond back at a set price, typically par. They protect
against **rising rates** and against **credit deterioration**, which is why a putable bond yields
less.

**Convertible bonds** — terminology to know:

```
Conversion ratio     = number of shares received per bond
Conversion price     = Par value / Conversion ratio
Conversion value     = Share price × Conversion ratio
Straight value       = Value as a bond alone, ignoring the conversion option
Minimum value        = max(Conversion value, Straight value)
Market conversion price = Convertible bond price / Conversion ratio
Market conversion premium per share = Market conversion price − Share price
```

A convertible gives the investor **equity upside with a bond floor** — which is why they accept a
lower coupon. The **straight value acts as a floor**, though that floor falls if the issuer's credit
deteriorates.

### Legal, regulatory, and tax considerations

- **Registration and disclosure** requirements vary by market: a domestic public issue faces full
  regulatory disclosure; a **eurobond** or a private placement (Rule 144A in the US) faces much less.
- **Bearer versus registered** form affects tax enforcement and transferability.
- **Taxation of interest** — usually ordinary income. **Original issue discount** on a zero-coupon
  or deep-discount bond may be taxed as **imputed interest annually**, even though no cash is
  received until maturity — a genuine cash flow problem for a taxable holder.
- **Premium amortisation** may be deductible against interest income.
- **Capital gains** on a bond bought at a discount in the secondary market are typically taxed as
  capital gains, at a different rate.
- **Withholding tax** on cross-border coupon payments, often reduced by tax treaty.
- **Tax-exempt issues** — US municipal bonds are exempt from federal income tax for US investors,
  which is why their yields are below comparable taxable bonds.

---

## Formulas to know cold

```
FLOATING-RATE NOTE
  Coupon = Reference rate + Quoted margin
  Price stays near par (coupon resets); duration ≈ time to the NEXT RESET
  Cap benefits the ISSUER;  Floor benefits the INVESTOR

CONTINGENCY PROVISIONS — whoever holds the option pays for it
  Callable bond   = Straight bond − Call option      → lower price, HIGHER yield
  Putable bond    = Straight bond + Put option       → higher price, LOWER yield
  Convertible     = Straight bond + Conversion option → higher price, LOWER yield

CONVERTIBLE BOND TERMS
  Conversion ratio = shares per bond
  Conversion price = Par / Conversion ratio
  Conversion value = Share price × Conversion ratio
  Minimum value    = max(Conversion value, Straight value)
  Market conversion price = Convertible price / Conversion ratio
  Market conversion premium per share = Market conversion price − Share price

PRINCIPAL STRUCTURES
  Bullet (all at maturity) · Fully amortising · Partially amortising (balloon) · Sinking fund
```

---

## Exam traps

> **Trap 1 — Who benefits from a call.** The **issuer**. Callable bonds are worth **less** and yield
> **more** than otherwise identical straight bonds. Putable and convertible features benefit the
> **investor** — higher price, lower yield.

> **Trap 2 — FRN duration.** An FRN's interest rate duration is approximately the time to the **next
> reset**, not to maturity. But its **credit** risk is unaffected by the reset mechanism.

> **Trap 3 — Caps and floors.** A **cap** benefits the **issuer**; a **floor** benefits the
> **investor**. Same logic as calls and puts.

> **Trap 4 — Sinking funds.** They **reduce credit risk** but create **reinvestment risk** for the
> investor, whose bonds may be redeemed at par when rates have fallen.

> **Trap 5 — Zero-coupon tax treatment.** Accretion may be taxed as **imputed interest annually**
> with no cash received — a real problem for a taxable holder.

> **Trap 6 — PIK coupons.** Paying interest in more bonds is a significant **credit warning**, not a
> neutral structural choice.

> **Trap 7 — Convertible minimum value.** It is the **maximum** of conversion value and straight
> value, not the minimum of them.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A bond has a conversion ratio of 25 and a par value of 1,000. The share price is 46 and the convertible trades at 1,180. Compute the conversion price, conversion value, market conversion price, and market conversion premium per share.

<details><summary>Answer</summary>

**Conversion price** = 1,000 / 25 = **40.00**
**Conversion value** = 46 × 25 = **1,150**
**Market conversion price** = 1,180 / 25 = **47.20**
**Market conversion premium per share** = 47.20 − 46 = **1.20** (about 2.6% of the share price)

Interpretation: buying the convertible and converting immediately costs 47.20 per share versus 46 in the market — a 1.20 premium. That premium is what the investor pays for the **bond floor**: if the share price collapses, the convertible's value is supported by its straight value as a bond, while the shares are not.

</details>

**2.** Why does a callable bond yield more than an otherwise identical straight bond?

<details><summary>Answer</summary>

Because the investor has **sold an option to the issuer**, and must be compensated for it.

The issuer will call when it is advantageous to *them* — specifically when **interest rates fall** and they can refinance more cheaply. But that is precisely when the bond would otherwise be **most valuable** to the investor, since falling rates raise bond prices.

So the call **caps the investor's upside**: the price cannot rise much above the call price, because the bond will be redeemed. The investor also faces **reinvestment risk** — receiving par back in a low-rate environment and having to reinvest at those lower rates.

```
Callable bond value = Straight bond value − Call option value
```

A lower price for the same promised cash flows means a **higher yield**. The extra yield is the premium the investor receives for writing the call.

The symmetric case: a **putable** bond gives the *investor* an option, so it trades at a **higher** price and a **lower** yield.

</details>

**3.** A floating-rate note pays SOFR + 60bp, resetting quarterly. Rates rise sharply. What happens to its price? What if instead the issuer is downgraded?

<details><summary>Answer</summary>

**Rates rise:** the price barely moves. At the next quarterly reset the coupon adjusts upward to the new SOFR plus the same 60bp margin, so the bond's cash flows keep pace with the market. Its interest rate **duration is approximately the time to the next reset** — a maximum of three months here — so a 200bp rate rise might move the price by a fraction of a percent. This is the point of an FRN.

**The issuer is downgraded:** the price **falls meaningfully**. The reset mechanism adjusts for the **reference rate**, not for the **credit spread**. If the market now demands 180bp for this issuer's credit while the note pays only 60bp, the note is under-compensating by 120bp for its remaining life, and the price falls below par until the **discount margin** equals the required spread.

**The lesson:** an FRN removes interest rate risk, not credit risk. Its price behaviour is almost entirely a credit story (LM8).

</details>

**4.** Contrast a bullet structure, a fully amortising structure, and a sinking fund from the investor's perspective.

<details><summary>Answer</summary>

**Bullet:** coupons only, then the **entire principal at maturity**. The investor's capital stays outstanding for the full term, earning the coupon. Maximum interest rate sensitivity (the longest duration of the three) and maximum credit exposure at maturity — the issuer must refinance or repay a single large sum, which is a concentrated **refinancing risk**.

**Fully amortising:** principal is repaid **gradually** with each payment, so the balance declines to zero at maturity. Lower duration than a bullet of the same maturity, because the cash flows arrive earlier. Lower credit risk — there is no large final repayment to refinance. But the investor faces **reinvestment risk** on the returning principal throughout the life.

**Sinking fund:** the issuer must retire a **specified portion each year**, either by buying bonds in the open market or by redeeming bonds **selected by lot**, usually at par. Credit risk is reduced for the same reason as amortisation. But the investor faces an additional problem: **their specific bond may be called at par**, and the issuer is most likely to redeem (rather than buy in the market) when the bonds trade **above** par — i.e. when rates have fallen. That is adverse selection against the investor, and it creates reinvestment risk at exactly the wrong time.

</details>

---

## Done when

- [ ] I can describe four principal repayment structures and their implications for the investor
- [ ] I can describe eight coupon structures including PIK and index-linked variants
- [ ] I can state the price and yield effect of call, put, and conversion features and explain why
- [ ] I can compute the full set of convertible bond terms
- [ ] I can explain why an FRN's price is insensitive to rates but not to credit
- [ ] I can state who benefits from a cap and who from a floor
- [ ] I can explain the tax treatment of original issue discount and why it is a cash flow problem
- [ ] I answered the self-check cold, several days after first study

---

← [LM01 Fixed-Income Instrument Features](lm-01-fixed-income-instrument-features.md)  ·  [Topic index](README.md)  ·  [LM03 Fixed-Income Issuance and Trading](lm-03-fixed-income-issuance-and-trading.md) →
