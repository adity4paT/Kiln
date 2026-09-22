# QM · LM11 — Introduction to Financial Data Science

## At a glance

| | |
| --- | --- |
| **Topic** | Quantitative Methods (6-9% of the exam) |
| **Hours budgeted** | 6 |
| **Prerequisites** | LM6–LM10. Conceptual closing module for the topic. |
| **Where it shows up** | 1 question. Pure recall — know the definitions and the categories. |

## Learning Outcome Statements

*Verbatim from the 2027 Level I Topic Outlines. The candidate should be able to:*

- describe how big data, machine learning, and artificial intelligence are used in financial data science, fintech, and investment management

---

## Core concepts

### Big data

Conventionally characterised by the **four Vs**:

| V | Meaning |
| --- | --- |
| **Volume** | The sheer quantity of data — terabytes to petabytes |
| **Variety** | Structured (databases, spreadsheets), semi-structured (JSON, XML), and unstructured (text, images, audio, video) |
| **Velocity** | The speed at which it arrives — real-time streams versus periodic batches |
| **Veracity** | Its reliability and credibility — the quality problem, and the one most often overlooked |

**Alternative data** is the investment-relevant subset: data not from traditional financial
statements or market feeds.

| Source | Examples |
| --- | --- |
| **Individuals** | Social media posts, product reviews, web search trends |
| **Business processes** | Credit card transactions, supply chain records, point-of-sale data, corporate exhaust data |
| **Sensors** | Satellite imagery (parking lot occupancy, oil storage tank levels), GPS, IoT devices, shipping transponders |

**The recurring problems with alternative data:** short history (no long backtest possible), selection
bias (whose credit cards? which app users?), **privacy and regulatory risk**, high cost, and
**alpha decay** — once a dataset is widely bought, its informational edge disappears.

### Machine learning

**Definition:** algorithms that learn patterns from data **without being explicitly programmed with
the rules**. The model infers the relationship rather than having it specified.

**The three categories** — know these cold:

| Type | Training data | Goal | Examples |
| --- | --- | --- | --- |
| **Supervised** | **Labelled** — inputs *and* known outputs | Predict the output for new inputs | Regression, classification, penalised regression (LASSO), support vector machines, random forests, neural networks |
| **Unsupervised** | **Unlabelled** — inputs only | Find structure in the data | Clustering (k-means, hierarchical), dimension reduction (principal components analysis) |
| **Deep learning / reinforcement** | Varies | Complex pattern recognition; learning by trial and reward | Neural networks with many layers, image and speech recognition, algorithmic trading agents |

> **The distinction the exam tests:** **supervised learning has labelled target data; unsupervised
> learning does not.** A model trained to predict whether a bond defaults (you know which ones did)
> is supervised. A model that groups equities into clusters with no pre-defined categories is
> unsupervised.

**Overfitting** is the central problem in machine learning. A model with enough flexibility can fit
the **noise** in the training data perfectly and then fail completely on new data.

| Error type | Meaning |
| --- | --- |
| **In-sample error** | Error on the training data. Low — often deceptively so |
| **Out-of-sample error** | Error on data the model has never seen. **This is the one that matters** |
| **Bias error** | The model is too simple to capture the real relationship — **underfitting** |
| **Variance error** | The model is too complex and has learned noise — **overfitting** |

The **bias-variance trade-off**: reducing one typically increases the other. The goal is the
complexity level that minimises **total out-of-sample error**.

**Guarding against overfitting:** split the data into **training**, **validation**, and **test** sets;
use **cross-validation**; and penalise complexity (regularisation).

### Data processing steps

| Step | What it involves |
| --- | --- |
| **Conceptualisation** | Define the problem and what the output should be |
| **Data collection** | Gather from internal and external sources |
| **Data preparation and wrangling** | Cleansing (errors, duplicates, missing values) and preprocessing (normalising, scaling) |
| **Data exploration** | Exploratory analysis, feature selection, feature engineering |
| **Model training** | Algorithm selection, evaluation, tuning |

For **text data** specifically: **text preparation** (removing HTML tags, punctuation, numbers,
white space), then **tokenisation** (breaking into words), then normalisation (lowercasing, removing
**stop words**, **stemming** or **lemmatisation** to reduce words to their root), then building a
**bag-of-words** or document-term matrix.

### Applications in investment management

