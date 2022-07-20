# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st

st.write("Addition of Two numbers")

st.header("User input parameters")

def user_data():
    no1 = st.number_input('Number 1')
    no2 = st.number_input('Number 2')
    
    return (no1 - no2)

ans = user_data()

final = 'Subtraction Result: ' + str(ans)

st.subheader(final)

