import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
import seaborn as sns
import streamlit as st

data_raw = pd.read_csv('train.csv', sep=',')
data = data_raw.copy()

print('Number of participants: ', len(data))
data.head()

print('Is there any missing value? ', data.isnull().values.any())
print('How many missing values? ', data.isnull().values.sum())
data.dropna(inplace=True)
print('Number of participants after eliminating missing values: ', len(data))
print(data)
col3, col4 = st.columns((1, 3))

data_val = data
fig, ax = plt.subplots(figsize=(25, 10))
sns.set_style("darkgrid")
sns.set_style("dark")
sns.set_theme(style='darkgrid', palette='deep')
sns.heatmap(data_val.corr(), ax=ax, annot=True, annot_kws={"size": 9}, fmt='.1f', linewidths=.5, cbar=True,
            xticklabels=1, yticklabels=1,
            cbar_kws={"orientation": "vertical"}, cmap='BuPu')

with col4:
    st.pyplot(fig)
