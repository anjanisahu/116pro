import csv
from turtle import color
import plotly.express as px
import plotly.graph_objects as go
import statistics
import pandas as pd
import plotly.figure_factory as ff
import random
df=pd.read_csv("regression.csv")
purchased=df["Purchased"].tolist()
salary=df["EstimatedSalary"].tolist()
ages=df["Age"].tolist()
print(len(salary))
colours=[]
for i in purchased:
    if (i==0):
        colours.append("red")
    else:
        colours.append("green")
fig=go.Figure(data=go.Scatter(x=salary,y=ages,mode="markers",marker=dict(color=colours)))
fig.show()

