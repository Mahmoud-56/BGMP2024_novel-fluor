#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

#Blu bin

# Load the CSV file,  assuming no header
df1 = pd.read_csv("/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_pacbio_output/blu/09_final_output/bluereads.0--0-final.csv", header=None, usecols=[0, 1], names=["UMI", "Count"])

# Convert 'Count' column to numeric, handling any non-numeric values
df1["Count"] = pd.to_numeric(df1["Count"], errors='coerce')

# Summary statistics for the 'Count' column
print(df1["Count"].describe())


# Plot the histogram for the 'Count' column
plt.figure(figsize=(10, 6))
plt.hist(df1["Count"], bins=30, color='skyblue', edgecolor='black', log=True)
plt.xlabel("Count")
plt.ylabel("Frequency")
plt.title("Histogram of UMI Counts (Log Scale)")
plt.savefig("blu_bin1_UMI_counts.png")


#Red bin

df2 = pd.read_csv("/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_pacbio_output/red/09_final_output/redreads.0--0-final.csv",header=None,usecols=[0, 1], names=["UMI", "Count"])

# Convert 'Count' column to numeric, handling any non-numeric values
df2["Count"] = pd.to_numeric(df1["Count"], errors='coerce')

# Summary statistics for the 'Count' column
print(df2["Count"].describe())

# Plot the histogram for the 'Count' column
plt.figure(figsize=(10, 6))
plt.hist(df2["Count"], bins=30, color='red', edgecolor='black', log=True)
plt.xlabel("Count")
plt.ylabel("Frequency")
plt.title("Histogram of UMI Counts (Log Scale)")
plt.savefig("red_bin1_UMI_counts.png")
