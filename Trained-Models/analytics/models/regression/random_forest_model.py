import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.grid_search import GridSearchCV
import data.DataParser as dp
from sklearn.externals import joblib

subjects = ["Art","Citizenship_Education","English","Geography","Health","History","Mathematics","PTS","Religion","Science","Sinhala","Tamil"]
    
for subject in subjects :
    
    df = dp.generate_dataset([subject])
    
    target = df[subject+"_9"]
    train = df.loc[:, df.columns != subject+'_9']
    
    
    param_grid = {
        'bootstrap': [True],
        'max_depth': [80, 90, 100, 110],
        'max_features': [2, 3],
        'min_samples_leaf': [3, 4, 5],
        'min_samples_split': [8, 10, 12],
        'n_estimators': [100, 200, 300, 1000]
    }
    
    grid = GridSearchCV(estimator = RandomForestRegressor(),
                        param_grid = param_grid,
                        cv=10,
                        scoring='neg_mean_squared_error')
    
    grid.fit(train,target)
    
    joblib.dump(grid.best_estimator_, 'joblibs/rnd'+subject+'_xgb.joblib') 