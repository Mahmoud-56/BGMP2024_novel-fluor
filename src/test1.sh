#!/bin/bash

#SBATCH --partition=bgmp
#SBATCH --account=bgmp
#SBATCH --mem=64G

set -eu
conda activate illumina

/usr/bin/time nextflow run test1.nf --trace -profile local
