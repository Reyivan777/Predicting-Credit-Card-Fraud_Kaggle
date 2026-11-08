# Predicting Credit Card Fraud — Kaggle

A learning-focused machine learning project for the [Kaggle Playground Series S6E11: Predicting Credit Card Fraud](https://www.kaggle.com/competitions/playground-series-s6e11/overview).

## Goal

Predict the probability that a credit card transaction is fraudulent. Kaggle evaluates predictions using **ROC-AUC**.

This repository documents exploratory data analysis, preprocessing, baseline models, validation, experiments, and conclusions. The project is developed incrementally to understand each decision rather than just optimize the leaderboard score.

## Getting started

1. Clone the repository and open a terminal in its root.
2. Install the Kaggle downloader:

   ```bash
   python -m pip install "kagglehub>=1.0.3"
   ```

3. Sign in to Kaggle and accept the competition rules on the [competition page](https://www.kaggle.com/competitions/playground-series-s6e11/overview). If Kaggle asks for authentication locally, follow the [KaggleHub authentication instructions](https://github.com/Kaggle/kagglehub#authenticate).
4. Download the original files:

   ```bash
   python download_data.py
   ```

This places `train.csv`, `test.csv`, and `sample_submission.csv` in the local `data/` folder. The folder is ignored by Git so raw competition data does not need to be committed.

## Project progress

- [ ] Explore and understand the dataset
- [ ] Establish a logistic-regression baseline
- [ ] Evaluate with cross-validation and ROC-AUC
- [ ] Compare alternative models
- [ ] Document final results and Kaggle submission

## Data source

Kaggle Playground Series, Season 6 Episode 11. Original files are downloaded directly from Kaggle rather than stored in this repository.
