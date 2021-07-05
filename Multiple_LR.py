#!/usr/bin/env python
# coding: utf-8

# In[1]:



# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


# Importing the dataset
dataset = pd.read_csv('C:/Users/miant/Desktop/Python/50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[3]:


dataset.head(5)


# In[ ]:


print(X)


# In[ ]:


print(y)


# In[4]:


# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
print(X)


# In[5]:


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[6]:


# Training the Multiple Linear Regression model on the Training set
#This is the same code we used in Simple Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[7]:


# Predicting the Test set results
#Remember that we need to check our training results on the Test set but we can't plot a graph
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2) #we display values with only 2 decimals after the comma
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# In[8]:


#We calculate the precision of the model or r^2
print('The precision of the model is ')
print(regressor.score(X_train, y_train))


# In[9]:



#We build the equation
print('a = ')
print(regressor.coef_)

print('The interception is: ')
print(regressor.intercept_)


# In[10]:


print(regressor.predict([[1, 0, 0, 160000, 130000, 300000]]))


# In[ ]:




