# FSA · LM12 — Introduction to Financial Statement Modeling

## At a glance

| | |
| --- | --- |
| **Topic** | Financial Statement Analysis (11-14% of the exam) |
| **Hours budgeted** | 4 |
| **Prerequisites** | LM11 (ratios and DuPont). This is the capstone of the FSA block. |
| **Where it shows up** | 1–2 questions, and it is the direct bridge into Equity LM8. Conceptual rather than computational. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- demonstrate the development of a sales-based pro forma company model
- explain how behavioral factors affect analyst forecasts and recommend remedial actions for analyst biases
- explain how the competitive position of a company based on a Porter's five forces analysis affects prices and costs
- explain how to forecast industry and company sales and costs when they are subject to price inflation or deflation
- explain considerations in the choice of an explicit forecast horizon and an analyst's choices in developing projections beyond the short-term forecast horizon

---

## Core concepts

### The sales-based pro forma model

Everything keys off revenue. Build in this order and the model stays internally consistent.

| Step | What you do | Anchor |
| --- | --- | --- |
| 1 | **Forecast revenue** | Top-down (market size × share) or bottom-up (volume × price, or units × ASP by segment) |
| 2 | **Forecast COGS and gross margin** | Common-size % of revenue, adjusted for known input-cost and mix changes |
| 3 | **Forecast operating expenses** | Split **fixed** vs **variable** — variable scales with revenue, fixed does not |
| 4 | **Forecast working capital** | Hold DOH, DSO, and days payables constant unless there is a stated reason to change them |
| 5 | **Forecast capex and depreciation** | Off fixed asset turnover, the existing asset base's age, and stated plans |
| 6 | **Forecast the capital structure** | Debt schedule → interest expense; then tax rate → net income |
| 7 | **Derive the cash flow statement** | From the forecast income statement and balance-sheet movements |
| 8 | **Sensitivity-test** | Flex the two or three assumptions the answer actually depends on |

**Top-down vs. bottom-up:**

- **Top-down** starts with the economy or the industry, then applies a market share assumption.
  Better for cyclical and commodity businesses, and for sanity-checking whether an implied share is
  plausible.
- **Bottom-up** builds from the company's own units — stores, customers, subscribers, segments —
  and aggregates. Better where you have granular disclosure, and it forces you to be specific.
- **A hybrid is standard**: build bottom-up, then check the result against the top-down market size.
  If your bottom-up forecast implies the company will take 60% of a market where it has 22%, the
  model is wrong regardless of how carefully each line was built.

**The fixed/variable cost split is the highest-value modelling decision.** A business with mostly
fixed costs has high **operating leverage**: a 10% revenue increase produces a much larger profit
increase, and a 10% decline is brutal. Modelling all costs as a constant percentage of revenue
silently assumes zero operating leverage — and produces forecasts that are systematically wrong in
both directions.

### Forecasting under inflation and deflation

The core question: **can the company pass input-cost changes through to customers?** That is a
function of competitive position, which is why the Porter LOS sits in this module.

| Situation | Effect |
| --- | --- |
| Input costs rise, **full** pass-through | Revenue and costs both rise; **gross margin % is preserved**, absolute gross profit rises |
| Input costs rise, **partial** pass-through | Margin compresses. Typical for commoditised products and weak brands |
| Input costs rise, pass-through with a **lag** | Margin dips, then recovers. Common with contracted or list pricing |
| **Deflation** in inputs, competitive market | Prices fall too; margin roughly preserved, revenue falls |
| **Deflation** in inputs, strong market position | Prices held; **margin expands** |

Practical points:

- Separate **volume growth from price growth** in the revenue forecast. A 9% revenue increase that
  is 8% price and 1% volume is a very different business from 1% price and 8% volume — and in an
  inflationary period, only the second is real growth.
- Watch the **inventory cost-flow method** interaction: in inflation, **FIFO** reports lower COGS
  and higher margin than **LIFO** (FSA LM6). Cross-company margin comparisons in an inflationary
  period are meaningless without adjusting for this.
- Consider **input-specific** rather than general inflation. A packaging company cares about resin
  and energy prices, not CPI.

### Porter's five forces and its effect on prices and costs

The LOS is specifically about how competitive position **affects prices and costs** — so map each
force to a line in the model.

| Force | High force means | Effect on the model |
| --- | --- | --- |
| **Threat of new entrants** | Low barriers to entry | Caps long-run prices and margins; assume reversion |
| **Threat of substitutes** | Close alternatives exist | Caps pricing power; limits price-led revenue growth |
| **Bargaining power of buyers** | Concentrated, price-sensitive customers | Pressures **prices** → lower gross margin |
| **Bargaining power of suppliers** | Few suppliers, high switching costs | Raises **input costs** → lower gross margin |
| **Industry rivalry** | Many similar competitors, high fixed costs, slow growth | Price competition; margin compression |

The translation to modelling is direct: **strong competitive position → sustained pricing power →
you can forecast stable or expanding margins.** Weak position → assume margin **reversion toward the
industry mean**, because competition will compete away abnormal returns.

> A forecast of permanently expanding margins in a fragmented, low-barrier industry is not a
> forecast — it is a hope. The five forces are the discipline that stops you making it.