| Application | What it does |
| --- | --- |
| **Text analytics and NLP** | Extract information from filings, transcripts, news, and social media |
| **Sentiment analysis** | Score the tone of text as a signal; analyse earnings call language |
| **Robo-advisers** | Automated portfolio construction and rebalancing from a risk questionnaire |
| **Algorithmic trading** | Execution algorithms; high-frequency market making |
| **Risk management** | Anomaly detection, fraud detection, real-time exposure monitoring |
| **Credit scoring** | Alternative data for borrowers with thin credit files |
| **RegTech** | Automating compliance monitoring and regulatory reporting |
| **Portfolio construction** | Clustering for diversification; dimension reduction on factor sets |

### Fintech

The broader category: technology-driven innovation in financial services. Core areas include
**analytics and big data**, **automated advice**, **financial record keeping** (distributed ledger
technology and blockchain — see Alternative Investments LM7), and **capital allocation**
(peer-to-peer lending, crowdfunding).

### Limitations and risks

The LOS is descriptive, but the caveats are what an analyst is actually paid for:

- **Overfitting** — the dominant risk. A backtest that looks extraordinary is usually overfitted.
- **Black box problem** — complex models, particularly deep neural networks, can be accurate without
  being **interpretable**. In a regulated context you may be required to explain a decision, and
  "the model said so" is not an explanation.
- **Data quality** — garbage in, garbage out, at scale and at speed.
- **Selection and survivorship bias** in alternative datasets.
- **Non-stationarity** — financial relationships change. A model trained on one regime may fail
  entirely in the next, and unlike physical systems there is no stable underlying law.
- **Regulatory and privacy risk** — data sourcing can breach privacy law; material non-public
  information can enter through alternative data channels.
- **Crowding and alpha decay** — a signal everyone has stops being a signal.

---

## Formulas to know cold

No formulas. This module is pure recall. The two things to memorise:

```
BIG DATA — the four Vs:   Volume · Variety · Velocity · Veracity

MACHINE LEARNING — three categories:
    Supervised     → LABELLED data; predict a known target
    Unsupervised   → UNLABELLED data; find structure
    Deep / reinforcement learning → complex patterns; learning by reward

ERROR DECOMPOSITION
    Bias error     = model too simple  → UNDERFITTING
    Variance error = model too complex → OVERFITTING
    Goal: minimise OUT-OF-SAMPLE error, not in-sample error
```

---

## Exam traps

> **Trap 1 — Supervised vs unsupervised.** **Supervised = labelled** target data. Unsupervised has
> no target — it finds structure. This is the most reliably tested distinction in the module.

> **Trap 2 — Overfitting vs underfitting.** **Overfitting = high variance error**, a model too
> complex that has learned noise. **Underfitting = high bias error**, a model too simple.

> **Trap 3 — Judging a model on in-sample error.** In-sample error can always be driven to zero with
> enough complexity. Only **out-of-sample** performance is evidence.

> **Trap 4 — Assuming more data is always better.** More data of **poor veracity**, or from a biased
> selection, makes things worse, not better — and does so with more apparent confidence.

> **Trap 5 — Believing alternative data is a permanent edge.** **Alpha decays** as a dataset becomes
> widely adopted. Short histories also make robust backtesting impossible.

> **Trap 6 — Ignoring interpretability.** A more accurate model can be unusable if you cannot explain
> its decisions to a regulator, a client, or a risk committee.

---

## Self-check

*Closed book. Commit to an answer before opening the fold.*

**1.** Distinguish supervised from unsupervised machine learning with an investment example of each.

<details><summary>Answer</summary>

**Supervised learning** trains on **labelled** data — inputs paired with known outputs — to predict the output for new inputs. Example: training a model on historical bond issuers where you know which ones defaulted, to predict default probability for new issuers. The 'default / no default' label is the target.

**Unsupervised learning** works on **unlabelled** data to find structure without a pre-defined answer. Example: clustering a universe of equities by their return behaviour to discover groupings that may cut across conventional sector classifications — you do not tell the algorithm what the groups should be.

The defining difference is simply whether a target variable exists in the training data.

</details>

**2.** What is overfitting, why is it the central problem in machine learning, and how is it controlled?

<details><summary>Answer</summary>

**Overfitting** occurs when a model has enough flexibility to fit the **noise** in the training data rather than only the underlying signal. It produces near-perfect in-sample performance and poor out-of-sample performance.

