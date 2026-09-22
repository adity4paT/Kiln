# Formula Sheet

**How to use this: cover the right-hand column and reproduce each formula from the prompt.** Friday
is the formula drill day. The whole sheet takes about 25 minutes once you know it; the first few
attempts will take an hour.

Every formula here is one you must be able to write **cold**. If it is on this sheet, it is
memorisation-grade. Anything not here can be re-derived.

---

## Quantitative Methods

| Prompt | Formula |
| --- | --- |
| Holding period return | `HPR = (P1 − P0 + D1) / P0` |
| Chaining returns | `(1+R_total) = (1+R1)(1+R2)...(1+Rn)` |
| Arithmetic mean | `R̄ = ΣR / n` |
| Geometric mean | `RG = [(1+R1)...(1+Rn)]^(1/n) − 1` |
| Harmonic mean | `XH = n / Σ(1/Xi)` |
| Mean ordering | `Harmonic ≤ Geometric ≤ Arithmetic` |
| Volatility drag | `Geometric ≈ Arithmetic − σ²/2` |
| Annualising | `R_annual = (1 + R_period)^(periods per year) − 1` |
| Continuous compounding | `r_cc = ln(1 + HPR) = ln(P1/P0)` |
| Fisher relation (exact) | `Real = (1 + Nominal)/(1 + Inflation) − 1` |
| Required return | `Real risk-free + Expected inflation + Risk premium` |
| **Present value** | `PV = Σ CFt/(1+r)^t` |
| Gordon growth | `V0 = D1/(r − g)`, requires `g < r` |
| Implied return | `r = D1/P0 + g` |
| Implied growth | `g = r − D1/P0` |
| Sustainable growth | `g = b × ROE`, `b = 1 − payout ratio` |
| **Forward rate** | `(1+z_A)^A × (1+F(A,B))^B = (1+z_(A+B))^(A+B)` |
| Forward FX (no-arbitrage) | `F = S × (1 + r_price)/(1 + r_base)` |
| Sample variance | `s² = Σ(xi − x̄)²/(n − 1)` |
| Target semi-deviation | `√[Σ(xi − B)²/(n − 1)]` over `xi < B` only |
| Coefficient of variation | `CV = s / x̄` — **lower is better** |
| Covariance | `Cov(X,Y) = Σ(xi − x̄)(yi − ȳ)/(n − 1)` |
| Correlation | `ρ = Cov(X,Y)/(σx σy)` |
| Skew: mean/median/mode | Positive skew: `Mean > Median > Mode` |
| Excess kurtosis | `Kurtosis − 3`. `> 0` = leptokurtic = **fat tails** |
| Bayes' formula | `P(E\|I) = P(I\|E) × P(E) / P(I)` |
| Total probability | `P(A) = Σ P(A\|Si) P(Si)` |
| Binomial | `P(X=x) = C(n,x) p^x (1−p)^(n−x)`; mean `np`, var `np(1−p)` |
| Standardising | `Z = (X − μ)/σ` |
| Critical values (two-tailed) | 90% → **1.65** · 95% → **1.96** · 99% → **2.58** |
| Standard error | `σ/√n` (σ known) · `s/√n` (σ unknown) |
| Confidence interval | `x̄ ± t(α/2, n−1) × s/√n` |
| Test statistic | `(Sample statistic − Hypothesised)/Standard error` |
| Degrees of freedom | Mean: `n−1` · Regression: `n−2` · χ² independence: `(r−1)(c−1)` |
| **Portfolio variance (2 assets)** | `σp² = w1²σ1² + w2²σ2² + 2w1w2ρ12σ1σ2` |
| GMVP weight (2 assets) | `w1* = (σ2² − Cov)/(σ1² + σ2² − 2Cov)` |
| Utility | `U = E(R) − ½Aσ²` |
| Capital allocation line | `E(Rp) = Rf + [(E(RP) − Rf)/σP] × σp` |
| **OLS slope** | `b1 = Cov(X,Y)/Var(X)`; `b0 = Ȳ − b1X̄` |
| ANOVA | `SST = SSR + SSE`; `R² = SSR/SST`; `SEE = √[SSE/(n−2)]` |
| F-statistic | `F = MSR/MSE`, df `1, n−2`. In simple regression `F = t²` |
| Prediction interval | `Ŷ ± t(α/2,n−2) × sf`, `sf = SEE√[1 + 1/n + (X−X̄)²/Σ(Xi−X̄)²]` |
| Log-log slope | An **elasticity**: 1% ΔX → b1% ΔY |

