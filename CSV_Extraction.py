import pandas as pd
# Extract data from csv files
#Comma-separated values (CSV) files - text files that use commas to separate records.
#https://www.football-data.co.uk/englandm.php

# reading 1 csv file from website
df_premier24 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2425/E0.csv')#can write path of file on computer to read csv.
print(df_premier24)

# rename columns
df_premier24.rename(columns={'FTHG':'home_goals',
                             'FTAG':'away_goals'}, inplace=True)
print(df_premier24)