## HW12 - Generators and iterators

### 1. ```fasta_reader``` is a generator, that accepts the path to fasta-file and returns pairs (id, sequence).

```
# usage example

reader = fasta_reader(os.path.join(".", "data", "sequences.fasta"))
print(type(reader))
for id_, seq in reader:
    print(id_, seq[:50])
```
>\<class 'generator'>\
>\>Seq1 MVELKEPFATLWRGKDPFEEVKTLQGEVFRELETRRTLRFEMAGKSYFLK\
>\>Seq2 MKLMLAEPFKSLWAGRDAFAEVEALKGEVYRELEARRTLRTEVDGRGFFV\
>\>Seq3 MRLVLEEPFKRLWNGRDPFEAVEALQGKVYRELEGRRTLRTEVDGRGYFV

### 2. Class ```SeqModifier``` reads sequences from fasta-file and returns with some modifications.
- minimum one argument - path to fasta-file
- object allows its iteration (infinite)
- while returning the sequence, it is modified with defined probability (methods for modifiction are **deletion** and **random_mutation**)

```
# usage example with default parameters (probability=0.7, modification='deletion', n_to_mutate=5)

seq_mod_1 = SeqModifier(os.path.join(".", "data", "sequences.fasta"))

for i in range(3):
    print(next(seq_mod_1))

iter_seq = iter(seq_mod_1)
# infinite cycle
# for i in iter_seq:
#    ...
```

### Additional tasks:
#### 1. Generator ```iter_append(iterable, item)``` "adds" element item in the "end" of iterable.

```
# usage example 1

generator1 = iter_append([1, 2, 3, 4], "ABCD")

for i in generator1:
    print(i)
```
> 1\
> 2\
> 3\
> 4\
> ABCD
```
# usage example 2

filt = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
generator2 = iter_append(filt, [5, 6, 7, 8])

print(type(generator2))

for i in generator2:
    print(i)
```

> <class 'generator'>\
> 2\
> 4\
> \[5, 6, 7, 8]
