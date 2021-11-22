import pandas as pd

df= pd.DataFrame([[15,'남','덕영중'], [17,'여','수리중']],
 index=['준서','예은'],
 columns=['나이','성별','학교'])

print(df)

print(df.index)

print(df.columns)

df.index=['학생1','학생2']
df.columns=['연령','남녀','소속']

print(df)

print(df.index)
print(df.columns)

exam_data={'수학':[90,80,70], '영어':[98,89,95],
'음악':[85,95,100], '체육':[100,90,90]}

df= pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df)

df2=df[:]
df2.drop('우현',inplace=True)
print(df2)
df3=df[:]
df3.drop(['우현','인아'], axis=0, inplace=True)
print(df3)
df3.drop(['체육'], axis=1, inplace=True)
print(df3)
df4= df.copy()
print(df4)

label1=df.loc['서준']
print(label1)
position1=df.iloc[0]
print(position1)

label2= df.loc[['서준', '우현']]
position2= df.iloc[[0,1]]
print(label2)
print(position2)

label3=df.loc['서준':'우현']
position3=df.iloc[0:1]
print(label3)
print(position3)

exam_data={'이름':['서준','우현','인아'],
'수학':[90,80,70],
'영어':[98,89,95],
'음악':[85,95,100],
'체육':[100,90,90]}

print(df)

print(exam_data)
df= pd.DataFrame(exam_data)
print(df)
df['이름']

df.영어

english=df.영어
print(english)
print(df[['영어','수학']])

df.loc[0,2]

df.set_index('이름',inplace=True)
print(df)
a=df.iloc[0,2]
print(a)
print(df)
b=df.loc['서준','영어']
print(b)

c= df.loc['서준',['음악','체육']]
print(c)
d= df.iloc[0,[2,3]]
print(d)

e=df.loc['인아','수학':'체육']
print(e)

g= df.loc[['서준','인아'],['수학','영어']]
print(g)
e= df.iloc[0:2,1:3]
print(e)
df1=df
df1['국어']=80
print(df1)
df['컴퓨터']=[20,50,80]
print(df)
df['국사']=[50,90]

df.loc[3]=0

print(df)

df.loc[4]=0
print(df)

df.loc[1]=['동규',90,80,50,40]
print(df)
df.loc['행']=df.loc[1]
df=pd.DataFrame(exam_data)
df.set_index('이름',inplace=True)

df.iloc[0][3]=80
df.loc['인아']['수학']=100

df=df.transpose()

ndf=df.set_index('체육')
print(ndf)
ndff=df.set_index(['체육','음악'])
print(ndff)

dict_data = {'c0':[3,2,1], 'c1':[4,5,6], 'c2':[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df=pd.DataFrame(dict_data, index=['r0','r1','r2'])
new_index=['r0','r1','r2','r3','r4','r5']
ndf=df.reindex(new_index)
print(ndf
ndf2=df.reindex(new_index, fill_value='홍')
print(ndf2)

ndf2=df.reset_index()
ndf2=df.sort_index(ascending=False)

ndf2=df.sort_values(by='c0', ascending=False)

student1=pd.Series({'국어':100,'영어':80, '수학':85})
print(student1)

print(student1/200)
student2=pd.Series({'국어':90,'영어':40,'수학':100})

addition=student1+student2
subtraction=student1-student2
multiplication=student1*student2
division=student1/student2
result=pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

pip install seaborn

import seaborn as sns

titanic=sns.load_dataset('titanic')
df=titanic.loc[:,['age','fare']]
print(df.head())

addition=df+10
print(addition.head())
subtraction= addition-df
print(subtraction.head())