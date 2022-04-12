import os 
from email.parser import Parser
import pandas as pd

root = 'maildir'

def analysis(input_file, to_email, from_email, email_body, ):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = f.read()


        email = Parser().parsestr(data)
        to_email.append(email['to'])
        from_email.append(email['from'])
        date.append(email['date'])
        subject.append(email['subject'])
        email_body.append(email.get_payload())
        path.append(input_file)
    except:
        print("encoding error")

date = []
subject = []
to_email = []
from_email = []
email_body = []
path = []
dictionary = {'From' : from_email, 'To' : to_email, 'Date': date, 'Subject' : subject, 'Body' : email_body, 'Path' : path}


for dir, folders, filenames in os.walk(root):
    for filename in filenames:
        analysis(os.path.join(dir, filename), to_email, from_email, email_body)
        
data_frame = pd.DataFrame(dictionary)
data_frame.to_csv('emails.csv', index=False)