# BA II Plus — Setup and Exam Drills

Only two calculators are permitted: the **Texas Instruments BA II Plus** (including the
Professional) and the **HP 12C**. This guide covers the BA II Plus, which the large majority of
candidates use. If you use the 12C, the concepts map over but the keystrokes do not.

> **Do this in week 1.** Not in month 4. A calculator you fight with costs you 10–15 questions'
> worth of time across two sessions, and every one of those is a guessed answer.

---

## One-time setup (do it now)

### 1. Decimal places → 9 (floating)

```
[2ND] [FORMAT]  →  9  [ENTER]  →  [2ND] [QUIT]
```

Default is 2 decimal places, which silently rounds your intermediate results. Set it to 9 and
round only at the end. This alone eliminates a category of "my answer is close to option B but not
exactly" problems.

### 2. Payments per year → 1

```
[2ND] [P/Y]  →  1  [ENTER]  →  [2ND] [QUIT]
```

Default is 12. Leave it at 1 and handle periodicity yourself by adjusting N and I/Y. Mixing the
two conventions is the single most common calculator error at Level I.

> **Trap:** with P/Y = 1, a 5-year semiannual bond at 6% nominal is **N = 10, I/Y = 3**, not
> N = 5, I/Y = 6. Do the conversion in your head, every time, out loud if it helps.

### 3. Know your two clears

| Keys | Clears | Use when |
| --- | --- | --- |
| `[2ND] [CLR TVM]` | N, I/Y, PV, PMT, FV | Between every TVM question |
| `[2ND] [CLR WORK]` | The worksheet you are currently in (CF, DATA, etc.) | Between every cash-flow or statistics question |
| `[CE/C]` twice | The display and pending operation | Mid-calculation typo |

**Leftover values from the previous question are the #1 source of wrong answers on this machine.**
Build the reflex: new question → clear.

### 4. Chain vs. AOS

```
[2ND] [FORMAT]  →  ↓ ↓ ↓ ↓  →  [2ND] [SET]  to toggle Chn / AOS
```

**Chn** (chain) evaluates strictly left to right: `2 + 3 × 4 = 20`.
**AOS** respects operator precedence: `2 + 3 × 4 = 14`.

Pick one and never change it. Most candidates prefer **Chn** because it matches how you read a
formula aloud, and it forces you to use parentheses deliberately. Whichever you choose, know which
one you are in — it changes answers.

---

## The five worksheets you actually need

### TVM — the workhorse

Keys: `N`, `I/Y`, `PV`, `PMT`, `FV`, plus `CPT` to solve.

**Sign convention is the whole game.** Money in is positive, money out is negative. If PV and FV
have the same sign, the calculator returns `Error 5` when solving for I/Y — that error message is
telling you your signs are wrong, not that the question is broken.

```
Bond: 5 years, semiannual, 6% coupon, 8% YTM, par 1000. Price?
  N = 10        (5 × 2)
  I/Y = 4       (8 / 2)
  PMT = 30      (1000 × 6% / 2)
  FV = 1000
  CPT PV  →  -918.89     →  price is 918.89
```

The negative sign is correct and expected: you pay out 918.89 to receive the coupons and par.

`[2ND] [BGN]` switches to annuity-due (payments at the start of each period) — an annuity due is
worth more. `[2ND] [SET]` toggles, `[2ND] [QUIT]` exits. **Always check the BGN indicator is off**
before an ordinary-annuity question.

### CF / NPV / IRR — capital allocation

```
[CF] [2ND] [CLR WORK]
  CF0 = -1000  [ENTER] ↓
  C01 = 300    [ENTER] ↓
  F01 = 3      [ENTER] ↓      ← F = frequency, how many times in a row
  C02 = 500    [ENTER] ↓
  F02 = 1      [ENTER]
[NPV]  I = 10 [ENTER] ↓  CPT   →  NPV
[IRR]  CPT                      →  IRR
```

The **F (frequency)** register is where people lose marks — it means "this exact cash flow repeats
F times consecutively", not "this cash flow occurs in year F". Used well it is a large time-saver
on Corporate Issuers questions.

