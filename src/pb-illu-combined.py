#!/usr/bin/env python 

import csv

protein_file = "/projects/bgmp/shared/groups/2024/novel-fluor/malm/BGMP2024_novel-fluor/reports/bluereads_combined_final_output.csv"
counts_file = "/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/final_MEF_and_counts/blue_counts.tsv"


barcode_to_protein = {}

with open(protein_file, 'r') as pf:
    reader = csv.reader(pf)
    for row in reader:
        if len(row) < 2: # not enough entries 
            continue
        barcode, protein_seq = row[0], row[3]  # barcode is in column 1 and protein sequence in column 3
        barcode_to_protein[barcode] = protein_seq

# find the same barcodes in the illumina counts file 

results = []

with open(counts_file, 'r') as cf:
    reader = csv.reader(cf, delimiter='\t')
    for row in reader:
        barcode = row[0]
        if barcode in barcode_to_protein:
            counts = row[1:]  # Assuming counts start from the second column
            protein_seq = barcode_to_protein[barcode]
            results.append((barcode, protein_seq, counts))

# Step 3: Output results
output_file = "../reports/blue_counts_per_bin.tsv"

with open(output_file, 'w' , newline = '') as out_f:
    writer = csv.writer(out_f, delimiter = '\t')
    writer.writerow(["Barcode", "Protein_Sequence", "Counts_Bin1", "Counts_Bin2", "Counts_Bin3", "Counts_Bin4",
                     "Counts_Bin5", "Counts_Bin6", "Counts_Bin7", "Counts_Bin8", "Counts_Bin9"])
    for result in results:
        writer.writerow([result[0], result[1]] + result[2])


