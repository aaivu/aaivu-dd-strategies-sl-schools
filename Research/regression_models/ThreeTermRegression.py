import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import pandas as pd
import os

dirname = os.path.dirname(__file__)

csv_file_1 = "sirisaman_full.csv";
csv_file_2 = "southland_full.csv";

path_1 = os.path.join(dirname, "../Data/" + csv_file_1);
path_2 = os.path.join(dirname, "../Data/" + csv_file_2);

subject = "English"

# reading the csv file and selecting subject columns
df1 = pd.read_csv(path_1, usecols=[subject, subject + ".1", subject + ".2"]);
df1.fillna(0, inplace=True);
df1.replace('ab', 0, inplace=True);

df2 = pd.read_csv(path_2, usecols=[subject, subject + ".1", subject + ".2"]);
df2.fillna(0, inplace=True);
df2.replace('ab', 0, inplace=True);

# add data to numpy array
np_marks_array_1 = df1.as_matrix().astype(float);
np_marks_array_2 = df2.as_matrix().astype(float);

input_marks = np.append(np_marks_array_1, np_marks_array_2, axis=0);

margin = int(len(input_marks) * (2/3))
train_data = input_marks[:margin, :];
test_data = input_marks[margin:, :];

# generating polynomial numpy arrays
poly = PolynomialFeatures(degree=2);
poly_train = poly.fit_transform(train_data[:, [0]]);
poly_test = poly.fit_transform(test_data[:, [0]]);

poly_train = np.append(poly_train, poly.fit_transform(train_data[:, [1]]), axis=1);
poly_test = np.append(poly_test, poly.fit_transform(test_data[:, [1]]), axis=1);


# polynomial regression
poly_regr = linear_model.LinearRegression();
poly_regr.fit(poly_train, train_data[:, [2]]);

predicted_test_data = poly_regr.predict(poly_test);
print("Mean Square Error :", mean_squared_error(test_data[:, [2]], predicted_test_data));
print("R2 Score :", poly_regr.score(poly_test, test_data[:, [2]]));

# plotting
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(train_data[:, 0], train_data[:, 1], train_data[:, 2]);

plot_data = []
for i in range(0, 100):
    plot_data.append([i]);

poly_plot_data = poly.fit_transform(plot_data)
poly_plot_data = np.append(poly_plot_data, poly_plot_data, axis=1);
predicted_plot_data = poly_regr.predict(poly_plot_data);


for i in range(0,100):
    ax.plot(plot_data, plot_data, predicted_plot_data[:,0], c='r',linewidth=2)

plt.show();