### Behavioural biases in forecasting — and the remedies

The LOS asks you to **recommend remedial actions**, so learn the pairs, not just the biases.

| Bias | How it shows up | Remedy |
| --- | --- | --- |
| **Overconfidence** | Forecast ranges far too narrow; too much precision | Widen intervals; track your own historical hit rate |
| **Illusion of control** | Believing more detail in the model means more accuracy | Focus on the 2–3 assumptions that drive the answer; test sensitivity |
| **Conservatism** | Under-reacting to new information; clinging to a prior forecast | Force a formal review on each new data point; pre-commit to what would change your mind |
| **Representativeness** | Over-extrapolating a short run of good (or bad) results | Use longer histories; check base rates for the industry |
| **Confirmation** | Seeking data that supports the existing view | Deliberately build the opposing case; seek disconfirming evidence |
| **Anchoring** | Stuck on the prior estimate, or on management's guidance | Re-derive from primary drivers before looking at the old model |
| **Availability** | Over-weighting recent or vivid events | Use structured, systematic data rather than salience |
| **Management guidance bias** | Treating guidance as the base case | Build your own forecast first, *then* compare |

The general remedy underneath all of them: **a structured, documented process, applied consistently,
with the assumptions written down and revisited.** A model whose assumptions are explicit can be
challenged; one where they are buried in cell formulas cannot.

### Choosing the forecast horizon

| Consideration | Implication |
| --- | --- |
| **Investment horizon** | Match the forecast period to how long you intend to hold |
| **Cyclicality** | The explicit period must span a **full cycle**, or you bake the current phase into perpetuity |
| **Business maturity** | High-growth companies need longer explicit periods, until growth normalises |
| **Portfolio turnover** | High-turnover strategies need less distant detail |
| **Visibility** | Contracted revenue (utilities, long-term contracts) supports longer horizons; fashion retail does not |

Typical explicit horizons run **3 to 10 years**, with 5 as the common default — long enough to reach
a normalised state, short enough that the assumptions mean something.

**Beyond the explicit horizon** you have three options:

1. **A terminal value** based on a perpetuity growth rate, which must be no higher than long-run
   nominal GDP growth. Anything above that implies the company eventually becomes the whole economy.
2. **A terminal multiple** (EV/EBITDA, P/E) based on where mature peers trade.
3. **A normalised earnings level** that averages through the cycle, for cyclical businesses where
   any single year is unrepresentative.

> The discipline that matters: **the terminal value often accounts for 60–80% of the total valuation.**
> An analyst who spends four weeks on the explicit five years and ten minutes on the terminal
> assumption has mis-allocated effort by an order of magnitude. Sensitivity-test the terminal growth
> rate and the terminal multiple before anything else.

---

## Formulas to know cold

```
Revenue forecast (top-down)   = Industry size × Market share
Revenue forecast (bottom-up)  = Σ (Units × Average selling price), by segment or product
Revenue growth decomposition  = (1 + volume growth) × (1 + price growth) − 1

Variable cost forecast = Variable cost % × Forecast revenue
Fixed cost forecast    = Prior fixed costs × (1 + inflation), independent of revenue

Working capital, held at current efficiency:
    Receivables = DSO × Revenue / 365
    Inventory   = DOH × COGS / 365
    Payables    = Days payables × Purchases / 365

Terminal value (perpetuity growth) = CF_(n+1) / (r − g),   with g ≤ long-run nominal GDP growth
Terminal value (exit multiple)     = Terminal-year metric × Peer multiple
```

---

## Exam traps

> **Trap 1 — Modelling all costs as a percentage of revenue.** That assumes **zero operating
> leverage** and gets both upside and downside wrong. Split fixed from variable.

> **Trap 2 — Confusing price growth with volume growth.** In an inflationary period, revenue growth
> can be entirely price. Decompose it.

> **Trap 3 — Assuming full cost pass-through by default.** Pass-through depends on competitive
> position — which is what the five forces assess.

> **Trap 4 — Terminal growth above long-run nominal GDP.** Mathematically it implies the company
> eventually exceeds the size of the economy. It is always wrong.

> **Trap 5 — Anchoring on management guidance.** Build your own forecast **first**, then compare.
> Starting from guidance means you are forecasting management's forecast.

> **Trap 6 — Mistaking model detail for accuracy.** A 40-tab model with the same weak revenue
> assumption is not better than a one-page model with the same assumption. This is the *illusion of
> control*.

> **Trap 7 — An explicit horizon shorter than the business cycle.** For a cyclical company, a 3-year
> forecast from a peak bakes peak conditions into the terminal value.

> **Trap 8 — Ignoring inventory cost-flow methods when comparing margins in inflation.** FIFO vs
> LIFO changes reported margin with no economic difference (FSA LM6).

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A company's revenue grew 11%. Volume grew 2% and prices rose 9%. Input costs rose 12% and the company has weak pricing power in a fragmented market. What happens to gross margin, and what do you forecast for next year?

<details><summary>Answer</summary>

Input costs (+12%) rose faster than prices (+9%), so **gross margin compresses** — pass-through was partial.

