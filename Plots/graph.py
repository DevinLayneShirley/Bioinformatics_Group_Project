#import packages
import pandas
from plotnine import *
from scipy.optimize import minimize
from scipy.stats import norm

# cat all hits files for each transcript
# generate a table of counts - transcript, model, hits
# read table into dataframe
# 6 graphs - subset data (one for each transcript)

cat .hits | grep -v '#' | awk '{print $1,$3}' > hits.table

data=pandas.read_csv("hits.table", header=0, index_col=0)
data=pandas.DataFrame({"x": , "y": })
def nllike (p, obs):
	B0=p[0]
	B1=p[1]
	sigma=p[2]
expected =B0+B1*obs.x
nll=-1*norm(expected,sigma).logpdf(obs.y).sum()
return nll

ggplot(data,aes(" "))+geom_histogram()
ggplot(data,aes(" "))+geom_histogram()
ggplot(data,aes(" "))+geom_histogram()
ggplot(data,aes(" "))+geom_histogram()
ggplot(data,aes(" "))+geom_histogram()
ggplot(data,aes(" "))+geom_histogram()
