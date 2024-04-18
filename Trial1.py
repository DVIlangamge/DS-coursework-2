import streamlit as st
import pandas as pd
import numpy as np

st.title(''' # Market Basket Analysis Results''')

df = pd.read_excel('G:\Visual Studio\cleaned_dataset_global (1).xlsx')
st.dataframe(df)
