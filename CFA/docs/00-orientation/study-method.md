# The Study Method Behind This Plan

This file explains *why* the plan is shaped the way it is. Read it once, at the start. If you
understand the reasoning you will make better calls when the plan meets reality — and it will.

---

## 1. Why this study order?

The curriculum is printed in a conventional order (Quants → Economics → FSA → …). This plan
deliberately departs from it. Each move has a reason.

### FSA first (Month 1, 80 hours)

Financial Statement Analysis is the **prerequisite topic that isn't labelled as one**. Equity
valuation asks you to forecast financial statements. Corporate Issuers asks you to compute a cash
conversion cycle and a WACC off reported figures. Fixed Income credit analysis asks you to compute
leverage and coverage ratios from the same statements. If you learn FSA last, you spend three other
topics faking a foundation you don't have.

It is also the topic with the highest *front-loading benefit*: it is 11–14% of the exam on its own,
and it decays slowly because it is procedural rather than definitional.

### Quantitative Methods, split in two

QM is the only topic in this plan that is deliberately cut in half, and the split point is exact:

- **LM1–LM5 in Month 1 (40 hours).** Returns, types of returns, benchmarking, time value of money,
  and the statistical characteristics of returns. These are *tools*. Discounting in particular is
  load-bearing for Equity, Fixed Income, Corporate Issuers, and Derivatives. Learning these late
  would be like learning arithmetic in the last week.
- **LM6–LM11 in Month 5 (80 hours).** Distributions, hypothesis testing, portfolio risk/return,
  simulation, regression, and financial data science. These are *heavy, abstract, and fast-fading*.
  Studied in Month 1 they'd be forgotten by exam day. Studied in Month 5 they are fresh, and by
  then you have real assets and real portfolios to hang the statistics on — which is the difference
  between memorising a t-test and understanding one.

The double hour allocation on the second half (80 hours for 6 modules vs 40 for 5) is not a typo.
Hypothesis testing and simple linear regression are the two most reliably difficult modules at
Level I, and they sit in that block.

### Economics late (Month 5, 40 hours)

Economics is broad, largely *descriptive*, and only 6–9% of the exam. It is the topic most tolerant
of being learned fast and recently — most of its LOS use the verbs *describe* and *explain*, which
reward recency, not depth of practice. Putting it in Month 5 keeps it fresh. The one calculation-
heavy module (Exchange Rate Calculations) is the exception, and the schedule gives it explicit
drill time.

### Ethics in parallel, every day, all 150 days

This is the most important design choice in the plan.

- Ethics is **15–20%** — the largest single topic on the exam.
- It is the **official tie-breaker**: borderline candidates are decided on their Ethics band.
- And crucially, it does **not** reward cramming. Ethics questions are scenario-based. You are not
  asked to recite Standard III(B); you are asked whether a described action violates it. That skill
  is pattern recognition built by repeated exposure to *many different scenarios over time*. One
  hour a day for 150 days beats a 150-hour block, by a wide margin.

One hour a day, every day, from day one. Non-negotiable.

---

## 2. The daily shape

```
┌───────────────────────────────────────────────────────┐
│  5 hours/day × 150 days = 750 hours                   │
├───────────────────────────────────────────────────────┤
│  Hour 1   Core topic — new material                   │
│  Hour 2   Core topic — new material                   │
│  Hour 3   Core topic — worked problems                │
│  Hour 4   Core topic — questions, timed               │
│  Hour 5   ETHICS (always, no exceptions)              │
└───────────────────────────────────────────────────────┘
```

Two rules about this block:

**The 50/10 rule.** 50 minutes of work, 10 minutes off, genuinely off — not a screen. Five of these
is a study day. Attempting 5 unbroken hours produces roughly 3 hours of real learning.

**Hours 3 and 4 are not optional.** The single most common failure mode is spending all four core
hours reading and none answering. Reading produces *familiarity*, which feels like knowledge and
isn't. If you are behind, cut reading time, not question time.

