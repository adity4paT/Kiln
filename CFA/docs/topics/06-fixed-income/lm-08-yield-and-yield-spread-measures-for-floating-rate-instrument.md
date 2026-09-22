# FI · LM08 — Yield and Yield Spread Measures for Floating-Rate Instruments

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | LM2 (FRN structure), LM7 (spread measures). |
| **Where it shows up** | 1–2 questions. The discount margin and money market yield conversions are the calculable parts. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- calculate and interpret yield spread measures for floating-rate instruments
- calculate and interpret yield measures for money market instruments

---

## Core concepts

### Floating-rate notes: the two margins

```
Coupon = Market reference rate (MRR) + Quoted margin
```

| Term | Meaning |
| --- | --- |
| **Quoted margin (QM)** | The **contractual** spread over the reference rate, fixed at issuance |
| **Discount margin (DM) / required margin** | The spread the **market currently requires** for this issuer's credit |

**The relationship determines the price:**

| Condition | Price |
| --- | --- |
| **DM = QM** | Price = **par** |
| **DM > QM** (credit has **deteriorated** since issue) | Price **below par** |
| **DM < QM** (credit has **improved**) | Price **above par** |

> **This is the FRN's entire price story.** Because the coupon resets to the current reference rate,
> interest rate changes barely move the price. What moves it is the gap between the **contractual**
> margin and the margin the market now demands — i.e. **credit**.

**Computing the discount margin.** Price the FRN as a bond whose cash flows are based on the current
reference rate plus the quoted margin, and solve for the discount rate; the discount margin is that
rate minus the reference rate.

```
              (MRR + QM) × (FV/m)                      (MRR + QM) × (FV/m) + FV
PV = ─────────────────────────────── + ... + ─────────────────────────────────────
     [1 + (MRR + DM)/m]                       [1 + (MRR + DM)/m]^N
```

In practice this is solved on the calculator: set `PMT = (MRR + QM) × FV/m`, `FV = par`, `N` = number
of periods, `PV = −price`, solve for `I/Y`, multiply by `m`, and subtract the MRR.

**Simplified approximation for a one-period-to-reset FRN:**

```
DM ≈ QM + (Par − Price) / (Price × Years to maturity) × ... 
```

— but the exam generally expects the full calculator solution, so learn that.

### Money market yield measures

Money market instruments (maturity ≤ one year) use conventions that differ from bond conventions,
and the differences are **precisely what is tested**.

| Measure | Formula | Basis | Denominator |
| --- | --- | --- | --- |
| **Holding period yield (HPY)** | `(P1 − P0 + D1)/P0` | Actual | **Price paid** |
| **Bank discount yield (BDY)** | `(D/F) × (360/t)` | **360** days | **FACE value** |
| **Money market yield (MMY / CD equivalent)** | `HPY × (360/t)` | **360** days | Price paid |
| **Bond equivalent yield (BEY)** | `HPY × (365/t)` | **365** days | Price paid |
| **Effective annual yield (EAY)** | `(1 + HPY)^(365/t) − 1` | 365, **compounded** | Price paid |

> **The bank discount yield is the odd one out, and therefore the one tested.** It divides the
> discount by **face value** (a larger denominator than the price) and uses a **360-day** year (a
> smaller multiplier than 365). Both distortions push it **down**, so BDY **understates** the true
> return and is **not comparable** to any other measure.

**The ordering, for a discount instrument:**

```
BDY  <  MMY  <  BEY  <  EAY
```

**Converting between them:**

```
MMY = (360 × BDY) / (360 − t × BDY)

BDY = (360 × MMY) / (360 + t × MMY)
```

**Add-on rate instruments** (certificates of deposit, repos, bank loans) quote interest **added to**
the principal at maturity, rather than as a discount from face. For these, the quoted rate is
already an add-on (money market) yield — no conversion from a discount basis is needed.

**Instruments quoted on a discount basis:** Treasury bills, commercial paper, banker's acceptances.
**Instruments quoted on an add-on basis:** CDs, repos, bank deposits.

### Why the conventions matter

An investor comparing a Treasury bill quoted at a 4.80% **bank discount** yield with a certificate of
deposit quoted at a 4.85% **add-on** rate is comparing two different things. Converting the T-bill to
a money market yield might give 4.92%, making it the better investment despite the lower quoted
number.

> **This is not a technicality.** Money market portfolios are large and the differences are real
> basis points. The exam tests it because it is a genuine professional trap, not because the
> arithmetic is interesting.

---

## Formulas to know cold

```
FLOATING-RATE NOTES
  Coupon = Market reference rate (MRR) + Quoted margin (QM)
  Discount margin (DM) = the margin the MARKET currently requires

  DM = QM  →  price = PAR
  DM > QM  →  price BELOW par   (credit has deteriorated)
  DM < QM  →  price ABOVE par   (credit has improved)

  Solving for DM on the calculator:
    PMT = (MRR + QM) × FV/m ;  FV = par ;  N = periods ;  PV = −price
    → CPT I/Y, × m, then subtract MRR

MONEY MARKET YIELDS
  HPY = (P1 − P0 + D1)/P0
  BDY = (D/F) × (360/t)              ← FACE value denominator, 360 days. UNDERSTATES the return
  MMY = HPY × (360/t)                ← price denominator, 360 days
  BEY = HPY × (365/t)                ← price denominator, 365 days
  EAY = (1 + HPY)^(365/t) − 1        ← compounded, 365 days

  ORDERING:  BDY < MMY < BEY < EAY

  CONVERSIONS
    MMY = (360 × BDY) / (360 − t × BDY)
    BDY = (360 × MMY) / (360 + t × MMY)

  DISCOUNT basis: T-bills, commercial paper, banker's acceptances
  ADD-ON basis:   CDs, repos, bank deposits
```

---

## Exam traps

> **Trap 1 — Bank discount yield's denominator.** It uses **face value**, not the price paid, and a
> **360-day** year. Both understate the true return, and BDY is **not comparable** to any other
> measure without conversion.

> **Trap 2 — Quoted margin vs discount margin.** **QM is contractual** and fixed at issuance;
> **DM is what the market requires now**. The gap between them sets the FRN's price.

> **Trap 3 — FRN price direction.** **DM > QM → price below par.** The market demands more than the
> bond contractually pays, so the price must fall.

> **Trap 4 — Thinking an FRN is risk-free.** The reset removes **interest rate** risk, not **credit**
> risk. FRN price movements are almost entirely a credit story.

> **Trap 5 — 360 vs 365.** Money market yield uses **360**; bond equivalent yield uses **365**.
> Mixing them produces a small, plausible, wrong answer.

> **Trap 6 — Comparing a discount-basis quote to an add-on quote.** T-bills are quoted on a
> **discount** basis, CDs on an **add-on** basis. Convert before comparing.

> **Trap 7 — Getting the ordering wrong.** `BDY < MMY < BEY < EAY`. If your BDY comes out highest,
> you have used the price instead of face value in the denominator.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A 120-day Treasury bill with a face value of 1,000,000 is purchased for 984,000. Compute the HPY, BDY, MMY, BEY, and EAY.

<details><summary>Answer</summary>

Discount D = 1,000,000 − 984,000 = 16,000

**HPY** = 16,000 / 984,000 = **1.6260%**

**BDY** = (16,000/1,000,000) × (360/120) = 0.016 × 3 = **4.800%**

**MMY** = 1.6260% × (360/120) = 1.6260% × 3 = **4.878%**

**BEY** = 1.6260% × (365/120) = 1.6260% × 3.04167 = **4.946%**

**EAY** = (1.016260)^(365/120) − 1 = (1.016260)^3.04167 − 1 = **5.038%**

**Ordering confirmed: BDY (4.800) < MMY (4.878) < BEY (4.946) < EAY (5.038).** The BDY is lowest because it divides by 1,000,000 (face) rather than 984,000 (price) and uses a 360-day year.

</details>

**2.** An FRN pays SOFR + 45bp. The market now requires SOFR + 120bp for this issuer. Is the note above or below par, and why?

<details><summary>Answer</summary>

**Below par.**

The **quoted margin** is 45bp — that is what the note contractually pays above SOFR, fixed at issuance. The **discount margin** the market now requires is 120bp.

Since **DM (120) > QM (45)**, the note pays 75bp less than investors now demand for this credit. For its yield to rise to the required level, its **price must fall below par**.

**What has happened:** the issuer's credit quality has **deteriorated** since issuance. Note that nothing about the reference rate matters here — SOFR could have moved 300bp in either direction and the note's coupon would have followed it. **An FRN's price is a credit statement, not an interest rate statement.**

The magnitude of the discount depends on the remaining maturity: 75bp a year for five years produces a much larger discount than 75bp for six months.

</details>

**3.** Why does the bank discount yield understate a T-bill's true return?

<details><summary>Answer</summary>

**Two separate distortions, both pushing downward:**

**(1) The denominator is face value, not the price paid.** The investor's actual outlay is the *purchase price*, which is less than face. Dividing the discount by the larger number (face) produces a smaller ratio. The return should be measured against what was actually invested.

**(2) The year is 360 days, not 365.** Annualising by multiplying by 360/t rather than 365/t understates the annual rate by a factor of 365/360, roughly 1.4%.

**Neither is an error** — both are conventions, established when calculation was done by hand and 360 divided conveniently. But the result is that BDY is **not an economic return measure** and is **not comparable** to any other yield.

**The practical consequence:** a T-bill quoted at 4.80% BDY and a CD quoted at 4.85% add-on look close, but the T-bill's money market yield is 4.878% — it is actually the higher-yielding instrument. Convert before comparing.

</details>

**4.** A 90-day instrument has a bank discount yield of 3.60%. Convert it to a money market yield.

<details><summary>Answer</summary>

MMY = (360 × BDY) / (360 − t × BDY)
    = (360 × 0.036) / (360 − 90 × 0.036)
    = 12.96 / (360 − 3.24)
    = 12.96 / 356.76
    = 0.036329 = **3.633%**

The money market yield is **3.3 basis points higher** than the bank discount yield, because it divides by the price paid rather than by face value. (Both use a 360-day year, so that difference does not enter here — it would if converting to a bond equivalent yield.)

</details>

---

## Done when

- [ ] I can distinguish quoted margin from discount margin and state which way the price moves
- [ ] I can compute an FRN's discount margin on the calculator
- [ ] I can explain why an FRN's price movements are a credit story, not a rate story
- [ ] I can compute HPY, BDY, MMY, BEY, and EAY and reproduce their ordering
- [ ] I can explain both reasons the bank discount yield understates the return
- [ ] I can convert between bank discount yield and money market yield in both directions
- [ ] I can state which instruments are quoted on a discount basis and which on an add-on basis
- [ ] I answered the self-check cold, several days after first study

---

← [LM07 Yield and Yield Spread Measures for Fixed-Rate Bonds](lm-07-yield-and-yield-spread-measures-for-fixed-rate-bonds.md)  ·  [Topic index](README.md)  ·  [LM09 The Term Structure of Interest Rates: Spot, Par, and Forward Curves](lm-09-the-term-structure-of-interest-rates-spot-par-and-forward-cu.md) →
