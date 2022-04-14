import pandas as pd
from typing import Dict,List


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