#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


input_file1 = "/projects/bgmp/shared/groups/2024/novel-fluor/malm/BGMP2024_novel-fluor/reports/red_counts_per_bin.csv" 
data = pd.read_csv(input_file1)


bin_columns = [f"Counts_Bin{i}" for i in range(1, 10)]

bin_totals = data[bin_columns].sum()

print(bin_totals)




# plt.figure(figsize=(10, 6))
plt.bar(bin_totals.index, bin_totals.values, color='darkblue')
plt.xlabel("Bins", fontsize=14)
plt.ylabel("Total Counts", fontsize=14)
plt.title("Red Proteins Counts Per Bin", fontsize=16)
plt.xticks(rotation=45)
plt.yscale("log")
plt.tight_layout()

plt.savefig("Red-prot-counts-per-bin.png")