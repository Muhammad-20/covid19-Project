import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout = "wide", page_title = "Covid19 Analysis")
st.image("https://bourbonnaiscare.com/wp-content/uploads/2020/03/covid-19-pictures-1364x682.jpg")

st.title("Covid19")
page = st.sidebar.radio('Pages', ['Univariate Analysis', 'MultiVariate Analysis'])

if page == 'Univariate Analysis':

    st.title('Univariate Analysis')

    for col in df.columns:
        st.plotly_chart(px.histogram(data_frame= df, x= col, title= col))
elif page == 'MultiVariate Analysis':
        st.plotly_chart(px.bar(data_frame=df,x="Jurisdiction_Residence",y= "COVID_deaths"))

df= pd.read_csv("cleaned_df.csv")
st.dataframe(df)
