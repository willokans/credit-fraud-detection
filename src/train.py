from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, recall_score, f1_score, average_precision_score

from src.data_loader import load_data

def train_model(random_state=42):
    df = load_data()

    x = df.drop(columns=["Class"])
    y = df["Class"]

    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                        test_size=0.2,
                                                        random_state=random_state)

    model = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(class_weight="balanced",
                                    max_iter=1000, random_state=random_state)),
    ])

    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    y_scores = model.predict_proba(x_test)[:,1]

    metrics = {
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
        "pr_auc": average_precision_score(y_test, y_scores),
    }

    return model, metrics

def main():
    _, metrics = train_model()
    for name, value in metrics.items():
        print(f" {name}: {value:.4f}")

if __name__ == "__main__":
    main()