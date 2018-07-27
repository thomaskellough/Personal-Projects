import random
import logging

logging.basicConfig(filename='gene_expression.log', level=logging.DEBUG,
                    format='%(funcName)s - %(levelname)s: %(message)s')

nucleotide_list = ['A', 'T', 'G', 'C']
start_codon = 'AUG'
stop_codon = ['UAA', 'UAG', 'UGA']

dna_template_dict = {'A': 'T',
                     'T': 'A',
                     'G': 'C',
                     'C': 'G'}

transcribe_dict = {'A': 'U',
                   'T': 'A',
                   'C': 'G',
                   'G': 'C'}

codon_dict = {'Phe': ['UUU', 'UUC'],
              'Leu': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
              'Ile': ['AUU', 'AUC', 'AUA'],
              'Met': ['AUG'],
              'Val': ['GUU', 'GUC', 'GUA', 'GUG'],
              'Ser': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
              'Pro': ['CCU', 'CCC', 'CCA', 'CCG'],
              'Thr': ['ACU', 'ACC', 'ACA', 'ACG'],
              'Ala': ['GCU', 'GCC', 'GCA', 'GCG'],
              'Tyr': ['UAU', 'UAC'],
              'His': ['CAU', 'CAC'],
              'Gln': ['CAA', 'CAG'],
              'Asn': ['AAU', 'AAC'],
              'Lys': ['AAA', 'AAG'],
              'Asp': ['GAU', 'GAC'],
              'Glu': ['GAA', 'GAG'],
              'Cys': ['UGU', 'UGC'],
              'Trp': ['UGG'],
              'Arg': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
              'Gly': ['GGU', 'GCG', 'GGA', 'GGG'],
              'STOP': ['UAA', 'UAG', 'UGA']}


def dict_to_list(dict):
    codon_list = []
    for k, v in dict.items():
        temp_list = []
        temp_list.extend([k, v])
        codon_list.append(temp_list)
    return codon_list


def create_random_sequence(number):
    sequence = ''
    for i in range(number):
        sequence += random.choice(nucleotide_list)
    return sequence


def create_dna_template_strand(sequence):
    dna_template_strand = ''
    for nucleotide in sequence:
        nucleotide = dna_template_dict[nucleotide]
        dna_template_strand += nucleotide
    return dna_template_strand


def transcribe(sequence):
    mRNA = ''
    for nucleotide in sequence:
        nucleotide = transcribe_dict[nucleotide]
        mRNA += nucleotide
    return mRNA


def translate(sequence, start):
    logging.debug('Translating mRNA')
    logging.debug(f'Sequence entering:\n{sequence}')
    logging.debug('Creating codon list from codon dictionary')
    codons_list = dict_to_list(codon_dict)
    codon_list = []
    start = sequence.index(start_codon)
    peptide_chain = sequence[start:]
    initial_length = len(peptide_chain)
    logging.debug(f'Initial length of the peptide chain is: {initial_length}')

    def find_stop_codon(temp_peptide_chain, difference):
        logging.debug(f'Peptide chain entering:\n{peptide_chain}')
        for stop in stop_codon:
            if (temp_peptide_chain.index(stop) - start) % 3 == 0:
                logging.debug(f'Peptdie chain found with stop codon at {peptide_chain.index(stop)}. \
                New sequence is\n{peptide_chain}')
                stop_sequence_index = temp_peptide_chain.index(stop) + difference
                final = final_stop_sequence[:stop_sequence_index + 3]
                return final
            else:
                logging.debug(f'{stop} at {peptide_chain.index(stop)} is not a stop codon')
                temp_peptide_chain = temp_peptide_chain[temp_peptide_chain.index(stop) + 1:]
                difference = initial_length - len(temp_peptide_chain)
                logging.debug(f'NEW STOP SEQUENCE:\n{peptide_chain}\nLength: {len(peptide_chain)}')
                logging.debug(f'Difference is: {difference}')
                return find_stop_codon(temp_peptide_chain, difference)

    final_stop_sequence = peptide_chain
    peptide_chain = find_stop_codon(final_stop_sequence, 0)
    logging.debug(f'Printing sequence out of loop.\n{peptide_chain}')
    temp_sequence = ''
    print(f'Chain out of loop:\n{peptide_chain}')
    for i in range(0, len(peptide_chain), 3):
        codon = peptide_chain[i] + peptide_chain[i + 1] + peptide_chain[i + 2]
        temp_sequence += codon
        if codon in stop_codon:
            break
    peptide_chain = temp_sequence
    logging.debug(f'peptide_chain after the find_stop_codon function.\n{peptide_chain}')
    print(f'Chain after finding first stop codon:\n{peptide_chain}')
    for i in range(0, len(peptide_chain), 3):
        codon = peptide_chain[i] + peptide_chain[i + 1] + peptide_chain[i + 2]
        for group in codons_list:
            if codon in group[1]:
                codon_list.append(group[0])
    return codon_list


sequence = create_random_sequence(1000)
print(f'Intial sequence:\n{sequence}')
DNA_template = create_dna_template_strand(sequence)
print(f'DNA template:\n{DNA_template}')
mRNA = transcribe(DNA_template)
print(f'mRNA:\n{mRNA}')
peptide_chain = translate(mRNA, 0)
protein = ''
for amino_acid in peptide_chain:
    protein += amino_acid + '-'
print(protein.replace('STOP-', 'STOP'))
