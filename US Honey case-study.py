#!/usr/bin/env python
# coding: utf-8

# ## US Honey Case Study

# In[1]:


import numpy as np, pandas as pd, matplotlib.pyplot as plt, seaborn as sns


# In[3]:


df = pd.read_csv(r'C:\Users\Dell1\Desktop\Case Studies\US Honey Case study\US_honey_dataset.csv')


# In[4]:


df.head()


# In[5]:


df.tail()


# In[10]:


df.drop('Unnamed: 0',axis=1, inplace=True )


# In[11]:


df.state.nunique()


# In[12]:


df.shape


# In[13]:


df.info()


# In[14]:


df.describe()


# In[15]:


df.isnull().sum()


# ### Which are the top 5 honey producing states

# In[22]:


df1 = df.groupby('state').sum()['production'].reset_index()


# In[23]:


df1


# In[25]:


df1.sort_values('production', ascending=False).head(5)


# In[26]:


# Inference: North Dakota, California, South Dakota, Florida, Montana are the top 5 honey producing states of all time


# In[27]:


df1.sort_values('production', ascending=False, inplace=True)


# In[28]:


df1.head()


# ### Visualization

# In[31]:


plt.figure(figsize=(15,10))

sns.barplot(data=df1, x=df1.state, y=df1.production)
plt.xticks(rotation=90)
plt.show()


# In[32]:


sns.barplot(data=df1, x=df1.state.head(5), y=df1.production,)
plt.xticks(rotation=90)
plt.show()


# ### The change in Average price of honey in all these years - state wise

# In[35]:


df1 = df.groupby('state').mean()['average_price'].reset_index()


# In[36]:


df1


# In[37]:


df1.sort_values('average_price', ascending=False, inplace=True)


# In[38]:


df1.head()


# ### Visualization

# In[39]:


sns.barplot(data=df1, x=df1.state.head(5), y=df1.average_price,)
plt.xticks(rotation=90)
plt.show()


# In[40]:


plt.figure(figsize=(15,10))

sns.barplot(data=df1, x=df1.state, y=df1.average_price,)
plt.xticks(rotation=90)
plt.show()


# In[41]:


# Inference: The states virginia, illinois, north carolina, nevada, kentucky are the top 5 states with highest prices of honey for all these years.


# ### The change in Average price of honey in all these years - year wise

# In[42]:


df1 = df.groupby('year').mean()['average_price'].reset_index()


# In[43]:


df1


# In[44]:


sns.lineplot(data=df1, x=df1.year, y=df1.average_price)
plt.show()


# In[45]:


# Inference: between 1995 to 2016 honey prices were increasing, and then after 2016 it had a sudden drop


# ### Which was the year when honey production was highest

# In[48]:


df1 = df.groupby('year').sum()['production'].reset_index()


# In[49]:


df1


# In[50]:


df1.sort_values('production', ascending=False, inplace=True)


# In[51]:


df1


# In[52]:


sns.lineplot(data=df1, x=df1.year, y=df1.production)
plt.show()


# In[53]:


# Inference: year 2000 witnessed the maximum production.


# ### Which state had the most contribution in the year 2000

# In[56]:


df1 = df[df.year==2000]


# In[57]:


df1


# In[59]:


df1.sort_values('production', ascending=False)


# ### Visualization

# In[62]:


plt.figure(figsize=(15,10))

sns.barplot(data=df1, x='state', y='production')
plt.xticks(rotation=90)
plt.show()


# In[63]:


plt.figure(figsize=(15,10))

sns.barplot(data=df1.sort_values('production', ascending=False), x='state', y='production')
plt.xticks(rotation=90)
plt.show()


# In[64]:


# Inference: The state of North Dakota had the highest contribution in production for the year 2000.


# ### Which state had most number of colonies in the year 2000

# In[65]:


df1.sort_values('colonies_number', ascending=False)


# ### Visualization

# In[66]:


plt.figure(figsize=(15,10))
sns.barplot(data= df1.sort_values('colonies_number', ascending=False), x='state', y='colonies_number')
plt.xticks(rotation=90)
plt.show()


# In[67]:


#Inteference: California had the most number of colonies in the year 2000, but it did not had the most production for that year.


# ## Inference:
# 
# - North Dakota, California, South Dakota, Florida, Montana are the top 5 honey producing states of all time.
# 
# - The states virginia, illinois, north carolina, nevada, kentucky are the top 5 states with highest prices of honey for all these years.
# 
# - Between 1995 to 2016 honey prices were gradually increasing, and then after 2016 it had a sudden drop.
# 
# - Year 2000 witnessed the maximum honey production.
# 
# - The state of North Dakota had the highest contribution in production for the year 2000.
# 
# - California had the most number of colonies in the year 2000, but it did not had the most production for that year.

# In[ ]:




