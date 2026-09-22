# CI · LM05 — Capital Investments and Capital Allocation

## At a glance

| | |
| --- | --- |
| **Topic** | Corporate Issuers (6-9% of the exam) |
| **Hours budgeted** | 12 |
| **Prerequisites** | QM LM4 (time value of money). BA II Plus CF/NPV/IRR worksheet. |
| **Where it shows up** | 3 questions — the largest allocation in Corporate Issuers. NPV and IRR are certainties. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe types of capital investments
- describe the capital allocation process, calculate net present value (NPV), internal rate of return (IRR), and return on invested capital (ROIC), and contrast their use in capital allocation
- describe principles of capital allocation and common capital allocation pitfalls
- describe types of real options relevant to capital investments

---

## Core concepts

### Types of capital investment

| Type | Purpose | Analytical treatment |
| --- | --- | --- |
| **Maintenance / going concern** | Replace worn-out assets; stay in business | Often mandatory. Compare alternatives on cost |
| **Expansion** | Grow capacity or enter new markets | Full NPV analysis. The highest-uncertainty category |
| **Regulatory / compliance / safety** | Required by law | Not optional. Choose the lowest-cost compliant option |
| **Other** | R&D, strategic, exploratory | Hardest to quantify; often best framed as a **real option** |

The distinction matters because it changes the decision rule. A compliance project is a
cost-minimisation problem, not an NPV-maximisation one — the alternative is not "do nothing", it is
"stop operating".

### The capital allocation process

1. **Generate ideas** — the most valuable and most neglected step; ideas typically come from
   operations, not finance
2. **Analyse individual proposals** — forecast incremental cash flows, compute NPV
3. **Plan the capital budget** — fit projects to available capital and strategic priorities
4. **Monitor and conduct a post-audit** — compare actual results to forecast

> The **post-audit** is the step companies skip, and it is the one that improves the process.
> Comparing outcomes to forecasts identifies systematic bias in the estimates, improves future
> forecasting, and disciplines the people making optimistic projections.

### Net present value

```
NPV = Σ  CFt / (1 + r)^t  −  Initial investment

Accept if NPV > 0.  Among mutually exclusive projects, choose the HIGHEST NPV.
```

NPV is the **increase in shareholder wealth** from accepting the project, measured in today's
currency. It is the theoretically correct criterion, without qualification.

On the BA II Plus: `CF` → `2ND CLR WORK` → CF0 (negative) → C01, F01, C02, F02… → `NPV` → enter I →
↓ → `CPT`.

### Internal rate of return

```
IRR is the discount rate at which NPV = 0:   Σ CFt / (1 + IRR)^t − Investment = 0

Accept if IRR > required rate of return (the hurdle rate).
```

IRR is intuitive — a percentage return — which is why managers prefer it. It is also **wrong more
often than NPV**, in four specific ways:

| Problem | What happens |
| --- | --- |
| **Reinvestment assumption** | IRR implicitly assumes intermediate cash flows are reinvested **at the IRR**. NPV assumes reinvestment at the **cost of capital**, which is realistic. A 40% IRR project does not offer 40% reinvestment opportunities |
| **Multiple IRRs** | A project with **more than one sign change** in its cash flows can have several IRRs, or none. Common with decommissioning costs at the end |
| **Scale** | IRR ignores project size. A 50% return on 1,000 (NPV 300) versus 20% on 100,000 (NPV 12,000) — IRR picks the wrong one |
| **Timing / cash flow pattern** | IRR can rank mutually exclusive projects differently from NPV when cash flow timing differs |

> **The rule:** when NPV and IRR conflict on **mutually exclusive** projects, **always follow NPV**.
> NPV measures value added in currency; IRR measures a rate that may not be achievable on the amount
> that matters.
>
> **The crossover rate** is the discount rate at which two projects have the same NPV. Below it one
> project wins, above it the other. It is found by computing the IRR of the *difference* between the
> two projects' cash flows.

### Return on invested capital

```
ROIC = After-tax operating profit / Average invested capital
     = NOPAT / Average (Debt + Equity)

where NOPAT = EBIT × (1 − tax rate)
```

ROIC measures how efficiently a company converts **all** the capital it employs into operating
profit, independent of how that capital was financed.

