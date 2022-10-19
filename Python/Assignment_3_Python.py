#!/usr/bin/env python
# coding: utf-8

# ## Assignment Python

# 1. Read a file constitution.txt. Create a dictionary with an entry for each letter in the alphabet. The keys are letters and the values will be the counts of the number of times a letter has viewed. Go through each character in `data`, skipping characters that aren't letters. For every letter, increment the count stored in `letter_counts` for that letter. Create a bar chart for the letter frequencies.
# 

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


def alphabet_count(string):
    d = dict()
    letters_counts = 0
    
    for i in range(len(string)):
        if(string[i].isalpha()):
            if string[i] in d:
                d[string[i]] += 1
                letters_counts += 1
            else:
                d[string[i]] = 1
                letters_counts = 1
        else:
            pass
        
        
    return d

file = open('constitution.txt','r')
file1 = file.read()
pd.Series(alphabet_count(file1)).plot.bar(figsize = (15,7))




                
        
    


# In[ ]:





# In[ ]:





#  3. View and analyse the dataset using Pandas. 
# 

# In[3]:


import pandas as pd


#  a.Read data from csv file Federal Aviation Authority (FAA) Dataset

# In[4]:




dataset = pd.read_csv('faa_ai_prelim.csv')
dataset


#  b. View content of the data

# In[5]:



dataset


# c.View the dataset shape

# In[7]:



dataset.shape


# d.Show all the columns present in the dataset

# In[10]:



dataset.columns


#  e.Extract the following attributes from the dataset: 
#  
#  'ACFT_MAKE_NAME', 'LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT'1 'FLT_PHASE', 'EVENT_TYPE_DESC', 'FATAL_FLAG'
# 

# In[9]:


dataset[['ACFT_MAKE_NAME', 'LOC_STATE_NAME', 'ACFT_MODEL_NAME', 'RMK_TEXT', 'FLT_PHASE','EVENT_TYPE_DESC', 'FATAL_FLAG']]


# f. Show missing values count for each column. 
# 

# In[11]:


dataset.isnull().sum()


# g.Clean the dataset and replace the fatal flag NaN with “No”
# 

# In[12]:


dataset.info()


# In[27]:


dataset['FATAL_FLAG'].replace(np.nan,"No")


# h.Verify if the missing values are replaced.
# 

# In[46]:


dataset['FATAL_FLAG'].replace(np.nan,"No",inplace = True)


# i.Remove all the observations where aircraft names (ACFT_MAKE_NAME) are not available
# 

# In[47]:


dataset[dataset['ACFT_MAKE_NAME'].isnull().dropna()]


# j. Find the aircraft types and their occurrences in the dataset
# 

# In[48]:


dataset['ACFT_MAKE_NAME'].value_counts()


# k. Display the observations where fatal flag is “Yes”.
# 

# In[44]:


dataset[dataset['FATAL_FLAG'] == "Yes"]


# l. Show the accidents with fatality.
# 

# In[49]:


dataset[(dataset['EVENT_TYPE_DESC'] == 'Accident') & (dataset['FATAL_FLAG'] == 'Yes')]


# In[ ]:




