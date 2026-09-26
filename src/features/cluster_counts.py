import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_PATH / "data" / "processed" / "customer_segments.csv"
OUTPUT_PATH = BASE_PATH / "reports" / "figures" / "cluster_sizes.png"

df = pd.read_csv(DATA_PATH)

cluster_counts = df["Cluster"].value_counts().sort_index()

plt.figure(figsize=(8, 5))

plt.bar(
    cluster_counts.index.astype(str),
    cluster_counts.values
)

plt.xlabel("Customer Cluster")
plt.ylabel("Number of Customers")
plt.title("Number of Customers in Each Cluster")

for i, value in enumerate(cluster_counts.values):
    plt.text(i, value + 1, str(value), ha="center")

plt.grid(axis="y", alpha=0.3)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT_PATH, dpi=300, bbox_inches="tight")
plt.show()

print("Cluster size chart created successfully!")
print("Saved to:", OUTPUT_PATH)