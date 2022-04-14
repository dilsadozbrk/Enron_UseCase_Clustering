# Enron_UseCase_Clustering
## Global Roadmap

| Data Selection | Data Pre-processing | Clustering | Visualization |
| -------------- | ------------------- | ---------- | ------------- |
| Choose relevant folders and parts of emails to focus on | Email content to be cleaned & identify unique keywords | K-Means or Hierarchical Clustering & Topic Modelling | Dropdowns for high-level and low-level topics |
| Result: csv with raw info | Result: matrix containing unique keywords | Result: features/topics and resulting emails | Result: Relevant emails displayed to user based on topic selection


### MVP
1. Selecting an appropriate algorithm
2. Split dataset into chunks
3. High-level topics → displayed on command line (later iterations → sub-topics + streamlit)

### Daily Roadmap
Day 1 → Goal: Data Exploration + Initial Experimentation
- [X] Convert all email files into one raw csv - Dilsad and Aditya
- [X] Extract to, from, subject, and message info from emails - Fortune, Dilsad, Aditya
- [X] Clean message body - Nemish

Day 2 --> Goal: Pre-process data and first iteration of clustering
- [X] Clean message body - Nemish & Fortune
- [X] Streamlit first iteration - Fortune
- [X] Initial implementation of LDA - Dilsad & Aditya

Issue faced:
1. Several errors raised when implementting Mallet-LDA package - Dilsad & Aditya
2. Streamlit installation issue - Fortune
3. Preprocessing code not optimized so extended execution time - Nemish

Day 3 --> Goal: Extract emails based on topics
- [X] Figure out how to extract emails based on topics - Dilsad & Aditya  
- [X] Display extracted emails on Streamlit (dependency on above step) - Fortune
- [X] Complete preprocessing code optimization - Aditya & Nemish
- [X] Pipeline brainstorming

Issued faced:
1. Processing power of machines

Day 4
- [] Run model on entire dataset to get topics & tokens - Dilsad/Aditya
- [] Feed topics & tokens to Streamlit - Fortune
- [] Create dataframe with topics, tokens, and emails - Fortune
- [] Create a structure for project pipeline - Nemish

Day 5

### Ideas
1. User can provide keyword and synonyms could be used to display relevant emails
