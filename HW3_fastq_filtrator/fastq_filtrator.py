# 1. Filter based on GC-content + 3. Filter based on length

def length_and_gc_count_filter(file_path, length_bounds, gc_bounds,
                               save_filtered, good_lines, bad_lines):
    with open(file_path) as file:
        counter = 2  # counter for second lines with nucleic acid sequence
        number = 0  # ordinal number
        for line in file:
            counter += 1
            number += 1
            if counter == 4:
                counter = 0
                seq = line.upper().strip()
                gc_content = round(((seq.count('C') + seq.count('G'))/len(seq)*100), 1)  # count gc-content
                if length_bounds[0] <= len(seq) <= length_bounds[1] and gc_bounds[0] <= gc_content <= gc_bounds[1]:
                    good_lines.add(number - 1)  # add all four lines for one sequence
                    good_lines.add(number)
                    good_lines.add(number + 1)
                    good_lines.add(number + 2)
                elif save_filtered is True:
                    bad_lines.add(number - 1)
                    bad_lines.add(number)
                    bad_lines.add(number + 1)
                    bad_lines.add(number + 2)


# 2. Filter based on quality + saving the result to files

def quality_filter(file_path, output_file_good, output_file_bad, quality_threshold,
                   save_filtered, good_lines, bad_lines):
    with open(file_path) as file:
        counter = 0  # counter for fourth lines with nucleic acid sequence
        number = 0  # ordinal number
        for line in file:
            counter += 1
            number += 1
            if counter == 4:
                counter = 0
                quality_seq = line.strip()
                sum_quality = 0
                for symbol in quality_seq:
                    sum_quality += (ord(symbol) - 33)  # count Q-score
                mean_quality = sum_quality/len(quality_seq)
                if mean_quality < quality_threshold and number in good_lines:
                    good_lines.remove(number - 3)
                    good_lines.remove(number - 2)
                    good_lines.remove(number - 1)
                    good_lines.remove(number)
                    if save_filtered is True:
                        bad_lines.add(number - 3)
                        bad_lines.add(number - 2)
                        bad_lines.add(number - 1)
                        bad_lines.add(number)
    with open(file_path) as file:  # save passed reads
        with open(output_file_good, "w") as out:
            number = 0
            for line in file:
                number += 1
                if number in good_lines:
                    out.write(line)
    if save_filtered is True:  # save filtered reads
        with open(file_path) as file:
            with open(output_file_bad, "w") as out:
                number = 0
                for line in file:
                    number += 1
                    if number in bad_lines:
                        out.write(line)


# Main function, combining all previous in one algorithm

def main(input_fastq, output_file_prefix,
         gc_bounds=(0, 100), length_bounds=(0, 2**32),
         quality_threshold=0, save_filtered=False):
    file_path = input_fastq
    output_file_good = output_file_prefix + "_passed.fastq"
    output_file_bad = output_file_prefix + "_failed.fastq"
    good_lines = set()
    bad_lines = set()
    length_and_gc_count_filter(file_path, length_bounds, gc_bounds,
                               save_filtered, good_lines, bad_lines)
    quality_filter(file_path, output_file_good, output_file_bad,
                   quality_threshold, save_filtered, good_lines, bad_lines)


# Receiving arguments from user

print("Welcome to fastq_filtrator!")
print("Enter path to fastq file")
input_fastq = input()
print("Enter file prefix to output file (without .fastq extension)")
output_file_prefix = input()
print("Do you want to set filter parameters manually? y/n")
if input() == "y":
    print("Enter gc_content_bounds: two numbers separated by white space or one upper-bound number (default 0, 100)")
    gc_bounds = [int(i) for i in input().split(" ")]
    if len(gc_bounds) == 1:
        gc_bounds = (0, gc_bounds[0])
    else:
        gc_bounds = (gc_bounds[0], gc_bounds[1])
    print("Enter length_bounds: two numbers separated by white space or one upper-bound number(default 0, 2**32)")
    length_bounds = [int(i) for i in input().split(" ")]
    if len(length_bounds) == 1:
        length_bounds = (0, length_bounds[0])
    else:
        length_bounds = (length_bounds[0], length_bounds[1])
    print("Enter quality_threshold: one number from 0 to 40 (default 0)")
    quality_threshold = int(input())
    print("Enter save_filtered argument (True/False, default False)")
    save_filtered = bool(input())
    main(input_fastq, output_file_prefix, gc_bounds, length_bounds, quality_threshold, save_filtered)
else:
    main(input_fastq, output_file_prefix)
