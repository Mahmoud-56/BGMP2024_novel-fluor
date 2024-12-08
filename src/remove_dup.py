#!/usr/bin/env python 

# removes duplicates from final tsv files of pacbio data according to barcode in col1

import csv



input_file = "/projects/bgmp/shared/groups/2024/novel-fluor/malm/BGMP2024_novel-fluor/reports/redreads_combined_final_output.csv"  
output_file = "output_deduplicated_red_final.csv"


unique_barcodes = set()  # To track unique barcodes

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        if len(row) < 1: 
            continue

        barcode = row[0].strip()
        if barcode not in unique_barcodes:
            unique_barcodes.add(barcode)  # Mark barcode as seen
            writer.writerow(row)  # Write unique row to the output file