> **Trap:** a cash flow of zero in a year must still be entered as `C0n = 0, F0n = 1`. Skipping it
> shifts every subsequent flow one period earlier.

### DATA / STAT — descriptive statistics and regression

```
[2ND] [DATA] [2ND] [CLR WORK]
  X01 = ...  [ENTER] ↓  Y01 = ...  [ENTER] ↓   (repeat)
[2ND] [STAT]
  [2ND] [SET] to choose:  1-V (one variable)  or  LIN (linear regression)
  ↓ ↓ to scroll:  n, x̄, Sx (sample SD), σx (population SD), ȳ, Sy, σy, a, b, r
```

For QM this gives you mean, sample and population standard deviation, and — in LIN mode — the
regression intercept `a`, slope `b`, and correlation `r` directly. Learning LIN mode saves
substantial time on the Simple Linear Regression module.

> **Trap:** `Sx` is the *sample* standard deviation (divides by n−1); `σx` is the *population*
> standard deviation (divides by n). The exam will hand you a sample and expect `Sx`. Reaching for
> the wrong one gives an answer that is plausibly close — which is exactly how it gets past you.

### Percent change / compound growth — `[2ND] [Δ%]`

Occasionally faster than TVM for simple growth-rate questions, but TVM does everything it does.
Skip it if you're short on setup time.

### Depreciation, Bond, Breakeven worksheets

`[2ND] [DEPR]`, `[2ND] [BOND]`, `[2ND] [BRKEVN]` exist and work. **Deliberately do not learn them.**
Every Level I question they solve is solvable with TVM or plain arithmetic, and each worksheet adds
another set of settings to get wrong under time pressure. Fewer tools, better reflexes.

---

## Memory registers — the underrated feature

```
[STO] 1      store the displayed value in register 1   (registers 0–9)
[RCL] 1      recall it
```

Use these for multi-step problems: store the intermediate result instead of writing it down and
re-typing it. Fewer transcription errors, and you keep full precision instead of the 4 digits you
copied onto the board.

---

## Speed drills

Do these until each is automatic. Target times assume you've done the setup above.

| Drill | Target | Covers |
| --- | --- | --- |
| Price a semiannual bond from N/I/Y/PMT/FV | 25 s | Fixed Income, constantly |
| Solve for I/Y given price (i.e. find YTM), then ×2 | 30 s | Fixed Income |
| NPV and IRR of a 5-flow project with one repeat | 60 s | Corporate Issuers |
| Mean + sample SD of 8 numbers via DATA/STAT | 45 s | Quantitative Methods |
| Slope, intercept, and r via LIN mode | 60 s | Quantitative Methods |
| PV of a growing perpetuity (plain arithmetic, no worksheet) | 15 s | Equity |
| FV of an annuity due (BGN on, then **off** again) | 30 s | Quantitative Methods |
| Effective annual rate from a nominal rate, m = 4 | 20 s | Quantitative Methods, Fixed Income |

Run the full set once a week from Month 2. It takes six minutes and it keeps the reflexes alive.

---

## Exam-day calculator checklist

- [ ] Fresh batteries installed **the week before** — not the night before
- [ ] A second permitted calculator in your bag (allowed, and cheap insurance)
- [ ] Decimals set to 9
- [ ] P/Y = 1
- [ ] Chn/AOS set to your choice and verified
- [ ] BGN indicator **off**
- [ ] Calculator cover in your bag — some centres require the case be left with your belongings;
      check the current Candidate Bulletin for the rules in force

---

## Errors, decoded

| Message | What it actually means |
| --- | --- |
| `Error 5` | Solving for I/Y with no sign change in the cash flows. Your PV/FV/PMT signs are wrong. |
| `Error 4` | A register is out of range (e.g. N too large, or a frequency ≤ 0). |
| `Error 7` | Iteration limit hit — usually an IRR problem with multiple sign changes and no real solution. |
| An answer that's *nearly* right | Almost always: decimals set to 2, P/Y set to 12, BGN left on, or a stale register you forgot to clear. |

That last row is worth internalising. When your answer is close but not equal to any option, the
problem is nine times out of ten a *setting*, not your finance.
