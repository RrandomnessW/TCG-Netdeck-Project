#Code for table extraction from websites. Extracted the tables for list of episodes from wikipedia.
# install pandas first (pip install)
import pandas as pd #pd represents pandas
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
print( len(simpsons) )
print( simpsons[0] )
print( simpsons[1] )

