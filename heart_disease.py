#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


# In[ ]:


st.title('Heart disease')


#     Namen: Saadia Dif
#            Jesse van Evert
#            Sandor Miezenbeek
#            Nadia Portier
#     Groep: nr 3
# 

# In[ ]:


st.header('Steps')


# In[ ]:


st.write('1. Kaggle API')
st.write('2. DATA')
st.write('3. Exploratory Data Analysis and Understanding the problem')
st.write('4. Data Analysis')
st.write('5. Cleaning dataset')
st.write('6. Modeling')
st.write('7. Evaluation')


# In[ ]:


st.header('Kaggle API')


# In[ ]:


st.write('Eerst moet kaggle worden geïnstalleerd met de command: pip install kaggle.')
st.write('Daarna moet er een API token worden gedownload van kaggle; deze token moet je vervolgens naar de .kaggle map op je computer kopiëren.')
st.write('Vervolgens moet je de API importeren zoals hieronder:')


# In[7]:


st.code('from kaggle.api.kaggle_api_extended import KaggleApi', language='python')
from kaggle.api.kaggle_api_extended import KaggleApi


# In[ ]:


st.write('Nadat de API is geïmporteerd kennen we deze toe aan een variabele. '
         'Daarna voeren we authenticate() uit want je moet geauthenticeert zijn voordat je data kan binnenhalen.')


# In[8]:


st.code('api = KaggleApi()', language='python')
st.code('api.authenticate()', language='python')
api = KaggleApi()
api.authenticate()


# In[ ]:


st.write('Na de voorstaande stappen te hebben uitgevoerd kunnen we een dataset downloaden via de API op de onderstaande manier:')


# In[9]:


st.code("api.dataset_download_file('johnsmith88/heart-disease-dataset', file_name='heart.csv')", language='python')
#api.dataset_download_file('johnsmith88/heart-disease-dataset', file_name='heart.csv')


# In[ ]:


st.header('3. Data')


# In[10]:


heart_disease_df = pd.read_csv('heart.csv')


# In[11]:


heart_disease_df_rename = pd.read_csv('heart.csv')


# In[12]:


st.dataframe(heart_disease_df.head())


# In[ ]:


st.write('De afkorting van sommige kolomen zijn nietszeggend, dus deze gaan we veranderen')


# In[13]:


heart_disease_df_rename.rename(columns={"age": "Age",
                                 "sex": "Sex",
                                "cp": "CPT",
                                "trestbps": "RBP",
                                "chol": "S.Chol",
                                "fbs": "FBP",
                                "restecg": "R.ECG",
                                "thalach": "max.HRA",
                                "exang": "EIA",
                                "oldpeak": "Oldpeak",
                                "slope": "Slope",
                                "ca": "N.mv",
                                "thal": "TSL",
                                "target": "Target"},inplace=True)


# In[14]:


heart_disease_df_rename.columns = [['Age', 'Sex', 'CPT', 'RBP', 'S.Chol', 'FBP', 'R.ECG', 'max.HRA', 'EIA', 'Oldpeak', 'Slope', 'N.mv', 'TSL', 'Target'], 
                            ['', '1=M 0=F', 'type 0-3', '>130-140 concern', '>200 concern', '> 120 1=true 0=false', 'result 0-2', '', '1=yes 0=no', 'in mm', ' up,flat,down 0=better heart 1=healty heart 2=unhealthy heart', 'color vessels 0-3', '1,3= normal 6=fixed defect 7=reversable defect', '1=disease 0=not disease']]  




# In[15]:


st.dataframe(heart_disease_df_rename)


# ### Abbreviations

