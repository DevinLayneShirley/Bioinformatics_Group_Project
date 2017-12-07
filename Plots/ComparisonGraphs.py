#creates graphs of expression levels for each treatment

#import packages
import pandas
from plotnine import *

#load tables
C1data=pandas.read_table("Control1Counts.txt")
C2data=pandas.read_table("Control2Counts.txt")
O1data=pandas.read_table("Obese1Counts.txt")
O2data=pandas.read_table("Obese2Counts.txt")

#name columns of tables
C1data.columns=['Count','sample','Model'] #define column names in dataframe 'data'
C2data.columns=['Count','sample','Model']
O1data.columns=['Count','sample','Model']
O2data.columns=['Count','sample','Model']

#create histogram plots
ggplot(C1data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Control1 Transcript Counts')+ theme ( axis_text_x = element_text ( angle = 90 ))
ggplot(C2data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Control2 Transcript Counts')+ theme ( axis_text_x = element_text ( angle = 90 ))
ggplot(O1data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Obese1 Transcript Counts')+ theme ( axis_text_x = element_text ( angle = 90 ))
ggplot(O2data,aes(x='Model',y='Count'))+geom_col(size=20)+ggtitle('Obese2 Transcript Counts')+ theme ( axis_text_x = element_text ( angle = 90 ))

