import nltk, re, csv
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer
from random import shuffle
training = pd.read_csv("C:\\Users\\bhada\\Downloads\\SMM\\Data_Project\\Data_folder\\Training_data_final.csv", names =["Hotel_id", "Username", "Sentiment", "Reviews", "Overall","Value", "Rooms", "Location", "Cleanliness", "Check In","Services", "Business Services"], encoding="Latin1",low_memory= False)


from sklearn.feature_extraction.text import TfidfVectorizer

#************ tv object to fetch the important feature from the reviews ******************#

tv = TfidfVectorizer(min_df= 10)
X = tv.fit_transform(training["Reviews"])



Y = training["Sentiment"]

from sklearn.utils import shuffle

X, Y = shuffle(X, Y)
#***********************training the data and fitting it with SVM classifier********************#
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.10, random_state=3057)
clf = SVC(kernel="linear", verbose=3)
clf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score

#***********************code that predict the sentiment for rest of the test data******************#

y_pred = clf.predict(X_test)
print(accuracy_score(y_test, y_pred))

df = pd.read_csv("C:\\Users\\bhada\\Downloads\\SMM\\Data_Project\\out_file\\Test_data_fin_1.csv", names =["Hotel_id", "Username", "Sentiment", "Reviews", "Overall","Value", "Rooms", "Location", "Cleanliness", "Check In","Services", "Business Services"], encoding="Latin1")
#print(df.head())
print("Review:",df['Reviews'].iloc[1])

test_review = tv.transform(df["Reviews"])
#print(test_review.shape())
review_predict = clf.predict(test_review)
df["Sentiment"] = review_predict

df.to_csv('res_data_2.csv',sep=',',encoding= 'utf-8')
print(review_predict)
#****************************************end of code**************************************************#



