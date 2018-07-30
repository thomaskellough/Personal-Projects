"""
Creates a mendelian table with two parents of two separate genotypes.
"""
import logging
logging.basicConfig(filename='mendelian.log', level=logging.DEBUG,
                    format='%(funcName)s - %(levelname)s: %(message)s')

# Dictionary that holds phenotypes and genotypes off offspring
allele_count = {
    'Round, yellow seeds': [0, 'RRYY', 'RYYr', 'RRYy', 'RYry'],
    'Round, green seeds': [0, 'RRyy', 'Rryy'],
    'Wrinkled, yellow seeds': [0, 'YYrr', 'Yrry'],
    'Wrinkled, green seeds': [0, 'rryy']}


def mendelian(g1, g2, g3, g4):
    logging.debug('Entering mendelian function...')
    genotype = ''
    temp_genotype = ''
    genotype_list = []
    for allele_1 in g1:
        for allele_2 in g2:
            for allele_3 in g3:
                for allele_4 in g4:
                    genotype += allele_1 + allele_2 + allele_3 + allele_4 + '|'
                    temp_genotype += allele_1 + allele_2 + allele_3 + allele_4
                    genotype_list.append(temp_genotype)
                    logging.debug(f'Appended {temp_genotype} to list.')
                    temp_genotype = ''
            print(genotype)
            genotype = ''
    sorted_genotypes = [''.join(sorted(_)) for _ in genotype_list]
    logging.debug(f'Calculating phenotypes.')
    for genotype in sorted_genotypes:
        for v in allele_count.values():
            if genotype in v:
                logging.debug(f'Found {genotype} in {v}.')
                v[0] += 1


# The arguments are ordered as:
# Genotype 1 Parent 1
# Genotype 1 Parent 2
# Genotype 2 Parent 1
# Genotype 2 Parent 2
# In this example:
# R: dominant round/r: recessive wrinkled
# Y: dominant yellow seeds/y: recessive green seeds
mendelian('Rr', 'Rr', 'Yy', 'Yy')

# Used for justification of printing offspring phenotypes and their ratios
max_length = 0
for string in allele_count.keys():
    length = len(string)
    if length > max_length:
        max_length = length

print('=' * (max_length + 4))
count_list = list(allele_count.values())
for i, key in enumerate(allele_count):
    print(key.ljust(max_length) + ': ' + str(count_list[i][0]))
