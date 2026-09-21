import pandas as pd
import joblib
import mlflow
import mlflow.sklearn
from pathlib import Path
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

BASE_PATH = Path(__file__).resolve().parents[2]
mlflow.set_tracking_uri("sqlite:///C:/Users/Harshni/Documents/InsightHub/mlflow.db")

DATA_PATH = BASE_PATH / "data" / "processed" / "segmentation_data.csv"
MODEL_PATH = BASE_PATH / "models" / "kmeans_model.pkl"
RESULT_PATH = BASE_PATH / "data" / "processed" / "customer_segments.csv"

mlflow.set_experiment("InsightHub_Customer_Segmentation")


def train_model():

    df = pd.read_csv(DATA_PATH)

    X = df[
        [
            "Age",
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    ]

    with mlflow.start_run():

        n_clusters = 5

        model = KMeans(
            n_clusters=n_clusters,
            random_state=42,
            n_init=10
        )

        df["Cluster"] = model.fit_predict(X)

        score = silhouette_score(X, df["Cluster"])

        mlflow.log_param("n_clusters", n_clusters)
        mlflow.log_param("random_state", 42)
        mlflow.log_metric("silhouette_score", score)

        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)

        joblib.dump(model, MODEL_PATH)
        df.to_csv(RESULT_PATH, index=False)

        mlflow.sklearn.log_model(model, "kmeans_model")

        print("K-Means training completed!")
        print(f"Silhouette Score: {score:.4f}")
        print("MLflow tracking completed!")
        print(f"Model saved to: {MODEL_PATH}")
        print(f"Segments saved to: {RESULT_PATH}")


if __name__ == "__main__":
    train_model()