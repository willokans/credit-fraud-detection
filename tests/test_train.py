from sklearn.pipeline import Pipeline
from src.train import train_model

def test_train_model_runs_and_returns_pipeline():
    model, _ = train_model()
    assert isinstance(model, Pipeline)

def test_train_model_metric_present_and_bounded():
    _, metrics = train_model()
    for key in ("precision", "recall", "f1", "pr_auc"):
        assert key in metrics
        assert 0.0 <= metrics[key] <= 1.0

def test_train_model_beats_naive_baseline():
    _, metrics = train_model()
    assert metrics["recall"] > 0.5
    assert metrics["f1"] > 0.05
    assert metrics["pr_auc"] > 0.3

