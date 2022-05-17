from collections import defaultdict
from datasets import DatasetDict, get_dataset_config_names
import os

print(f"Current position: {os.getcwd()}")

# Show number of different config
xtreme_subsets = get_dataset_config_names("xtreme")
print(f"XTREME has {len(xtreme_subsets)} configurations")

# Look for config start with PAN
panx_subsets = [s for s in xtreme_subsets if s.startswith("PAN")]
print(f"Number of panx subset: {len(panx_subsets)}")
print(f"First 3 panx datasets: {panx_subsets[:3]}")

for i in range(3):
    print((panx_subsets[i]["train"]))

# langs = ["de", "fr", "it", "en"]
# fracs = [0.629, 0.229, 0.084, 0.059]