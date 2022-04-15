import pandas as pd
from typing import Dict,List
import streamlit as st
import re


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


def get_dic_subject(list_emails,emails) -> Dict:
    my_list = []
    
    for counter,elem in enumerate(list_emails):
        subject = emails["Subject"].iloc[elem]
        my_list.append(f"Email n°{elem} : {subject}")
    my_dict = {}
    counter = 0

    for elem in my_list:
        my_dict[counter] = elem
        counter += 1

    return my_dict



def load_css(path):
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


def remove_nan_subject(emails):
    emails["Subject"] = emails["Subject"].fillna("Unknown subject")
    return emails

def get_only_subject(list_subject):
    my_list = []
    for elem in list_subject:
        my_list.append(list_subject[elem])
    return my_list


def get_index_email(option_email):  
    option_email = option_email.split(":")[0]
    option_email = int(option_email.split("°")[1])
    return option_email


def load_text(path):
    with open(path) as file:
        st.markdown(f"<p id='text-history'>{file.read()}</p>",unsafe_allow_html=True)