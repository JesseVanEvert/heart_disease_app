#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
import plotly.express as px
import streamlit as st


# In[59]:


st.title('API')


# In[60]:


st.write('Eerst moet kaggle worden geïnstalleerd met de command: pip install kaggle')
st.write('Daarna moet er een API token worden gedownload van kaggle; deze token moet je vervolgens naar de .kaggle map op je computer kopiëren.')
st.write('Vervolgens moet je de API importeren zoals hieronder.')


# In[61]:


st.code('from kaggle.api.kaggle_api_extended import KaggleApi', language='python')
from kaggle.api.kaggle_api_extended import KaggleApi


# In[62]:


st.write('Nadat de API is geïmporteerd kennen we deze toe aan een variabele. Daarna voeren we authenticate() uit want je moet geauthenticeert zijn voordat je data kan binnenhalen.')


# In[63]:


st.code('api = KaggleApi()', language='python')
st.code('api.authenticate()', language='python')
api = KaggleApi()
api.authenticate()


# In[64]:


st.write('Na de voorstaande stappen te hebben uitgevoerd kunnen we een dataset downloaden via de API op de onderstaande manier.')


# In[65]:


st.code("api.dataset_download_file('johnsmith88/heart-disease-dataset', file_name='heart.csv')", language='python')
#api.dataset_download_file('johnsmith88/heart-disease-dataset', file_name='heart.csv')


# ## Data verkenning

# In[66]:


heart_disease_df = pd.read_csv('heart.csv')


# In[67]:


heart_disease_df.head()
st.dataframe(heart_disease_df.head())


# In[68]:


heart_disease_df.describe()


# age
# sex
# chest pain type (4 values)
# resting blood pressure
# serum cholestoral in mg/dl
# fasting blood sugar > 120 mg/dl
# resting electrocardiographic results (values 0,1,2)
# maximum heart rate achieved
# exercise induced angina
# oldpeak = ST depression induced by exercise relative to rest
# the slope of the peak exercise ST segment
# number of major vessels (0-3) colored by flourosopy
# thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
# 

# ## Analyse

# ### Slider

# In[69]:


chol_pressure_df = heart_disease_df[['chol', 'thalach', 'age', 'sex', 'target']]
chol_pressure_df.age = pd.to_numeric(chol_pressure_df.age)
chol_pressure_df['sex'] = chol_pressure_df['sex'].astype(int)
sorted_chol = chol_pressure_df.sort_values(['age'], ascending=True)
#heart_disease_df = heart_disease_df.sort_values(['age'], ascending=True)


# In[73]:


fig = px.scatter(sorted_chol, x="chol", y="thalach",
                 animation_frame="age",
                 color="sex",)

fig["layout"].pop("updatemenus")
st.plotly_chart(fig)


# In[72]:


fig = px.scatter(heart_disease_df, x="chol", y="thalach",
                 animation_frame="age",
                 color="sex",)

fig["layout"].pop("updatemenus")
st.plotly_chart(fig)

