import nltk, re, csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import RegexpParser
from random import shuffle
from nltk.tokenize import PunktSentenceTokenizer
#rom nltk.tokenize import TokenizerI
#from wordcloud import WordCloud

#Initializing for short usage
stopset = list(set(stopwords.words('english')))
ps = PorterStemmer()
lemm = WordNetLemmatizer()

#******* Code that removes links, special characters etc. *************#

def preprocess(y):

    #The following code removes links, special characters etc.
    y = re.sub(r'http\S+', ' ', y)
    y = re.sub(r'[^\x00-\x7f]', r' ', y)
    y = re.sub(r'[^a-zA-Z]+', r' ', y)
    y = re.sub(r'\b\w{1,2}\b', r' ', y)

    return (y.lower())

#******* Code that removes links, special characters etc. *************#
def advprocess(y):

    #tokenizing using word_tokenize function from nltk package
    y = nltk.word_tokenize(y)

    #The following code make use of list comprehension for compact view
    y = [word for word in y if word not in stopset]
    y = [lemm.lemmatize(word) for word in y]
    y = [ps.stem(word) for word in y]


    return (' '.join(y))

training = pd.read_csv("C:\\Users\\bhada\\Downloads\\SMM\\Data_Project\\out_file\\Test_data_fin_1.csv", names =["Hotel_id", "Username", "Sentiment", "Reviews", "Overall","Value", "Rooms", "Location", "Cleanliness", "Check In","Services", "Business Services"], encoding="Latin1",low_memory= False)

print("Review:",training['Reviews'].iloc[1])

training.Reviews = [preprocess(Reviews) for Reviews in training.Reviews]

training.Reviews = [advprocess(Reviews) for Reviews in training.Reviews]

print("Review_update:",training.Reviews.iloc[1])
noun_out = []
disc_out = {}

#********* code to tagged each of the word in the processed reviews ***********************#

for Reviews in training.Reviews:

    tokenized = nltk.word_tokenize(Reviews)

    def process_content():
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)

                for item in tagged:
                    if (item[1][0] == 'N'):
                        noun_out.append(item[0])

                namedEnt = nltk.ne_chunk(tagged)

        except Exception as e:
            print(str(e))

    process_content()

	
# ******************Printing the all the result to the output file sent_out.txt*****************#
outfile = open("sent_out.txt", 'w')
for words in noun_out:
    outfile.write("%s\n" % words)





