## HW3 - Fastq-filtrator for operations with fastq-files

The program can:
1. Filter reads based on GC-content
2. Filter reads based on length
3. Filter reads based on quality (Q-score)
4. Save filtered reads to file

It takes the following arguments:
- **input_fastq** - the path to file .fatstq
- **output_file_prefix** - prefix to output files ("_passed.fastq" will be added to output with correct reads and 
"_failed.fastq" for output with filtered reads (only if the argument **save_filtered** is **True**)
- **gc_bounds** - interval* of GC-content (per cent) for filtration (_default = (0, 100)_, i.e. all reads preserved). If one number is given, it is the upper bound.
- **length_bounds** - interval* of read length (nucleotides) for filtration (_default = (0, 2^32)_). If one number is given, it is the upper bound.
- **quality_threshold** - the threshold for mean value of nucleotide quality (scale phred 33)
- **save_filtered** - whether the program should save filtered (_default = False_)

*_All intervals include upper and lower bounds._
