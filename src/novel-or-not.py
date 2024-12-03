#!/usr/bin/env python 

import argparse 
from Bio.Blast import NCBIWWW, NCBIXML
import pandas as pd



def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--in_file",type=str,help="input file containing prot seq, MEF value")
    parser.add_argument("-o1","--out_file1",type=str,help="")
    parser.add_argument("-o2","--out_file2",type=str,help="")
    return parser.parse_args()

args = get_args()

data = pd.read_csv(args.in_file)


sequences = data['protein']


known_proteins = []
novel_proteins = []

novel_counter = 1
coverage_threshold = 0.95  # 95% query coverage is the threshold 

for seq in sequences:
    if len(seq) > 180:  # sequences less than 180 bp are less likely to be trully fluorescent 
        #  BLAST search

        print(f"BLASTing sequence: {seq[:30]}...")  # Show the first 30 characters for tracking
        result_handle = NCBIWWW.qblast("blastp", "nr", seq)

        # Parse BLAST results
        blast_records = NCBIXML.read(result_handle)

        is_known = False

        for alignment in blast_records.alignments:
            for hsp in alignment.hsps:
                # Calculate query coverage
                query_coverage = hsp.align_length / len(seq)
                
                if query_coverage >= coverage_threshold:  
                    known_proteins.append({"Protein": seq, "Match": alignment.title})
                    is_known = True
                    break
            if is_known:
                break

        if not is_known: # we have a novel sequence 
            novel_proteins.append({"Protein": seq, "Novel ID": f"Novel_{novel_counter}"})
            novel_counter += 1

# Save results to files
pd.DataFrame(known_proteins).to_csv(args.out_file1, sep="\t", index=False)
pd.DataFrame(novel_proteins).to_csv(args.out_file2, sep="\t", index=False)

