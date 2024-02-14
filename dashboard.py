import pandas as pd 
import plotly.express as px
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title='ONLINE SHOPING', layout='wide', page_icon="tshirt")
st.title(":tshirt: :blue[ONLINE SHOPING] :tshirt:")
df=pd.read_csv('C:/Users/DSAI/Desktop/project/shopping_behavior_updated (1).csv')
with st.sidebar:
    selected = option_menu(menu_title="Main Menu",options=["Data", "Charts", "Bar1","Bar2","Conclusion"],icons=["bar","bar","bar","bar","bar"]
                       ,menu_icon="cast",default_index=0)



if selected=="Data":
    st.subheader("Description")
    st.markdown('The Consumer Behavior and Shopping Habits Dataset is a robust collection of consumer information crucial for market analysis and tailored marketing strategies. It covers Customer IDs for identification, Age and Gender for demographics, and Purchase Amount in USD for transaction value. Details like Item Purchased, Category, and Location provide insights into product preferences and regional trends. Size, Color, and Season data cater to specific consumer choices.')
    st.subheader("Data")
    df=pd.read_csv('C:/Users/DSAI/Desktop/project/shopping_behavior_updated (1).csv')
    df
if selected=="Charts":
    col1,col2=st.columns(2)
    with col1:
        st.subheader(':green[Bar-Chart of Shoping Season]')
        fig7 = px.bar(data_frame=df, x=df['Season'].value_counts().index,
       y=df['Category'].value_counts().values,
       color_discrete_sequence=px.colors.qualitative.Antique,width=350)
        st.plotly_chart(fig7, use_container_width=True)
    with col2:
        st.subheader(':green[Pie of Categories oF Shoping]')
        fig1 = px.pie(names=df['Category'].value_counts().index, values=df['Category'].value_counts().values,
                       color_discrete_sequence=px.colors.qualitative.Pastel,width=350)
        st.plotly_chart(fig1, use_container_width=True)
    col1,col2=st.columns(2)
    with col1:
        st.subheader(':green[Donut Chat of Subscription Status]')
        fig2 = px.pie(df, names='Subscription Status',width=300,hole=0.5,color_discrete_sequence=px.colors.qualitative.Set2)
        st.plotly_chart(fig2)
    with col2:
       st.subheader(':green[Size Bought by Different Age Groups]')
       fig = px.bar(df, x='Size', y='Age',
                 color='Gender',width=400)
       st.plotly_chart(fig)
     
if selected=="Bar1":   
       st.subheader(':green[Payment Method of Male/Female]')
       selected_Gender = st.selectbox("Gender", df['Gender'].unique())
       a = df[df['Gender'] == selected_Gender][['Payment Method', 'Purchase Amount (USD)']]
       fig6 = px.bar(data_frame=a, x='Purchase Amount (USD)', y='Payment Method',
              color_discrete_sequence=px.colors.qualitative.Set2, width=350)
       st.plotly_chart(fig6, use_container_width=True)

if selected=="Bar2":
       st.subheader(':green[Item Purchase in Perticular Location]')
       selected_Location = st.selectbox("Location", df['Location'].unique())
       b = df[df['Location'] == selected_Location][['Purchase Amount (USD)', 'Item Purchased']]
       fig6 = px.bar(data_frame=b, x='Item Purchased', y='Purchase Amount (USD)',
              color='Item Purchased', width=350)
       st.plotly_chart(fig6, use_container_width=True)
if selected=="Conclusion":
    st.markdown(':red[Bar-Chart of Shoping Season]')
    st.markdown('Highest shoping done in Spring Season ')
    st.markdown(':red[Pie of Categories oF Shoping]')
    st.markdown('Highest shoping Category is Clothing ')
    st.markdown(':red[Donut Chat of Subscription Status]')
    st.markdown('only 27% have Subscription ')
    st.markdown(':red[Size Bought by Different Age Groups]')
    st.markdown('Size M were Bought by Peoples')
    st.markdown(':red[Payment Method of Male/Female]')
    st.markdown('Mostly Males pay by cash and Females pay by paypal')
    st.markdown(':red[Item Purchase in Perticular Location]')