> **The comparison that matters:** **ROIC versus WACC**. A company earning ROIC **above** its WACC
> is creating value; **below** it is destroying value, regardless of whether earnings are growing.
> A company growing rapidly at a ROIC below WACC destroys value *faster* the more it grows — which
> is why growth is not automatically good.

### Other criteria, and their limits

| Method | Rule | Problem |
| --- | --- | --- |
| **Payback period** | Years to recover the initial investment | **Ignores the time value of money** and everything beyond the payback date |
| **Discounted payback** | Same, using discounted cash flows | Fixes the TVM problem; still ignores cash flows after payback |
| **Profitability index (PI)** | PV of future cash flows / Initial investment. Accept if PI > 1 | Useful under capital rationing; can conflict with NPV on scale |

PI = 1 + NPV/Investment, so PI > 1 is exactly equivalent to NPV > 0 for accept/reject. They differ
only in **ranking** when capital is constrained.

### Principles of capital allocation

Four rules, each with a matching pitfall:

**1. Decisions are based on cash flows, not accounting income.** Accounting income includes non-cash
items and allocations that do not represent economic reality.

**2. Cash flows are incremental.** Include only what **changes** as a result of the decision.

- **Sunk costs are excluded.** Money already spent is irrelevant — a feasibility study already paid
  for does not belong in the analysis.
- **Opportunity costs are included.** Land the company already owns is not free; its cost is the
  best alternative use (e.g. what it would sell for).
- **Externalities are included.** **Cannibalisation** — a new product taking sales from an existing
  one — is a real incremental cost.

**3. Timing matters.** Cash flows are discounted from when they occur.

**4. Cash flows are analysed on an after-tax basis.** Tax is a real cash outflow.

**5. Financing costs are excluded from the cash flows.** They are captured in the **discount rate**.
Deducting interest from the project's cash flows *and* discounting at WACC double-counts the cost of
debt.

### Common pitfalls

| Pitfall | What it looks like |
| --- | --- |
| **Including sunk costs** | "We've already spent 2m on the study, so we must proceed" |
| **Ignoring opportunity costs** | Treating an owned asset as free |
| **Ignoring cannibalisation** | Forecasting new-product revenue as entirely incremental |
| **Over-optimistic forecasts** | Systematic bias; the reason post-audits matter |
| **Inconsistent treatment of inflation** | Nominal cash flows discounted at a real rate, or vice versa |
| **Using the wrong discount rate** | Applying the company WACC to a project of different risk |
| **Politics and empire-building** | Projects approved on sponsor seniority rather than NPV |
| **Failing to consider alternatives** | Evaluating one option in isolation |
| **Basing decisions on EPS or accounting return** | EPS accretion is not value creation |

> **Two of these are near-certain exam items:** sunk costs must be **excluded**, opportunity costs
> must be **included**. Expect a question that plants both in the same scenario.

### Real options

A **real option** is the flexibility embedded in a capital project — the right, but not the
obligation, to take a future action. Like financial options, real options have value **because
uncertainty exists**, and standard NPV analysis ignores them entirely.

| Real option | The right to | Example |
| --- | --- | --- |
| **Timing (deferral)** | **Wait** and invest later with better information | Delay a mine opening until commodity prices clarify |
| **Sizing — expansion** | **Scale up** if things go well | Build a plant with room to add a second line |
| **Sizing — abandonment** | **Exit** and recover salvage value if things go badly | Sell the assets if the product fails |
| **Flexibility — price setting** | Adjust **price** in response to demand | Dynamic pricing capability |
| **Flexibility — production** | Change **inputs or outputs** | A refinery that switches between crude grades |
| **Fundamental** | The entire project **is** an option | Exploration drilling; drug development trials |

```
Project value including options = NPV (without options) + Value of the real options
```

> **The implication:** a project with a **negative** conventional NPV can still be worth undertaking
> if its embedded options are valuable enough. Early-stage R&D is the canonical case — most
> individual projects have a negative expected NPV, and the portfolio is valuable because a small
> number of them can be scaled enormously. Traditional NPV systematically **undervalues flexibility**.

---

## Formulas to know cold

```
NPV = Σ CFt/(1+r)^t − Initial investment        Accept if NPV > 0
  BA II Plus: CF → CF0, C01/F01, C02/F02… → NPV → I= → ↓ → CPT

IRR: the rate where NPV = 0                     Accept if IRR > hurdle rate
  BA II Plus: same CF entry → IRR → CPT

ROIC = NOPAT / Average invested capital
     = EBIT(1 − t) / Average (Debt + Equity)
  Value created when  ROIC > WACC

Payback period = years to recover the initial outlay   [ignores TVM and later flows]
Discounted payback = same, with discounted flows       [still ignores later flows]

Profitability index  PI = PV of future cash flows / Initial investment
                        = 1 + NPV/Investment            Accept if PI > 1

Project value with flexibility = NPV(without options) + Value of real options
```

---

## Exam traps

> **Trap 1 — Including sunk costs.** Money already spent is **irrelevant** to the decision. Feasibility
> studies, prior R&D, and past marketing spend are all excluded.

> **Trap 2 — Excluding opportunity costs.** An asset the company already owns is **not free**. Its
> cost is the value of the best alternative use.

> **Trap 3 — Ignoring cannibalisation.** Lost sales on an existing product are a **real incremental
> cost** of the new one.

> **Trap 4 — Deducting interest from project cash flows.** Financing cost is captured in the
> **discount rate**. Including it in the cash flows too **double-counts** it.

> **Trap 5 — Following IRR over NPV on mutually exclusive projects.** When they conflict, **NPV
> wins**. IRR's reinvestment assumption and scale-blindness are the reasons.

> **Trap 6 — Missing multiple IRRs.** More than one sign change in the cash flows can produce
> multiple IRRs. Non-conventional cash flow patterns (decommissioning costs) are the usual cause.

> **Trap 7 — Applying the company WACC to a project of different risk.** A higher-risk project
> requires a higher discount rate, or you will systematically over-accept risky projects.

> **Trap 8 — Assuming growth creates value.** Growth at a **ROIC below WACC destroys value faster**.
> Value creation requires ROIC > WACC, not growth.

> **Trap 9 — Ignoring real options.** A negative-NPV project with valuable embedded flexibility may
> still be worth undertaking. Conventional NPV undervalues optionality.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** A project costs 500,000 and generates 150,000 a year for 5 years. The required return is 11%. Compute NPV and IRR, and state the decision.

<details><summary>Answer</summary>

**NPV:** N=5, I/Y=11, PMT=150,000, FV=0 → CPT PV = 554,392.
NPV = 554,392 − 500,000 = **54,392**

**IRR:** N=5, PV = −500,000, PMT = 150,000, FV = 0 → CPT I/Y = **15.24%**

**Decision: accept.** NPV is positive (adds 54,392 to shareholder wealth) and IRR of 15.24% exceeds the 11% hurdle. Both criteria agree — as they always do for a conventional, independent project. They can only conflict on mutually exclusive choices.

</details>

**2.** A company spent 200,000 on a feasibility study. The project requires 1,000,000 of new equipment and will use land the company already owns, which could be sold for 300,000. What is the relevant initial investment?

<details><summary>Answer</summary>

**1,300,000.**

- The 200,000 feasibility study is a **sunk cost** — already spent, unrecoverable, and unaffected by the decision. **Exclude it.**
- The 1,000,000 equipment is a direct incremental outlay. **Include it.**
- The land is **not free**. Using it forgoes the 300,000 it could be sold for — an **opportunity cost**. **Include it.**

This is the most reliably tested combination in the module: one sunk cost to exclude and one opportunity cost to include, in the same scenario.

</details>

**3.** Project A: invest 10,000, NPV 4,000, IRR 35%. Project B: invest 100,000, NPV 12,000, IRR 18%. They are mutually exclusive and the cost of capital is 10%. Which do you choose?

<details><summary>Answer</summary>

**Project B.**

B adds **12,000** to shareholder wealth; A adds 4,000. NPV measures value created in currency, which is what shareholders actually receive.

A's superior IRR is misleading for two reasons:
1. **Scale** — a 35% return on 10,000 produces less value than an 18% return on 100,000. IRR is a rate and ignores the base it applies to.
2. **Reinvestment** — IRR implicitly assumes the intermediate cash flows are reinvested at 35%. If the company had 35% opportunities available for the remaining 90,000, it would take them; the fact that its cost of capital is 10% indicates it does not.

**The rule: on mutually exclusive projects, when NPV and IRR conflict, follow NPV.**

</details>

