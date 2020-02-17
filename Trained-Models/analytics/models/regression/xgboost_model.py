import pandas as pd
import numpy as np
import xgboost
from sklearn.grid_search import GridSearchCV
import data.DataParser as dp
from sklearn.externals import joblib

subjects = ["Art","Citizenship_Education","English","Geography","Health","History","Mathematics","PTS","Religion","Science","Sinhala","Tamil"]
    
for subject in subjects :
    
    df = dp.generate_dataset([subject])
    
    target = df[subject+"_9"]
    train = df.loc[:, df.columns != subject+'_9']
    
    
    params_grid = {
            'max_depth' : [1,2,3],
            'n_estimators' : [5,10,25,50,75,100],
            'learning_rate' : np.linspace(0,1,10)
            }
    
    params_fixed = {'objective' : 'reg:linear',
                    'silent' : True,
                    'missing' : -1}
    
    grid = GridSearchCV(estimator = xgboost.XGBRegressor(**params_fixed),
                        param_grid = params_grid,
                        cv=10,
                        scoring='neg_mean_squared_error')
    
    grid.fit(train,target)
    
    joblib.dump(grid.best_estimator_, 'joblibs/'+subject+'_xgb.joblib') 
