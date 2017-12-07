#import packages
import pandas
from plotnine import *

#load tables
C1=pandas.read_csv("control1.csv")
C2=pandas.read_csv("control2.csv")
O1=pandas.read_csv("obese1.csv")
O2=pandas.read_csv("obese2.csv")

#create histogram plots
ggplot(C1,aes(x='Protein',y='Count'))+geom_col(color='lightcoral',fill='lightcoral')+ggtitle('Control1 Transcript Counts')+theme_classic()
ggplot(C2,aes(x='Protein',y='Count'))+geom_col(color='palegreen',fill='palegreen')+ggtitle('Control2 Transcript Counts')+theme_classic()
ggplot(O1,aes(x='Protein',y='Count'))+geom_col(color='paleturquoise',fill='paleturquoise')+ggtitle('Obese1 Transcript Counts')+theme_classic()
ggplot(O2,aes(x='Protein',y='Count'))+geom_col(color='plum',fill='plum')+ggtitle('Obese2 Transcript Counts')+theme_classic()

