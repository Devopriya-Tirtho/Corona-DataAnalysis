# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:50:47 2020

@author: Hp
"""
import streamlit as st
import pydeck as pdk
import plotly.express as px
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

org_df = pd.read_csv("covid19_Confirmed_dataset.csv")

df_agg = df.groupby("Country/Region").sum()
#df_agg.loc["India"].plot()
#df_agg.loc["Bangladesh"].plot()
"""
df_agg.loc['Bangladesh'].diff().plot()
df_agg.loc['India'].diff().plot()
plt.legend()"""

print(df_agg.loc['Bangladesh'].diff().max())

countries = list(df_agg.index)
max_rate = []
for i in countries:
    max_rate.append(df_agg.loc[i].diff().max())
    

df_agg["max_infect_rate"] = max_rate


corona_data = pd.DataFrame(df_agg["max_infect_rate"])



df_hrep = pd.read_csv("worldwide_happiness_report.csv")

useless_cols = ["Overall rank","Score","Generosity","Perceptions of corruption"]


df_hrep.drop(useless_cols,axis=1,inplace=True)




df_hrep.set_index("Country or region",inplace = True)






data = corona_data.join(df_hrep,how="inner")




data.corr()
'''
x = data["GDP per capita"]
y = data["max_infect_rate"]
sns.scatterplot(x,y)'''

x = data["GDP per capita"]
y = data["max_infect_rate"]
sns.scatterplot(x,np.log(y))

sns.regplot(x,np.log(y))




######################































