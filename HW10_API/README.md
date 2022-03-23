## HW10 - Create API for the [GENSCAN](http://argonaute.mit.edu/GENSCAN.html) Web Server at MIT

Function ```run_genscan``` accepts all arguments, existing on the web-site:
- sequence or sequence_file
- organism
- exon_cutoff
- print_options
- sequence_name (optional)

Returns an object from class ```GenscanOutput``` with attributes **status**, **cds_list**, **intron_list** and **exon_list**.

The example of usage on [npm1.fasta](https://github.com/anna-kapitonova/BI_2021_Python/blob/api/HW10_API/data/npm1.fasta) is included in ```"__main__"```
