#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


#our question is to take top states who are killed in over speeding ,
#Drunken Driving/Consumption of Alcohol & Drug,Driving on Wrong Side,Jumping Red Light,Use of Mobile Phone.  Here null values is in rank and we not going to take into our analysis.


# In[3]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px


# In[4]:


df=pd.read_csv("D:\projects\data_raw\Rd accident\Road-Accidents-2018-Annexure-36-Reason.csv")
df


# In[5]:


#checking its shape and info it will give as rows and columns.
df.shape


# In[6]:


df.info() #as data types all are given right we go to next .


# In[7]:


#To check dupliactes in States/Uts
df.duplicated().value_counts()


# In[8]:


df.duplicated().sum()


# In[9]:


#descriptive statistical values
df.describe()


# In[10]:


#checking is there any null values
df.isnull().sum()


# In[11]:


df.dropna(inplace=True)


# In[12]:


df.isnull().sum()


# In[13]:


#With Required column forming one new dataframe
data=df[['States/UTs','Over-Speeding - Persons Killed - Number','Drunken Driving/Consumption of Alcohol & Drug - Persons Killed','Driving on Wrong Side - Persons Killed','Jumping Red Light - Persons Killed','Use of Mobile Phone - Persons Killed']]
data


# In[15]:


#counting values
data.value_counts()


# In[16]:


#sorting values of Over-Speeding - Persons Killed - Number
over_speed=data[['States/UTs','Over-Speeding - Persons Killed - Number']]
over_speed


# In[21]:


over_speed.sort_values(by='Over-Speeding - Persons Killed - Number',ascending=False)


# In[22]:


over_speed.reset_index(inplace=True,drop=True)


# In[23]:


over_speed


# In[24]:


#checking outliers
over_speed.boxplot()


# In[25]:


#overall plot state wise persons where killed  by over speeding
fig=px.bar(over_speed,x="States/UTs",y='Over-Speeding - Persons Killed - Number',hover_name='States/UTs',color='Over-Speeding - Persons Killed - Number')
fig.show()


# In[26]:


#top 5 states in India - persons killed by over speeding

top_5=over_speed.head(5)


# In[27]:


fig=px.bar(top_5,x="States/UTs",y='Over-Speeding - Persons Killed - Number',hover_name='States/UTs',color='Over-Speeding - Persons Killed - Number')
fig.show()


# In[28]:


#least 5  states in India persons killed in over speeding
top_5l=over_speed.tail(5)


# In[29]:


fig=px.bar(top_5l,x="States/UTs",y='Over-Speeding - Persons Killed - Number',hover_name='States/UTs',color='Over-Speeding - Persons Killed - Number')
fig.show()


# In[30]:


#values of Over-Speeding - Persons Killed - Number
drunken_drive=data[['States/UTs','Drunken Driving/Consumption of Alcohol & Drug - Persons Killed']]
drunken_drive


# In[31]:


#sorting by values for Drunken Driving/Consumption of Alcohol & Drug - Persons Killed
drunken_drive.sort_values(by='Drunken Driving/Consumption of Alcohol & Drug - Persons Killed',ascending=False)
drunken_drive.reset_index(inplace=True,drop=True)


# In[32]:


drunken_drive


# In[33]:


#checking outliers - 1750 is not that much high value compare to population
drunken_drive.boxplot()


# In[34]:


fig=px.bar(drunken_drive,x="States/UTs",y='Drunken Driving/Consumption of Alcohol & Drug - Persons Killed',title="Drunken Driving/Consumption of Alcohol & Drug - Persons Killed",hover_name='States/UTs',color='Drunken Driving/Consumption of Alcohol & Drug - Persons Killed')
fig.show()


# In[35]:


#top 5 states in India -Drunken Driving/Consumption of Alcohol & Drug - Persons Killed

top_5dd=drunken_drive.head(5)


# In[36]:


#Least 5 states in India -Drunken Driving/Consumption of Alcohol & Drug - Persons Killed
least_5dd=drunken_drive.tail(5)


# In[37]:


fig=px.bar(top_5dd,x="States/UTs",y='Drunken Driving/Consumption of Alcohol & Drug - Persons Killed',hover_name='States/UTs',title='Top 5 States Persons killed in Drunken Driving/Consumption of Alcohol & Drug  ',color='Drunken Driving/Consumption of Alcohol & Drug - Persons Killed')
fig.show()