---

## Financial Statement Analysis

| Prompt | Formula |
| --- | --- |
| **Basic EPS** | `(NI − Preferred dividends)/Weighted average shares` |
| Treasury stock method | `Net new shares = N × (Avg market price − Exercise price)/Avg market price` |
| Antidilution test | Exclude if `ΔNumerator/ΔDenominator > Basic EPS` |
| **Indirect CFO** | `NI + non-cash − gains + losses ± working capital` |
| Working capital signs | Assets **opposite**, liabilities **with** |
| Cash from customers | `Revenue − ΔReceivables + ΔUnearned revenue` |
| Cash to suppliers | `COGS + ΔInventory − ΔPayables` |
| Capex | `Ending gross PP&E − Beginning gross PP&E + Gross cost of disposals` |
| Dividends paid | `Beginning RE + NI − Ending RE` |
| **FCFF** | `CFO + Interest(1−t) − Capex` |
| **FCFE** | `CFO − Capex + Net borrowing` |
| FCFE from FCFF | `FCFF − Interest(1−t) + Net borrowing` |
| **FIFO from LIFO** | Inventory: `+ LIFO reserve` · COGS: `− ΔLIFO reserve` |
| FIFO equity / income | Equity `+ reserve × (1−t)` · Income `+ Δreserve × (1−t)` |
| Straight-line depreciation | `(Cost − Salvage)/Useful life` |
| Double-declining | `(2/Life) × Beginning NBV` — ignores salvage in the rate |
| Gain on disposal | `Proceeds − Carrying amount` |
| Average asset age | `Accumulated depreciation / Annual depreciation` |
| IFRS impairment | `Carrying − max(FV − costs, Value in use)` |
| US GAAP impairment | Step 1: carrying vs **undiscounted** CF · Step 2: loss = carrying − FV |
| Funded status | `Plan assets − PV of benefit obligation` |
| Income tax expense | `Taxes payable + ΔDTL − ΔDTA` |
| DTL arises when | `Taxable income < Accounting profit` |
| Effective tax rate | `Income tax expense / Pre-tax income` |
| Cash tax rate | `Cash taxes paid / Pre-tax income` |
| Inventory turnover | `COGS / Average inventory`; DOH `= 365/turnover` |
| Receivables turnover | `Revenue / Average receivables`; DSO `= 365/turnover` |
| **Cash conversion cycle** | `DOH + DSO − Days of payables` |
| Interest coverage | `EBIT / Interest` |
| **DuPont (3-part)** | `ROE = (NI/Rev) × (Rev/Assets) × (Assets/Equity)` |
| **DuPont (5-part)** | `(NI/EBT)(EBT/EBIT)(EBIT/Rev)(Rev/Assets)(Assets/Equity)` |
| Accruals proxy | `NI − CFO`. High and rising = lower earnings quality |

---

## Corporate Issuers

| Prompt | Formula |
| --- | --- |
| Net working capital | `(CA − Cash) − (CL − Short-term debt)` |
| Cost of trade credit | `[1 + d/(1−d)]^(365/days beyond discount) − 1` |
| Bank discount yield | `(D/F) × (360/t)` — **face value, 360 days** |
| Money market yield | `HPY × (360/t)` |
| Bond equivalent yield | `HPY × (365/t)` |
| Effective annual yield | `(1 + HPY)^(365/t) − 1` |
| Yield ordering | `BDY < MMY < BEY < EAY` |
| **NPV** | `Σ CFt/(1+r)^t − Investment`. Accept if `> 0` |
| Profitability index | `PV of future CF / Investment = 1 + NPV/Investment` |
| **ROIC** | `EBIT(1−t) / Average invested capital` |
| Value creation test | `ROIC > WACC` |
| **WACC** | `wd·rd(1−t) + wp·rp + we·re` — **market weights**, only debt tax-adjusted |
| Cost of preferred | `Dp / Pp` |
| Cost of equity (CAPM) | `Rf + β(E(RM) − Rf)` |
| DOL | `Q(P−V) / [Q(P−V) − F]` |
| DFL | `EBIT / (EBIT − Interest)` |
| DTL | `DOL × DFL` |
| MM I (no taxes) | `V_L = V_U` |
| MM II (no taxes) | `re = r0 + (r0 − rd)(D/E)` |
| MM with taxes | `V_L = V_U + tD` |
| Static trade-off | `V_L = V_U + PV(tax shield) − PV(distress costs)` |

---

## Equity Investments

| Prompt | Formula |
| --- | --- |
| Total return | `(P1 − P0 + D1)/P0` |
| Buyback EPS test | EPS rises if after-tax cost of funds `<` earnings yield (E/P) |
| Buyback BVPS test | BVPS falls if repurchase price `>` BVPS |
| Float | `Shares outstanding − Restricted shares` |
| **Enterprise value** | `Market cap + Debt + Preferred + Minorities − Cash` |
| Pairing rule | EV ↔ **pre-interest** (EBITDA, EBIT, sales) · Equity ↔ **post-interest** |
| Model–rate pairing | DDM & FCFE → `re` · **FCFF → WACC → EV** |
| **Gordon growth** | `V0 = D1/(r − g)` |
| Two-stage | `Σ Dt/(1+r)^t + [D(n+1)/(r−gL)]/(1+r)^n` — discount TV **n** periods |
| **H-model** | `[D0(1+gL) + D0·H·(gS−gL)]/(r − gL)`, `H` = **half** the decline period |
| Preferred stock | `V0 = Dp / r` |
| Justified leading P/E | `payout / (r − g)` |
| Justified trailing P/E | `payout(1+g) / (r − g)` |
| **Justified P/B** | `(ROE − g)/(r − g)` — `P/B > 1 ⟺ ROE > r` |
| Justified P/S | `[net margin × payout × (1+g)]/(r − g)` |
| **CAPM** | `E(Ri) = Rf + βi[E(RM) − Rf]` |
| Beta | `Cov(Ri,RM)/Var(RM) = ρ(i,M) σi/σM` |
| Adjusted beta | `(2/3)raw β + (1/3)(1.0)` |

---

## Portfolio Management

| Prompt | Formula |
| --- | --- |
| Portfolio return | `E(Rp) = Σ wi E(Ri)` — always a weighted average |
| **Portfolio variance** | `w1²σ1² + w2²σ2² + 2w1w2ρ12σ1σ2` |
| ρ = +1 | `σp = w1σ1 + w2σ2` — no diversification |
| ρ = −1 | `σp = \|w1σ1 − w2σ2\|` — can reach zero |
| Capital market line | `E(Rp) = Rf + [(E(RM) − Rf)/σM] × σp` — **total risk, efficient portfolios** |
| **Security market line** | `E(Ri) = Rf + βi[E(RM) − Rf]` — **systematic risk, any asset** |
| Portfolio beta | `βp = Σ wi βi` — **is** a weighted average |
| **Sharpe ratio** | `(Rp − Rf)/σp` — **total** risk, whole portfolio |
| **Treynor ratio** | `(Rp − Rf)/βp` — **systematic** risk, a component |
| M² | `(Rp − Rf)(σM/σp) + Rf` — same ranking as Sharpe |
| **Jensen's alpha** | `Rp − [Rf + βp(RM − Rf)]` |
| Utility | `U = E(R) − ½Aσ²` |
| Five constraints | **L**iquidity · **T**ime horizon · **T**axes · **L**egal · **U**nique |