Real (volume) growth is only **2%**; almost all the revenue growth is price, which is not a sign of demand strength.

Forecast: in a **fragmented market with weak pricing power**, assume margin continues under pressure and reverts toward the industry mean. Do not extrapolate 11% revenue growth — if inflation moderates, the price component collapses and revenue growth drops toward 2–3%. Model volume and price as separate lines so this is visible.

</details>

**2.** Why does the fixed/variable cost split matter more than almost any other modelling decision?

<details><summary>Answer</summary>

It determines **operating leverage** — the sensitivity of profit to revenue.

With a high fixed-cost base, a 10% revenue rise produces a much larger percentage rise in operating profit (fixed costs are spread over more revenue), and a 10% fall is correspondingly severe. Modelling every cost as a constant percentage of revenue assumes profit scales **linearly** with revenue, which is true of almost no real business.

The practical consequence: a fixed-percentage model understates upside in a recovery and understates downside in a downturn — it is wrong in both directions, which is worse than being wrong in one.

</details>

**3.** List the five forces and say which line of the income statement each primarily pressures.

<details><summary>Answer</summary>

1. **Threat of new entrants** → caps long-run **prices and margins** (forces reversion)
2. **Threat of substitutes** → caps **prices** / revenue growth
3. **Bargaining power of buyers** → pressures **prices** → gross margin
4. **Bargaining power of suppliers** → raises **input costs (COGS)** → gross margin
5. **Industry rivalry** → **price competition** and higher operating spend (marketing, discounting) → operating margin

Buyers and suppliers squeeze gross margin from opposite ends; entrants and substitutes cap how long any abnormal margin can persist; rivalry determines how hard the fight is right now.

</details>

**4.** A cyclical steel producer is at a cyclical peak. What horizon and terminal approach would you use, and why?

<details><summary>Answer</summary>

Use a **long explicit horizon — at least a full cycle, typically 7–10 years** — so the forecast spans both the peak and a trough. A 3-year model from a peak carries peak margins straight into the terminal value.

For the terminal value, use **normalised mid-cycle earnings** rather than terminal-year earnings: average margins and volumes across a full historical cycle, applied to a normalised capacity assumption. Alternatively, use a **mid-cycle exit multiple** on normalised EBITDA.

The error to avoid is capitalising peak earnings at a peak multiple — the classic way cyclical businesses get overvalued at exactly the wrong moment.

</details>

**5.** An analyst has forecast 20% growth for three years. Growth comes in at 6%, and the analyst revises to 18%. Which bias is this, and what is the remedy?

<details><summary>Answer</summary>

**Conservatism bias** — under-reacting to new information and clinging to a prior view. Possibly compounded by **anchoring** on the original 20% figure.

Remedies: (1) **re-derive the forecast from primary drivers** (volume, price, market share) *without* opening the previous model; (2) pre-commit in writing to what evidence would falsify the thesis, before the data arrives; (3) impose a formal review triggered by each earnings release; (4) track your own forecast errors over time — a personal hit-rate record is the most effective single corrective for both conservatism and overconfidence.

</details>

**6.** Why must the terminal growth rate not exceed long-run nominal GDP growth?

<details><summary>Answer</summary>

Because a company growing faster than the economy **forever** would eventually become larger than the entire economy — mathematically impossible. The perpetuity growth rate is a statement about the indefinite future, not the next decade.

Practically: terminal value frequently represents 60–80% of a DCF's total value, and it is extremely sensitive to `g` in the `CF/(r − g)` denominator. A `g` of 4% versus 2% with `r` = 8% changes the terminal value by 50%. This is why sensitivity-testing `g` matters more than refining year-4 SG&A.

</details>

**7.** Your bottom-up model implies the company's revenue will grow from 22% to 41% market share in five years. What do you do?

<details><summary>Answer</summary>

**Stop and reconcile against the top-down view.** A near-doubling of share in a mature market requires a specific, defensible mechanism: a structural cost advantage, a patent, a network effect, a distribution lock-up, or competitor exit.

If you cannot name the mechanism and explain why incumbents cannot respond, the bottom-up build has compounded optimistic assumptions line by line — each individually plausible, collectively impossible. Revisit the per-segment growth rates.

This cross-check is the main reason to build both ways. Bottom-up models fail silently; the top-down check is what catches them.

</details>

---

## Done when

- [ ] I can lay out the eight steps of a sales-based pro forma model in order
- [ ] I can explain when top-down beats bottom-up, and why a hybrid cross-check is standard
- [ ] I can split costs into fixed and variable and explain the operating leverage consequence
- [ ] I can decompose revenue growth into price and volume and say why it matters in inflation
- [ ] I can map each of Porter's five forces to the income statement line it pressures
- [ ] I can name six forecasting biases and state a specific remedy for each
- [ ] I can choose a forecast horizon for a cyclical company and justify the terminal approach
- [ ] I can state why terminal growth is capped at long-run nominal GDP growth
- [ ] I answered the self-check cold, several days after first study

---

← [LM11 Financial Analysis Techniques](lm-11-financial-analysis-techniques.md)  ·  [Topic index](README.md)
