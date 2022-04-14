import pandas as pd
import numpy as np
import nltk
import re
from typing import List,Dict
from nltk.stem import SnowballStemmer as sbs
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt



def create_variables(data):
    """
    This function will create 5 lists. Taking the data from
    the emails["messages"], we can found the "from" the "to" the "date"
    the "subject" of the email for every mail
    """
    Body_list = []
    From_list = []
    To_list = []
    Date_list = []
    Subject_list = []

    for data_message in data:

        email = data_message.split("\n")
        end = False
        message = []

        for part in email:
            if end == False:
                if part.find(":"):
                    if part.startswith("Date:"):
                        Date = part.split(": ")[1]
                    if part.startswith("From:"):
                        From = part.split(": ")[1]
                    if part.startswith("To:"):
                        To = part.split(": ")[1]
                    if part.startswith("Subject:"):
                        Subject = part.split(": ")[1]
                    if part.startswith("X-FileName:"):
                        end = True
            else:
                message.append(part)

        Body = "\n".join(message) #put in one string the body of the email


        From_list.append(From)
        To_list.append(To)
        Subject_list.append(Subject)
        Date_list.append(Date)
        Body_list.append(Body)

    return From_list,To_list,Date_list, Subject_list, Body_list
                

def create_columns(From,To,Date,Subject,Body,emails):
    """
    This function will create 5 news columns in the dataframe
    named emails
    """
    emails["From"] = From
    emails["To"] = To
    emails["Date"] = Date
    emails["Subject"] = Subject
    emails["Body"] = Body
    
    return emails



def get_words_list(body:str) -> List[str]:
    """
    This function is kinda of manual tokenization
    """
    pattern = "\\S+"
    my_list = re.findall(pattern,body)
    my_string = " ".join(my_list)
    pattern = "\\w+"
    my_list = re.findall(pattern,my_string)
    my_string = " ".join(my_list)
    pattern = "\\D+"
    my_list = re.findall(pattern,my_string)
    return my_list



def stemmed_word(body:List[str]) -> List[str]:
    """
    This function replace the list of word by the list of 
    root of the word
    """
    #choose english words
    stemmer = sbs("english")
    body_stemmed = []
    for word in body:
        body_stemmed.append(stemmer.stem(word))
    
    return body_stemmed



def clean_word(body:List[str]) -> List[str]:
    """
    clean the list of word in the body of the email. 
    Delete every word contain in the stop word list.
    """
    #create stop word list
    stop_words = stopwords.words("english")
    body_cleaned = []
    for word in body:
        if word.lower() not in stop_words:
            body_cleaned.append(word)
    
    return list(set(body_cleaned)) #delete duplicate


def create_document_term_matrix(body):
    cv = CountVectorizer()
    X = cv.fit(body)
    my_columns = X.get_feature_names()
    X = cv.transform(body)
    my_values = X.toarray()
    df = pd.DataFrame(my_values,columns=my_columns)
    return df

def get_top_10_dt_matrix(df):
    return list(df.sum().sort_values(ascending=False).head(10).index.values)

def get_number_emails(emails:pd.DataFrame) ->Dict:
    my_list = []
    
    for counter,elem in enumerate(emails["Subject"]):
        my_list.append(f"email n°{counter} : {elem}")
    my_dict = {}
    counter = 0

    for elem in my_list:
        my_dict[counter] = elem
        counter += 1

    return my_dict

def convert_tuples_to_dict(list_tuples):
    counter = 0
    my_dict = {}
    for elem in list_tuples:
        my_dict[counter] = elem[1]
        counter += 1
    return my_dict

if __name__ == "__main__":

    emails = pd.read_csv("emails-small.csv")    
    From,To,Date, Subject, Body = create_variables(emails["message"])
    emails = create_columns(From,To,Date,Subject,Body,emails)
    test = emails["Body"][12]
    body = get_words_list(test)
    stemmed_body = stemmed_word(body)
    body_cleaned = clean_word(stemmed_body)
    df = create_document_term_matrix(body_cleaned)
    print(df)
    print(get_top_10_dt_matrix(df))