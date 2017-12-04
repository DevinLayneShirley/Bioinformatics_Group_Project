import pandas
from plotnine import *
data=pandas.read_csv("expressionlevels.csv")
plot=ggplot(data,aes(x='Protein',y='ExpressionLevel',color='Treatment'))
plot+geom_jitter(width=.1,height=.3,alpha=.5,size=5)+theme_classic()+ggtitle('Protein Expression Levels for Each Treatment')
?geom_jitter