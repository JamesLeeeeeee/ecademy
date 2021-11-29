import seaborn as sns

titanic= sns.load_dataset('titanic')

df= titanic.loc[:,['age','fare']]

df['ten']=10
df.head()

def add_10(n):
    return n+10

def add_two(a,b):
    return a+b
print(add_10(10))

add_two(10,10)

sr1= df['age'].apply(add_10)
sr1.head()

s2=df['age'].apply(add_two, b=10)
s2.head()

sr3=df['age'].apply(lambda x: add_10(x))
sr3.head()

df_map= df.applymap(add_10)
df_map.head()
df.head()

dfmap=df.apply(add_10)
dfmap.head()

def missing_value(series):
    return series.isnull()

result= df.apply(missing_value, axis=0)
result.head()
type(result)
def min_max(x):
    return=max(x)-min(x)

def add_two(a,b):
    return a+b

df['add']= df.apply(lambda x: add_two(x['age'], x['ten']), axis=1)

df.head()

df['add']= df.apply(add_two(df['age'],df['ten']), axis=1) #안되넴 넘파이 배열을 함수에 하나하나 적용이 어려워 람다를 쓰는 듯

def missing_count(x):
    return missing_value(x).sum()

def total_number_missing(x):
    return missing_count(x).sum()

result_df= df.pipe(missing_value)
print(result_df.head())

result_series= df.pipe(missing_count)
print(result_series)

result_value= df.pipe(total_number_missing)
print(result_value)