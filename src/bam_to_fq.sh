#!/bin/bash

#SBATCH --partition=bgmp
#SBATCH --account=bgmp
#SBATCH --error=LOG/bam_to_fastq_%j.err
#SBATCH --time=1-00:00:00            
#SBATCH --nodes=5                  
#SBATCH --cpus-per-task=5


#source /projects/bgmp/shared/groups/2024/novel-fluor/envs/starcode


samtools fastq /projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/blue_pb/m64047_230308_062131.ccs.demux.bam > /projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/blue_pb/m64047_230308_062131.ccs.demux.fastq

samtools fastq /projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/red_pb/m64047_230306_210601.ccs.demux.bam > /projects/bgmp/shared/groups/2024/novel-fluor/shared/dat/red_pb/m64047_230306_210601.ccs.demux.fastq