**4.** EBIT is 840, the tax rate is 25%, and average invested capital is 4,200. WACC is 9.5%. Compute ROIC and assess.

<details><summary>Answer</summary>

NOPAT = 840 × (1 − 0.25) = **630**

ROIC = 630 / 4,200 = **15.0%**

ROIC (15.0%) **exceeds** WACC (9.5%) by 5.5 percentage points → the company is **creating value**. Every unit of capital employed returns more than it costs.

Economic profit = (ROIC − WACC) × Invested capital = 0.055 × 4,200 = **231**.

The important corollary: because ROIC > WACC, **growth creates value here** — reinvesting more capital at 15% against a 9.5% cost adds wealth. Had ROIC been below WACC, growth would have destroyed value faster the more the company invested.

</details>

**5.** A company is considering launching a new product that will generate 5m of revenue, but 1.5m of that will come from customers who would otherwise have bought its existing product. How is this treated?

<details><summary>Answer</summary>

The 1.5m is **cannibalisation** — an **externality** that must be included as an incremental cost.

Only **3.5m** of the revenue is genuinely incremental to the company. More precisely, the incremental analysis should deduct the **lost contribution margin** on the existing product (the 1.5m of revenue less the variable costs no longer incurred), not the full 1.5m of revenue.

Ignoring cannibalisation systematically **overstates NPV** and is one of the most common capital allocation errors in practice, particularly for line extensions.

The counter-argument worth knowing: if a competitor would capture those sales anyway, the sales are lost regardless, and cannibalising yourself is better than being cannibalised. That argument is sometimes legitimate and very often used to wave away a real cost — it requires evidence, not assertion.

</details>

**6.** Name four real options and explain why a project with negative conventional NPV might still be worth undertaking.

<details><summary>Answer</summary>

**Timing (deferral)** — the right to wait and invest later with better information.
**Expansion** — the right to scale up if early results are good.
**Abandonment** — the right to exit and recover salvage value if results are poor.
**Flexibility** — the right to change inputs, outputs, or price in response to conditions.
(Also **fundamental options**, where the whole project is an option — exploration drilling, drug trials.)

**Why negative NPV can still be worth it:** conventional NPV values a project as a fixed, committed plan with a single expected path. It **ignores the value of the decisions you can make later**.

An early-stage R&D project may have a negative expected NPV as a standalone commitment, yet be worth funding because it buys the **right, not the obligation**, to invest heavily if it succeeds — and to abandon cheaply if it does not. The asymmetry (uncapped upside, limited downside) is exactly option value, and it **rises with uncertainty**.

So: `Project value = NPV(committed plan) + Value of embedded options`. Conventional NPV systematically undervalues flexibility, and does so most in precisely the high-uncertainty projects where flexibility is worth most.

</details>

**7.** Why must financing costs be excluded from project cash flows?

<details><summary>Answer</summary>

Because the cost of financing is already captured in the **discount rate**.

The **WACC** is a weighted average of the after-tax cost of debt and the cost of equity. Discounting a project's cash flows at WACC is exactly the operation that charges the project for the capital it uses.

If you also deduct interest expense from the project's cash flows and *then* discount at WACC, you have charged for the debt **twice** — understating NPV and rejecting projects that create value.

The clean separation: **cash flows measure the project's operating economics** (unlevered, after tax); **the discount rate measures the cost of the capital funding it**. Mixing the two is the single most common structural error in project analysis.

</details>

---

## Done when

- [ ] I can compute NPV and IRR on the BA II Plus in under 60 seconds for a 5-flow project
- [ ] I can state all four problems with IRR and why NPV wins on mutually exclusive projects
- [ ] I can compute ROIC and explain the ROIC vs WACC comparison, including what it says about growth
- [ ] I can apply the incremental cash flow principle: exclude sunk costs, include opportunity costs and cannibalisation
- [ ] I can explain why financing costs belong in the discount rate, not the cash flows
- [ ] I can name at least eight capital allocation pitfalls
- [ ] I can name six real options and explain why they make negative-NPV projects potentially worthwhile
- [ ] I answered the self-check cold, several days after first study

---

← [LM04 Working Capital and Liquidity](lm-04-working-capital-and-liquidity.md)  ·  [Topic index](README.md)  ·  [LM06 Capital Structure](lm-06-capital-structure.md) →
