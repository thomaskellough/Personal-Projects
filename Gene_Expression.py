from random import choice
from tkinter import *
import tkinter.messagebox
import logging
import re

logging.basicConfig(filename='gene_expression.log', level=logging.DEBUG,
                    format='%(funcName)s - %(levelname)s: %(message)s')

nucleotide_list = ['A', 'T', 'G', 'C']
start_codon = 'AUG'
stop_codon = ['UAA', 'UAG', 'UGA']

mRNA_dict = {'A': 'U',
             'T': 'A',
             'G': 'C',
             'C': 'G'}

tRNA_dict = {'A': 'U',
             'U': 'A',
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
              'Gly': ['GGU', 'GGC', 'GGA', 'GGG'],
              'STOP': ['UAA', 'UAG', 'UGA']}


def dict_to_list(dict_of_codons):
    codon_list = []
    for k, v in dict_of_codons.items():
        temp_list = []
        temp_list.extend([k, v])
        codon_list.append(temp_list)
    return codon_list


def create_random_sequence(number):
    sequence = ''.join(choice(nucleotide_list) for _ in range(number))
    return sequence


def transcribe(sequence):
    mRNA_strand = ''
    for nucleotide in sequence:
        nucleotide = mRNA_dict[nucleotide]
        mRNA_strand += nucleotide
    return mRNA_strand


def mRNA_to_tRNA(sequence):
    tRNA = ''
    for nucleotide in sequence:
        nucleotide = tRNA_dict[nucleotide]
        tRNA += nucleotide
    return tRNA


def translate(sequence):
    try:
        logging.debug('Beginning translation...')
        amino_acids = dict_to_list(codon_dict)
        amino_acids_list = []
        # Find start codon
        logging.debug('Searching for start codon...')
        for nucleotide in range(0, len(sequence), 3):
            codon = sequence[nucleotide] + sequence[nucleotide + 1] + sequence[nucleotide + 2]
            if codon == start_codon:
                start_index = sequence.index(codon)
                break
        start_peptide_chain = sequence[start_index:]
        logging.debug(f'Peptide chain from start codon.\n{start_peptide_chain}')

        # Find stop codon
        logging.debug('Searching for stop codon...')
        peptide_chain = []
        for nucleotide in range(0, len(start_peptide_chain), 3):
            codon = start_peptide_chain[nucleotide] \
                    + start_peptide_chain[nucleotide + 1] \
                    + start_peptide_chain[nucleotide + 2]
            peptide_chain.append(codon)
            if codon in stop_codon:
                break
        logging.debug(f'Peptide chain after finding stop codon.\n{peptide_chain}')

        # Determine amino acid
        logging.debug('Creating amino acid list')
        for codon in peptide_chain:
            for amino_acid in amino_acids:
                if codon in amino_acid[1]:
                    amino_acids_list.append(amino_acid[0])
        logging.debug(f'List of amino acids:\n{amino_acids_list}')

        # Return a string of amino acids
        logging.debug('Converting amino acid list to a string')
        aa_string = '-'.join(amino_acids_list)
        logging.debug(f'String of amino acids.\n{aa_string}')
        return aa_string
    except IndexError:
        return 'No protein found'
      
   
sequence = create_random_sequence(1000)
print(f'Random sequence:\n{sequence}')
sequence = transcribe(sequence)
print(f'mRNA:\n{sequence}')
tRNA = mRNA_to_tRNA(sequence)
print(f'tRNA:\n{tRNA}')
amino_acids = translate(sequence)
print(f'Amino acids:\n{amino_acids}')
