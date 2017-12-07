#creates graphs of expression levels for each treatment

#import packages
import pandas
from plotnine import *

#load tables
C1=pandas.read_table("Control1Counts.txt", delimiter= " ", header= None)
C2=pandas.read_table("Control2Counts.txt", delimiter= " ", header= None)
O1=pandas.read_table("Obese1Counts.txt", delimiter= " ", header= None)
O2=pandas.read_table("Obese2Counts.txt", delimiter= " ", header= None)

#name columns of tables
C1.columns=['Count','Treatment','Protein'] #define column names in dataframe 'data'
C2.columns=['Count','Treatment','Protein']
O1.columns=['Count','Treatment','Protein']
O2.columns=['Count','Treatment','Protein']

#create histogram plots
ggplot(C1,aes(x='Protein',y='Count'))+geom_col(color='lightcoral',fill='lightcoral')+ggtitle('Control1 Transcript Counts')+theme_classic()
ggplot(C2,aes(x='Protein',y='Count'))+geom_col(color='palegreen',fill='palegreen')+ggtitle('Control2 Transcript Counts')+theme_classic()
ggplot(O1,aes(x='Protein',y='Count'))+geom_col(color='paleturquoise',fill='paleturquoise')+ggtitle('Obese1 Transcript Counts')+theme_classic()
ggplot(O2,aes(x='Protein',y='Count'))+geom_col(color='plum',fill='plum')+ggtitle('Obese2 Transcript Counts')+theme_classic()

#create cumulative graphs
#add data (concetenated table)
data=pandas.read_table("expressionlevels.txt",delimiter=" ", header=None)
#add columns 
data.columns=['Count','Treatment','Protein']
#create ggplot
plot=ggplot(data,aes(x='Protein',y='Count',color='Treatment'))
#create scatter plot with noise so that all points are visibile 
plot+geom_jitter(width=.1,height=.3,alpha=.5,size=5)+theme_classic()+ggtitle('Protein Expression Levels for Each Treatment')