---

## Fixed Income

| Prompt | Formula |
| --- | --- |
| **Bond price** | `Σ C/(1+r)^t + F/(1+r)^N`. Semiannual: `N×2, I/Y÷2, PMT÷2`, **double the I/Y** |
| Premium / discount | Coupon `>` YTM → premium · Coupon `<` YTM → discount |
| Accrued interest | `Coupon × (days since last / days in period)` |
| Full price | `Flat price + Accrued interest` |
| Day counts | Government **actual/actual** · Corporate **30/360** |
| Periodicity conversion | `(1 + APR_m/m)^m = (1 + APR_n/n)^n` |
| Yield to worst | The **lowest** of YTM and all YTCs |
| Z-spread | Constant spread added to **every spot rate** |
| OAS (callable) | `Z-spread − option cost` → **OAS < Z-spread** |
| FRN price | `DM > QM` → below par · `DM < QM` → above par |
| **Forward rate** | `F(A,B) = [(1+z_(A+B))^(A+B)/(1+z_A)^A]^(1/B) − 1` |
| Curve ordering (upward) | **Forward > Spot > Par** |
| **Macaulay duration** | `Σ[t × PV(CFt)]/Price`. Zero-coupon: `= maturity` |
| **Duration gap** | `MacDur − Horizon`. `>` → price risk · `<` → reinvestment risk |
| **Modified duration** | `MacDur/(1+r)`; `%ΔP ≈ −ModDur × ΔY` |
| Approximate ModDur | `(PV− − PV+)/(2 × ΔY × PV0)` |
| Money duration / PVBP | `ModDur × Full price`; `PVBP = MoneyDur × 0.0001` |
| Approximate convexity | `(PV− + PV+ − 2PV0)/(ΔY² × PV0)` |
| **Price with convexity** | `%ΔP ≈ (−ModDur × ΔY) + (½ × Convexity × ΔY²)` |
| **Effective duration** | `(PV− − PV+)/(2 × ΔCurve × PV0)` — for embedded options |
| Key rate durations | Sum to **effective duration** |
| **Expected loss** | `PD × LGD × Exposure`; `Recovery = 1 − LGD` |
| Credit ratios | `Debt/EBITDA` · `FFO/Debt` (higher better) · `EBIT/Interest` |
| Prepayment risk | Rates **fall** → contraction · Rates **rise** → extension |
| DSCR (CMBS) | `Net operating income / Annual debt service` |

---

## Derivatives

| Prompt | Formula |
| --- | --- |
| **Forward price** | `F0 = S0(1+r)^T + FV(costs) − FV(benefits)` |
| Continuous form | `F0 = S0 e^((r + c − i)T)` |
| Contango / backwardation | `F0 > S0` contango · `F0 < S0` backwardation (convenience yield) |
| **Forward value (long)** | `Vt = St − F0/(1+r)^(T−t)`; short `= −Vt` |
| Futures value | Resets to **zero** after each daily settlement |
| Futures vs forward price | Positive correlation with rates → **futures price higher** |
| Swap rate | `(1 − Z_n)/Σ Z_t` — the **par rate**. Fixed payer gains when rates rise |
| Option payoffs | Call `max(0, ST−X)` · Put `max(0, X−ST)` |
| Breakevens | Call `X + c0` · Put `X − p0` |
| Option value | `Exercise value + Time value` |
| **Six factors** | S↑: call↑ put↓ · X↑: call↓ put↑ · T↑: both↑ · **σ↑: both↑** · r↑: call↑ put↓ · Div↑: call↓ put↑ |
| **Put-call parity** | `c0 + X/(1+r)^T = p0 + S0` |
| Forward parity | `c0 − p0 = (F0 − X)/(1+r)^T`; `F0 = X → c0 = p0` |
| Hedge ratio (delta) | `h = (c+ − c−)/(S+ − S−)` |
| **Risk-neutral probability** | `π = [(1+r) − d]/(u − d)` |
| Binomial value | `c0 = [πc+ + (1−π)c−]/(1+r)` |

