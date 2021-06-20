import pandas as pd
import numpy as np
import joblib

data=pd.read_csv('dataset.csv')

x_col = [ 'followers', 'article', 'document', 'image', 'poll', 'text', 'video', 'achievement', 'call to action','insights', 'job opening','other','num_hashtags', 'num_links', 'contlen' ]
y_col = ['Impressions']

 
X = data[x_col]
y = data[y_col]
y=y['Impressions']

X.columns=[ 'followers', 'article', 'document', 'image', 'poll', 'text', 'video', 'achievement', 'call to action', 'insights', 'job opening', 'other', 'num_hashtags', 'num_links', 'contlen' ]

val1=np.sqrt( X.loc[:,['followers']] )
val2=np.sqrt( X.loc[:,['num_hashtags']] )
val3=np.sqrt( X.loc[:,['num_links']] )
val4=np.sqrt( X.loc[:,['contlen']] )
X.loc[:,['followers']] = val1
X.loc[:,['num_hashtags']] =val2
X.loc[:,['num_links']] = val3
X.loc[:,['contlen']] = val4
y=np.log(y) 

 
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor 
from sklearn.ensemble import RandomForestRegressor

m1 = KNeighborsRegressor(n_neighbors = 16)
m2 = XGBRegressor( n_estimators=200, learning_rate=0.3, subsample=0.9, max_depth=6, colsample_bytree=0.65, min_child_weight=5)
m3=RandomForestRegressor(n_estimators=110,min_samples_split=20,min_samples_leaf=4,max_features='auto',max_depth=None,bootstrap=True)

from sklearn.ensemble import VotingRegressor
vot = VotingRegressor(estimators=[ ('m1', m1), ('m2', m2) ,('m3', m3) ],  n_jobs=-1)
vot.fit(X, y)
#final_model
 
 

filename = 'model.pkl'
joblib.dump(vot, filename)

