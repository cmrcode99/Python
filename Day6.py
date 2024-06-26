import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
data= load_diabetes()
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(data.data,data.target, random_state=0)
from sklearn.linear_model import LinearRegression
clf= LinearRegression()
clf.fit(x_train,y_train)
predicted= clf.predict(x_test)
expected= y_test
plt.figure(figsize=(4,3))
plt.scatter(expected, predicted)
plt.plot([0,50],[0,50], "--k")
plt.xlabel("True price($1000s)")
plt.ylabel("Predicted Price($1000s)")
plt.show()
print(predicted)
print(expected)

from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=2)
x_poly= poly_reg.fit_transform(x)