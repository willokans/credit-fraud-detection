Read CLAUDE.md for the full project brief. We're starting Phase 1: build a
working baseline end to end before anything fancy.

1. Set up the repo structure described in CLAUDE.md (src/, tests/, etc.)
2. Set up a Python virtual environment and requirements.txt with: pandas,
   scikit-learn, mlflow, fastapi, uvicorn, pytest
3. Write a script that downloads/loads the Kaggle Credit Card Fraud Detection
   dataset (assume it's already downloaded to data/raw/ as creditcard.csv —
   tell me if you need me to place it there first)
4. Do minimal EDA and explain the class imbalance in the data
5. Train a simple logistic regression baseline (no MLflow yet — that's next),
   using appropriate metrics for imbalanced classification (precision, recall,
   F1, PR-AUC — not accuracy), and explain why each metric matters here
6. Write a short tests/ file that sanity-checks the training script runs and
   produces a model with reasonable metrics

Explain each step as you go — I'm learning this stack, don't just hand me
finished code without walking me through the decisions.
