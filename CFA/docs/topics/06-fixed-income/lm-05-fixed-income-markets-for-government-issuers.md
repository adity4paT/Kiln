# FI · LM05 — Fixed-Income Markets for Government Issuers

## At a glance

| | |
| --- | --- |
| **Topic** | Fixed Income (11-14% of the exam) |
| **Hours budgeted** | 3 |
| **Prerequisites** | LM1–LM4. |
| **Where it shows up** | 1 question. Descriptive. Short module. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe funding choices by sovereign and non-sovereign governments, quasi-government entities, and supranational agencies
- contrast the issuance and trading of government and corporate fixed-income instruments

---

## Core concepts

### Sovereign issuers

National governments borrowing **in their own currency** occupy a unique position: they can, in
principle, always repay by creating money. That makes local-currency sovereign default rare but not
impossible — it is a **policy choice** rather than an inability, and the cost of the alternative
(inflation, currency collapse) is sometimes judged higher.

**Foreign-currency sovereign debt is different.** A government cannot print another country's
currency, so it must earn or borrow it. Foreign-currency sovereign defaults are consequently far
more common than local-currency ones — a distinction that credit rating agencies formalise by
assigning **separate local-currency and foreign-currency ratings** (LM15).

**Names by country:**

| Country | Instruments |
| --- | --- |
| **United States** | **T-bills** (≤1 year, discount), **T-notes** (2–10 years), **T-bonds** (>10 years), **TIPS** (inflation-linked), **FRNs** |
| **United Kingdom** | **Gilts**, including index-linked gilts |
| **Germany** | **Bubills** (short), **Schätze** (2y), **Bobls** (5y), **Bunds** (10y+) |
| **Japan** | **JGBs** |
| **France** | **BTFs**, **BTANs**, **OATs** |

**Issuance mechanism:** almost universally by **auction**, single-price (Dutch) or multiple-price
(LM3), conducted on a published calendar. **Primary dealers** — a designated group of banks — are
obliged to bid at every auction and to make markets in the secondary market, in exchange for
privileged access.

### Non-sovereign government issuers

States, provinces, regions, and municipalities. They **cannot print money**, so they carry genuine
credit risk, and they typically yield more than the sovereign.

| Type | Backed by |
| --- | --- |
| **General obligation (GO) bonds** | The issuer's **full faith, credit, and taxing power** |
| **Revenue bonds** | The **cash flow from a specific project** — a toll road, an airport, a utility. No general claim on the issuer, so **higher yield** |

Some are supported explicitly or implicitly by the national government. **US municipal bonds** carry
a distinctive feature: their interest is generally **exempt from federal income tax** for US
investors, which is why their nominal yields sit below comparable taxable bonds. The comparison is
made on a **taxable-equivalent yield** basis:

```
Taxable-equivalent yield = Municipal yield / (1 − marginal tax rate)
```

### Quasi-government entities

Government-sponsored or government-owned agencies — national mortgage agencies, development banks,
export credit agencies, and infrastructure authorities.

Key question for the analyst: is the government support **explicit** (a formal guarantee) or
**implicit** (an expectation with no legal obligation)? Implicitly supported debt yields more,
because the support might not materialise — though historically it usually has, which is precisely
what makes the pricing difficult.

### Supranational agencies

Institutions owned by multiple sovereign governments: the **World Bank** (IBRD), the **IMF**, the
**European Investment Bank**, the **Asian Development Bank**, the **African Development Bank**, and
others.

- Typically rated **AAA**, backed by the callable capital commitments of their member sovereigns
- Issue large, liquid, benchmark-sized bonds in major currencies
- Lend for development and for crisis support

### Government versus corporate: issuance and trading

| Dimension | **Government** | **Corporate** |
| --- | --- | --- |
| **Issuance mechanism** | **Auction**, on a published calendar | **Underwritten** syndicate, opportunistically timed |
| **Predictability** | High — the calendar is announced in advance | Issuer chooses the window |
| **Liquidity** | **Very high**, especially on-the-run | Much lower, and highly variable by issue |
| **Bid-ask spreads** | **Narrow** — often a fraction of a basis point on benchmarks | **Wide** and variable |
| **Credit risk** | Minimal in local currency | The dominant risk |
| **Price driver** | **Interest rates**, almost entirely | Rates **and** credit spread |
| **Issue size** | Very large, repeatedly tapped | Smaller, one-off |
| **Standardisation** | High | Low — each issue is a negotiated contract |
| **Role** | The **benchmark** against which everything else is priced | Priced as a **spread** over the benchmark |
| **Settlement** | Often same-day or T+1 | T+1 or T+2 |
| **Documentation** | Standard | Individually negotiated |

> **The most important structural point:** government bonds are the **benchmark**. Corporate bond
> pricing is expressed as a **spread over** the government curve or a swap curve (LM7), which is why
> the government market's liquidity and depth matter to every other issuer. A dysfunctional
> government bond market makes every other bond harder to price.

---

## Formulas to know cold

