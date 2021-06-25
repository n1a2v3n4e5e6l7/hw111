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
median = statistics.median(data)
mode = statistics.mode(data)
std1start,std1end = mean-std,mean+std
std2start,std2end = mean-2*std,mean+2*std 
std3start,std3end = mean-3*std,mean+3*std
fig = ff.create_distplot([data],["Math_score"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean"))
fig.add_trace(go.Scatter(x = [std,std],y = [0,0.17],mode = "lines",name = "standard deviation"))
fig.add_trace(go.Scatter(x = [std1start,std1start],y = [0,0.17],mode = "lines",name = "standard deviation 1 start"))
fig.add_trace(go.Scatter(x = [std1end,std1end],y = [0,0.17],mode = "lines",name = "standard deviation 1 end"))
fig.add_trace(go.Scatter(x = [std2start,std2start],y = [0,0.17],mode = "lines",name = "standard deviation 2 start"))
fig.add_trace(go.Scatter(x = [std2end,std2end],y = [0,0.17],mode = "lines",name = "standard deviation 2 end"))
fig.add_trace(go.Scatter(x = [std3start,std3start],y = [0,0.17],mode = "lines",name = "standard deviation 3 start"))
fig.add_trace(go.Scatter(x = [std3end,std3end],y = [0,0.17],mode = "lines",name = "standard deviation 3 end"))
fig.show()
datawithin1std = [result for result in data if result>std1start and result<std1end]
datawithin2std = [result for result in data if result>std2start and result<std2end]
datawithin3std = [result for result in data if result>std3start and result<std3end]
print("mean: ",mean)
print("median: ",median)
print("mode: ",mode)
print("standard deviation: ",std)
print("% of data between first standard deviation",(len(datawithin1std)*100/len(data)))
print("% of data between second standard deviation",(len(datawithin2std)*100/len(data)))
print("% of data between third standard deviation",(len(datawithin3std)*100/len(data)))