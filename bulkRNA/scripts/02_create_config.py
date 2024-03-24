#!/usr/bin/python3
import re

# create a new output file
outfile = open('config.json', 'w')

# get all sample names
allSamples = list()
read = ["1", "2"]
numSamples = 0

with open('sample_read_info.txt', 'r') as infile:
    for line in infile:
        numSamples += 1
        split = line.split()
        sampleAttributes = split[0].split('/') # 01.RawData/A_14/A_14_1.fq.gz treatement_ID_R1
        stemName = sampleAttributes[1] 
        allSamples.append(stemName)

# create header and write to outfile
header = '''{{
    "Commment_Input_Output_Directories": "This section specifies the input and output directories for scripts",
    "counts_dir" : "../counts/", 
    "rawReads" : "/research/labs/neurology/fryer/projects/aducanumab/2024_bulkRNA/01.RawData/",
    "rawQC" : "../rawQC/",
    "trimmedReads" : "../trimmedReads/",
    "trimmedQC" : "../trimmedQC/",
    "starAligned" : "../starAligned/",
    "bamstats" : "../bamstats/",
    "multiQC_raw_report" : "../rawQC/multiqc_report",
    "multiQC_trimmed_report" : "../trimmedQC/multiqc_report",

    "Comment_Reference" : "This section specifies the location of the mouse , Ensembl reference genome",
    "Mmusculus_dir" : "/research/labs/neurology/fryer/projects/references/mouse/refdata-gex-mm10-2020-A_star_2.7.4/",
    "Mmusculus_gtf" : "/research/labs/neurology/fryer/projects/references/mouse/refdata-gex-mm10-2020-A/genes/genes.gtf",
    "Mmusculus_fa" : "/research/labs/neurology/fryer/projects/references/mouse/refdata-gex-mm10-2020-A/fasta/genome.fa",

    "Comment_Sample_Info": "The following section lists the samples that are to be analyzed",
    "sample_names": {0},
    "read": {1},
'''
outfile.write(header.format(allSamples, read))

# config formatting
counter = 0
with open('sample_read_info.txt', 'r') as infile:
    for line in infile:
        counter += 1
        # store sample name and info from the fastq file
        split = line.split()
        sampleAttributes = split[0].split('/') # 01.RawData/A_14/A_14_1.fq.gz treatement_ID_R1
        base = sampleAttributes[1] + '/' + sampleAttributes[2]
        base = base.replace(".fq.gz", "")
        sampleName1 = base
        sampleName2 = re.sub(r'_1$', '_2', sampleName1)
        base = base.replace("_1", "")
        sampleInfo = split[1]

        split = line.split()
        sampleAttributes = split[0].split('/')
        stemName = sampleAttributes[1]
        stemID = sampleAttributes[1] 

        # break down fastq file info
        # @A00742:819:H5T7HDSXC:1:1101:1832:1000 1:N:0:TACCAACTGC+TNCGAGCTTG
        # @<instrument>:<run number>:<flowcell ID>:<lane>:<tile>:<x-pos>:<y-pos>
        sampleInfo = sampleInfo.split(':')
        instrument = sampleInfo[0]
        runNumber = sampleInfo[1]
        flowcell = sampleInfo[2]

        lane = sampleInfo[6]
        ID = stemID  # ID tag identifies which read group each read belongs to, so each read group's ID must be unique
        SM = stemName  # Sample
        PU = flowcell  # Platform Unit

        out = '''
    "{0}":{{
        "fq1": "{1}",
        "fq2": "{2}",
        "ID": "{3}",
        "SM": "{4}",
        "PU": "{5}",
        "PL": "Illumina"
        '''
        outfile.write(out.format(stemName, sampleName1, sampleName2, stemName, SM, PU))
        if (counter == numSamples):
            outfile.write("}\n}")
        else:
            outfile.write("},\n")
outfile.close()
