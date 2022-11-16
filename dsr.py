import streamlit as st
import pandas as pd
import plotly.express as plt
data=st.file_uploader("Upload")
if data is not None:
    file=pd.read_csv(data)
    st.write(file.head())
    st.write(plt.box(file['Age']))