import pandas as pd
import streamlit as st
import numpy as np
df = pd.read_csv('breath_col_list.csv')

st.title('呼吸関連カラム名のリスト')
st.dataframe(df, width=600)
