#!/usr/bin/env python
import csv 


 

def read_csv_file(csv_file):
    umi_dict = {}
    with open(csv_file, 'r') as f:
        read = csv.reader(f) #Default delimiter is comma
        for row in read:
            umi = row[0]
            dna_seq = row[2]
            prot_seq = row[3]
            umi_dict[umi] = (dna_seq, prot_seq)
    return umi_dict


def read_tsv_file(tsv_file):
    umi_counts = {}
    with open(tsv_file, 'r') as f:
        next(f)
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            umi = row[0]
            counts = list(map(int, row[1:]))  # Convert counts to integers
            umi_counts[umi] = counts
    return umi_counts


    # Function to combine data and write to a new TSV file
def combine_and_write_output(csv_file, tsv_file):
    
    umi_dict = read_csv_file(csv_file)
    umi_counts = read_tsv_file(tsv_file)

    for bin_num in range(1, 10):
        output_file = f'bin_{bin_num}_output.tsv'
        
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f, delimiter='\t')
            
            # Write the header
            writer.writerow(['UMI', 'DNA Sequence', 'Protein Sequence', 'Count'])
            
            # Write the combined data for this bin
            for umi, (dna_sequence, protein_sequence) in umi_dict.items():
                if umi in umi_counts:
                    counts = umi_counts[umi]
                    bin_count = counts[bin_num - 1]  # Select the count for the current bin
                    writer.writerow([umi, dna_sequence, protein_sequence, bin_count])

# File paths
csv_file = '/projects/bgmp/shared/groups/2024/novel-fluor/malm/redreads_combined_pb_final_output.csv'
tsv_file = '/projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/counts_per_bin/red_counts_FINAL.tsv' 
  


combine_and_write_output(csv_file, tsv_file)