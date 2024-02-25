import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import streamlit as st
import pandas as pd
import time
import copy
import matplotlib.pyplot as plt
import plotly_express as px
import seaborn as sns


def app():
    header = st.beta_container()
    dataset = st.beta_container()
    datapreprocessing = st.beta_container()
    features = st.beta_container()
    graphs = st.beta_container()
    model_training = st.beta_container()

    @st.cache
    def get_data(filename):
        data1 = pd.read_csv(filename, sep='\t')

        return data1

    @st.cache
    def feat(data2):
        x = data2.describe()
        return x

    @st.cache
    def pre_data(filename1):

        data2 = filename1.copy()
        return data2

    @st.cache
    def grapy(data4):
        df = data4
        numeric_cols = list(df.select_dtypes(['float64', 'int64']).columns)
        text_data = df.select_dtypes(['object'])
        text_cols = text_data.columns
        return df, numeric_cols, text_cols

    with header:
        st.markdown(
            '<h2 style="background-color:Grey; border-radius:5px; padding:5px 15px ; text-align:center ; font-family:arial;color:white"><i>Analysis</i></h2>',
            unsafe_allow_html=True)
        st.subheader("- Let's understand and analyize it.")

    with dataset:
        with st.beta_expander("Dataset-"):
            st.header("*Online Dataset*")
            dataset = get_data('unsuperdate.csv')

            if st.button('View Data'):
                latest_iteration = st.empty()
                for i in range(100):
                    latest_iteration.info(f' {i + 1} %')
                    time.sleep(0.05)
                time.sleep(0.2)
                latest_iteration.empty()
                st.info("data-final.csv")
                st.write(dataset.head(50))
                x_val = dataset.shape[0]
                y_val = dataset.shape[1]
                st.write("Data-shape :", x_val, "Features :", y_val)

    with datapreprocessing:
        with st.beta_expander("Pre-Processed Data-"):
            st.header("Data after Pre-processing:")
            dd = dataset.copy()
            data = copy.deepcopy(pre_data(dd))
            st.write(data.head())
            pd.options.display.max_columns = 150

            data.drop(data.columns[50:107], axis=1, inplace=True)
            data.drop(data.columns[51:], axis=1, inplace=True)
            st.write('Number of participants: ', len(data))
            data.head()

            st.write('Is there any missing value? ', data.isnull().values.any())
            st.write('How many missing values? ', data.isnull().values.sum())
            data.dropna(inplace=True)
            st.write('Number of participants after eliminating missing values: ', len(data))

            # For ease of calculation lets scale all the values between 0-1 and take a sample of 5000
            if st.button("Final Data"):
                d1 = data.copy()
                d1.drop(d1.columns[50], axis=1, inplace=True)
                st.write(d1.head())
                x_valnew = d1.shape[0]
                y_valnew = d1.shape[1]
                st.write("Data-shape :", x_valnew, "Features :", y_valnew)
    with features:
        with st.beta_expander("Features-"):
            st.header("*Features Description:*")
            y3 = copy.deepcopy(data)
            y3.drop(y3.columns[50], axis=1, inplace=True)
            y = copy.deepcopy(feat(y3))
            st.write(y)
    with graphs:
        with st.beta_expander("Graphical Visualization-"):
            st.header("*Graphical representation:*")
            df, numeric_cols, text_cols = grapy(y3)

            col3, col4 = st.columns((1, 3))

            with col3:
                chart_select = st.selectbox(label="Select the chart-type", options=[
                    'Scatter-plots', 'Histogram', 'Distplot', 'Box-plot', 'Violin-plot', 'Heat-map'
                ])
                if chart_select == 'Scatter-plots':
                    st.subheader("Scatter-plot Settings:")
                    x_values = st.selectbox('X-axis', options=numeric_cols)
                    y_values = st.selectbox('Y-axis', options=numeric_cols)
                    with col4:
                        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
                        st.plotly_chart(plot)
                if chart_select == 'Histogram':
                    st.subheader("Histogram Settings:")
                    x_values = st.selectbox('value', options=numeric_cols)
                    x_val = np.array(df[x_values])
                    fig, ax = plt.subplots(figsize=(15, 9))
                    sns.set_style("dark")
                    sns.set_style("darkgrid")
                    sns.histplot(data=x_val, kde=True)
                    with col4:
                        st.pyplot(fig)
                if chart_select == 'Distplot':
                    st.subheader("Distplot Settings:")
                    x_values = st.selectbox('value', options=numeric_cols)
                    x_val = np.array(df[x_values])
                    fig, ax = plt.subplots(figsize=(15, 9))
                    sns.set_style("dark")
                    sns.set_style("darkgrid")
                    sns.distplot(x_val)
                    with col4:
                        st.pyplot(fig)
                if chart_select == 'Box-plot':
                    st.subheader("Box-plot Settings:")
                    x_values = st.selectbox('X-axis', options=numeric_cols)
                    y_values = st.selectbox('Y-axis', options=numeric_cols)
                    with col4:
                        plot = px.box(data_frame=df, x=x_values, y=y_values)
                        st.plotly_chart(plot)
                if chart_select == 'Violin-plot':
                    st.subheader("Violin-plot Settings:")
                    x_values = st.selectbox('X-axis', options=numeric_cols)
                    y_values = st.selectbox('Y-axis', options=numeric_cols)
                    with col4:
                        plot = px.violin(data_frame=df, x=x_values, y=y_values, points='all', box=True)
                        st.plotly_chart(plot)
                if chart_select == 'Heat-map':
                    st.subheader('Heat-map')

                    data_val = y3
                    fig, ax = plt.subplots(figsize=(25, 10))
                    sns.set_style("darkgrid")
                    sns.set_style("dark")
                    sns.set_theme(style='darkgrid', palette='deep')
                    sns.heatmap(data_val.corr(), ax=ax, annot=True, annot_kws={"size": 9}, fmt='.1f', linewidths=.5,
                                cbar=True, xticklabels=1, yticklabels=1,
                                cbar_kws={"orientation": "vertical"}, cmap='BuPu')

                    with col4:
                        st.pyplot(fig)
    with model_training:
        with st.beta_expander("Model Training-"):
            st.header("Train")
            dnew = data.copy()
            dnew.drop(dnew.columns[50], axis=1, inplace=True)
            st.write(dnew.head())
            if st.button("Score :"):
                data = pd.read_csv('unsuper/outneww.csv', sep=',')
                from sklearn.metrics import silhouette_score
                df_model = data.drop('Clusters', axis=1)
                y = data.iloc[:, [50]]
                score = silhouette_score(df_model, y.values.ravel(), metric='euclidean', sample_size=2000)
                st.write('Silhoutte Score : %.3f' % score)
