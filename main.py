#%% import libraries
import pickle
from sklearn.base import BaseEstimator, TransformerMixin

#%% UTILITY FUNCTIONS

# normalize_hour 
class normalize_hour(BaseEstimator, TransformerMixin):
  def __init__(self):
    # print('__init__')
    return None

  def fit(self, X, y=None):
    return self

  def transform(self, X, y=None):
    X_ = X.copy()
    X_ = X_/24
    # return X_.todense()
    return X_
    
# Normalize_weekdays()
class normalize_weekday(BaseEstimator, TransformerMixin):
  def __init__(self):
    # print('__init__')
    return None

  def fit(self, X, y=None):
    return self

  def transform(self, X, y=None):
    X_ = X.copy()
    X_ = X_/6
    # return X_.todense()
    return X_

# day_diff_365
class days_diff_365(BaseEstimator, TransformerMixin):
  def __init__(self):
    # print('__init__')
    return None

  def fit(self, X, y=None):
    return self

  def transform(self, X, y=None):
    X_ = X.copy()
    X_ = X_/365
    # return X_.todense()
    return X_

# facing_product_count()
class facing_prod_count(BaseEstimator, TransformerMixin):
  def __init__(self):
    # print('__init__')
    return None

  def fit(self, X, y=None):
    return self

  def transform(self, X, y=None):
    X_ = X.copy()
    X_ = X_/10
    # return X_.todense()
    return X_




#%% reading model 

filename = '00_Best_m2_rfc_without_extVar_y0_v1_c17v1.sav'
loaded_model = pickle.load(open(filename, 'rb'))



#%% columns order
label = 'vanillacompleteyogurt_chobani_150ml'
date = '2021-11-11'
location_id =  '00163EA7-2B19-1EEC-89AE-C895B5833AC9'
weekday = 3
county = 'Summit County'
chob_category = 'Complete'
img_hour = 13
EmploymentRate= 3.6
NielsenHousingRank = 112.0
HousingPriceIncr = 0.0
CivilianLaborForce=267333
TS =18.77
QV2M = 6.71
RH2M = 49.75 
WS10M = 8.01
WD10M = 167.14
ALLSKY_SFC_SW_DWN = 1.35 
ALLSKY_KT = 0.58
previous_count =  2.0 
day_diff = 1
previous_date = '2021-11-10' 
note = 0
index_col = 0 
y3 = 1
#%% Creating some singles inputs 
One_dataPoint = [['vanillacompleteyogurt_chobani_150ml', '2021-11-11',
       '00163EA7-2B19-1EEC-89AE-C895B5833AC9', 3, 'Summit County',
       'Complete', 13, 3.6, 112.0, 0.0, 267333, 18.77, 6.71, 49.75, 8.01,
       167.14, 1.35, 0.58, 2.0, 1, '2021-11-10', 0, 0, 1]]

Second_dataPoints = [['plainyogurt_chobani_150ml', '2021-12-07',
       '00163EA7-2B19-1EEC-89AE-C97B08FE3ACC', 1, 'Canadian County',
       'Core', 13, 1.5, 480.0, -60.0, 77427, 10.24, 2.62, 34.81, 3.01,
       178.96, 1.0, 0.48, 0.0, 28, '2021-11-09', 0, 4, 0]]

Thrid_dataPoints = [['almondcocolocomultipack_chobani_4x150ml', '2021-12-08',
       '00163EA7-2A6C-1EEC-89AE-C941A91E0E6D', 2, 'Orange County',
       'multipack', 16, 3.7, 6.0, -26.67, 1591638, 16.33, 8.85, 79.62,
       4.23, 273.39, 0.08, 0.34, 0.0, 7, '2021-12-01', 0, 6, 1]]


#%% Function
def model_predicts(X, model):
    model = model 
    X = X

    prediction = model.predict(X)

    return prediction

# %%
model_predicts(Thrid_dataPoints, loaded_model )
