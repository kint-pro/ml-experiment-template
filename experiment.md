# Experiment: EXPERIMENT_NAME

## Research Question

STATE THE CORE QUESTION IN ONE SENTENCE.

## Background

WHY THIS MATTERS. 2-3 SENTENCES MAX. LINK TO RELEVANT PAPERS.

## Setup

### Data
- Source:
- Size: train / val / test
- Generation method:

### Methods Compared

**Method 1: BASELINE_NAME**
- Description:
- Why this is the baseline:

**Method 2: PROPOSED_NAME**
- Description:
- Hypothesis:

### Model Architecture

DESCRIBE THE SHARED ARCHITECTURE. BOTH METHODS MUST USE THE SAME MODEL TO ISOLATE THE EFFECT OF THE METHOD.

### Implementation

- Framework:
- Solver:
- Hardware:

## Metrics

### Primary Metric
- Name:
- Definition:
- Why this metric:

### Secondary Metrics
- Name:
- Definition:

## Experimental Procedure

1. Generate/load data (fixed seeds)
2. For each seed (n=10):
   a. Train Method 1
   b. Train Method 2
   c. Evaluate both on test set
   d. Record all metrics
3. Aggregate results (mean, std, min, max)
4. Generate comparison figures

## Comparison Framework

- Meaningful difference threshold: >X%
- Statistical validity: N seeds, paired comparison
- All results reported as mean +/- std

## Expected Results

STATE HYPOTHESES BASED ON LITERATURE. THESE ARE PREDICTIONS, NOT GUARANTEES.

1.
2.
3.

## References

- [1]
- [2]
