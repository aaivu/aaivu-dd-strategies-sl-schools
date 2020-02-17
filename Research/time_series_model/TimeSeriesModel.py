import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as ax
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import pandas as pd
from copy import deepcopy
import os

dirname = os.path.dirname(__file__)

csv_file_1 = "sirisaman_full.csv";
csv_file_2 = "southland_full.csv";

path_1 = os.path.join(dirname, "../Data/" + csv_file_1);
path_2 = os.path.join(dirname, "../Data/" + csv_file_2);

subject = "Mathematics"

#reading the csv file and selecting subject columns
df1 = pd.read_csv(path_1, usecols=["Index No.",subject, subject + ".1", subject + ".2", subject + ".3", subject + ".4", subject + ".5", subject + ".6", subject + ".7", subject + ".8"]);
df1.fillna(0, inplace=True);

df2 = pd.read_csv(path_2, usecols=["Index No.",subject, subject + ".1", subject + ".2", subject + ".3", subject + ".4", subject + ".5", subject + ".6", subject + ".7", subject + ".8"]);
df2.fillna(0, inplace=True);

def fill_missing(marks,window):
    for i in range(0,len(marks)):
        if(marks[i]<0):
            marks[i] = ewma_forecast(np.array(marks[0:i]),window);

    return marks;

# def naive_forecast(train_data):
#     return [train_data[-1],train_data[-1]];
#
# def simple_average_forecast(train_data):
#     mean = np.mean(train_data);
#     return  [mean, mean];
#
# def order_calculator(array):
#     order=1;
#     for i in range(0,len(array)-2):
#         if(((array[i+1]-array[i])*(array[i+2]-array[i+1]))<0):
#             order = order+1;
#
#     return order;
#
# def auto_regressive_forecast(train_data):
#
#     poly = PolynomialFeatures(degree=order_calculator(train_data));
#     poly_train = poly.fit_transform([[0],[1],[2],[3],[4],[5],[6]]);
#     poly_test = poly.fit_transform([[7],[8]]);
#
#     poly_regr = linear_model.LinearRegression();
#     poly_regr.fit(poly_train, train_data);
#     return poly_regr.predict(poly_test)[0:2];
#
# def moving_average_forecast(input_data, window):
#     return pd.rolling_mean(input_data, window)[7:9]

def ewma_calculator(data, window):

    alpha = 2 /(window + 1.0)
    alpha_rev = 1-alpha

    scale = 1/alpha_rev
    n = data.shape[0]

    r = np.arange(n)
    scale_arr = scale**r
    offset = data[0]*alpha_rev**(r+1)
    pw0 = alpha*alpha_rev**(n-1)

    mult = data*pw0*scale_arr
    cumsums = mult.cumsum()
    out = offset + cumsums*scale_arr[::-1]
    return out

def ewma_forecast(data, window):
    fill_missing(data,window)
    return ewma_calculator(data,window)[-1];

# add data to numpy array
np_marks_array_1 = df1.as_matrix().astype(float);
np_marks_array_2 = df2.as_matrix().astype(float);

input_marks = np.append(np_marks_array_1, np_marks_array_2, axis=0);

index = 223;

train_data = input_marks[index][1:9];
test_data = input_marks[index][9];
predict = ewma_forecast(train_data,3)