#     Age		Age					          Age in years
#     Sex     Sex					          1= male 0 = female
#     CPT 	Chest Pain Type		          0= Typical angina: chest pain related decrease blood supply to the heart
#                                           1= Atypical angina: chest pain not related to heart
#                                           2= Non-anginal pain: typically esophageal spasms (non heart related)
#                                           3= Asymptomatic: chest pain not showing signs of disease
#     RBP     Resting Blood Pressure        Above 130-140 is typically cause for concern
#     S.Chol	Serum Cholestoral	          Above 200 is cause for concern 
#     FBP		Fasting Blood Sugar	          > 120 mg/dl 1=true; 0=false 
#                                           >126 mg/dl signals diabetes                               
#     R.ECG	Resting ElectroCardioGraphic  0=Nothing to note
#                                           1= ST T Wave abnormality signals non-normal heart beat
#                                           2= Possible or definite left ventricular hypertrophy
#     max.HRA	Maximum Heart Rate Achieved				
#     EIA		Exercise Induced Angina		  1 = yes 0 = no
#     Oldpeak	                              ST depression induced by exercise relative to rest 
#                                           looks at stress of heart during excercise unhealthy heart will stress more
#     Slope   The slope of the peak 		  0= Upsloping: better heart rate with excercise (uncommon)
#                                           1= Flatsloping: minimal change (typical healthy heart
#                                           2= Downslopins: signs of unhealthy heart
#     N.mv    Number of Major Vessels       Colored by flourosopy	(0-3)
#                                           Colored vessel means the doctor can see the blood passing through
#                                           The more blood movement the better (no clots)
#     TSL		Thalium Stress Result		  1,3= normal
#                                           6= fixed defect: used to be defect but ok now
#                                           7= reversable defect: no proper blood movement when excercising
#     Target	Target Have disease or not	  1 = yes 0 = no

# In[ ]:


st.header('4. Exploratory Data Analysis and Understanding the problem')


# In[ ]:


st.write('Aantal rijen en aantal kolommen')


# In[16]:


st.write(heart_disease_df.shape)


# In[ ]:


st.write('Beknopte samenvatting van de dataset')


# In[17]:


#concise summary of our dataset.
st.write(heart_disease_df.info())


# In[ ]:


st.write('Statistische beschrijving per kolom')


# In[18]:


#Generating descriptive statistics.
st.write(heart_disease_df.describe().T)


# In[ ]:


st.header('5. Data Analysis')


# In[ ]:


st.write('How many people have heart disease or no heart disease')


# In[19]:


st.write(heart_disease_df.target.value_counts())


# In[1]:


#plotting bar chart.
fig = heart_disease_df.target.value_counts().plot(kind = 'bar', color=["lightblue", 'lightpink'])
fig.set_xticklabels(labels=['Has heart disease', "Doesn't have heart disease"], rotation=0);
plt.title("Heart Disease values")
plt.ylabel("Amount");
#st.pyplot(fig)


#     #Van de gehele dataset is er geen groot verschil tussen wel of geen hartziekte hebben. 
#     #Er zijn wel meer mensen die een hartziekte hebben in het figuur. (blauw) 

# In[ ]:


st.write('How many Male/Female are in the dataset')


# In[21]:


st.write(heart_disease_df.sex.value_counts())


# In[22]:


#visualizing in Pie chart
labels = 'Male', 'Female'
explode = (0, 0)

fig1, ax1 = plt.subplots()
ax1.pie(heart_disease_df.sex.value_counts(), explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90, colors = ['#fe9999','#99e9ff'])
ax1.axis('equal')
st.pyplot(fig1)


#     #Er zijn meer mannen dan vrouwen aanwezig in de dataset. 
#     #70% mannen en 30% vrouwen

# In[ ]:


st.write('People of which sex has the most heart disease')


# In[23]:


#Sex; 1= Male, 0=Female
#target; 1= heart disease, 0= no heart disease
st.write(pd.crosstab(heart_disease_df.target, heart_disease_df.sex))


# In[24]:


#visualizing in countplot
fig = sns.countplot(x = 'target', data = heart_disease_df, hue = 'sex', color= 'pink')
fig.set_xticklabels(labels=["Doesn't have heart disease", 'Has heart disease'], rotation=0)
plt.legend(['Female', 'Male'])
plt.title("Heart Disease Frequency for Sex");
st.pyplot(fig)


#     # Onderscheid maken tussen wel en geen hartziektes, man/vrouw. 
#     # Figuur is niet betrouwbaar, er zijn meer mannen aanwezig in de dataset zoals net te zien was in de pie chart. 
#     # In dropdown wordt dit nog weergegeven in percentages 

# In[ ]:


st.write('Age distribution plot')


# In[25]:


#create a distribution plot with normal distribution curve
sns.displot( x = 'age', data = heart_disease_df, bins = 30, kde = True)
skewness=str(heart_disease_df["age"].skew())
kurtosis=str(heart_disease_df["age"].kurt())
plt.legend([skewness,kurtosis],title=("skewness and kurtosis"))
st.plotly_chart(plt)


#     # Er is een leeftijd verdelig te zien
#     # De data is niet normaal verdeeld, dit is te zien aan de 2 toppen
#     
# #Skewness is a measure of symmetry, or more precisely, 
# #the lack of symmetry. A distribution, or data set, 
# #is symmetric if it looks the same to the left and right 
# #of the center point. 
# 
# #Kurtosis is a measure of whether the data are heavy-
# #tailed or light-tailed relative to a normal distribution.

# In[ ]:


st.write('Max. Heart rate distribution plot')


# In[26]:


sns.displot(x = 'thalach', data = heart_disease_df, bins = 30, kde = True, color = 'chocolate')
skewness=str(heart_disease_df["thalach"].skew())
kurtosis=str(heart_disease_df["thalach"].kurt())
plt.legend([skewness,kurtosis],title=("skewness and kurtosis"))
st.plotly_chart(plt)


#     # Er is een maximale hartslagverdeling te zien 
#     # De data is niet normaal verdeeld, dit is de zien aan de scheve verdeling (skewness)

# ### Heatmap

# In[27]:


corr = heart_disease_df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
f, ax = plt.subplots(figsize=(11, 9))
cmap = sns.diverging_palette(230, 20, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot = True);


#     # Er is een heatmap te zien, waar je de correlaties tussen de verschillende categorien kunt bekijken. 
#     # als voorbeeld, de Chest pain (CP) en Target heeft de grootste correlatie van 0.43

# ### 5.1  Slider

# ### Cholesterol and Target

# In[28]:


fig = px.box(heart_disease_df, y='chol', x= 'target', 
            points="all", color='target')
              
sliders = [
    {'steps':[
        {'method':'update','label':'Both',
             'args':[{'visible':[True,True]}]},
        {'method':'update','label':'0, no heart disease',
             'args':[{'visible':[True,False]}]},
        {'method':'update','label':'1, heart disease',
             'args':[{'visible':[False,True]}]}
    ]}
]
 
 
fig.update_layout({'sliders':sliders})
 
 
fig.update_layout({'xaxis':{'title':{'text':'Target'}}})
fig.update_layout({'yaxis':{'title':{'text':'Chol, (>200 concern)'}}})
fig.update_layout({'title':{'text':'High cholesterol leads to heart disease distribution'}})
fig.show()


#     # Cholesterol gehalte >200 mg/dl kan leiden tot een hartziekte
#     # Uit deze visualisatie laat ziet dat alleen een te hoge cholesterol gehalte niet altijd lijdt tot hartziekte
#     # Hier kunnen geen verdere uitspraken gedaan worden, en zou er verdere onderzoek gedaan moeten worden. 

# ### Resting blood pressure, OK and Concern

# In[29]:


fig = px.box(heart_disease_df, y='trestbps', x= 'target', 
            points="all", color='target')
              
sliders = [
    {'steps':[
        {'method':'update','label':'Both',
             'args':[{'visible':[True,True]}]},
        {'method':'update','label':'0, no heart disease',
             'args':[{'visible':[True,False]}]},
        {'method':'update','label':'1, heart disease',
             'args':[{'visible':[False,True]}]}
    ]}
]
 
 
fig.update_layout({'sliders':sliders})
 
 
fig.update_layout({'xaxis':{'title':{'text':'Target'}}})
fig.update_layout({'yaxis':{'title':{'text':'trestbps, (>130 concern)'}}})
fig.update_layout({'title':{'text':'High resting blood pressure leads to heart disease distribution'}})
fig.show()


#     # Resting blood pressure  > 130 kan leiden tot een hartziekte (concern)
#     # Uit deze visualisatie laat ziet dat alleen een te hoge bloeddruk niet altijd lijdt tot hartziekte
#     # Hier kunnen geen verdere uitspraken gedaan worden, en zou er verdere onderzoek gedaan moeten worden, 
#     bijv combinaties met andere categorien

# ### Target and CP 

# In[112]:


fig = px.box(heart_disease_df, y='age', x= 'target', color='cp')
              
sliders = [
    {'steps':[
        {'method':'update','label':'All cp',
             'args':[{'visible':[True,True]}]},
        {'method':'update','label':'cp 0 and 2',
             'args':[{'visible':[True,False]}]},
        {'method':'update','label':'cp 1 and 3',
             'args':[{'visible':[False,True]}]}
    ]}
]
 
 
fig.update_layout({'sliders':sliders})
 
 
fig.update_layout({'xaxis':{'title':{'text':'Target'}}})
fig.update_layout({'yaxis':{'title':{'text':'Age'}}})
fig.update_layout({'title':{'text':'Age vs Target vs Chestpain distribution'}})
fig.show()


# ### 5.2 Checkbox 

# ### Cholesterol gehalte gepaard met Bloeddruk

#     # Nadia nog toevoegen

# In[ ]:





# ### Chest pain and Age

# In[30]:


fig = px.box(heart_disease_df, y='age', x= 'cp', title= 'Chestpain versus age, Boxplot + checkbox ', 
            points="all", color='cp')
fig.update_layout(width = 800, boxgroupgap = 0.2, boxgap = 0.8)
fig.update_xaxes(categoryorder='array')
fig.show()


#     # Spreiding van alle leeftijden van de verschillende typen chestpain
#     # Je kan de verschille typen chestpai selecteren en deselecteren (checkbox)
#     # type 3 lijd tot hartziekte en daar zitten de oudste personen. 
#     
#     
#     0: Typische angina: pijn op de borst gerelateerd aan verminderde bloedtoevoer naar het hart
#     1: Atypische angina: pijn op de borst niet gerelateerd aan het hart
#     2: Niet-angina-pijn: meestal slokdarmspasmen (niet gerelateerd aan het hart)
#     3: Asymptomatisch: pijn op de borst die geen tekenen van ziekte vertoont

# ### 5.3 Dropdown

# #### 5.3.1 Percentage calculations 

# #### Percentage Male/Female

# In[31]:


pd.DataFrame(heart_disease_df.sex.value_counts())


# In[32]:


Gender_dataframe = pd.DataFrame({'total gender': [1025],
                'total male': [713],
            'total female': [312]})
Gender_dataframe 


# In[33]:


Male_df_pct = Gender_dataframe['total male']/Gender_dataframe['total gender']*100
Female_df_pct = Gender_dataframe['total female']/Gender_dataframe['total gender']*100


# In[34]:


print(Male_df_pct)
print(Female_df_pct)


# In[35]:


Gender_df_pct = pd.DataFrame({'Male': [69.6],
                              'Female': [30.4]})
Gender_df_pct


# #### Percentage male and female chest pain type 

# In[36]:


pd.DataFrame(heart_disease_df.cp.value_counts())


# In[37]:


cp_dataframe = pd.DataFrame({'total': [1025],
                'type 0': [497],
            'type 1': [167],
                            'type 2': [284],
                            'type 3': [77]})
cp_dataframe 


# In[38]:


cp_zero_male = len(heart_disease_df[(heart_disease_df.cp==0)&(heart_disease_df.sex==1)])
cp_one_male = len(heart_disease_df[(heart_disease_df.cp==1)&(heart_disease_df.sex==1)])
cp_two_male = len(heart_disease_df[(heart_disease_df.cp==2)&(heart_disease_df.sex==1)])
cp_three_male = len(heart_disease_df[(heart_disease_df.cp==3)&(heart_disease_df.sex==1)])


# In[39]:


cp_zero_female = len(heart_disease_df[(heart_disease_df.cp==0)&(heart_disease_df.sex==0)])
cp_one_female = len(heart_disease_df[(heart_disease_df.cp==1)&(heart_disease_df.sex==0)])
cp_two_female = len(heart_disease_df[(heart_disease_df.cp==2)&(heart_disease_df.sex==0)])
cp_three_female = len(heart_disease_df[(heart_disease_df.cp==3)&(heart_disease_df.sex==0)])


# In[40]:


print(cp_zero_male, cp_one_male, cp_two_male, cp_three_male)
print(cp_zero_female, cp_one_female, cp_two_female, cp_three_female)


# In[41]:


cp_sex_dataframe = pd.DataFrame({'total T0': cp_dataframe['type 0'],
                                  'male T0': [cp_zero_male],
                                  'female T0': [cp_zero_female],
                            'total T1': cp_dataframe['type 1'],
                            'male T1': [cp_one_male],
                            'female T1': [cp_one_female],
                        'total T2': cp_dataframe['type 2'],
                        'male T2': [cp_two_male],
                        'female T2': [cp_two_female],
                    'total T3': cp_dataframe['type 3'],
                    'male T3': [cp_three_male],
                    'female T3': [cp_three_female]
                                 })
cp_sex_dataframe 


# In[42]:


cp0_male_pct = cp_sex_dataframe ['male T0']/cp_sex_dataframe ['total T0']*100
cp0_female_pct= cp_sex_dataframe ['female T0']/cp_sex_dataframe ['total T0']*100

