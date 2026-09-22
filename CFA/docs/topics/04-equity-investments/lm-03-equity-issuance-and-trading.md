# EQ · LM03 — Equity Issuance and Trading

## At a glance

| | |
| --- | --- |
| **Topic** | Equity Investments (11-14% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM1. QM LM3 for the index weighting methods. |
| **Where it shows up** | 1–2 questions. Order types and liquidity measures are the calculable parts. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe primary and secondary public equity markets and their functions
- compare exchange, off-exchange, and over-the-counter equities trading
- describe liquidity measures for a publicly listed security and calculate float and average daily volume
- describe types of equity indexes

---

## Core concepts

### Primary and secondary markets

| | **Primary market** | **Secondary market** |
| --- | --- | --- |
| What happens | **New** securities are issued | **Existing** securities change hands |
| Who receives the proceeds | The **issuer** | The **selling investor** |
| Function | Raises capital | Provides **liquidity** and **price discovery** |

Both matter to the issuer. A company only raises money in the primary market, but a **liquid
secondary market lowers the cost of that capital** — investors pay more for a security they can sell.

**Primary market mechanisms:**

| Mechanism | How it works |
| --- | --- |
| **IPO** | First public sale, via underwriters who build a book of demand and set the price |
| **Seasoned (follow-on) offering** | An already-listed company issues more shares |
| **Rights offering** | Existing shareholders get the right to buy new shares pro rata, usually at a discount. **Protects them from dilution** — but is typically **dilutive to the share price** because the new shares are issued below market |
| **Private placement** | Sold directly to a small number of qualified investors; no public offering |
| **Shelf registration** | Registers an issue once, then sells in tranches as needed |
| **Direct listing** | Lists existing shares; **raises no capital** |

**Underwriting arrangements:** in a **firm commitment** the underwriter **buys the entire issue**
and bears the risk of not reselling it; in a **best efforts** deal the underwriter acts only as
agent and bears no inventory risk.

### Trading venues

| Venue | Characteristics |
| --- | --- |
| **Exchange** | Centralised, regulated, transparent order book, listing requirements, standard rules |
| **Alternative trading systems / dark pools** | Electronic venues with **limited pre-trade transparency**. Used to execute large orders without revealing intent and moving the price |
| **Over-the-counter (OTC)** | Dealer networks, bilateral negotiation, no central venue. Where unlisted and small securities trade |

**Why dark pools exist:** a large institutional order displayed on a public book invites front-running
and moves the price against the buyer. The trade-off is systemic: less pre-trade transparency may
worsen overall **price discovery** even as it improves execution for the individual large order.

### Order types

| Order | Instruction |
| --- | --- |
| **Market order** | Execute immediately at the best available price. **Certainty of execution, uncertainty of price** |
| **Limit order** | Execute only at a specified price or better. **Certainty of price, uncertainty of execution** |
| **Stop (stop-loss) order** | Becomes a market order once a trigger price is reached |
| **Stop-limit** | Becomes a limit order once triggered |
| **All-or-nothing** | Fill entirely or not at all |
| **Immediate or cancel** | Fill what can be filled now; cancel the rest |

**Validity:** day orders, good-till-cancelled, on-open, on-close.

> **The fundamental trade-off:** a market order guarantees execution but not price; a limit order
> guarantees price but not execution. Everything else is a variation on that.

**Long and short positions:** a **short sale** borrows shares, sells them, and buys them back later
to return. The short seller profits if the price falls, **pays any dividends** to the lender, and
faces **theoretically unlimited loss** since the price can rise without bound. Margin requirements
and the risk of a forced buy-in (if the lender recalls the shares) add practical constraints.

### Liquidity measures

**Float** — the shares actually available to public investors:

```
Float = Shares outstanding − Restricted shares
```

Restricted shares are those held by insiders, founders, governments, and strategic holders, plus
shares subject to lock-up. **Float, not shares outstanding, determines investable liquidity** and is
the basis for float-adjusted index weighting (QM LM3).

**Average daily volume:**

```
Average daily trading volume = Total shares traded over a period / Number of trading days
```

**Other liquidity measures:**

| Measure | What it captures |
| --- | --- |
| **Bid-ask spread** | The immediate cost of a round trip. Narrower = more liquid |
| **Spread as % of price** | Makes spreads comparable across price levels |
| **Turnover ratio** | Volume traded / shares outstanding — how actively the shares change hands |
| **Market depth** | The size available at each price level in the book |
| **Amihud illiquidity** | Price impact per unit of volume traded |

> **Why liquidity matters to valuation, not just to trading:** illiquid securities carry a **liquidity
> premium** — investors demand a higher return, so the price is lower. This is one of the components
> of the required return (QM LM1) and a large part of why private equity is valued at a discount to
> comparable listed companies.

### Types of equity index

Beyond the weighting methods (QM LM3 — price, equal, market-cap, float-adjusted cap):

| Category | Basis |
| --- | --- |
| **Broad market** | The whole market or a large representative sample |
| **Multi-market** | Across countries or regions |
| **Sector** | A single industry |
| **Style** | Value vs. growth; large, mid, small cap |
| **Thematic** | A theme — clean energy, cybersecurity, ageing demographics |
| **Fundamentally weighted** | Weighted by revenue, book value, earnings, or dividends rather than price. Breaks the link to price, so it does **not** automatically overweight whatever has risen most |
| **Factor** | Weighted by an exposure — momentum, quality, low volatility |

**What indexes are used for:** performance benchmarking, gauging market sentiment, the basis for
index funds and ETFs, asset allocation modelling, and as a proxy for the market portfolio in CAPM
and beta estimation.

> **Index construction choices are investment decisions in disguise.** A cap-weighted index
> mechanically holds more of whatever has risen most — a momentum tilt nobody chose. Equal weighting
> tilts small. Fundamental weighting tilts value. There is no neutral index; there is only a set of
> choices you should be able to name.

---

## Formulas to know cold

```
Float = Shares outstanding − Restricted shares (insiders, government, strategic, locked-up)

Average daily trading volume = Total shares traded in a period / Number of trading days

Bid-ask spread          = Ask − Bid
Spread as % of price    = (Ask − Bid) / Midpoint       [or / Ask]
Turnover ratio          = Shares traded over a period / Shares outstanding

Market capitalisation         = Price × Shares outstanding
Float-adjusted market cap     = Price × Float           ← the index-weighting basis
```

---

## Exam traps

> **Trap 1 — Market vs limit order.** **Market order: certain execution, uncertain price.**
> **Limit order: certain price, uncertain execution.** Asked directly and often.

> **Trap 2 — Float vs shares outstanding.** Float **excludes** restricted and insider holdings. It is
> the basis for float-adjusted index weighting and the true measure of investable liquidity.

> **Trap 3 — Rights offerings and dilution.** A rights issue **protects existing shareholders from
> ownership dilution** (they can maintain their proportional stake) but is typically **dilutive to
> the share price**, because the new shares are issued at a discount to market.

> **Trap 4 — Firm commitment vs best efforts.** In a **firm commitment** the underwriter **buys the
> issue** and bears the resale risk. In **best efforts** it is merely an agent.

> **Trap 5 — Short selling and dividends.** The short seller **pays** any dividends to the share
> lender, and faces **theoretically unlimited** loss.

> **Trap 6 — Assuming dark pools are unambiguously good.** They improve execution for large orders
> but reduce pre-trade transparency, which can degrade overall price discovery.

> **Trap 7 — Thinking any index is neutral.** Every weighting scheme embeds a tilt: cap-weighted
> toward momentum and large caps, equal-weighted toward small caps, fundamental toward value.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company has 500m shares outstanding. Founders hold 120m, a government agency holds 40m, and 25m are subject to lock-up. Compute the float and explain why it matters.

<details><summary>Answer</summary>

Float = 500 − 120 − 40 − 25 = **315m shares**

Why it matters:
- **Index weighting.** Float-adjusted market-cap indexes weight by float, not total shares. This company's index weight is based on 315m, not 500m — a 37% reduction.
- **Investable liquidity.** Only 315m shares can actually change hands. The effective liquidity, bid-ask spread, and price impact of a large order all depend on float.
- **Volatility.** A small float relative to interest in the stock produces larger price moves on a given order size.
- **Index inclusion.** Many indexes have minimum float requirements; a company with a low float ratio may be excluded entirely despite a large market capitalisation.

</details>

**2.** Explain the trade-off between a market order and a limit order, and when you would use each.

<details><summary>Answer</summary>

**Market order:** executes immediately at the best available price. **Execution is certain; price is not.** You may get a much worse price than expected in a fast-moving or thin market.

**Limit order:** executes only at your price or better. **Price is certain; execution is not.** If the market never reaches your limit, the order never fills.

**When to use each:**
- **Market order** when **immediacy matters more than price** — closing a losing position quickly, trading a highly liquid large-cap where the spread is a fraction of a percent, or acting on time-sensitive information.
- **Limit order** when **price matters more than immediacy** — building a position patiently, trading an illiquid security with a wide spread, or in a volatile market where a market order risks a poor fill.

For a large institutional order neither is used naively: the order is worked over time through algorithms, or crossed in a dark pool, precisely to avoid the price impact a displayed market order would cause.

</details>

**3.** Why might a company's cost of equity fall when its shares become more liquid, even though the company itself has not changed?

<details><summary>Answer</summary>

Because **liquidity is a component of the required return** (QM LM1).

Investors demand a **liquidity premium** as compensation for the difficulty and cost of exiting a position at fair value. An illiquid security carries wider spreads, greater price impact, and the risk of being unable to sell at all in stressed conditions — real costs that must be compensated.

When liquidity improves — through index inclusion, a larger float, an uplisting to a major exchange, or growing institutional coverage — that premium **shrinks**. The required return falls, and since price is the discounted value of unchanged cash flows at a lower discount rate, the **share price rises**.

This is why companies pursue index inclusion and major-exchange listings, and why the announcement of index addition typically produces a positive price reaction: nothing about the business changed, but the cost of its equity did.

</details>

**4.** A company undertakes a rights offering at a 20% discount to market. Is an existing shareholder harmed?

<details><summary>Answer</summary>

**Not if they exercise the rights.** A rights offering gives existing holders the right to buy new shares **pro rata**, so a holder who subscribes in full maintains exactly their proportional ownership — **no ownership dilution**.

The share price will fall toward the theoretical ex-rights price, because new shares were issued below market and the pre-existing value is now spread over more shares. But the shareholder's **total wealth** is unchanged: the fall in the value of their existing holding is offset by the discount they capture on the new shares.

**A shareholder who does not exercise is harmed** — they suffer the price decline and the ownership dilution with no offsetting benefit. In most jurisdictions rights are tradeable, so a holder who cannot or will not subscribe should **sell the rights**, capturing their value rather than letting them lapse.

The distinction the exam tests: rights offerings protect against **ownership** dilution, not against a **price** decline.

</details>

---

## Done when

- [ ] I can distinguish primary from secondary markets and say why secondary liquidity matters to issuers
- [ ] I can describe six primary market mechanisms including which raise capital
- [ ] I can state the market vs limit order trade-off and when each is appropriate
- [ ] I can compute float and average daily volume and explain why float drives index weighting
- [ ] I can name five liquidity measures and explain the liquidity premium's effect on price
- [ ] I can explain what a rights offering protects against and what it does not
- [ ] I can name seven index categories and explain why no index is neutral
- [ ] I answered the self-check cold, several days after first study

---

← [LM02 Equity Jurisdictions, Classes, and the Voting Process](lm-02-equity-jurisdictions-classes-and-the-voting-process.md)  ·  [Topic index](README.md)  ·  [LM04 Sources of Equity Returns](lm-04-sources-of-equity-returns.md) →
