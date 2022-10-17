#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


# 1.a Read data from csv file fire department of New York City (FDNY)


file = pd.read_csv('FDNY.csv')


# In[5]:


# 1.b View content of the data

display(file)


# In[6]:


#1.c View first five records

file.head()


# In[7]:


#1.d Skip the first row from dataset while reading

file.loc[1:]


# In[8]:


#1.e View first five records from fixed dataset

file.head(5)


# In[10]:


#1.f Show statistics of the dataset.
file.describe()


# In[12]:


#1.g Display columns of the dataset

file.columns


# In[13]:


#1.h Show the datatypes of each column

file.dtypes


# In[14]:


#1.i View index of dataset

file.index


# In[15]:


#1.j Find the total number of fire department facilities in New York city.

#file['FacilityName'].unique().size
file['FacilityName'].describe()


# In[16]:


#1.k View FDNY information for each borough.

file['Borough'].value_counts()


# In[17]:


#1.l Find the total number of fire department facilities in each borough.(Use groupby)

file.groupby(['Borough']).size()


# In[11]:


#1.m Find total number of fire department facilities in Manhattan (use groupby)

file.groupby(['Borough']).get_group("Manhattan")


# In[18]:


#1.n Clean the dataset and drop null/nan value.

file.dropna(inplace=True)


# In[19]:


file


# In[ ]:




