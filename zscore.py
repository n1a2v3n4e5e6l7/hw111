import plotly.figure_factory as ff
import plotly.graph_objects as go 
import statistics
import random
import pandas as pd 
import csv

file = pd.read_csv("medium_data.csv")
data = file["Math_score"].tolist()
mean = statistics.mean(data)
std = statistics.stdev(data)
print("mean : ",mean)
print("std : ",std)

def randommeans(n):
    dataset = []
    for i in range(0,n):
        index = random.randint(0,len(data)-1)
        value = data[index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def showfig(meanlist,std):
    fig = ff.create_distplot([meanlist],["average"],show_hist = False)
    fig.add_trace(go.Scatter(x = [mean,mean],y = [0,12],mode = "lines",name = "mean"))
    fig.add_trace(go.Scatter(x = [std,std],y = [0,12],mode = "lines",name = "standard deviation"))
    fig.show()
def samplestd():
    meanlist = []
    for i in range(0,1000):
        setofmeans = randommeans(100)
        meanlist.append(setofmeans)
    std = statistics.stdev(meanlist)
    
    print ("sampling standard deviation = ",std)
    showfig(meanlist,std)
    return(meanlist[0])
samplemean = samplestd()
zscore = samplemean-mean/std
print(zscore)
