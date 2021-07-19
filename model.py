import pandas as pd
import numpy as np
import joblib

data=pd.read_csv('smalldata.csv')

x_col = [ 'followers', 'article', 'document', 'image', 'poll', 'text', 'video', 'achievement', 'call to action','insights', 'job opening','other','num_hashtags', 'num_links', 'contlen' ,'num_hash_ratio','num_links_ratio']
y_col = ['Impressions']

 
X = data[x_col]
y = data[y_col]
y=y['Impressions']

X.columns = [ 'followers', 'article', 'document', 'image', 'poll', 'text', 'video', 'achievement', 'call to action','insights', 'job opening','other','num_hashtags', 'num_links', 'contlen' ,'num_hash_ratio','num_links_ratio']

 
 
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor 
from sklearn.ensemble import RandomForestRegressor

m1 = KNeighborsRegressor(n_neighbors = 8)
m2= XGBRegressor( n_estimators=200,learning_rate=0.04,subsample=0.95,max_depth=4,colsample_bytree=1 ,min_child_weight=2) 
m3=RandomForestRegressor(n_estimators=600,min_samples_split=10,min_samples_leaf=2,max_features='auto',max_depth=30,bootstrap=True)

from sklearn.ensemble import VotingRegressor
vot = VotingRegressor(estimators=[ ('m1', m1), ('m2', m2) ,('m3', m3) ],  n_jobs=-1)
vot.fit(X, y)
#final_model
 
 

filename = 'model.pkl'
joblib.dump(vot, filename)

