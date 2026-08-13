import pandas as pd

EXPECTED_COLUMNS = ["Time"] + [f"V{i}" for i in range(1, 29)] + ["Amount", "Class"]

def load_data(path: str = "data/raw/creditcard.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    
    if list(df.columns) != EXPECTED_COLUMNS:
        raise ValueError(
                            f"Unexpected columns in {path}. \n"
                            f"Expected: {EXPECTED_COLUMNS} \n"
                            f"Got: {list(df.columns)}"
                        )

    n_missing = df.isnull().sum().sum()
    if n_missing > 0:
        raise ValueError(f"Found {n_missing} missing values in {path}")

    if df.shape[0] == 0:
        raise ValueError(f"{path} loaded but contains 0 rows")

    print(f"Loaded {df.shape[0]} rows, {df.shape[1]} columns from {path}")
    return df