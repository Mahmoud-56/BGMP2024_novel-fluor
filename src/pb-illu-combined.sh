#!/bin/bash

#SBATCH --partition=bgmp
#SBATCH --account=bgmp

/usr/bin/time -v ./pb-illu-combined.py


