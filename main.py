import streamlit as st
import pandas as pd


st.write("""
# Simple Apriori App

""")


uploaded_file = st.file_uploader("Choose a dataset:")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, index_col=0, names=list('abcdefghi'))
    st.write(df)

    items = df.to_dict('records')

    support = st.text_input('Enter your minimum support:')

    if support:
        st.write(support)

        st.write('Your resulting data is:')
        data = pd.DataFrame(items)
        st.dataframe(data)