---

## Alternative Investments

| Prompt | Formula |
| --- | --- |
| Fee sequence | Gross → − mgmt fee → hurdle (hard/soft) → high water mark → − perf fee |
| Hard vs soft hurdle | Hard: fee on the **excess** · Soft: fee on **all** returns once cleared |
| PIC | `Called / Committed` |
| **DPI** | `Distributions / Paid-in` — **realised** |
| RVPI | `NAV / Paid-in` — **unrealised** |
| **TVPI** | `DPI + RVPI` |
| LBO return sources | Operations + **debt paydown** + multiple expansion |
| **NOI** | `Rental income − Operating expenses` (before financing, tax, depreciation) |
| **Cap rate** | `NOI / Value` — **lower cap rate = higher value** |
| FFO | `NI + Depreciation − Gains on property sales` |
| AFFO | `FFO − Recurring maintenance capex and leasing costs` |
| **Commodity return** | `Spot + Roll + Collateral` |
| Roll return | Contango → **negative** · Backwardation → **positive** |

---

## Economics

| Prompt | Formula |
| --- | --- |
| Profit maximisation | `MR = MC` (all structures) |
| Breakeven / shutdown | Breakeven `P = ATC` · **Shutdown `P < AVC`** |
| **HHI** | `Σ(share as %)²`. `<1500` unconcentrated · `>2500` highly concentrated |
| Fiscal multiplier | `1/[1 − MPC(1−t)]` |
| Fiscal stance | Judge by the change in the **structural** deficit |
| Three lags | Recognition → **Action** → Impact |
| Impossible trinity | Fixed rate · free capital flows · independent policy — **pick two** |
| **% change in a currency** | `(New − Old)/Old` applies to the **base** currency only |
| **Real exchange rate** | `Nominal × (CPI_base / CPI_price)` |
| Marshall–Lerner | `\|export elasticity\| + \|import elasticity\| > 1` |
| Balance of payments | `Current + Capital + Financial = 0` |
| Cross-rate | Arrange so the common currency **cancels**; invert if needed |
| **Covered interest parity** | `F(P/B) = S × (1 + r_price)/(1 + r_base)` — **price rate on top** |
| Forward premium rule | The **higher-rate** currency trades at a **forward discount** |
| Forward points | `Spot + Points/scaling`. **10,000** for 4-decimal · **100** for JPY |

---

## Ethics — the remedy map

*Nothing to calculate. This table is what must be automatic.*

| Prompt | Remedy |
| --- | --- |
| Material non-public information | **ABSTAIN** — II(A). Disclosure does **not** cure |
| Market manipulation | **ABSTAIN** — II(B) |
| Additional compensation from a client | **PRIOR WRITTEN CONSENT**, all parties — IV(B) |
| Independent practice competing with employer | **PRIOR WRITTEN CONSENT** — IV(A) |
| Conflicts of interest | **DISCLOSE** — prominent, plain, effective — VI(A) |
| Referral fees | **DISCLOSE** before any agreement, **both directions** — VI(C) |
| Gift from a client | **DISCLOSE to the employer** — I(B) |
| Personal vs client trades | **PRIORITISE**: client → employer → self — VI(B) |
| Disseminating recommendations | **TREAT FAIRLY** — simultaneous, pro rata — III(B) |
| Basis for a recommendation | **REASONABLE AND ADEQUATE BASIS** — V(A) |
| Supervisory red flag | **INVESTIGATE AND RESTRICT** — IV(C) |
| Ongoing violation | **DISSOCIATE** — I(A). Whistleblowing not required |
| Law vs the Code | Follow the **STRICTER** — I(A) |
| Record retention | **7 years** where regulation is silent — V(C) |
| The designation | **"CFA" is an ADJECTIVE** — "John Smith, CFA" ✓ |
