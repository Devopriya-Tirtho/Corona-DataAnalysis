#!/usr/bin/env python
# coding: utf-8

# In[51]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


#importing data
org_df = pd.read_csv("covid19_Confirmed_dataset.csv")


# In[7]:


org_df.head()


# In[8]:


#dropping unnecessary cols

df = org_df.drop(["Lat", "Long"], axis=1)


# In[9]:


df.head()


# In[10]:


df_agg = df.groupby("Country/Region").sum()


# In[11]:


df_agg.head()


# In[17]:


#plotting

df_agg.loc["India"].plot()
df_agg.loc["China"].plot()
df_agg.loc["Australia"].plot()
plt.legend()


# In[19]:


df_agg.loc["China"][:3].plot()
plt.legend()


# In[22]:


df_agg.loc['China'].diff().plot()
df_agg.loc['India'].diff().plot()
plt.legend()


# In[23]:


#maximum infection rate in china in one day

df_agg.loc['China'].diff().max()


# In[24]:


#maximum infection rate in India in one day

df_agg.loc['India'].diff().max()


# In[25]:


#maximum infection rate in Australia in one day

df_agg.loc['Australia'].diff().max()


# In[28]:




countries = list(df_agg.index)
max_rate = []
for i in countries:
    max_rate.append(df_agg.loc[i].diff().max())


# In[31]:


df_agg["max_infect_rate"] = max_rate


# In[32]:


df_agg.head()


# In[33]:


corona_data = pd.DataFrame(df_agg["max_infect_rate"])


# In[34]:


corona_data.head()


# In[36]:


corona_data.shape


# In[37]:


df_hrep = pd.read_csv("worldwide_happiness_report.csv")


# In[38]:


df_hrep.head()


# In[39]:


useless_cols = ["Overall rank","Score","Generosity","Perceptions of corruption"]


# In[43]:


df_hrep.drop(useless_cols,axis=1,inplace=True)
df_hrep.head()


# In[44]:


df_hrep.set_index("Country or region",inplace = True)
df_hrep.head()


# In[45]:


corona_data.shape


# In[46]:


df_hrep.shape


# In[47]:


data = corona_data.join(df_hrep,how="inner")
data.head()


# In[49]:


data.corr()


# In[55]:


x = data["GDP per capita"]
y = data["max_infect_rate"]
sns.scatterplot(x,y)


# In[56]:


x = data["GDP per capita"]
y = data["max_infect_rate"]
sns.scatterplot(x,np.log(y)) #apply logscaling to y


# In[57]:


sns.regplot(x,np.log(y))


# In[ ]:


people in developed are more prone to corona virus

