#add packages
import pandas
from plotnine import *
#add data
data=pandas.read_csv("expressionlevels.csv")
#create ggplot
plot=ggplot(data,aes(x='Protein',y='Count',color='Treatment'))
#create scatter plot with noise so that all points are visibile 
plot+geom_jitter(width=.1,height=.3,alpha=.5,size=5)+theme_classic()+ggtitle('Protein Expression Levels for Each Treatment')
