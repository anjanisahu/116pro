import csv
import plotly.express as px
import plotly.graph_objects as go
import statistics
import pandas as pd
import plotly.figure_factory as ff
import random
from sklearn.model_selection import train_test_split
df=pd.read_csv("regression.csv")
purchases=df["Purchased"]
factors=[["EstimatedSalary","Age"]]
#variable
salary_train,salary_test,purchase_train,purchase_test = train_test_split(factors,purchases,test_size = 0.25,random_state = 0)
from sklearn.preprocessing import StandardScaler
print(salary_train[0:10])  
sc_x = StandardScaler() 
salary_train = sc_x.fit_transform(salary_train) 
salary_test = sc_x.transform(salary_test)
print(salary_train[0:10])
