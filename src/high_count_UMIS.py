#!/usr/bin/env python


import pandas as pd

# Load the CSV file, assuming no header, and only relevant columns
df = pd.read_csv("/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/NF_pacbio_output/blu/09_final_output/bluereads.0--0-final.csv", header=None, usecols=[0, 1], names=["UMI", "Count"])

# Convert 'Count' column to numeric, handling any non-numeric values
df["Count"] = pd.to_numeric(df["Count"], errors='coerce')



high_count_threshold = 17500
high_count_umis = df[df["Count"] > high_count_threshold]

high_count_umis.to_csv("high_count_umis_blu.csv", index=False)




