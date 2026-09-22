# AI · LM07 — Introduction to Digital Assets

## At a glance

| | |
| --- | --- |
| **Topic** | Alternative Investments (7-10% of the exam) |
| **Hours budgeted** | 5 |
| **Prerequisites** | LM1–LM2, QM LM11 (financial data science). |
| **Where it shows up** | 1 question. Descriptive; the DLT characteristics and the asset-class comparison are the targets. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe financial applications of distributed ledger technology
- explain investment features of digital assets and contrast them with other asset classes
- describe investment forms and vehicles used in digital asset investments
- analyze sources of risk, return, and diversification among digital asset investments

---

## Core concepts

### Distributed ledger technology

**A distributed ledger is a database shared across a network of computers, with no single central
authority.** A **blockchain** is the most common form: transactions are grouped into blocks, each
cryptographically linked to the previous one, forming a chain that cannot be altered retroactively
without redoing all subsequent work.

| Feature | Detail |
| --- | --- |
| **Distributed** | Every participant holds a copy; no central database to attack or corrupt |
| **Cryptographically secured** | Transactions are signed and verified; blocks are chained by hash |
| **Immutable** | Once recorded and confirmed, an entry cannot practically be altered |
| **Consensus-driven** | The network agrees on validity through a **consensus mechanism** |
| **Transparent** (usually) | Public blockchains allow anyone to inspect the ledger |

**Consensus mechanisms:**

| Mechanism | How it works | Trade-off |
| --- | --- | --- |
| **Proof of work** | Validators ("miners") compete to solve a computational puzzle | Very secure; **enormous energy consumption**; slow |
| **Proof of stake** | Validators are selected in proportion to the assets they "stake" as collateral | Far more energy-efficient; raises concentration concerns |

**Permissionless versus permissioned:**

| | **Permissionless (public)** | **Permissioned (private)** |
| --- | --- | --- |
| Participation | Open to anyone | Restricted to approved participants |
| Transparency | Full | Limited to participants |
| Use | Public cryptocurrencies | **Enterprise and financial institution applications** |

### Financial applications of DLT

| Application | Detail |
| --- | --- |
| **Cryptocurrencies** | Digital bearer assets transferable without an intermediary |
| **Tokenisation** | Representing ownership of real assets — property, art, private equity — as digital tokens, enabling **fractional ownership** and potentially secondary trading of otherwise illiquid assets |
| **Smart contracts** | Self-executing code that performs when conditions are met, without an intermediary. Underlies decentralised finance (**DeFi**) |
| **Post-trade processing** | Clearing and settlement, potentially reducing settlement from days to near-instant and removing reconciliation |
| **Trade finance** | Documentary credit, bills of lading, supply chain verification |
| **Identity and compliance** | Know-your-customer records shared securely between institutions |
| **Central bank digital currencies (CBDCs)** | Sovereign digital money, under active development in many jurisdictions |

> **Tokenisation is the application with the clearest investment relevance.** If an illiquid asset —
> a building, a private company stake, a fund interest — can be represented as divisible, tradeable
> tokens, the **illiquidity discount** shrinks and access widens. Whether the legal and regulatory
> infrastructure will support this at scale remains unresolved, but it is the mechanism by which DLT
> would most directly affect the alternatives universe.

### Types of digital asset

| Type | Description |
| --- | --- |
| **Cryptocurrencies** | Designed as a medium of exchange or store of value (Bitcoin being the original) |
| **Stablecoins** | Pegged to a reference asset, usually a fiat currency. Backed by **fiat reserves**, by **crypto collateral** (overcollateralised), or **algorithmically** — the last of which has failed repeatedly |
| **Utility tokens** | Provide access to a product or service on a network |
| **Security tokens** | Represent a claim on an underlying asset or cash flow — economically a security, and generally regulated as one |
| **Non-fungible tokens (NFTs)** | Unique, non-interchangeable tokens representing a specific item |
| **CBDCs** | Central bank issued |

### Investment characteristics — contrasted with other asset classes

| | **Digital assets** | **Equities** | **Bonds** | **Commodities** |
| --- | --- | --- | --- | --- |
| **Cash flows** | **None** (for most) | Dividends | Coupons | None |
| **Intrinsic value basis** | **Contested** — no cash flows to discount | Discounted cash flows | Discounted cash flows | Supply and demand |
| **Volatility** | **Extreme** | High | Moderate | High |
| **Regulation** | **Evolving and inconsistent** across jurisdictions | Well established | Well established | Established |
| **Custody** | **Self-custody or a specialist custodian**; private key loss is **irreversible** | Standard | Standard | Standard |
| **Trading** | 24/7, global, fragmented across venues | Exchange hours | OTC | Exchange and OTC |
| **Correlation** | Initially low, but has **risen materially** with institutional adoption | — | — | — |

