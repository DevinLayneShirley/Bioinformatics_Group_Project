#import packages
import pandas
from plotnine import *

# cat all hits files for each transcript
# generate a table of counts - transcript, model, hits
# read table into dataframe
# 4 graphs - subset data (one for each sample)

C1data=pandas.read_table("Control1Counts.txt")
C2data=pandas.read_table("Control2Counts.txt")
O1data=pandas.read_table("Obese1Counts.txt")
O2data=pandas.read_table("Obese2Counts.txt")

C1data.columns=['Count','sample','Model'] #define column names in dataframe 'data'
C2data.columns=['Count','sample','Model']
O1data.columns=['Count','sample','Model']
O2data.columns=['Count','sample','Model']

ggplot(C1data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Control1 Transcript Counts')
ggplot(C2data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Control2 Transcript Counts')
ggplot(O1data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Obese1 Transcript Counts')
ggplot(O2data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Obese2 Transcript Counts')

