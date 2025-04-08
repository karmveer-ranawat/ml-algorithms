import os
import numpy as np
import matplotlib.pyplot as plt
import cv2
# Accessing My Google Drive
## Import required libraries
import pandas as pd
## Upload dataset
from google.colab import files
uploaded =files.upload()
Choose Files no files selected Upload widget is only available when the cellhas been
executed in the current browser session. Please rerun this cell to enable.
Saving COVID_DATA5.csv to COVID_DATA5.csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
Dataset = pd.read_csv("COVID_DATA5.csv")
# importing an array of features
x = Dataset.iloc[:, :-1].values
# importing an array of dependent variable
y = Dataset.iloc[:, -1].values
print(x) # returns an array of features
print(y)



Dataset['Total'].fillna(Dataset['Total'].mean())
#Dataset['Total'].fillna(0)
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])],
remainder=’passthrough’)
x = np.array(ct.fit_transform(x))
print(x)



fom sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size =0.3,random_state=1)
print(x_train)


print(x_test)



from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# we only aply the feature scaling on the features other than dummy variables.
x_train[:, 3:] = sc.fit_transform(x_train[:, 3:])
x_test[:, 3:] = sc.fit_transform(x_test[:, 3:])
print(x_train)



print(x_test) 