> **The valuation problem is fundamental, and the exam expects you to recognise it.** A cryptocurrency
> generates no cash flows, so **no discounted cash flow model applies** — the same problem as
> commodities (LM5), but without even a marginal cost of production to anchor the price (though
> proof-of-work mining cost is sometimes offered as a loose floor).
>
> Proposed valuation approaches — network value models based on user counts, stock-to-flow scarcity
> models, or comparison to gold's market value — are all essentially **narrative**, and none has an
> accepted theoretical foundation. Price is determined by supply, demand, and sentiment.

### Investment forms and vehicles

| Vehicle | Detail |
| --- | --- |
| **Direct ownership** | Holding the asset, with **self-custody** (own private keys) or a specialist custodian |
| **Exchange-traded products** | Spot and futures-based ETFs and ETNs, offering regulated access without custody |
| **Futures and options** | Listed derivatives on major exchanges |
| **Hedge funds and venture funds** | Managed exposure to digital assets and to the surrounding infrastructure |
| **Equities of related businesses** | Exchanges, miners, and infrastructure providers — an indirect and imperfect proxy |
| **Staking and lending** | Earning yield by staking assets or lending them — carrying **counterparty and smart contract risk**, as multiple failures have demonstrated |

### Risk, return, and diversification

**Return sources:** price appreciation, **staking rewards** (for proof-of-stake networks), and
lending or liquidity provision yields.

**Risks:**

| Risk | Detail |
| --- | --- |
| **Extreme volatility** | Drawdowns of 70–80% have occurred repeatedly |
| **Regulatory** | The **dominant** risk. Treatment varies enormously by jurisdiction and is still evolving. An adverse ruling can render an asset untradeable |
| **Custody and operational** | **Private key loss is irreversible** — there is no recovery mechanism and no central authority to appeal to |
| **Exchange and counterparty** | Multiple large exchanges and lenders have failed with total loss of customer assets |
| **Technology** | Protocol bugs, smart contract exploits, 51% attacks |
| **Liquidity** | Thin outside the largest assets; fragmented across venues |
| **Fraud and manipulation** | Limited regulatory oversight; documented wash trading and manipulation |
| **Concentration** | Ownership is highly concentrated in some assets, enabling large price impact |
| **Environmental** | Proof-of-work energy consumption, which is itself a regulatory risk |

**Diversification:**

- **Initially low correlation** with traditional assets, which was the original institutional case
- **That correlation has risen substantially** as institutional participation grew. Digital assets
  now behave largely as a **high-beta risk asset**, selling off with equities in risk-off episodes
- The **claimed inflation hedge is unproven** — digital assets fell sharply during the 2022
  inflationary episode, which was the first real test

> **The honest analytical position:** digital assets have **no established valuation framework**, an
> **unresolved regulatory status**, and a **short history** dominated by a single extraordinary bull
> market. The diversification case that justified early institutional interest has **weakened
> materially** as correlations rose.
>
> None of that makes them uninvestable — but it does mean any allocation is a position taken on
> conviction and sizing, not on the analytical footing available for other asset classes. An analyst
> should be able to state that plainly rather than reaching for either enthusiasm or dismissal.

---

## Formulas to know cold

```
DISTRIBUTED LEDGER TECHNOLOGY
  Distributed · cryptographically secured · IMMUTABLE · consensus-driven · (usually) transparent

  CONSENSUS MECHANISMS
    Proof of WORK  — computational competition. Very secure, ENORMOUS energy use, slow
    Proof of STAKE — validators chosen by assets staked. Energy-efficient, concentration concerns

  PERMISSIONLESS (public, open) vs PERMISSIONED (private, approved participants — enterprise use)

FINANCIAL APPLICATIONS
  Cryptocurrencies · TOKENISATION (fractional ownership of illiquid assets) · smart contracts / DeFi
  · post-trade clearing and settlement · trade finance · identity/KYC · CBDCs

TYPES OF DIGITAL ASSET
  Cryptocurrencies · STABLECOINS (fiat-backed / crypto-collateralised / ALGORITHMIC — repeatedly failed)
  · utility tokens · security tokens · NFTs · CBDCs

THE VALUATION PROBLEM
  NO CASH FLOWS → no DCF possible (as with commodities, LM5)
  and no marginal production cost to anchor the price
  → proposed models (network value, stock-to-flow) are essentially NARRATIVE

KEY RISKS
  REGULATORY (the dominant one) · extreme volatility · CUSTODY (private key loss is IRREVERSIBLE)
  · exchange/counterparty failure · technology · liquidity · fraud · concentration · environmental

DIVERSIFICATION: initially low correlation, but it has RISEN MATERIALLY.
  Digital assets now behave largely as a HIGH-BETA RISK ASSET.
```

