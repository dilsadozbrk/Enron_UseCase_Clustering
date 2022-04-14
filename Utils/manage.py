import pandas as pd
from typing import Dict,List
import streamlit as st


def get_number_emails(emails:pd.DataFrame) -> Dict:
    my_list = []
    
    for counter,elem in enumerate(emails["Subject"]):
        my_list.append(f"email n°{counter} : {elem}")
    my_dict = {}
    counter = 0

    for elem in my_list:
        my_dict[counter] = elem
        counter += 1

    return my_dict



def open_css(path):
    with open(path) as file:
        st.markdown(f"<style>{file.read()}</style>",unsafe_allow_html=True)


def get_list_email_by_token(token,emails):
    counter = 0
    word = token
    list_index = []
    for elem in emails["Keywords"]:
        if word in emails["Keywords"].iloc[counter]:
            list_index.append(counter)
        counter += 1
    return list_index


