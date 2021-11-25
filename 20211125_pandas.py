import seaborn as sns

df= sns.load_dataset('titanic')

df.head()
df.info()
nan_deck=df['deck'].value_counts(dropna=False)
print(nan_deck)

print(df.head().isnull())

print(df.isnull().sum(axis=0))

print(df.dropna(axis=1, thresh=500).columns)

df_age= df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))

print(df['age'].head(10))

mean_age=df['age'].mean(axis=0)

df['age'].fillna(mean_age, inplace=True)

print(df['age'].head(10))

print(df['embark_town'][825:830])

most_freq=df['embark_town'].value_counts(dropna=True).idxmax()

print(most_freq)

df['embark_town'].fillna(most_freq, inplace=True)
import pandas as pd
df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})

df_dup=df.duplicated()
print(df_dup)

col_dup= df['c2'].duplicated()
print(col_dup)

df2= df.drop_duplicates()
print(df2)

df3= df.drop_duplicates(subset=['c2','c3'])
print(df3)

import os

dir=os.getcwd()

df=pd.read_csv(dir+'/part5/auto-mpg.csv', header=None)

df.head()

df.columns= ['mpg','cylinders',' displacement','horsepower','weight','acceleration',
'model year','origin',' name']

mpg_to_kpl=1.60934/3.78541
print(mpg_to_kpl)

df['kpl']=df['mpg']*mpg_to_kpl

print(df.head(3))

df['kpl']=df['kpl'].round(2)

print(df['horsepower'].unique())
import numpy as np
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'],axis=0, inplace=True)
df['horsepower']=df['horsepower'].astype('float')
print(df['horsepower'].dtypes)
df.head(2)
df['origin']=df[' origin']
df.drop([' origin'], axis=1,inplace=True)
df.rename(columns={'nm':'kpl'}, inplace=True)
df.rename(columns={' name':'name'}, inplace=True)

df['origin'].replace({1:'USA', 2:'EU',3:'JPN'}, inplace=True)
print(df['origin'].unique())
print(df['origin'].dtypes)

df['origin']=df['origin'].astype('category')
print(df['origin'].dtypes)
print(df['model year'].sample(3))
df['model year']= df['model year'].astype('category')

df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower']= df['horsepower'].astype('float')

count, bin_dividers= np.histogram(df['horsepower'], bins=3)
print(count, bin_dividers)
bin_names=['저출력','보통출력','고출력']

df['hp_bin']= pd.cut(x=df['horsepower'],
bins=bin_dividers,
labels=bin_names,
include_lowest=True)

print(df[['horsepower','hp_bin']].head(10))

horsepower_dummies= pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(19))

from sklearn import preprocessing

label_encoder= preprocessing.LabelEncoder()
onehot_encoder=preprocessing.OneHotEncoder()
onehot_labeled= label_encoder.fit_transform(df['hp_bin'].head(15))
print(onehot_labeled)
print(type(onehot_labeled))
onehot_reshaped= onehot_labeled.reshape(len(onehot_labeled),1)
print(onehot_reshaped)

onehot_fitted= onehot_encoder.fit_transform(onehot_reshaped)
print(onehot_fitted)

df=pd.read_csv(dir+'/part5/auto-mpg.csv',header=None)

df.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower']=df['horsepower'].astype('float')

print(df.horsepower.describe())

df.horsepower= df.horsepower/abs(df.horsepower.max())
print(df.horsepower.head(2))

df=pd.read_csv(dir+'/part5/auto-mpg.csv',header=None)
df.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower']=df['horsepower'].astype('float')
print(df.horsepower.describe())

min_x=df.horsepower-df.horsepower.min()

min_max=df.horsepower.max()-df.horsepower.min()
df.horsepower= min_x/min_max
df.horsepower.head(5)
print(df.horsepower.describe())

df=pd.read_csv(dir+'/part5/stock-data.csv')
print(df.head())

df.info()
df['New Date']=pd.to_datetime(df['Date'])

df.set_index('New Date', inplace=True)
df.drop('Date',axis=1, inplace=True)

print(df.head())
print(df.info())

dates=['2019-01-01','2020-03-01','2021-06-01']
ts_dates= pd.to_datetime(dates)
ts_dates
pr_day= ts_dates.to_period(freq='D')
print(pr_day)
pr_month= ts_dates.to_period(freq='M')
print(pr_month)
pr_year= ts_dates.to_period(freq='Y')
print(pr_year)

ts_ms= pd.date_range(start='2019-01-01', end=None,
periods=6, freq='MS', tz='Asia/Seoul')
print(ts_ms)

ts_me= pd.date_range('2019-01-01', periods=6, freq='M', tz='Asia/Seoul')
print(ts_me)

ts_3m= pd.date_range('2019-01-01', periods=6,
freq='3M', tz='Asia/Seoul')
print(ts_3m)
df=pd.read_csv(dir+'/part5/stock-data.csv')
df['new_Date'] = pd.to_datetime(df['Date'])
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())

print(df.index)
df.set_index('new_Date', inplace=True)
df_y = df['2018']
print(df_y.head())
df_ym = df.loc['2018-07'] 
df_ym.head(5)
df_ym_cols = df.loc['2018-07', 'Start':'High'] 

df_ym_cols

df_ymd_range = df['2018-06-25':'2018-06-20']
df_ymd_range

today=pd.to_datetime('2021-11-25')
df['time_delta']=today- df.index
df.set_index('time_delta', inplace=True)
df.head(10)
df_180=df['1250 days': '1260 days']
print(df_180)