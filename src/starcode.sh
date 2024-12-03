#!/bin/bash

#SBATCH --partition=bgmp
#SBATCH --account=bgmp
#SBATCH --time=1-00:00:00 



    


conda activate starcode 

# Directory containing input files
INPUT_DIR="/projects/bgmp/shared/groups/2024/novel-fluor/malm/outputs/blu/06_extract"  
OUTPUT_DIR="/projects/bgmp/shared/groups/2024/novel-fluor/malm/dat/blu"  
STARCODE_LOCATION="/projects/bgmp/shared/groups/2024/novel-fluor/malm/starcode/starcode"

# Loop through each file in the input directory
for infile_barcodes in $INPUT_DIR/*barcodes.fasta; do
    base_file_name=$(basename "$infile_barcodes" .fasta)
    
    $STARCODE_LOCATION -i "$infile_barcodes" -o "$OUTPUT_DIR/$base_file_name-clustered.txt" --sphere -d 1 --print-clusters --seq-id
done

# Directory containing input files
INPUT_DIR="/projects/bgmp/shared/groups/2024/novel-fluor/malm/outputs/red/06_extract"  
OUTPUT_DIR="/projects/bgmp/shared/groups/2024/novel-fluor/malm/dat/red"  
STARCODE_LOCATION="/projects/bgmp/shared/groups/2024/novel-fluor/malm/starcode/starcode"

for infile_barcodes in $INPUT_DIR/*barcodes.fasta; do
    base_file_name=$(basename "$infile_barcodes" .fasta)
    
    $STARCODE_LOCATION -i "$infile_barcodes" -o "$OUTPUT_DIR/$base_file_name-clustered.txt" --sphere -d 1 --print-clusters --seq-id
done









# conda activate starcode 

# ./starcode-umi \
#   --umi-len 20 \
#   --starcode-path /projects/bgmp/shared/groups/2024/novel-fluor/malm/starcode/starcode \
#   --umi-d 1 \
#   --seq-d 1 \
#   --umi-cluster mp \
#   --seq-cluster mp \
#   --umi-threads 4 \
#   --seq-threads 4 \
#   --seq-id \
#   /projects/bgmp/shared/groups/2024/novel-fluor/malm/outputs/blu \
#   > /projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/blue_pb/starcode_output

# ./starcode-umi \
#   --umi-len 20 \
#   --starcode-path /projects/bgmp/shared/groups/2024/novel-fluor/malm/starcode \
#   --umi-d 1 \
#   --seq-d 1 \
#   --umi-cluster mp \
#   --seq-cluster mp \
#   --umi-threads 4 \
#   --seq-threads 4 \
#   --seq-id \
#   /projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/red_pb/m64047_230306_210601.ccs.demux.fastq \
#   > /projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/red_pb/starcode_output





# --umi-len N   Length of the UMI tags (required).
# --starcode-path path   Path to the `starcode` binary file (required).
# --umi-d X   Match distance (Levenshtein) for the UMI region.
# --seq-d Y   Match distance (Levenshtein) for the sequence region.
# --umi-cluster algo_umi   Clustering algorithm for the UMI region (`mp`, `s`, or `cc`).
# --seq-cluster algo_seq   Clustering algorithm for the sequence region (`mp`, `s`, or `cc`).
# --umi-cluster-ratio   Minimum clustering ratio for message passing in UMI.
# --seq-cluster-ratio   Minimum clustering ratio for message passing in sequence.
# --seq-trim Z   Number of nucleotides to trim from the sequence for clustering (default is 50, set to 0 for full length).
# --seq-id   Shows input sequence order of cluster components.
# --umi-threads A   Maximum number of parallel threads for UMI processing (default is 1).
# --seq-threads B   Maximum number of parallel threads for sequence processing (default is 1).
