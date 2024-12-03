#!/usr/bin/env python



import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data_file = "/projects/bgmp/shared/groups/2024/novel-fluor/malm/BGMP2024_novel-fluor/reports/blue_MEF.tsv"  
df = pd.read_csv(data_file)


df['MEF'] = pd.to_numeric(df['MEF'], errors='coerce')

# Plotting the fluorescence distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['MEF'], bins=9, kde=True, color='blue', edgecolor='black')
plt.title("Blue Fluorescence Distribution", fontsize=16)
plt.xlabel("Inferred Blue Fluorescence Value (MEF)", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig("Blue-Fluorescence-Distribution.png")

