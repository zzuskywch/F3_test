# Import necessary modules
import os
from sys import argv

# Read command-line arguments
target = argv[1]   # Target population
popu1 = argv[2]    # Popu1
num = argv[3]      # Number of results to output  num<0 descending ,,num>0ascending

# Set fuhao (direction of sorting) based on num
if '-' in num:   # if negative, sort in descending order
        infile = open('logfile', 'r')  # Open input file
        outfile1 = open('target_' + target + '.-' + popu1 + '.rscript', 'w')  # Open output R script file
        outfile = open('target_' + target + '.-' + popu1 + '.rfile', 'w')  # Open output file
        fuhao = -1  # Set direction of sorting to descending
else:   # if positive or zero, sort in ascending order
        infile = open('logfile.ascending', 'r')  # Open input file
        fuhao = 1  # Set direction of sorting to ascending

count = 0  # Initialize counter
for line in infile:   # Loop through input file
        l = line.split('\t')   # Split line by tab
        if l[1] == popu1 and l[3] == target:  # If the line corresponds to the target and popu1 populations
                outfile.write(l)   # Write the line to the output file
                count += 1   # Increment the counter
                if count >= abs(int(num)):   # If we've reached the desired number of results, break out of the loop
                        break
        else:   # If the line doesn't correspond to the target and popu1 populations, continue to the next line
                continue

# Close input and output files
infile.close()
outfile.close()

# Write R script to plot results
outfile1.write('library(ggplot2)\n')
if fuhao < 0:
        outfile1.write('data<-read.csv("target_' + target + '.-' + popu1 + '.rfile", sep="\t", header=F, col.names=c("result","PopA","PopB","PopC","F3","StdErr","Z","SNPs"))\n')
else:
        outfile1.write('data<-read.csv("target_' + target + '.' + popu1 + '.rfile", sep="\t", header=F, col.names=c("result","PopA","PopB","PopC","F3","StdErr","Z","SNPs"))\n')
outfile1.write('data2<-data[order(-data$F3),]\n')
outfile1.write('poplist<-data2$PopB\n')
outfile1.write('p<-ggplot(data2) + geom_point(mapping=aes(x=factor(PopB, level=poplist), y=F3), color="red", size=3, alpha=0.8) + geom_errorbar(aes(x=factor(PopB, level=poplist), ymin=F3-StdErr, ymax=F3+StdErr), width=0.3) + theme_classic() + coord_flip() + scale_y_continuous(position="right") + theme(axis.title.y=element_blank()) + ylab(expression(plain(paste(italic(f),"3 ('+target+';'+popu1+', X)"))))\n')
outfile1.write('ggsave(filename="target_' + target + '.' + popu1 + '.' + num + '.pdf", width=9
