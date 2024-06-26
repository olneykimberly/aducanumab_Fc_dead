#!/bin/bash
#SBATCH --job-name=adu_snake                         
#SBATCH --partition=cpu-short
##SBATCH -p lg-mem
##SBATCH --nodes=1                                     
##SBATCH --tasks=32                                      
#SBATCH --time=08:00:00 # 8 hours                                
#SBATCH --mem=5G
##SBATCH -n 10 # threaded 
#SBATCH -o slurm.adu_snake.out
#SBATCH -e slurm.adu_snake.err
#SBATCH --mail-user=olney.kimberly@mayo.edu

# source your bach profile to get your specific settings  
source $HOME/.bash_profile

module load python
conda activate adu_env

# 1) get read information
#sh 01_sample_read_info.sh

# 2) create config
#python 02_create_config.py

# 3) run snakemake - metaphlan alignment 
snakemake -s Snakefile -j 20 --nolock --latency-wait 15 --rerun-incomplete --cluster "sbatch --ntasks 20 --partition=cpu-short --mem=35G -t 04:00:00"