cp1_male_pct = cp_sex_dataframe ['male T1']/cp_sex_dataframe ['total T1']*100
cp1_female_pct= cp_sex_dataframe ['female T1']/cp_sex_dataframe ['total T1']*100

cp2_male_pct = cp_sex_dataframe ['male T2']/cp_sex_dataframe ['total T2']*100
cp2_female_pct= cp_sex_dataframe ['female T2']/cp_sex_dataframe ['total T2']*100

cp3_male_pct = cp_sex_dataframe ['male T3']/cp_sex_dataframe ['total T3']*100
cp3_female_pct= cp_sex_dataframe ['female T3']/cp_sex_dataframe ['total T3']*100


# In[43]:


print(cp0_male_pct)
print(cp0_female_pct)

print(cp1_male_pct)
print(cp1_female_pct)

print(cp2_male_pct)
print(cp2_female_pct)

print(cp3_male_pct)
print(cp3_female_pct)


# In[44]:


cp_df_pct = pd.DataFrame({'male type 0': [73.2],
                          'female type 0': [26.8],
                          
                          'male type 1': [65.9],
                          'female type 1': [34.1], 
                          
                          'male type 2': [61.6], 
                          'female type 2': [38.4], 
                          
                          'male type 3': [83.1],
                          'female type 3': [16.9]})
cp_df_pct


# #### Percentage male/female below and above 200 mg/ml chol 

# In[45]:


below_200_male = len(heart_disease_df[(heart_disease_df.chol<=200)&(heart_disease_df.sex==1)])
above_200_male = len(heart_disease_df[(heart_disease_df.chol>200)& (heart_disease_df.sex==1)])

below_200_female = len(heart_disease_df[(heart_disease_df.chol<=200)&(heart_disease_df.sex==0)])
above_200_female = len(heart_disease_df[(heart_disease_df.chol>200)& (heart_disease_df.sex==0)])


# In[46]:


print(below_200_male, above_200_male)
print(below_200_female, above_200_female)


# In[47]:


chol_sex_dataframe = pd.DataFrame({'male not concern': [below_200_male],
                                  'male concern': [above_200_male],
                                  'female not concern': [below_200_female],
                                   'female concern': [above_200_female]
                          })
chol_sex_dataframe 


# In[48]:


chol_not_concern_male_pct = chol_sex_dataframe ['male not concern']/Gender_dataframe ['total male']*100
chol_concern_male_pct= chol_sex_dataframe ['male concern']/Gender_dataframe ['total male']*100
chol_not_concern_female_pct = chol_sex_dataframe ['female not concern']/Gender_dataframe ['total female']*100
chol_concern_female_pct= chol_sex_dataframe ['female concern']/Gender_dataframe ['total female']*100


# In[49]:


print(chol_not_concern_male_pct)
print(chol_concern_male_pct)

print(chol_not_concern_female_pct)
print(chol_concern_female_pct)


# In[50]:


chol_df_pct = pd.DataFrame({'chol male not concern': [17.8],
                          'chol male concern': [82.2],
                          
                          'chol female not concern': [14.4],
                          'cholfemale concern': [85.6], 
                          })
chol_df_pct


# #### Percentage male/female resting blood pressure below and above 130

# In[51]:


below_130_male = len(heart_disease_df[(heart_disease_df.trestbps<130)&(heart_disease_df.sex==1)])
above_130_male = len(heart_disease_df[(heart_disease_df.trestbps>=130)& (heart_disease_df.sex==1)])

below_130_female = len(heart_disease_df[(heart_disease_df.trestbps<130)&(heart_disease_df.sex==0)])
above_130_female = len(heart_disease_df[(heart_disease_df.trestbps>=130)& (heart_disease_df.sex==0)])


# In[52]:


print(below_130_male, above_130_male)
print(below_130_female, above_130_female)


# In[53]:


trestbps_sex_dataframe = pd.DataFrame({'rbp male not concern': [below_130_male],
                                  'rbp male concern': [above_130_male],
                                  'rbp female not concern': [below_130_female],
                                   'rbp female concern': [above_130_female]
                          })
trestbps_sex_dataframe 


# In[54]:


rbp_not_concern_male_pct = trestbps_sex_dataframe ['rbp male not concern']/Gender_dataframe ['total male']*100
rbp_concern_male_pct= trestbps_sex_dataframe ['rbp male concern']/Gender_dataframe ['total male']*100
rbp_not_concern_female_pct = trestbps_sex_dataframe ['rbp female not concern']/Gender_dataframe ['total female']*100
rbp_concern_female_pct= trestbps_sex_dataframe ['rbp female concern']/Gender_dataframe ['total female']*100


