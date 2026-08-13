# Credit Card Fraud Detection

A staged build of a fraud detection pipeline on the Kaggle [Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) dataset — from a baseline classifier through experiment tracking to a served model.

## Roadmap

- [ ] **Phase 1 — Baseline** *(in progress)*: repo scaffolding, EDA, logistic regression baseline with imbalance-aware metrics (precision, recall, F1, PR-AUC), sanity tests.
- [ ] **Phase 2 — Experiment tracking**: MLflow integration for run tracking, metric logging, and model registry.
- [ ] **Phase 3 — Serving**: FastAPI endpoint to serve the trained model.

## Project structure

```
credit-fraud-detection/
├── data/
│   └── raw/              # creditcard.csv (not tracked in git)
├── src/
│   ├── data_loader.py    # loads + validates the raw dataset
│   └── eda.py             # class imbalance / summary stats
├── tests/                 # pytest sanity checks (coming in Phase 1)
├── requirements.txt
└── download_script.py     # re-fetches the dataset via the Kaggle API
```

## Setup

1. Clone the repo and place the dataset at `data/raw/creditcard.csv`, or run `download_script.py` with valid Kaggle API credentials saved to `kaggle.json` in the project root.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the EDA:
   ```bash
   python -m src.eda
   ```

Training, tracking, and serving instructions will be added here as those phases land.
