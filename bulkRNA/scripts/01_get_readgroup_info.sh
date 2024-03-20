#!/bin/bash

# change directory
cd /research/labs/neurology/fryer/projects/aducanumab/2024_bulkRNA/

# create file with list of R1 samples
awk '{print $2}' MD5.txt | grep _1. > R1_samples.txt

# loops through list and collect header information
touch sample_read_info.txt
for sample in `cat R1_samples.txt`; do
    zcat ${sample} | head -1 >> sample_read_info.txt	
done;

# combind header information and file name
paste -d "\t" R1_samples.txt sample_read_info.txt > R1_sample_read_info.txt
rm R1_samples.txt
rm sample_read_info.txt
mv R1_sample_read_info.txt /research/labs/neurology/fryer/m239830/aducanumab_Fc_dead/bulkRNA/scripts/sample_read_info.txt

