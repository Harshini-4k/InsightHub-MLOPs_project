import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_PATH / "data" / "processed" / "customer_segments.csv"
OUTPUT_PATH = BASE_PATH / "reports" / "figures" / "customer_segments.png"

df = pd.read_csv(DATA_PATH)

plt.figure(figsize=(8, 6))

for cluster in sorted(df["Cluster"].unique()):
    cluster_data = df[df["Cluster"] == cluster]

    plt.scatter(
        cluster_data["Annual Income (k$)"],
        cluster_data["Spending Score (1-100)"],
        label=f"Cluster {cluster}"
    )

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means")
plt.legend()
plt.grid(True)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight")
plt.show()

print("Cluster visualization created successfully!")
print("Saved to:", OUTPUT_PATH)