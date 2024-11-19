import streamlit as st
import pandas as pd

st.title("❤️❤️Website Developing using Python❤️❤️")
st.header("🚗🚗Website Developing using Python🚗🚗")

st.image('./img/020.jpg')
st.subheader("Nontawat Tingklongton")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))