---

## Exam traps

> **Trap 1 — Assuming digital assets have an established valuation framework.** They do **not**.
> With no cash flows, DCF is impossible, and unlike commodities there is not even a marginal
> production cost to anchor the price.

> **Trap 2 — Treating the low correlation as current.** It was low **initially**; it has **risen
> substantially** with institutional adoption. The diversification case has weakened.

> **Trap 3 — Proof of work vs proof of stake.** **Proof of work** is computational competition —
> secure but enormously energy-intensive. **Proof of stake** selects validators by assets staked.

> **Trap 4 — Assuming all stablecoins are equivalent.** **Fiat-backed**, **crypto-collateralised**,
> and **algorithmic** stablecoins have very different risk profiles. Algorithmic designs have failed
> repeatedly and catastrophically.

> **Trap 5 — Underestimating custody risk.** **Private key loss is irreversible.** There is no
> recovery mechanism, no central authority, and no insurance by default.

> **Trap 6 — Treating exchange balances as ownership.** Assets held on an exchange are a **claim on
> the exchange**, not direct ownership. Multiple large exchanges have failed with total customer
> loss.

> **Trap 7 — Assuming the inflation hedge is established.** It is **unproven**. Digital assets fell
> sharply in the 2022 inflationary episode — the first real test.

> **Trap 8 — Confusing permissionless and permissioned ledgers.** **Enterprise financial
> applications** overwhelmingly use **permissioned** ledgers, not public blockchains.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Why can't a discounted cash flow model be applied to a cryptocurrency, and what does that leave?

<details><summary>Answer</summary>

**Because there are no cash flows.** A cryptocurrency pays no dividend, no coupon, and no rent. Every valuation model in the curriculum — DDM, FCFE, FCFF, residual income (Equity LM6) — requires projecting cash flows and discounting them. With none, there is nothing to discount.

**This is the same problem as commodities (LM5), but worse.** A commodity at least has:
- A **marginal cost of production**, which anchors the long-run price to the cost curve
- **Physical supply and demand** from industrial consumption

A cryptocurrency has neither industrial demand nor, for most, a production cost. (Proof-of-work mining cost is sometimes offered as a loose floor, but it is circular — mining capacity adjusts to the price, not the reverse.)

