import csv
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import statistics
import random
import numpy as np

df=pd.read_csv('data.csv')
fig=px.scatter(df,y='quant_saved',color='rem_any')
fig.show()

with open('data.csv',newline='')as f:
  reader=csv.reader(f)
  savings_data=list(reader)
savings_data.pop(0)
total_entries=len(savings_data)
total_people_given_reminder=0
for data in savings_data:
  if int(data[3])==1:
    total_people_given_reminder+=1
fig=go.Figure(go.Bar(x=['Reminded','Not Reminded'],y=[total_people_given_reminder,(total_entries-total_people_given_reminder)]))
fig.show()


all_savings=[]
for data in savings_data:
  all_savings.append(float(data[0]))
print(f'mean of savings is : {statistics.mean(all_savings)}')
print(f'median of savings is : {statistics.median(all_savings)}')
print(f'mode of savings is : {statistics.mode(all_savings)}')

reminded_savings=[]
not_reminded_savings=[]
for data in savings_data:
  if int(data[3])==1:
    reminded_savings.append(float(data[0]))
  else:
    not_reminded_savings.append(float(data[0]))
print('results for people who were reminded to save : ')
print(f'mean of savings-{statistics.mean(reminded_savings)}')
print(f'median of savings-{statistics.median(reminded_savings)}')
print(f'mode of savings-{statistics.mode(reminded_savings)}')
print('results for people who were not reminded to save : ')
print(f'mean of savings-{statistics.mean(not_reminded_savings)}')
print(f'median of savings-{statistics.median(not_reminded_savings)}')
print(f'mode of savings-{statistics.mode(not_reminded_savings)}')

print(f'stdev of all the data:{statistics.stdev(all_savings)}')
print(f'stdev of people who were reminded : {statistics.stdev(reminded_savings)}')
print(f'stdev of people who were not reminded : {statistics.stdev(not_reminded_savings)}')

age=[]
savings=[]
for data in savings_data:
  if(float(data[5])!=0):
    age.append(float(data[5]))
    savings.append(float(data[0]))
correlation=np.corrcoef(age,savings)
print(f'correlation between the age of the person and their savings is : {correlation[0,1]}')

fig=ff.create_distplot([df['quant_saved'].tolist()],['Savings'],show_hist=False)
fig.show()