import requests
import re
from bs4 import BeautifulSoup


class GenscanOutput:
    def __init__(self, status, cds_list, intron_list, exon_list):
        self.status = status
        self.cds_list = cds_list
        self.intron_list = intron_list
        self.exon_list = exon_list


def run_genscan(sequence=None, sequence_file=None, organism="Vertebrate",
                exon_cutoff=1.00, sequence_name="", print_options='Predicted peptides only'):
    '''
    API for the GENSCAN Web Server at MIT
    Identification of complete gene structures in genomic DNA

        :param sequence: str with DNA sequence (default None)
        :param sequence_file: path to file with DNA sequence (default None)
        :param organism: one of the possible 'Vertebrate', 'Arabidopsis', 'Maize' (default 'Vertebrate')
        :param exon_cutoff: one of the possible 1.00, 0.5, 0.25, 0.1, 0.05, 0.02, 0.01 (default 1.00)
        :param sequence_name: str with name (default "")
        :param print_options: 'Predicted peptides only' (default) or 'Predicted CDS and peptides'

        :return: GenscanOutput object
    '''

    form_url = 'http://hollywood.mit.edu/cgi-bin/genscanw_py.cgi'

    if sequence_file is not None:
        with open(sequence_file, "rb") as sequence_file:
            files = {'-u': sequence_file}

            payload = {
            '-o': organism,
            '-e': exon_cutoff,
            '-n': sequence_name,
            '-p': print_options,
        }

            resp = requests.post(form_url, data=payload, files=files)

    else:
        payload = {
            '-o': organism,
            '-e': exon_cutoff,
            '-n': sequence_name,
            '-p': print_options,
            '-s': sequence
        }

        resp = requests.post(form_url, data=payload)

    soup = BeautifulSoup(resp.content).find('pre').text
    soup_string = str(soup)

    # extracting predicted peptides
    peptide_list = []

    for peptide in re.compile(r"aa\n[A-Y\n]+").findall(soup_string):
        peptide_list.append(peptide[2:].replace('\n', ""))

    # extracting predicted exons
    exon_list = []
    i = 1

    for exon in re.compile(r'1\.\d\d.+\d').findall(soup_string):
        exon_list.append((i, int(exon[11:18]), int(exon[18:25])))
        i += 1

    # extracting predicted introns from table with exons
    intron_list = []
    i = 1
    n_bp = int(re.compile(r'fasta.+bp').findall(soup_string)[0][7:-2])

    for j in range(len(exon_list)+1):
        if i == 1:
            intron_list.append((i, j, exon_list[j][1]-1))
        elif j == len(exon_list):
            intron_list.append((i, exon_list[i-2][2]+1, n_bp))
        else:
            intron_list.append((i, exon_list[i-2][2]+1, exon_list[i-1][1]-1))
        i += 1

    result = GenscanOutput(resp, peptide_list, intron_list, exon_list)

    return result


if __name__ == "__main__":

    print('Example usage: for human gene nucleophosmin 1 with default settings')
    result = run_genscan(sequence_file='./data/npm1.fasta', organism="Vertebrate",
                         exon_cutoff=1.00, sequence_name="NPM1", print_options='Predicted peptides only')
    print('\n')
    print('Status of the request:' + str(result.status))
    print('\n')
    print('List of predicted peptides:')
    print(*result.cds_list, sep='\n')
    print('\n')
    print('List of exons with start-end coordinates:')
    for exon in result.exon_list:
        print(*exon)
    print('\n')
    print('List of introns with start-end coordinates:')
    for intron in result.intron_list:
        print(*intron)
