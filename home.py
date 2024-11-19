import streamlit as st
import pandas as pd

st.title("🎡🎡Website Developing using Python🎡🎡")
st.header("🎡🎡Website Developing using Python🎡🎡")

st.subheader("Phanuwat Rungrueang")
st.image('./img/020.jpg')

st=pd.read('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(pd.head(10))