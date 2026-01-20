# DRDO RAC Expert Matching System

A lightweight AI system for Recruitment and Assessment Centre (RAC) under DRDO to match domain experts with interview board subjects and candidates' area of expertise.

## Problem Statement

RAC under DRDO, Ministry of Defence conducts interviews for recommending candidates under recruitment, assessment and for sponsorship to acquire higher qualification. The challenge is to manually match profile of subject experts w.r.t. interview board subject and candidates' area of expertise.

## Solution Overview

- **Matching Score Computation**: Provides matching scores for experts whose domain matches w.r.t. interview board subject and candidates area of expertise
- **Relevancy Score Prediction**: Predicts suitability of expert for a particular interview board through a relevancy score
- **Profile Score Analysis**: Determines profile score for each selected expert w.r.t. profile of candidates to be interviewed
- **Automated Expert Selection**: Ranks experts based on comprehensive scoring for interview board composition

## How It Works

- **Subject Matching Score**: Computes domain alignment between expert expertise and interview board subject
- **Profile Matching Score**: Analyzes compatibility between expert profile and candidate's area of expertise
- **Experience Scoring**: Normalizes years of experience for fair comparison
- **Relevancy Score**: Combines all factors to predict expert suitability for interview board
- **Suitability Prediction**: Categorizes experts as Highly Suitable, Suitable, or Less Suitable

## Folder Structure

```
/project_root
├── main.py              # Main execution script
├── data_utils.py        # Data loading and text cleaning utilities
├── embedding_utils.py   # Text similarity functions (no external deps)
├── scoring.py           # Matching score functions
├── relevancy.py         # Relevancy score computation
├── experts.json         # Expert profiles database
├── candidates.json      # Candidate profiles
├── subject.txt          # Interview board subject description
├── requirements.txt     # No dependencies needed
└── README.md           # This file
```

## Installation

No installation required! Uses only built-in Python libraries.

## How to Run

Simply execute the main script:

```bash
python main.py
```

The system will automatically:
- Load expert and candidate data
- Process the interview subject
- Compute matching scores and relevancy scores
- Predict expert suitability for interview board
- Display ranked results

## Sample Output

```
DRDO RAC Expert Matching System
==================================================
Interview Subject: Advanced Radar Systems and Signal Processing...
Candidate Profile: Arjun Mehta

Expert Suitability Analysis:
--------------------------------------------------------------------------------
1. Dr. Rajesh Kumar
   Subject Matching Score:  0.847
   Profile Matching Score:  0.723
   Experience Score:        0.720
   Relevancy Score:         0.772
   Suitability:             Highly Suitable

2. Dr. Priya Sharma
   Subject Matching Score:  0.654
   Profile Matching Score:  0.681
   Experience Score:        0.480
   Relevancy Score:         0.630
   Suitability:             Suitable

...
```

## Technical Features

- **Zero Dependencies**: Uses only built-in Python libraries
- **Rule-Based Scoring**: Simple, interpretable scoring functions
- **Modular Design**: Easy modification of scoring weights and algorithms
- **Completely Offline**: No external downloads or internet connection required
- **RAC-Specific**: Tailored for DRDO recruitment and assessment processes

## Customization

- Modify scoring weights in `relevancy.py`
- Add new experts in `experts.json`
- Update candidate profiles in `candidates.json`
- Change interview subject in `subject.txt`
- Adjust suitability thresholds in `main.py`