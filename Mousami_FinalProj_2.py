#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import os
import matplotlib.pyplot as plt
import plotly.express as px


# In[2]:


get_ipython().system('pip install plotly')


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[8]:


get_ipython().system('wget https://raw.githubusercontent.com/HadleyUIUC/FA22-IS445-FinalProject/main/query.csv?token=GHSAT0AAAAAABYFCNAP7YQCN55NVHSPLTD4Y4H5IKQ')


# In[26]:


usgs = pd.read_csv("query.csv", parse_dates=['time'])


# In[192]:


#Adding a new column to the dataframe 1 which records just the date of the observation
usgs['date'] = usgs['time'].dt.date


# In[193]:


#Filtering date after 22nd Nov for the visualization by creating a new dataframe (2)
usgs_1 = usgs[usgs['date'] >= pd.Timestamp('2022-11-22')]
#Parsing the dataframe 2's date
usgs_1['date'] = pd.to_datetime(usgs['date'])


# In[194]:


#Extracting the day information and adding a new column 
usgs_1['day_no'] = usgs_1['date'].dt.day


# In[196]:


usgs_1


# In[209]:


#Plot to visualize the pattern of earthquakes from 22nd Nov
#Plotted against magnitude
#the size of scatter points changes as per the depth of the earthquake
#The color shows the time of the day when the earthquake was recorded.
fig, ax = plt.subplots(dpi = 300)
c = ax.scatter(usgs_1['day_no'], usgs_1['mag'], 
               c = usgs_1['time'].dt.hour, 
               s = usgs_1['depth'].values, 
              alpha = 0.5)
ax.set_xlabel("Day")
ax.set_ylabel("Magnitude")
ax.set_title("Plotting the number of earthquakes per day from 22 Nov onwards")
cbar = fig.colorbar(c)
cbar.set_label('Time of the day (hr)', rotation=270, labelpad=15)


# In[212]:


#Plot to visualize the pattern of earthquakes from 22nd Nov
#Plotted showing everyday occurences
#the size of scatter points changes as per the depth of the earthquake
#The color shows the magnitude of the recorded earthquake.
fig, ax = plt.subplots(dpi = 300)
c = ax.scatter(usgs_1['time'].dt.hour,usgs_1['day_no'], 
               c = usgs_1['mag'], s = usgs_1['depth'].values, 
              alpha = 0.4)
ax.set_xlabel("Hour of the day")
ax.set_ylabel("Day")
ax.set_title("Earthquakes on a daily basis")
cbar = fig.colorbar(c)
cbar.set_label('Magnitude', rotation=270, labelpad=15)


# In[228]:


#Boxplot for errors
usgs_1 = usgs_1.dropna(subset=['magError', 'horizontalError','depthError'])
fig, ax = plt.subplots()
ax.boxplot(usgs_1['magError'], vert = False)
plt.title("Magnitude Error Distribution")
plt.show()


# In[227]:


error = [usgs_1['horizontalError'],usgs_1['depthError']]
fig, ax = plt.subplots()
ax.boxplot(error, vert = False)
plt.title("Horizontal and Depth Error")
ax.set_yticklabels(['Horizontal Error','Depth Error'])
plt.show()


# In[ ]:




