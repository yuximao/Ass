
import numpy as np
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

from sklearn import datasets,linear_model


#Loading the dataset
dataset=datasets.load_boston()

x = dataset.data[:,np.newaxis,2]
#getting the data and response of the dataset

y=dataset.target

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#split the data for training and testing
model= linear_model.LinearRegression()
model.fit(x_train,y_train)

y_pred=model.predict(x_test)

# Plot the training points
plt.scatter(x_test, y_test,  color='black')
plt.plot(x_test, y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()