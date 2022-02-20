import pandas as pd
import numpy as np
import seaborn as sns
import re
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv')
data = data.rename(columns={'pos': 'position'})
data = data.set_index('position')


#plot a diagram with number of reads for each nucleoride and position


ax = data.iloc[:, 9:].plot.bar(figsize=(20, 10), stacked=True)
x_l = ax.set_xlabel('Position')
y_l = ax.set_ylabel('Probability')


#selection of data:
#matches > mean(matches)
#columns pos, reads_all, mismatches, deletions, insertions


data = pd.read_csv('https://raw.githubusercontent.com/Serfentum/bf_course/master/14.pandas/train.csv')
data_selected = data[data.matches > np.mean(data.matches)].iloc[:, :6]
data_selected.to_csv('train_part.csv')


#perform EDA of chosen dataset (including correlations, distribution plots)


breast_cancer = pd.read_csv('./data/data.csv')
breast_cancer.drop('Unnamed: 32', axis=1, inplace = True)
breast_cancer.set_index('id')
breast_cancer = breast_cancer.loc[:, :'fractal_dimension_mean']
breast_cancer.info()

#change object to int (malignant - 1, benigh - 0)
le = LabelEncoder()
breast_cancer.diagnosis = le.fit_transform(breast_cancer.diagnosis)

breast_cancer.iloc[:, 1:].describe()
breast_cancer.iloc[:, 1:].corr()

plt.figure(figsize = (30, 30))
sns.pairplot(breast_cancer.iloc[:, 1:], hue='diagnosis')


#work with real data
#realize functions read_gff and read_bed6


def read_gff(file, names=['chr', 'source', 'type', 'start', 'end',
                          'score', 'strand','phase', 'attributes']):
    ''' 
    reads table from gff format

    :param file: path to file
    :paran names: column names

    :return: pandas dataframe
    '''

    df = pd.read_table(file, sep='\t', comment='#', names=names)

    return df


def read_bed6(file, names=['chr', 'start', 'end',
                           'name', 'score', 'strand']):
    ''' 
    reads table from gff format

    :param file: path to file
    :param names: column names

    :return: pandas dataframe
    '''

    df = pd.read_table(file, sep='\t', names=names)

    return df


gff = read_gff('data/rrna_annotation.gff')
bed = read_bed6('data/alignment.bed')


#from column 'attributes' save only data about rRNA type (16S, 23S, 5S)
gff.attributes = gff.attributes.str.extract(r'([1-6][1-6]?[S])')

#create a table, where the amount of each rRNA is showed for every chromosome (reference genome) + barplot
rrna_chr = gff.groupby('chr').agg({'attributes': 'value_counts'}).convert_dtypes().unstack().fillna(0)
rrna_chr = rrna_chr.reindex(index=rrna_chr.index.to_series().str.rsplit('_').str[-1].astype(int).sort_values().index)

ax = rrna_chr.plot.bar(figsize=(20, 10), stacked=False, colormap='summer')
x_l = ax.set_xlabel('Chromosome')
y_l = ax.set_ylabel('Count')
legend = ax.legend(['16S', '23S', '5S'])


#create a table with data about rRNA fully presented in the assembly (not just a fragment) + data about the contig
intersections = gff.merge(bed, how='right', on='chr', suffixes=['_rna', '_contig'])
intersections = intersections[(intersections.start_rna > intersections.start_contig) &
                              (intersections.end_rna <= intersections.end_contig)]