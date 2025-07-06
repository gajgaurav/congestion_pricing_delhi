# setup

import os

BASE_DIR = "congestion_pricing_delhi"

folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src/ingest",
    "src/process",
    "src/simulate",
    "src/pricing",
    "src/api",
    "dashboard",
    "configs",
    "tests"
]

os.makedirs(BASE_DIR, exist_ok = True)
for folder in folders:
    path = os.path.join(BASE_DIR, folder)
    os.makedirs(path, exist_ok = True)

# Create placeholder README and requirements
with open(os.path.join(BASE_DIR, "README.md"), "w") as f:
    f.write("# Dynamic Congestion Pricing for Delhi\n")

with open(os.path.join(BASE_DIR, "requirements.txt"), "w") as f:
    f.write("pandas\nnumpy\ngeopandas\nosmnx\nmatplotlib\nscikit-learn\nnetworkx\n")
