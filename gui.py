import streamlit as st
from Utils.manage import get_number_emails
from Utils.model import get_topic,run,get_tokens_by_topic
from Utils.model import show_graph
import pandas as pd
from typing import List,Dict

st.set_page_config(layout="wide")

@st.cache
def read_my_csv():
    emails = pd.read_csv("data/emails.csv")   
    return emails 

@st.cache
def start_model():
    vis = run()
    return vis


vis = start_model()
my_topic = vis.topic_order


list_subject:List = []
my_options:List = []
list_emails:List = []


emails:Dict = read_my_csv()
list_emails = get_number_emails(emails.head(100))
list_subject = [list_emails[number]for number in list_emails]


with st.sidebar:
    st.write("Salut lulu")

st.markdown("# "+f"<p style='background-color:#2F4F4F;font-size:1.2em'>Enron - email</p>",unsafe_allow_html=True)

st.markdown("### Select the topic")


option = st.selectbox(label="topic number",key="first-selection",options=my_topic)
option_token = st.multiselect(label="tokens",key="second-selection",options=get_tokens_by_topic(vis,option),default=get_tokens_by_topic(vis,option))        
option_email = st.selectbox(label="Test email",key="test-email",options=list_subject)

option_email = option_email.split(":")[0]
option_email = int(option_email.split("°")[1])

my_body = emails["Body"].iloc[option_email]
From = emails["From"][option_email]
Date = emails["Date"][option_email]
To = emails["To"][option_email]
Subject = emails["Subject"][option_email]

st.markdown(f"#### Original email [{Subject}]")#change to subject
st.markdown(f"##### From : {From}")
st.markdown(f"##### Date : {Date}")
st.markdown(f"##### To : {To}")
st.markdown(f"##### Subject : {Subject}")
st.markdown(f"##### Email")
st.markdown(f"<p style='color:yellow'>{my_body}</p>",unsafe_allow_html=True)


show_graph(vis)



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