---

## 3. The three-pass structure

Each learning module gets three passes, spread over time. Not three readings in one sitting.

| Pass | When | What you do | Output |
| --- | --- | --- | --- |
| **Pass 1 — Encode** | The scheduled day | Read the module notes with the LOS list open beside you. Work every example by hand. | Filled-in notes; formulas written out once, by hand |
| **Pass 2 — Retrieve** | 3–7 days later | Close the notes. Answer the module's self-check questions cold. Then the topic's end questions. | A score, and an entry in `weak-areas.md` for everything missed |
| **Pass 3 — Consolidate** | In the revision phase | Re-do only your logged weak areas + a timed mixed set | Weak-area entries closed out |

Pass 2 is where the learning actually happens. **Retrieval, not review.** The act of dragging an
answer out of memory without cues is what builds durable recall; re-reading a highlighted page
builds only the illusion of it.

### Spacing schedule

After Pass 1 on a module, the review intervals are: **Day +1 (quick), +7, +21, +60**. Those touches
are short — 10 to 20 minutes of self-check questions, not a re-read. The revision phase in Month 5
is engineered so the +60 touches land there naturally.

---

## 4. How to read a learning module

1. **Read the LOS first.** All of them, before the content. They are the specification. Content that
   doesn't serve an LOS is context, not testable material.
2. **Match the verb to the effort** (see `exam-overview.md`). *Calculate* → drill. *Describe* →
   bullets from memory. *Compare* → a two-column table.
3. **Work every formula by hand once**, then on the calculator until it's automatic. Writing it out
   once encodes it; the calculator makes it fast.
4. **Close the loop.** The module isn't finished until its "Done when" list is fully ticked and the
   self-check questions are answered cold.

---

## 5. Questions: how many, and when

| Phase | Target |
| --- | --- |
| Months 1–2 | ~30 questions per module, immediately after study |
| Month 3 | Add a weekly 60-question mixed set drawn from everything covered so far |
| Month 4 | 2 full topic tests per week + Mock #1 at the end of the month |
| Month 5 | Mocks #2–#5, spaced. Every mock fully reviewed *before* the next one |

**The review is worth more than the mock.** Budget 2–3 hours to review a 4.5-hour mock. For every
wrong answer, write in `weak-areas.md` which of these four it was:

- **(K) Knowledge gap** — didn't know it → back to the module
- **(A) Application error** — knew it, misapplied it → more questions on that LOS
- **(C) Careless** — misread the stem, wrong sign, wrong units → a process fix, not a study fix
- **(T) Time** — guessed because the clock ran out → a pacing fix

These four have four completely different remedies. Lumping them together as "I got it wrong" is
how candidates re-study material they already know while never fixing their real problem.

---

## 6. When you fall behind — and you will

Something will go wrong: a work crunch, illness, a week that evaporates. The plan has to survive it.

**Triage rules, in order:**

1. **Never cut Ethics.** The one hour a day holds, even on a half-day.
2. **Cut reading before questions.** If a module was budgeted 8 hours and you have 4, do 2 hours of
   notes and 2 of questions — not 4 of notes.
3. **Cut by weight.** If a whole block must shrink, take the time out of the lowest-weight topic
   ahead of you (Derivatives 5–8%, Economics 6–9%), never out of FSA, Equity, Fixed Income, or Ethics.
4. **Do not skip a module outright.** A 60-minute skim of a module's LOS + formulas + traps is worth
   far more than zero, and protects you from being blanked on 4 questions.
5. **Never restart the plan.** Restarting means re-studying what you already know. Rejoin at the
   current calendar date and pick up the missed material in the revision phase.

---

## 7. What "done" means

A module is done when every box in its **Done when** section is ticked. Not when the hours are
spent, not when you've read it, not when it feels familiar. If you can't do the "Done when" list,
the honest move is to leave it unticked in `trackers/progress-tracker.md` and come back — a tracker
you've lied to is worse than no tracker at all.
