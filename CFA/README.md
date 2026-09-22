# CFA Level I — 2027 Curriculum · Complete Learning Course

A self-paced, exam-focused course covering the **entire 2027 CFA Level I curriculum**:
102 learning modules across 10 topic areas, sequenced into a **150-day / 750-hour** study plan.

> **Scope note.** This course is a study *scaffold* built from the official 2027 Level I
> Topic Outlines (Learning Outcome Statements). The LOS text is the CFA Institute's; the
> notes, worked logic, traps, and drills here are original study material written to teach
> toward those LOS. It is a companion to — not a replacement for — the official curriculum
> readings, which remain the only authoritative source of testable content.

---

## Start here

| If you want to… | Go to |
| --- | --- |
| Understand the exam and how it's scored | [`docs/00-orientation/exam-overview.md`](docs/00-orientation/exam-overview.md) |
| Learn how to actually use this repo day to day | [`docs/00-orientation/how-to-use-this-course.md`](docs/00-orientation/how-to-use-this-course.md) |
| See the study method (why the order is what it is) | [`docs/00-orientation/study-method.md`](docs/00-orientation/study-method.md) |
| Set up your BA II Plus | [`docs/00-orientation/calculator-guide.md`](docs/00-orientation/calculator-guide.md) |
| See the full 5-month plan | [`docs/study-plan/master-plan.md`](docs/study-plan/master-plan.md) |
| Browse all ten topics | [`docs/topics/`](docs/topics/) |
| Start studying today | [`docs/topics/01-financial-statement-analysis/`](docs/topics/01-financial-statement-analysis/) |
| Drill formulas (Fridays) | [`resources/formula-sheet.md`](resources/formula-sheet.md) |
| Look up a term precisely | [`resources/glossary.md`](resources/glossary.md) |
| Plan the final six weeks | [`docs/study-plan/revision-phase.md`](docs/study-plan/revision-phase.md) |
| Track progress | [`trackers/progress-tracker.md`](trackers/progress-tracker.md) |

---

## The plan at a glance

Ten core blocks studied in sequence, with Ethics running **in parallel** from day 1 at ~1 hour/day.

| # | Topic | Exam weight | Order | Month | Days | Hours |
|---|---|---|---|---|---|---|
| 1 | Financial Statement Analysis | 11–14% | 1 | 1 | 20 | 80 |
| 2 | Quantitative Methods — LM1–LM5 | 6–9% (whole topic) | 2 | 1 | 10 | 40 |
| 3 | Corporate Issuers | 6–9% | 3 | 2 | 12 | 48 |
| 4 | Equity Investments | 11–14% | 4 | 2 | 18 | 72 |
| 5 | Portfolio Management | 8–12% | 5 | 3 | 10 | 40 |
| 6 | Fixed Income | 11–14% | 6 | 3 | 20 | 80 |
| 7 | Derivatives | 5–8% | 7 | 4 | 15 | 60 |
| 8 | Alternative Investments | 7–10% | 8 | 4 | 15 | 60 |
| 9 | Economics | 6–9% | 9 | 5 | 10 | 40 |
| 10 | Quantitative Methods — LM6–LM11 | (see #2) | 10 | 5 | 20 | 80 |
| 11 | **Ethical & Professional Standards** | **15–20%** | *simultaneous* | *simultaneous* | — | 150 |
| | **Total** | | | | **150** | **750** |

**Daily shape:** 4 hours core topic + 1 hour Ethics = 5 hours/day × 150 days = 750 hours.

Why this order is deliberate — and not the order the curriculum prints in — is explained in
[`docs/00-orientation/study-method.md`](docs/00-orientation/study-method.md). The short version:
FSA first because Equity, Corporate Issuers, and Fixed Income credit analysis all borrow from it;
QM split in two because the first five modules are prerequisites for everything and the last six
are heavy statistics best learned when you have real assets to apply them to; Ethics every day
because it is the single largest block and rewards long, slow exposure rather than a sprint.

---

## Repository layout

```
docs/
  00-orientation/     exam-overview · how-to-use-this-course · study-method · calculator-guide
  study-plan/         master-plan · month-01…month-05 · revision-phase
  topics/             README index + ten topic folders, one file per learning module
resources/            formula-sheet · glossary · mock-exam-tracker
trackers/             progress-tracker · daily-log · weak-areas
scripts/              progress.py · publish-to-cfa-repo.sh
curriculum.json       machine-readable index of every topic, module, and hour allocation
```

**134 files. 102 learning modules. Plain Markdown throughout** — nothing to build, nothing to
install, and every file is readable on a phone through the GitHub app on the commute.

### Anatomy of a learning-module file

Every one of the 102 module files follows the same shape, so the routine never changes:

1. **At a glance** — hours budgeted, prerequisites, where it shows up on the exam
2. **Learning Outcome Statements** — verbatim from the official 2027 outline
3. **Core concepts** — the teaching content, built to answer each LOS in order
4. **Formulas** — only the ones you must be able to reproduce cold
5. **Exam traps** — the specific ways this module is made hard
6. **Self-check** — retrieval questions with answers folded below
7. **Done when** — an explicit completion bar, so "studied it" is not a feeling

---

## Ground rules

- **The completion bar is the "Done when" list, not time spent.** Sitting with a module for four
  hours and not clearing its bar means the module is not done.
- **Ethics is not a topic you save for the end.** At 15–20% it is the heaviest single block on the
  exam, and it is the designated tie-breaker for borderline scores.
- **Questions beat re-reading.** From week 3 onward, at least a third of every study hour should be
  spent answering questions, not consuming material.
- **Log every miss.** [`trackers/weak-areas.md`](trackers/weak-areas.md) is the highest-value file in
  this repo by the final month.

---

## The two scripts

**`scripts/progress.py`** — reads the tracker and tells you where you stand. Standard library
only; no installation.

```
python3 scripts/progress.py              # per-topic and overall completion
python3 scripts/progress.py --next       # the next unfinished module
python3 scripts/progress.py --day 47     # where you should be on day 47, vs where you are
python3 scripts/progress.py --remaining  # hours left, by topic
```

**`scripts/publish-to-cfa-repo.sh`** — copies this course out into a standalone repository of its
own. Create an empty private repo on GitHub first (no README, no .gitignore, no licence), then:

```
./scripts/publish-to-cfa-repo.sh <your-github-username>
```

It stages the course, makes one clean commit, and pushes to `main`. Re-running it is safe.

---

## Licence and attribution

Learning Outcome Statements are © CFA Institute, reproduced here for personal candidate study use.
CFA Institute does not endorse, promote, or warrant the accuracy or quality of this material.
CFA® and Chartered Financial Analyst® are registered trademarks owned by CFA Institute.