# In[55]:


print(rbp_not_concern_male_pct)
print(rbp_concern_male_pct)

print(rbp_not_concern_female_pct)
print(rbp_concern_female_pct)


# In[56]:


rbp_df_pct = pd.DataFrame({'rbp male not concern': [48.2],
                          'rbp male concern': [51.8],
                          
                          'rbp female not concern': [36.2],
                          'rbp female concern': [63.8], 
                          })
rbp_df_pct


# ### Percentages onder elkaar

# In[57]:


Gender_df_pct


# In[58]:


cp_df_pct


# In[59]:


chol_df_pct


# In[60]:


rbp_df_pct


# ### Dropdown dataframe

# In[61]:


# 0= female 1= male
df_10 = pd.DataFrame({
    'Sex': ['female','male'],
    'CP_type_0': [27, 73],
    'CP_type_1': [34, 66],
    'CP_type_2': [38, 62],
    'CP_type_3': [17, 83],
    
    'Chol_OK': [14, 18],
    'Chol_concern': [86, 82],
    
    'rbp_OK': [36, 48],
    'rbp_concern': [64, 52]
})
df_10


# ### Dropdown

# In[62]:


fig = go.Figure()


# In[63]:


# Add surface trace
fig.add_trace(go.Bar(y=df_10['CP_type_0'], name = 'Chest pain type 0'))
fig.add_trace(go.Bar(y=df_10['CP_type_1'], name = 'Chest pain type 1'))
fig.add_trace(go.Bar(y=df_10['CP_type_2'], name = 'Chest pain type 2'))
fig.add_trace(go.Bar(y=df_10['CP_type_3'], name = 'Chest pain type 3'))

fig.add_trace(go.Bar(y=df_10['Chol_OK'], name = 'Cholesterol OK'))
fig.add_trace(go.Bar(y=df_10['Chol_concern'], name = 'Cholesterol concern'))

fig.add_trace(go.Bar(y=df_10['rbp_OK'], name = 'Bloodpressure OK'))
fig.add_trace(go.Bar(y=df_10['rbp_concern'], name = 'Bloodpressur concern'))
                             
fig.update_layout({'yaxis': {'title':{'text': 'Percentage'}}})
fig.update_layout({'title':{'text': 'Looking at heart disease through CP, Chol and rbp'}})


# In[64]:


dropdown_heart_disease = [
{'label': 'All categories', 'method':'update','args': [{'visible':[True, True, True, True, True, True, True, True]},{'title':'All categories'}]},
    
{'label': 'chest pain type 0', 'method':'update','args': [{'visible':[True, False, False, False, False, False, False, False]},{'title':'Chest pain type 0'}]},
{'label': 'chest pain type 1', 'method':'update','args': [{'visible':[False, True, False, False, False, False, False, False]},{'title':'Chest pain type 1'}]},
{'label': 'chest pain type 2', 'method':'update','args': [{'visible':[False, False, True, False, False, False, False, False]},{'title':'Chest pain type 2'}]},
{'label': 'chest pain type 3', 'method':'update','args': [{'visible':[False, False, False, True, False, False, False, False]},{'title':'Chest pain type 3'}]},
                 
{'label': 'Cholesterol OK ', 'method':'update','args': [{'visible':[False, False, False, False, True, False, False, False]},{'title':'Cholesterol OK <200'}]},
{'label': 'Cholesterol concern', 'method':'update','args': [{'visible':[False, False, False, False, False, True, False, False]},{'title':'Cholesterol concern >200'}]},
    
{'label': 'Bloodpressure OK', 'method':'update','args': [{'visible':[False, False, False, False, False, False, True, False]},{'title':'Bloodpressure OK <130'}]},
{'label': 'Bloodpressure concern', 'method':'update','args': [{'visible':[False, False, False, False, False, False, False, True]},{'title':'Bloodpressure concern >130'}]},

]
 


# ## 6. Cleaning Dataset

# In[107]:


heart_disease_df.isna().sum()


# ##there are no null values

# In[116]:


heart_disease_df.drop(['slope', 'oldpeak', 'exang', 'ca', 'thal', 'fbs'], axis=1)


# ####kolomen gedropt die we niet gebruikt hebben.

# ## 7. Modeling

# ## 8. Evaluation
