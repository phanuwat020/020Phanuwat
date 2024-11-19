import streamlit as st
import pandas as pd

st.title("🎡🎡Website Developing using Python🎡🎡")
st.header("🎡🎡Website Developing using Python🎡🎡")

st.subheader("Phanuwat Rungrueang")
st.image('./img/020.jpg')

dt=pd.read_csv('.data/iris-3.csvs')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))