**Why it is central in finance specifically:** financial data has a low signal-to-noise ratio and relationships are non-stationary. A flexible model given enough features will always find patterns in the noise, and a backtest can be made to look extraordinary. The result is a strategy that has never worked outside the sample it was fitted to.

**Controls:** split the data into **training, validation, and test** sets and never touch the test set until the end; use **cross-validation**; apply **regularisation** (penalise model complexity, as LASSO does); limit the number of features; and require **out-of-sample and out-of-period** validation before deployment.

</details>

**3.** Name the four Vs of big data and say which is most often underweighted.

<details><summary>Answer</summary>

**Volume** (quantity), **Variety** (structured, semi-structured, unstructured), **Velocity** (speed of arrival), and **Veracity** (reliability and credibility).

**Veracity is the one most often underweighted.** Volume, variety, and velocity are exciting and easy to measure; veracity is unglamorous and hard to assess. But a large, fast, varied dataset of poor quality produces confident, precise, wrong answers — and at scale, with an impressive-looking model behind it, those answers are far more persuasive than they deserve to be.

</details>

**4.** An analyst proposes buying satellite imagery of retailer parking lots to forecast quarterly sales. What should they consider?

<details><summary>Answer</summary>

**Potential value:** a genuinely leading indicator of footfall, available before the company reports.

**Concerns:**
- **Coverage and selection bias** — which stores are imaged? Do they represent the chain? Drive-through, delivery, and online sales are invisible to this data, and those channels have grown.
- **Short history** — satellite datasets typically span a few years, so you cannot backtest across a full cycle or validate the relationship in a downturn.
- **Alpha decay** — if this dataset is sold commercially, other managers have it. The signal is priced in quickly.
- **Cost** versus the incremental information over cheaper sources.
- **Regulatory and MNPI risk** — probably fine here, but the general question of whether an alternative dataset constitutes material non-public information must be answered by compliance, not by the analyst.
- **Non-stationarity** — the parking-lot-to-sales relationship shifts as the retailer's channel mix changes.

</details>

**5.** Explain the bias-variance trade-off and what it implies for model selection.

<details><summary>Answer</summary>

**Bias error** arises when the model is **too simple** to capture the true relationship — it systematically misses the pattern. This is **underfitting**.

**Variance error** arises when the model is **too complex** and fits the noise in the training sample — it responds strongly to which particular observations it happened to be trained on. This is **overfitting**.

The **trade-off**: increasing complexity reduces bias but increases variance, and vice versa. Total out-of-sample error is the sum of both (plus irreducible noise), so it is **U-shaped** in model complexity.

**Implication for model selection:** the goal is not the model with the lowest training error — that is always the most complex one. It is the complexity level that minimises **out-of-sample** error, which is found empirically via a validation set or cross-validation, not by inspection.

</details>

**6.** Why might a portfolio manager reject a more accurate machine learning model in favour of a less accurate one?

<details><summary>Answer</summary>

**Interpretability.** A deep neural network may outperform a simple regression out of sample, but it cannot explain *why* it made a particular recommendation.

That matters concretely:
- **Regulatory obligations** may require explaining decisions, particularly in credit and in advice to retail clients.
- **Fiduciary duty and client communication** — a manager must be able to articulate the investment thesis. 'The model said so' fails the CFA Institute Standard on suitability and on diligence and reasonable basis (Ethics Standard V).
- **Risk management** — an uninterpretable model cannot be stress-tested against intuition, so a failure mode is invisible until it fires.
- **Non-stationarity** — when the model starts failing, you cannot diagnose *why* without understanding what it was keying on.

Accuracy is one attribute among several. A slightly less accurate model you can defend, monitor, and debug may be the better professional choice.

</details>

---

## Done when

- [ ] I can name the four Vs and explain why veracity is the underweighted one
- [ ] I can define supervised, unsupervised, and deep/reinforcement learning with an investment example of each
- [ ] I can explain overfitting, the bias-variance trade-off, and how overfitting is controlled
- [ ] I can name three sources of alternative data and the standard problems with each
- [ ] I can list the data processing steps, including the text-specific ones
- [ ] I can name six applications of ML in investment management
- [ ] I can explain the black box problem and why it can outweigh accuracy
- [ ] I answered the self-check cold, several days after first study

---

← [LM10 Applications of Simple Linear Regression in Finance](lm-10-applications-of-simple-linear-regression-in-finance.md)  ·  [Topic index](README.md)
