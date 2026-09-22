# How To Use This Course

## Your daily loop

```
1.  Open  docs/study-plan/month-0X.md   → find today's date
2.  Open  the learning module(s) listed for today
3.  Read the LOS list first. All of them.
4.  Work through Core Concepts, doing every example by hand
5.  Do the module's Self-Check cold (answers are folded — don't peek)
6.  Log every miss in  trackers/weak-areas.md
7.  Hour 5: Ethics. Always.
8.  Tick the module in trackers/progress-tracker.md — only if "Done when" is clear
9.  Fill one line in trackers/daily-log.md
```

That's it. Nine steps, every day, for 150 days.

## Files you will touch daily

| File | What it's for |
| --- | --- |
| `docs/study-plan/month-0X.md` | Today's assignment. Your only source of "what do I do now?" |
| `docs/topics/**/lm-*.md` | The material itself |
| `trackers/daily-log.md` | One line per day: hours, modules, confidence 1–5 |
| `trackers/weak-areas.md` | Every miss, categorised K/A/C/T. **The highest-value file here.** |
| `trackers/progress-tracker.md` | Checkbox per module. Your map. |

## Files you will touch weekly

| File | What it's for |
| --- | --- |
| `resources/formula-sheet.md` | Friday drill: cover the right column, reproduce every formula |
| `resources/mock-exam-tracker.md` | From Month 4 — score, timing, and per-topic band per mock |
| `docs/topics/**/README.md` | Topic wrap-up checklist when you finish a block |

## Working with the module files

Each file has seven sections. Use them differently:

**At a glance** — Read before you start. Tells you the hours budgeted and what you need to already
know. If the prerequisites aren't solid, fix that first; the module will be twice as slow otherwise.

**Learning Outcome Statements** — The specification, verbatim from the 2027 outline. Read all of
them *before* the content. Re-read them *after*. If you can't answer one, you are not done.

**Core concepts** — The teaching. Written to answer the LOS in order. Work every number yourself;
reading a worked example is not the same as producing it.

**Formulas** — Only what you must reproduce cold. If it's here, it's memorisation-grade.

**Exam traps** — The specific ways this module is made hard. Read these twice. Most Level I losses
are not knowledge gaps, they're trap hits.

**Self-check** — Retrieval practice. Do it *closed-book*, several days after Pass 1 if you can.
Answers are in a collapsed `<details>` block — opening it before you've committed to an answer
destroys the entire value of the exercise.

**Done when** — The completion bar. Tick honestly.

## The markdown conventions

- `**bold**` in Core Concepts marks a term you should be able to define cold.
- A blockquote starting **"Trap:"** marks something that regularly costs marks.
- A table with two columns and a *compare/contrast* heading is a memorisation target — the exam
  tests the *differences*, so learn the rows, not the items.
- Formulas are written in plain text (not LaTeX) so they render identically on GitHub, in your
  editor, and on a phone.

## Using this on a phone

Every file is plain Markdown with no rendering dependencies. GitHub's mobile view is enough for the
Ethics hour, self-check questions, and formula drills on a commute. Reserve the desktop for the
calculation-heavy modules where you need the calculator and a scratch board.

## Tracking progress automatically

```bash
python3 scripts/progress.py          # completion %, by topic and overall
python3 scripts/progress.py --next   # what to study next, per the plan
```

The script reads `trackers/progress-tracker.md` and `curriculum.json` — nothing to configure.

## A note on honesty

This course has no grader. Its entire value rests on you not ticking boxes you haven't earned and
not peeking at answers before committing to one. The self-check answers are folded for a reason:
the moment you read an answer you *could* have retrieved, you convert a learning opportunity into a
false memory of competence. Those false memories are exactly what produces a surprise at 60% on a
first mock.
