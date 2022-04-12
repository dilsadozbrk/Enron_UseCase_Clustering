import streamlit as st
from enron import create_columns,get_top_10_dt_matrix,get_words_list,clean_word
from enron import create_document_term_matrix,stemmed_word,create_variables
from enron import get_number_emails
import pandas as pd

emails = pd.read_csv("emails-small.csv")    
From,To,Date, Subject, Body = create_variables(emails["message"])
emails = create_columns(From,To,Date,Subject,Body,emails)
list_emails = get_number_emails(emails)



my_options = ["lol","si","dodo"]

st.markdown("# Enron")
st.markdown("## email")

st.markdown("### Select the topic")


option = st.selectbox(label="topic",key="first-selection",options=my_options)

option_email = st.selectbox(label="Test email",key="test-email",options=list_emails)



test = emails["Body"][option_email]
body = get_words_list(test)
stemmed_body = stemmed_word(body)
body_cleaned = clean_word(stemmed_body)
df = create_document_term_matrix(body_cleaned)

