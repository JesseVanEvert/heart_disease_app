#!/usr/bin/env python
# coding: utf-8

# In[47]:


import pandas as pd
import plotly.express as px
import streamlit as st


# In[ ]:


st.title('API')


# In[ ]:


st.write('Eerst moet kaggle worden geïnstalleerd met de command: pip install kaggle')
st.write('Daarna moet er een API token worden gedownload van kaggle; deze token moet je vervolgens naar de .kaggle map op je computer kopiëren.')
st.write('Vervolgens moet je de API importeren zoals hieronder.')


# In[48]:


from kaggle.api.kaggle_api_extended import KaggleApi


# ###### Nadat de API is geïmporteerd kennen we deze toe aan een variabele. Daarna voeren we authenticate() uit want je moet geauthenticeert zijn voordat je data kan binnenhalen.

# In[49]:


api = KaggleApi()
api.authenticate()


# ###### Na de voorstaande stappen te hebben uitgevoerd kunnen we een dataset downloaden via de API op de onderstaande manier.

# In[50]:


#api.dataset_download_file('johnsmith88/heart-disease-dataset', file_name='heart.csv')


# ## Data verkenning

# In[51]:


heart_disease_df = pd.read_csv('heart.csv')


# In[52]:


heart_disease_df.head()


# In[53]:


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

# In[54]:


chol_pressure_df = heart_disease_df[['chol', 'thalach', 'age', 'sex']]
chol_pressure_df.age = pd.to_numeric(chol_pressure_df.age)
chol_pressure_df.sort_values(['age'], ascending=True)
fig = px.scatter(chol_pressure_df, x="chol", y="thalach", animation_frame="age", animation_group="sex",
            color="sex", hover_name="sex",
           log_x=True, size_max=55)

fig["layout"].pop("updatemenus") 
fig.show()

