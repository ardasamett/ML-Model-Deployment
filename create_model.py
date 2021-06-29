import pandas as pd
import pickle

df = pd.read_csv("salary.csv")

X = df.iloc[:,0:1].values
y = df.iloc[:,1:2].values

from sklearn.linear_model import LinearRegression

model = LinearRegression().fit(X,y)

pickle.dump(model, open('models/model.pkl','wb'))