import streamlit as st
import pandas as pd
import numpy as np
st.title('My first Cloud-app')
st.write("A Simple Dataframe:")
df=pd.DataFrame(np.random.randn(10,2),columns=['Col1','Col2'])
st.dataframe(df)