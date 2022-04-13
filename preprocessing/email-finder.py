import pickle
import pandas as pd
from tqdm import tqdm


keywords = []
for i in range (1, 3):
	with open(f'data/lemmatized_word_list_{i}.pkl', 'rb') as f:
		x = pickle.load(f)
	keywords += x
	print(i)

print(len(keywords))

df = pd.read_csv("emails.csv", nrows=20000)

df['Keywords'] = keywords


#print(df['Keywords'].head())

print(df.loc[df['Keywords'].str.contains('bastard', regex=False)])