**What is left — and none of it has an accepted theoretical foundation:**
- **Network value models** relating value to user counts or transaction volume (a Metcalfe's-law analogy)
- **Stock-to-flow** scarcity models based on the issuance schedule
- **Comparison to gold's market value**, on the argument that it serves a similar store-of-value function
- **Cost of production** as a loose floor

Each is essentially a **narrative** dressed as a model. Price is determined by supply, demand, and sentiment.

**What an analyst should say:** that the asset has no established valuation framework, so any position is a judgement about adoption and sentiment rather than a valuation conclusion. That is a legitimate thing to say — it is not the same as saying the asset is worthless, and it is far more honest than producing a spurious target price.

</details>

**2.** Contrast the three types of stablecoin on their backing and risk.

<details><summary>Answer</summary>

**Fiat-backed** — each token is backed by reserves of the reference currency (or short-dated government securities) held by the issuer.
- **Risk: the reserves.** Are they genuinely held, in what instruments, and are they audited by a credible firm? Several issuers have been found holding riskier assets than claimed.
- **Counterparty risk** on the issuer and its banking relationships
- **Regulatory risk** — increasingly the subject of specific legislation
- Generally the **most robust** type in practice, provided the reserves are real and liquid

**Crypto-collateralised** — backed by other digital assets, held in a smart contract and **overcollateralised** (for example, 150% of the token value) to absorb volatility.
- **Risk: the collateral is itself volatile.** A sharp fall can breach the collateral threshold, triggering automated liquidations
- **Liquidation cascades** — forced selling pushes prices down, triggering more liquidations
- **Smart contract risk** — a bug in the mechanism
- More transparent than fiat-backed (the collateral is visible on-chain) but structurally more fragile

**Algorithmic** — no meaningful collateral. The peg is maintained by an algorithm that expands and contracts supply, often via a paired volatile token.
- **Risk: the mechanism depends on continued confidence.** If holders lose faith and sell, the algorithm mints more of the paired token, driving its price down, prompting more selling — a **death spiral**
- **These have failed repeatedly and catastrophically**, with the 2022 collapse of a major algorithmic stablecoin destroying tens of billions in days
- There is no reserve to fall back on. The design is reflexive by construction

**The general point:** 'stablecoin' describes an **objective**, not a mechanism. The backing determines whether the objective is achievable, and the three mechanisms are not remotely equivalent in risk.

</details>

**3.** Why is custody risk qualitatively different for digital assets than for traditional securities?

<details><summary>Answer</summary>

Because **there is no recovery mechanism and no central authority**.

**Traditional securities:** ownership is recorded by a **custodian, registrar, or central securities depository**. If you lose your password, forget your broker, or die, the record still exists. Ownership can be re-established through the institution, and there are legal mechanisms — courts, probate, regulators — to resolve disputes. Assets are typically **segregated** from the custodian's own and often insured.

**Digital assets held in self-custody:** ownership **is** control of the **private key**. There is no separate record of who owns what beyond the key.
- **Lose the key and the asset is permanently inaccessible.** Not frozen, not recoverable through an appeal — gone. Substantial quantities of Bitcoin are estimated to be permanently lost this way.
- **Anyone who obtains the key owns the asset**, irreversibly. Transactions cannot be reversed, and there is no fraud department.
- **No central authority exists** to appeal to. That is the design intention, not a deficiency — but it removes every safeguard investors rely on elsewhere.

**Digital assets held on an exchange:** this is **not ownership** — it is a **claim on the exchange**. The exchange holds the keys. Multiple large exchanges have failed, with customer assets found to have been lent, rehypothecated, or simply misappropriated, and customers ranking as unsecured creditors.

**The institutional response:** regulated **qualified custodians** with segregated cold storage, multi-signature arrangements, insurance, and audited controls. This addresses the operational risk but reintroduces the counterparty risk that self-custody was meant to avoid — which is an unresolved tension rather than a solved problem.

</details>

**4.** Has the diversification case for digital assets held up?

<details><summary>Answer</summary>

**It has weakened substantially, and honesty about that is the analytically correct position.**

**The original case (roughly 2015–2020):** digital assets showed very low correlation with equities and bonds. In a mean-variance framework, an asset with high expected return and near-zero correlation earns an allocation even at high volatility. This was the argument that brought institutional money in.

**What changed:**

**(1) Institutional adoption itself.** As the same investors who hold equities began holding digital assets, the assets became subject to the **same risk-appetite cycle**. Risk-off episodes now produce selling in both simultaneously.

**(2) Leverage and shared liquidity.** Leveraged positions deleverage together, and the same funds hold both — the same mechanism that raises hedge fund correlations in crises (LM6).

**(3) Macro sensitivity.** Digital assets have become notably sensitive to **real interest rates** and liquidity conditions — the same drivers as long-duration growth equities. They now behave largely as a **high-beta risk asset**.

**(4) The 2022 test.** In a genuine inflationary shock with rising rates, digital assets fell sharply **alongside** equities and bonds — failing both as a diversifier and as an inflation hedge, in the first real test of either claim.

**What remains:** correlation is **not 1**, and the asset retains idiosyncratic drivers (regulatory news, protocol developments, adoption). There is some residual diversification.

**But the case is now much weaker**, and any allocation should be framed as a **conviction position on adoption**, sized accordingly, rather than as a portfolio-optimisation output derived from historical correlations that no longer describe the asset.

</details>

---

## Done when

- [ ] I can describe DLT's five features and contrast proof of work with proof of stake
- [ ] I can distinguish permissionless from permissioned ledgers and say which enterprises use
- [ ] I can name seven financial applications of DLT and explain why tokenisation matters most
- [ ] I can name six types of digital asset and contrast the three stablecoin designs
- [ ] I can explain why DCF cannot be applied and what that leaves
- [ ] I can explain why custody risk is qualitatively different here
- [ ] I can state honestly what has happened to the diversification case
- [ ] I answered the self-check cold, several days after first study

---

← [LM06 Hedge Funds](lm-06-hedge-funds.md)  ·  [Topic index](README.md)
