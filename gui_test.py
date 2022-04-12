import streamlit as st
from enron import create_columns,get_top_10_dt_matrix,get_words_list,clean_word
from enron import create_document_term_matrix,stemmed_word,create_variables
from enron import get_number_emails
import pandas as pd

st.set_page_config(layout="wide")

emails = pd.read_csv("emails-small.csv")    
From,To,Date, Subject, Body = create_variables(emails["message"])
emails = create_columns(From,To,Date,Subject,Body,emails)
list_emails = get_number_emails(emails)
test = 0


my_options = ["ceo","paper","work"]

st.markdown("# Enron")
st.markdown("## email")

st.markdown("### Select the topic")


option = st.selectbox(label="topic-test-input",key="first-selection",options=my_options)
option = st.multiselect(label="topic-test-input2",key="second-selection",options=my_options)

option_email = st.selectbox(label="Test email",key="test-email",options=list_emails)



my_body = emails["Body"][option_email]
From = emails["From"][option_email]
Date = emails["Date"][option_email]
To = emails["To"][option_email]
Subject = emails["Subject"][option_email]

st.markdown("#### Original email")
st.markdown(f"##### From : {From}")
st.markdown(f"##### Date : {Date}")
st.markdown(f"##### To : {To}")
st.markdown(f"##### Subject : {Subject}")
st.markdown(f"##### Email")
st.markdown(f"<p style='color:yellow'>{my_body}</p>",unsafe_allow_html=True)


body = get_words_list(my_body)
stemmed_body = stemmed_word(body)
body_cleaned = clean_word(stemmed_body)
df = create_document_term_matrix(body_cleaned)

st.markdown("#### cleaned email")
st.markdown(body_cleaned[0])

st.markdown("#### Document Term Matrix")
st.dataframe(df)

st.markdown("#### Top 10 tag")
st.table(get_top_10_dt_matrix(df))




hide_st_style = """
            <style>
            .css-18e3th9 {
                    padding-top: 0rem;
                    padding-bottom: 10rem;
                    padding-left: 5rem;
                    padding-right: 5rem;
                }
               .css-1d391kg {
                    padding-top: 3.5rem;
                    padding-right: 1rem;
                    padding-bottom: 3.5rem;
                    padding-left: 1rem;
                }
            
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style,unsafe_allow_html=True)