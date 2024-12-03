#!/bin/bash

#SBATCH --partition=bgmp
#SBATCH --account=bgmp
#SBATCH --time=1-00:00:00 

conda activate base

INPUT_DIR1="/projects/bgmp/shared/groups/2024/novel-fluor/malm/outputs/blu/06_extract"  
INPUT_DIR2="/projects/bgmp/shared/groups/2024/novel-fluor/malm/dat/blu/starcode/" 
OUTPUT_DIR="/projects/bgmp/shared/groups/2024/novel-fluor/malm/dat/blu/lamassembel"  
LAMSCRIPT= "/projects/bgmp/shared/groups/2024/novel-fluor/malm/BGMP_Plesa_project/src/runLamassemble.py"

for infile_genes in "$INPUT_DIR1"/*genes.fasta; do
    base_file_name=$(basename "$infile_genes" "-genes.fasta")
    infile_barcodes_clustered="$INPUT_DIR2/$base_file_name-clustered.txt"


python "$LAMASSEMBLE_SCRIPT" \
            -f "$infile_genes" \
            -s "$infile_barcodes_clustered" \
            -o "$OUTPUT_DIR/$base_file_name-consensus.fasta" \
            -t "$OUTPUT_DIR/$base_file_name-temp.fasta"

done





