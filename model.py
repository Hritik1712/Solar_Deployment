# -*- coding: utf-8 -*-
"""
Created on Tue May 19 19:43:46 2020

@author: Himanshu
"""

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('C:/Users/Himanshu/Desktop/Project_Deployment/Test.csv')


X = dataset.iloc[:, :4].astype(float)

#Converting words to integer values


y = dataset.iloc[:, -1].astype(float)

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()

#Fitting model with trainig data
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2, 9, 6]]))