# In[38]:


fig=px.bar(least_5dd,x="States/UTs",y='Drunken Driving/Consumption of Alcohol & Drug - Persons Killed',hover_name='States/UTs',title='LOWEST 5 States Persons killed in Drunken Driving/Consumption of Alcohol & Drug  ',color='Drunken Driving/Consumption of Alcohol & Drug - Persons Killed')
fig.show()


# In[39]:


#values of Driving on Wrong Side - Persons Killed
driving_wrongside=data[['States/UTs','Driving on Wrong Side - Persons Killed']]
driving_wrongside


# In[40]:


#sorting by values for Driving on Wrong Side - Persons Killed
driving_wrongside.sort_values(by='Driving on Wrong Side - Persons Killed',ascending=False)
driving_wrongside.reset_index(inplace=True,drop=True)
driving_wrongside


# In[41]:


driving_wrongside.boxplot() #2500 is not that much high value compare to population


# In[42]:


dw_top5=driving_wrongside.head(5)


# In[43]:


dw_low5=driving_wrongside.tail(5)


# In[44]:


fig=px.bar(dw_top5,x="States/UTs",y='Driving on Wrong Side - Persons Killed',hover_name='States/UTs',title='TOP 5 STATES IN INDIA - PERSONS KILLED IN DRIVING WRONG SIDE  ',color='Driving on Wrong Side - Persons Killed')
fig.show()


# In[54]:


fig=px.bar(dw_low5,x="States/UTs",y='Driving on Wrong Side - Persons Killed',hover_name='States/UTs',title='LOWEST 5 STATES IN INDIA - PERSONS KILLED IN DRIVING WRONG SIDE  ',color='Driving on Wrong Side - Persons Killed')
fig.show()


# In[46]:


#values of Jumping Red Light - Persons Killed
jumping_red=data[['States/UTs','Jumping Red Light - Persons Killed']]
jumping_red


# In[48]:


#sorting by values for Driving on Wrong Side - Persons Killed
jumping_red.sort_values(by='Jumping Red Light - Persons Killed',ascending=False)
jumping_red.reset_index(inplace=True,drop=True)
jumping_red


# In[49]:


jumping_red.boxplot() #400 is not that much high value compare to population


# In[50]:


jr_top5=jumping_red.head(5)
jr_lw5=jumping_red.tail(5)


# In[51]:


fig=px.bar(jr_top5,x="States/UTs",y='Jumping Red Light - Persons Killed',hover_name='States/UTs',title='TOP 5 STATES IN INDIA -PERSONS KILLED IN JUMPING RED LIGHT',color='Jumping Red Light - Persons Killed')
fig.show()


# In[52]:


fig=px.bar(jr_lw5,x="States/UTs",y='Jumping Red Light - Persons Killed',hover_name='States/UTs',title='LOWEST 5 STATES IN INDIA -PERSONS KILLED IN JUMPING RED LIGHT',color='Jumping Red Light - Persons Killed')
fig.show()


# In[55]:


#values  Use of Mobile Phone - Persons Killed
mobile_phone=data[['States/UTs','Use of Mobile Phone - Persons Killed']]
mobile_phone


# In[60]:


mobile_phone.boxplot() #2000 is not that much high value compare to population


# In[58]:


mp_top5=mobile_phone.head(5)
mp_lowest5=mobile_phone.tail(5)


# In[61]:


fig=px.bar(mp_top5,x="States/UTs",y='Use of Mobile Phone - Persons Killed',hover_name='States/UTs',title='TOP 5 STATES IN INDIA - PERSONS KILLED IN USING MOBILE WHILE DRIVING  ',color='Use of Mobile Phone - Persons Killed')
fig.show()


# In[62]:


fig=px.bar(mp_lowest5,x="States/UTs",y='Use of Mobile Phone - Persons Killed',hover_name='States/UTs',title='LOWEST 5 STATES IN INDIA - PERSONS KILLED IN USING MOBILE WHILE DRIVING  ',color='Use of Mobile Phone - Persons Killed')
fig.show()


# In[ ]:




