import streamlit as st
from Utils.manage import get_number_emails,load_css,get_list_email_by_token
from Utils.manage import get_dic_subject,remove_nan_subject,get_only_subject
from Utils.manage import get_index_email,load_text
from Utils.model import get_topic,run,get_tokens_by_topic
from Utils.model import show_graph
import pandas as pd
import pickle
from typing import List,Dict


@st.cache
def read_my_csv():
    emails = pd.read_csv("data/full_emails.csv")   
    return emails 

@st.cache
def start_model():
    vis = run()
    return vis

@st.cache
def initiate_dataframe():
    emails:Dict = read_my_csv()
    list_emails = get_number_emails(emails.head(100))
    emails = remove_nan_subject(emails)
    return list_emails,emails

#@st.cache
def create_topic_dict():
    with open("./data/topic_dict.pkl","rb") as file:
        data_dict = pickle.load(file)
        return data_dict


st.set_page_config(layout="wide")
load_css("CSS/style.css")

with open("./data/topic_dict.pkl","rb") as file:
    data_dict = pickle.load(file)

list_subject:List = []
my_options:List = []
list_emails:List = []
my_list:List = []
my_topics = data_dict
list_topic = my_topics.keys()
menu_graph = "Graph - Latent Dirichlet Allocation"
menu_investigation = "Investigation"
menu_history = "History"
menu_contact = "Contact"
my_menu = [menu_investigation,menu_graph,menu_history,menu_contact]

vis = start_model()
my_topic = vis.topic_order


list_emails,emails = initiate_dataframe()
list_subject = [list_emails[number]for number in list_emails]



with st.sidebar:
    st.image("./images/sec2.png")
    option_menu = st.selectbox(label="Menu",key="option-menu",options=my_menu)
    with st.expander("Description"):
        st.markdown("This tool using machine learning will allow you to sort more efficiently to help you in your research task")
    st.image("./images/Enron-logo.png")
    

if option_menu == menu_investigation:

    load_css("CSS/style.css")

    st.markdown("# Enron - email")
    st.markdown("### Investigation")
    column_left,column_right = st.columns(2)

    with column_left:
        option = st.selectbox(label="topic number",key="first-selection",options=list_topic)

    with column_right:
        option_token = st.selectbox(label="tokens",key="second-selection",options=my_topics[option])        
        
    list_emails = get_list_email_by_token(option_token,emails)
    list_subject = get_dic_subject(list_emails,emails)
    my_list = get_only_subject(list_subject)

    option_email = st.selectbox(label="select subject",key="test-email",options=my_list) 

    index_email = get_index_email(option_email)

    my_body = emails["Body"].iloc[index_email]
    From = emails["From"][index_email]
    Date = emails["Date"][index_email]
    To = emails["To"][index_email]
    Subject = emails["Subject"][index_email]

    st.markdown(f"#### Original email [{Subject}]")
    st.markdown(f"##### From : {From}")
    st.markdown(f"##### Date : {Date}")
    st.markdown(f"##### To : {To}")
    st.markdown(f"##### Subject : {Subject}")
    st.markdown(f"##### Email")
    st.markdown(my_body)

elif option_menu == menu_graph:
    load_css("CSS/style-graph.css")
    show_graph(vis)
    with st.expander("Description"):
        load_text("./text/LDA-description.txt")

elif option_menu == menu_history:
    with st.sidebar:
        with st.expander("More"):
            st.markdown("The Enron scandal, or Enron affair, is a case of fraud and financial manipulation discovered in 2001, which resulted in the bankruptcy of the Enron company, a time seventh capitalization of the United States, and in the dismantling and the de facto disappearance of his listener Andersen.")
        

    load_css("CSS/style-history.css")
    st.markdown("## History of Enron")
    with st.expander("Introduction"):
        load_text("./text/history.txt")
        st.image("./images/Ken_Lay.jpg")

elif option_menu == menu_contact:
    with st.sidebar:
        with st.expander("More"):
            st.markdown("Here you will find the team that developed this project.")
    #load_css("CSS/style.css")
    st.markdown("## Becode Bruxelles")
    st.markdown("## Promotion Bouman4")
    st.markdown("### Team TensorFlow")
    st.write("Nemish")
    st.write("Dilsad")
    st.markdown("#### Github")