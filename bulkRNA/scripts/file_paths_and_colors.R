# This script is sourced by my the Rmd files to read in color variables, gene annotation files, and load libraries

# read in metadata
metadata <- read.delim("../../metadata.tsv")
# rename treatment Fc silent Adu to Fc
metadata$Treatment <- gsub("Fc silent Adu", "Fc", metadata$Treatment)
metadata$Age.at.harvest <- gsub("w", "", metadata$Age.at.harvest) # remove w 
metadata$Age.at.harvest <- as.numeric(metadata$Age.at.harvest) # set as numeric 
metadata$Treatment <- factor(metadata$Treatment, levels = c("Adu", "Fc", "IgG")) # factor order of treatment

# color by treatment group
treatment_colors <- c("#B4464B", "gray35", "#4682B4")
#Adu_color <- "#B4464B" 
#Fc_color <- "gray35" 
#IgG_color <- "#4682B4" 

# path to reference annotation  
pathToRef = c("/research/labs/neurology/fryer/projects/references/mouse/refdata-gex-mm10-2020-A/genes/")
typeOfCount <-  c("_STAR.bamReadsPerGene.out.tab")

# Functions
saveToPDF <- function(...) {
  d = dev.copy(pdf,...)
  dev.off(d)
}

# libraries 
library(ComplexUpset)
library(gprofiler2)
library(dplyr)
library(edgeR)
library(limma)
library(ggrepel)
library(ggplot2)
library(gplots)
library(stringr)
require(variancePartition) 
library(reshape)
library(Glimma)
library(plyr)
library(corrplot)
library(ggpubr)
library(glmnet)
library(vroom)
library(tidyr)
library(gridExtra)
library(grid)
require(openxlsx)
library(mvIC) 
library(RColorBrewer)
library(reshape2)
library(data.table)
library(cowplot)
library(philentropy)
library(purrr)
library(BiocParallel)
library(mvIC)
library(matrixStats)

