import sqlite3
import pandas as pd
import re
import os


# read table with metadata from file through pandas

metadata = pd.read_csv(os.path.join('.', 'data', 'genotyping_data', 'metadata.csv'), index_col=0)


# read basic table from file through pandas

genstudio = pd.read_csv(os.path.join('.', 'data', 'genotyping_data', 'genstudio.csv'), index_col=0, low_memory=False)


# transform values from column 'Position' into two columns 'start' and 'end'

for i in range(genstudio.shape[0]):
    start_coordinate = re.compile(r'\d+\-').findall(genstudio.loc[i, 'Position'])
    if start_coordinate == []:
        genstudio.loc[i, 'Position_start'] = genstudio.loc[i, 'Position']
    else:
        genstudio.loc[i, 'Position_start'] = start_coordinate[0][:-1]

    end_coordinate = re.compile(r'\-\d+').findall(genstudio.loc[i, 'Position'])
    if end_coordinate == []:
        genstudio.loc[i, 'Position_end'] = genstudio.loc[i, 'Position']
    else:
        genstudio.loc[i, 'Position_end'] = end_coordinate[0][1:]

genstudio.drop('Position', axis=1, inplace=True)
genstudio.Position_start = genstudio.Position_start.astype(int)
genstudio.Position_end = genstudio.Position_end.astype(int)


# create sql database and save two tables there

connection = sqlite3.connect('genotyping_data.db')
genstudio.to_sql('genstudio', connection, if_exists='replace', index=False)
metadata.to_sql('metadata', connection, if_exists='replace', index=False)


# select from the database example

select_query = '''
                SELECT Chr, Position_start, Position_end
                FROM   genstudio
                '''
result = connection.execute(select_query).fetchall()
result[:5]


# select unique values

connection.execute('''SELECT DISTINCT Chr FROM genstudio''').fetchall()


# select limited number from the top

result2 = connection.execute('''SELECT *
                                FROM genstudio
                                WHERE `Log R Ratio` > 0.5
                                LIMIT 3''').fetchall()
pd.DataFrame(result2, columns=genstudio.columns)


# select by pattern

connection.execute('''SELECT *
                      FROM genstudio
                      WHERE SNP LIKE "_A%"''').fetchall()[0]


# insersion into the database example

metadata_new = [['unique_id', 'new_breed', 'another_sex'],
                ['one_more_unique_id', 'brand_new_breed', 'one_more_sex']]

insersion_query = '''INSERT INTO
                     metadata(dna_chip_id, breed, sex)
                     VALUES(?, ?, ?)'''

for dna_chip_id, breed, sex in metadata_new:
    connection.execute(insersion_query, (dna_chip_id, breed, sex))

connection.commit()

# or connection.executemany(insersion_query, metadata_new)


# combine two tables, based on the common column with sample_id/dna_chip_id

query = '''CREATE TABLE genstudio_with_metadata AS
                SELECT genstudio.*, metadata.breed, metadata.sex
                FROM   genstudio 
                INNER JOIN metadata 
                ON genstudio.[Sample ID] = metadata.dna_chip_id'''

connection.execute(query)
connection.commit()
connection.close()
