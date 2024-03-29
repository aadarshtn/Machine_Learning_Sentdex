import pandas as pd
import quandl,math,datetime
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

df = quandl.get("WIKI/GOOGL")
df["HL_Percent"] = (df["Adj. High"] - df["Adj. Low"]) / df["Adj. Low"] * 100.00
df["Percent_Change"] = (df["Adj. Close"] - df["Adj. Open"]) / df["Adj. Open"] * 100.00
df = df[["Adj. Close","Adj. Volume","HL_Percent","Percent_Change"]]

forecast_col = "Adj. Close"
df.fillna(-99999,inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out)

df["Label"] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(["Label"],1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:]

df.dropna(inplace=True)
y = np.array(df["Label"])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

##    clf = LinearRegression()
  ##  clf.fit(X_train, y_train)
    ##with open('linearregression.pickle','wb') as f:
      ##  pickle.dump(clf, f)

pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)

accuracy = clf.score(X_test, y_test)
forecast_set = clf.predict(X_lately)

print(forecast_set , accuracy , forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
print(last_unix)
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for x in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc = 2)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()


    







