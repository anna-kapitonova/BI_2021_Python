import os
import random


## 1. Create a generator, that accepts the path to fasta-file and returns pairs (id, sequence).


def fasta_to_lists(path):

    ids_list = list()
    seq_list = list()

    with open(path) as file:
        i = -1
        for line in file:
            if '>' in line:
                ids_list.append(line[:-1])
                i += 1
                seq_list.append([])
            else:
                seq_list[i].append(line[:-1])

    for i in range(len(seq_list)):
        seq_list[i] = "".join(seq_list[i])

    return [ids_list, seq_list]


def fasta_reader(path):

    ids_list = fasta_to_lists(path)[0]
    seq_list = fasta_to_lists(path)[1]
    iteration_list = []

    for i in range(len(seq_list)):
        iteration_list.append([ids_list[i], seq_list[i]])

    return (i for i in iter(iteration_list))


## 2. Create a class (without inheritance), that reads sequences with some modifications.
# - minimum one argument - path to fasta-file
# - object allows its iteration
# - infinite iteration for sequeunces in file
# - while returning the sequence, it is modified with defined probability (separate methods for modifications)


class SeqModifier:

    aa_list = list('ACDEFGHIKLMNPQRSTVWY')
    nucleotide_list = list('ACTGU')
    only_aa_set = set('DEFHKLMPQRSVWY')

    def __init__(self, path, probability=0.7, modification='deletion', n_to_mutate=5):
        self.path = path
        self.probability = probability
        self.modification = modification
        self.ids_list = fasta_to_lists(path)[0]
        self.seq_list = fasta_to_lists(path)[1]
        self.n_seq = len(self.seq_list)
        self.n_to_mutate = n_to_mutate
        self.cur_index = -1

        self.iteration_list = [[x, y] for x, y in zip(self.ids_list, self.seq_list)]

        if self.modification == 'deletion':
            self.deletion()

        elif self.modification == 'random mutation':
            self.random_mutation()

        if set(self.seq_list[0]).issubset(self.only_aa_set):
            self.type = 'protein'
            self.list_for_choice = self.aa_list
        else:
            self.type = 'nucleic_acid'
            self.list_for_choice = self.nucleotide_list

    def decision(self):
        return random.random() < self.probability

    def deletion(self):

        seq_list_to_print = self.seq_list

        for i in range(self.n_seq):
            if self.decision(): # probability check
                deletion_start = random.randint(0, len(self.seq_list[i]) - self.n_to_mutate)
                deletion_end = deletion_start + self.n_to_mutate
                seq_list_to_print[i] = self.seq_list[i][:deletion_start]\
                                        + self.seq_list[i][deletion_end:]

        self.iteration_list = [[x, y] for x, y in zip(self.ids_list, seq_list_to_print)]

    def random_mutation(self):

        seq_list_to_print = self.seq_list

        for i in range(self.n_seq):
            if self.decision(): # probability check

                for i in range(self.n_to_mutate): # we need n_aa mutations
                    mutation_site = random.randint(0, len(self.seq_list[i]) - 1) # choose mutation site
                    seq_list_to_print[i] = self.seq_list[i][:mutation_site]\
                                            + random.choice(self.list_for_choice)\
                                            + self.seq_list[i][mutation_site + 1:]

        self.iteration_list = [[x, y] for x, y in zip(self.ids_list, seq_list_to_print)]

    def __iter__(self):
        return self

    def __next__(self):

        self.cur_index += 1

        if self.cur_index == self.n_seq:
            self.cur_index = 0
            if self.modification == 'deletion':
                self.deletion()

            elif self.modification == 'random mutation':
                self.random_mutation()

        return self.iteration_list[self.cur_index][0] + " " + self.iteration_list[self.cur_index][1]


## 1*. Create a generator iter_append(iterable, item), that "add" element item in the "end" of iterable.


def iter_append(iterable, item):
    yield from iterable
    yield item


## 2*. Create a function, that "unzip" nested lists.


def generator_from_nested_lists(list1):
    for i in list1:
        if isinstance(i, list):
            yield from generator_from_nested_lists(i)
        else:
            yield i


def nested_lists_unpacker(list1):
    list_to_print = []
    for i in generator_from_nested_lists(list1):
        list_to_print.append(i)

    return list_to_print
