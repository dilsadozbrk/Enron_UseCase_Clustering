import pickle

with open('data/lemmatized_word_list.pkl', 'rb') as f:
    x = pickle.load(f)

print(x[0:2])