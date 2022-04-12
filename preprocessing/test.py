import json

with open('data/clean_body.json') as file:
    data = json.load(file)
    print(data[0])