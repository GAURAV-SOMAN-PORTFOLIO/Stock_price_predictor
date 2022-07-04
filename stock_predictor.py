# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O5iJbysX3WygNW4n4CBK1Bd2dWSsc_ou
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as  plt
# %matplotlib inline

df = pd.read_csv('TATACONSUM.csv')
df.head()

df.tail()

df1 = df.reset_index()
df.head()

df2 = df1.drop(['Date','Adj Close'],axis = "columns")
df2.head()

plt.plot(df2.Close)

ma100 = df2.Close.rolling(100).mean()
ma200 = df2.Close.rolling(200).mean()
ma100.head(500)

plt.figure(figsize = (13,6))
plt.plot(df.Close)
plt.plot(ma100,'r')
plt.plot(ma200,'g')

y = df2['Close']
X = df2.drop(['Close','index'] ,axis="columns")

X = X.dropna()
y = y.dropna()



from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.1,shuffle=False)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train,y_train)

X_test.shape

y_pred = model.predict(X_test)
y_pred.shape

y_test = y_test.reset_index()

y_test = y_test.drop('index',axis='columns')

plt.figure(figsize=(15,19))
plt.plot(y_test,'b')
plt.plot(y_pred,'g')

model.predict([[652.000000,	655.000000,	640.650024,	2314694.0]])

def prediction(open,high,low,volume):
    close_price = model.predict([[open,high,low,volume]]) 
    return close_price
prediction(727.00,	727.00,	707.00	,	1190195)

import pickle 
with open('TATA_pickle','wb') as f : 
  pickle.dump(model,f)

with open('TATA_pickle','rb') as f : 
  mp = pickle.load(f)

mp.predict([[727.00,	727.00,	707.00	,	1190195]])