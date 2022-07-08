#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd


# In[3]:


#importing the data into jupyter notebook
data = pd.read_csv(r"C:\Users\USER\Videos\New folder (8)\New folder\New folder\python files\project 1\1. Weather Data.csv")


# In[4]:


data


# In[5]:


# showing the first 5 rows of the data
data.head()


# In[6]:


# showimg number of rows & columns
data.shape


# In[7]:


# range of the data
data.index


# In[8]:


#names of column in the data
data.columns


# In[9]:


#datatype of each column
data.dtypes


# In[16]:


# unique values in column(weather)
data['Weather'].unique()


# In[18]:


# no of unique values in all columns
data.nunique()


# In[19]:


#showing number of non-null values in the data
data.count()


# In[20]:


#shows all the unique values with their count in a column(Weather)
data['Weather'].value_counts()


# In[22]:


#provides basic information about dataframe
data.info()


# In[ ]:





# In[ ]:


#find all the unique 'wind speed' values in the data


# In[26]:


data.head(2)


# In[23]:


# no of unique values in all columns
data.nunique()


# In[24]:


# no of unique values in column(Wind Speed_km/h)
data['Wind Speed_km/h'].nunique()


# In[25]:


# All the unique values in column(Wind Speed_km/h)
data['Wind Speed_km/h'].unique()


# In[ ]:





# In[27]:


#find the number of times when the 'weather is exactly clear'
#there are three ways to  get solve this: value_counts, filtering and groupby


# In[28]:


data.head(2)


# In[29]:


#value_counts
#data.head(2)
data.Weather.value_counts()


# In[30]:


#filtering
#data.head(2)
data[data.Weather == 'Clear']


# In[32]:


#groupby
#data.head(2)
data.groupby('Weather').get_group('Clear')


# In[ ]:





# In[33]:


#Find the number of times when the 'Wind speed was exactly 4km/h'


# In[35]:


#using filtering
data.head(2)
data[data['Wind Speed_km/h']==4]


# In[ ]:


#find all the null values in the data


# In[38]:


data.isnull().sum()


# In[39]:


# Rename the column 'Weather' of the dataframe to 'Weather Condition'


# In[41]:


data.rename(columns = {'Weather' : 'Weather Condition'}, inplace = True)


# In[42]:


data.head(2)


# In[ ]:





# In[43]:


# mean of visibility in the dataframe


# In[44]:


data.head(2)


# In[45]:


data.Visibility_km.mean()


# In[ ]:





# In[ ]:


# standard deviation of 'pressure' 


# In[46]:


data.Press_kPa.std()


# In[ ]:





# In[ ]:


# Variance of relative humidity 


# In[47]:


data['Rel Hum_%'].var()


# In[ ]:





# In[ ]:


# All instances when snow was recorded
#there are three ways to solve this: value_counts(), filtering & str.contains


# In[48]:


data.head(2)


# In[52]:


# value_counts()
data['Weather Condition'].value_counts()


# In[54]:


#filtering
data[data['Weather Condition'] == 'Snow']


# In[58]:


# str.contains
data[data['Weather Condition'].str.contains('Snow')]


# In[ ]:





# In[59]:


# All instances when 'Wind speed is above 24' and 'Visibility is 25'


# In[60]:


data.head(2)


# In[62]:


data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]


# In[ ]:


# mean value of each column against each 'Weather Condition'


# In[63]:


data.head(2)


# In[64]:


data.groupby('Weather Condition').mean()


# In[ ]:





# In[ ]:


#minimum & maximum value of each column against the 'Weather Condition'


# In[65]:


data.head(2)


# In[67]:


#minimum value of each column against the 'Weather Condition'
data.groupby('Weather Condition').min()


# In[69]:


# maximum value of each column against the 'Weather Condition'
data.groupby('Weather Condition').max()


# In[ ]:





# In[ ]:


# All the record where Weather Condition is Fog


# In[73]:


#data.head(2)
data[data['Weather Condition'] == 'Fog']


# In[ ]:





# In[ ]:


# All instances when 'Weather is Clear' or 'Visibility is above 40'


# In[74]:


data.head(2)


# In[77]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]


# In[ ]:





# In[ ]:


# find all instance when:
#    A. 'Weather is clear' and 'Relative humidity is greater than 50'
#    or
#    B. 'Visibility is above 40'


# In[78]:


data.head(2)


# In[80]:


data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]


# In[ ]:




