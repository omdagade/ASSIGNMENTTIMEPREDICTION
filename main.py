import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pickle


om=pd.read_csv('E:/assignmenttimeprediction.csv')
print(om)

x=om.drop('TIME',axis=1)
y=om['TIME']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 4)
LR=LinearRegression()
LR.fit(x_train,y_train)
prediction=LR.predict(x_test)

r2 = r2_score(y_test, prediction)
mse=mean_squared_error(y_test,prediction)
rmse=np.sqrt(mse)
print("R2 SCORE= ",r2)
print("MEAN SQUARED ERROR= ",mse)
print("ROOT MEAN SQUARED ERROR= ",rmse)

filename="assignmenttimepredictor.sav"
pickle.dump(LR,open(filename,"wb"))