```
TAXABLE-EQUIVALENT YIELD (for a tax-exempt municipal bond)
  Taxable-equivalent yield = Municipal yield / (1 − marginal tax rate)

  e.g. a 3.2% muni yield to a 37% taxpayer = 3.2% / 0.63 = 5.08% taxable-equivalent

NON-SOVEREIGN GOVERNMENT BONDS
  General obligation = backed by full faith, credit, and TAXING POWER
  Revenue bond       = backed by a SPECIFIC project's cash flows only → HIGHER yield

SOVEREIGN CREDIT
  Local-currency debt  → can be repaid by creating money → default is a POLICY CHOICE, rare
  Foreign-currency debt → cannot print it → default is far MORE common
  ⇒ rating agencies assign SEPARATE local- and foreign-currency ratings

ISSUANCE
  Government → AUCTION on a published calendar, via primary dealers
  Corporate  → UNDERWRITTEN syndicate, opportunistically timed
```

---

## Exam traps

> **Trap 1 — Assuming sovereign debt is risk-free.** Only **local-currency** sovereign debt
> approaches it. **Foreign-currency** sovereign debt carries real default risk, and there are many
> historical examples.

> **Trap 2 — General obligation vs revenue bonds.** **GO** is backed by the **taxing power**;
> **revenue** bonds are backed only by a **specific project's cash flows** and therefore yield more.

> **Trap 3 — Comparing municipal yields directly to taxable yields.** Use the **taxable-equivalent
> yield**: `muni yield / (1 − t)`.

> **Trap 4 — Explicit vs implicit government support.** Implicitly supported quasi-government debt
> yields **more**, because the support is an expectation rather than an obligation.

> **Trap 5 — Confusing the issuance mechanisms.** Governments issue by **auction** on a published
> calendar; corporates issue through **underwritten syndicates** at a time of their choosing.

> **Trap 6 — Missing the benchmark role.** Government yields are the reference against which all
> other bonds are quoted as a spread.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A municipal bond yields 3.4%. An investor faces a 35% marginal tax rate. What taxable yield would be equivalent?

<details><summary>Answer</summary>

Taxable-equivalent yield = 3.4% / (1 − 0.35) = 3.4% / 0.65 = **5.23%**

So a taxable corporate bond would need to yield **more than 5.23%** to beat the municipal bond for this investor, after tax.

Note the implication: the higher the investor's tax rate, the more valuable the exemption. For a 12% taxpayer the equivalent is only 3.4/0.88 = 3.86%, so municipal bonds are a poor fit. This is why the municipal market is dominated by high-bracket individual investors — the tax exemption is worth far more to them, and the market prices accordingly.

</details>

**2.** Why do rating agencies assign separate local-currency and foreign-currency ratings to sovereigns?

<details><summary>Answer</summary>

Because the **ability to repay is fundamentally different** in the two cases.

**Local-currency debt:** the government controls the currency it owes. It can, in the last resort, create money to repay. Default is therefore a **policy choice** — a judgement that the cost of repaying (inflation, currency depreciation, loss of monetary credibility) exceeds the cost of defaulting. It happens, but rarely.

**Foreign-currency debt:** the government **cannot create** the currency it owes. It must earn it through exports, borrow it, or draw on reserves. If export earnings collapse, reserves are exhausted, and markets close, the government simply cannot pay regardless of willingness. Foreign-currency sovereign defaults are consequently **far more common** historically.

**The practical consequence:** a sovereign can be rated, say, A for local-currency debt and BBB for foreign-currency debt simultaneously, and the difference is meaningful rather than technical. It is also why heavy foreign-currency borrowing is treated as a serious warning signal in sovereign credit analysis (LM15) — it converts a monetary problem into a solvency problem.

Note: a member of a currency union (e.g. the eurozone) does not control its own currency, so its 'local-currency' debt behaves more like foreign-currency debt.

</details>

**3.** Contrast how a government and a corporate issuer bring a new bond to market.

<details><summary>Answer</summary>

**Government:** by **auction**, on a **published calendar** announced months in advance. The size and maturity are pre-announced; **primary dealers** are obliged to bid. Pricing is discovered by the auction itself — single-price (Dutch) or multiple-price. The issuer has no discretion over timing: the calendar commits it to issue whether market conditions are favourable or not, which is part of what makes the market reliable.

**Corporate:** through an **underwritten syndicate** of investment banks, at a time **of the issuer's choosing**. The banks conduct **bookbuilding** — marketing the issue, gauging demand, and setting the coupon and spread — and typically buy the issue (firm commitment) before reselling it. Size and structure are tailored to demand.

**The key behavioural difference:** the corporate issuer can **wait for a favourable window** and will postpone if spreads widen. The government cannot. This is why corporate issuance is highly cyclical — heavy when spreads are tight, drying up in stress precisely when issuers need money most — while government issuance continues through the cycle.

</details>

---

## Done when

- [ ] I can distinguish local-currency from foreign-currency sovereign risk and explain the rating split
- [ ] I can name the main sovereign instruments in the US, UK, Germany, and Japan
- [ ] I can contrast general obligation and revenue bonds
- [ ] I can compute a taxable-equivalent yield and explain who municipal bonds suit
- [ ] I can distinguish explicit from implicit government support and its pricing effect
- [ ] I can contrast government and corporate issuance and trading on at least six dimensions
- [ ] I answered the self-check cold, several days after first study

---

← [LM04 Fixed-Income Markets for Corporate Issuers](lm-04-fixed-income-markets-for-corporate-issuers.md)  ·  [Topic index](README.md)  ·  [LM06 Fixed-Income Bond Valuation: Prices and Yields](lm-06-fixed-income-bond-valuation-prices-and-yields.md) →
