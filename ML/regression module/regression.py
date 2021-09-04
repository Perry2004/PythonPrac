import matplotlib.pyplot as plt
import pandas as pd

# define the size of the figure
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# data preprocessing

# open dataset file
# type equals pandas.core.frame.DataFrame
data = pd.read_csv('./datasets/MSFT.csv')

# set X and Y
# iloc: integer location
X = data.iloc[:, 1]  # first feature, date
Y = data.iloc[:, 2]  # second feature, high

# set x and y labels
plt.xlabel("Open")
plt.ylabel("High")

# scatter and show the figure
# plt.scatter(X, Y)
# plt.show()

# hypothesis y = m * x + c
# initialization
m = 0  # theta one
c = 0  # theta two
L = 0.0001  # the learning rate
epochs = 100  # the number of iterations to perform gradient descent
n = float(len(X))  # number of elements in X

# performing gradient descent
for i in range(epochs):
    Y_pred = m * X + c  # the current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))
    D_c = (-2/n) * sum(Y - Y_pred)  # derivative wrt c
    m = m - L * D_m  # update m
    c = c - L * D_c  # update c

print(m, c)

# making predictions
Y_pred = m * X + c

plt.scatter(X, Y)
plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')
plt.ioff()
plt.show()
