import matplotlib.pyplot as plt

# task 1


class Dogs:
    def __init__(self, age=0, weight=0, sex='undefined', breed='mongrel', color='mix'):
        self.age = age
        self.weight = weight
        self.sex = sex
        self.breed = breed
        self.color = color
        self.commands = set()

    def grow(self, month=1):
        self.age += month
        self.weight += month*0.5

    def train(self, *commands):
        for command in commands:
            self.commands.add(command)

    def contest_allowed(self):
        if self.age >= 12 and self.breed != 'mongrel' and len(self.commands) >= 3:
            return True
        else:
            return False


# task 2

good_nucleotides = set('AGCUagcu')

code = {"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
        "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
        "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
        "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
        "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
        "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
        "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
        "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
        "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
        "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
        "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

RNA_to_DNA = {"A": "T", "a": "t", "U": "A", "u": "a",
              "G": "C", "g": "c", "C": "G", "c": "g"}


class RNA:
    def __init__(self, sequence, protein_coding=True):
        if type(sequence) != 'str' and set(sequence).issubset(good_nucleotides):
            self.seq = sequence
            self.protein_coding = protein_coding
        else:
            print('RNA should contain only nucleotides from set {AGCUagcu}')

    def __repr__(self):
         return self.seq

    def translation(self):
        if self.protein_coding is True:
            codon = []
            protein = []
            for nucleotide in self.seq.upper():
                codon.append(nucleotide)
                if len(codon) == 3:
                    protein.append(code[''.join(codon)])
                    codon = []
            print(''.join(protein))
        else:
            print('It is not a protein-coding RNA, translation is not possible')

    def reverse_transcription(self):
        dna = []
        for nucleotide in self.seq:
            dna.append(RNA_to_DNA[nucleotide])
        print(''.join(dna))


# task 3


class PositiveSet(set):
    def __init__(self, *elements):
        self.set = set()
        for element in elements:
            if element > 0:
                self.set.add(element)

    def add(self, *elements):
        for element in elements:
            if element > 0:
                self.set.add(element)


# task 4


class Fasta:
    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return self.path
        
    def __str__(self):
        return self.path

    def count_number(self):
        self.number = 0
        with open(self.path) as file:
            for line in file:
                if line.startswith('>'):
                    self.number += 1
        print(self.number)

    def count_gc(self):
        self.gc = 0
        c, g, length = 0, 0, 0
        with open(self.path) as file:
            for line in file:
                if not line.startswith('>'):
                    c += line.count('C')
                    g += line.count('G')
                    length += len(line)-1
        self.gc = round((c + g)/length*100, 1)
        print(self.gc)
    
    def count_all(self):
        self.count_number()
        self.count_gc()

    def length_hist(self):
        length_list = []
        with open(self.path) as file:
            length_seq = 0
            for line in file:
                if not line.startswith('>'):
                    length_seq += len(line)-1
                else:
                    length_list.append(length_seq)
                    length_seq = 0
        length_list.append(length_seq)
        length_list.remove(0)

        fig, ax = plt.subplots(figsize=(15, 10))
        plt.rcParams['font.size'] = '16'
        for label in (ax.get_xticklabels() + ax.get_yticklabels()):
            label.set_fontsize(16)
        ax.hist(length_list, color="red")
        ax.set_xlabel("Sequence length (bp)", fontsize="16")
        ax.tick_params(axis='y', labelcolor="black")
        ax.set_title("Distribution of sequence lengths over all sequences", size=20)
        plt.show()

    def hist_4mers(self):
        four_mers = {}
        with open(self.path) as file:
            for line in file:
                if not line.startswith('>'):
                    mer = []
                    for nucleotide in line:
                        if nucleotide != '\n':
                            mer.append(nucleotide)
                            if len(mer) == 4:
                                try:
                                    four_mers[''.join(mer)] += 1
                                except KeyError:
                                    four_mers[''.join(mer)] = 1
                                mer = mer[1:]
        sum_mers = sum(four_mers.values())
        for key, value in four_mers.items():
            four_mers[key] = value/sum_mers
        sorted_mers = {}
        sorted_keys = sorted(four_mers, key=four_mers.get)
        for key in sorted_keys:
            sorted_mers[key] = four_mers[key]

        fig, ax = plt.subplots(figsize=(70, 10))
        for label in (ax.get_xticklabels()):
            label.set_fontsize(10)
        ax.bar(list(sorted_mers.keys()), sorted_mers.values(), color="red")
        ax.set_xlabel("4-mer frequency", fontsize="16")
        ax.tick_params(axis='y', labelcolor="black")
        ax.set_title("Distribution of 4-mers", size=20)
        plt.xticks(rotation=90)
        plt.show()
