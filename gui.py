import streamlit as st
from Utils.manage import get_number_emails,open_css,get_list_email_by_token
from Utils.model import get_topic,run,get_tokens_by_topic
from Utils.model import show_graph
import pandas as pd
from typing import List,Dict


@st.cache
def read_my_csv():
    emails = pd.read_csv("data/data_10k.csv")   
    return emails 

@st.cache
def start_model():
    vis = run()
    return vis



st.set_page_config(layout="wide")
open_css("CSS/style.css")

list_subject:List = []
my_options:List = []
list_emails:List = []

vis = start_model()
my_topic = vis.topic_order

emails:Dict = read_my_csv()
list_emails = get_number_emails(emails.head(100))
list_subject = [list_emails[number]for number in list_emails]
my_menu = ["search","graph"]


with st.sidebar:
    option_menu = st.selectbox(label="Menu",key="option-menu",options=my_menu)
    pass

if option_menu == "search":
    open_css("CSS/style.css")
    st.markdown("# Enron - email")

    st.markdown("### Select the topic")


    option = st.selectbox(label="topic number",key="first-selection",options=my_topic)
    option_token = st.selectbox(label="tokens",key="second-selection",options=get_tokens_by_topic(vis,option))        
    

    list_emails = get_list_email_by_token(option_token,emails)
    
    option_email = st.selectbox(label="select subject",key="test-email",options=list_emails)


    #list_emails:List = []

    #option_email = option_email.split(":")[0]
    #option_email = int(option_email.split("°")[1])

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
    st.markdown(my_body)

elif option_menu == "graph":
    open_css("CSS/style-graph.css")
    show_graph(vis)


