import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv(r"C:\Users\aka90\Downloads\logit classification.csv")
x = dataset.iloc[:, [2,3]].values
y = dataset.iloc[:,-1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)
'''

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
'''
from sklearn.preprocessing import Normalizer
sc = Normalizer()
x_train = sc.fit_transform(x_train) 
x_test = sc.fit_transform(x_test)
'''
# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB() 
classifier.fit(x_train, y_train)

from sklearn.naive_bayes import BernoulliNB

classifier = BernoulliNB()
classifier.fit(x_train, y_train)


from sklearn.naive_bayes import MultinomialNB

mu = MultinomialNB()
mu.fit(x_train, y_train)
'''
from sklearn.tree import DecisionTreeClassifier, plot_tree
Dc = DecisionTreeClassifier()
Dc.fit(x_train,y_train)






# Predicting the Test set results
y_pred = classifier.predict(x_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)

bias = classifier.score(x_train, y_train)
bias

