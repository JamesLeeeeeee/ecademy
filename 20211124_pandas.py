import pandas as pd

import os 
dir = os.path.dirname(os.path.realpath('__file__')) 
file_path = dir + '\\part3\\auto-mpg.csv'

df=pd.read_csv(file_path)

df.columns=['mpg','cyl','displac','horsepower','weight','accel','model year','origin','name']
df.head()
print(df.mean())

print(df['mpg'].mean())

print(df[['mpg','weight']].mean())

df.median()

df['cyl'].median()

df.max()

df['horsepower'].max()

df['weight'].min()

df.std()

df.corr()

df= pd.read_excel(dir+'\\part3\\남북한발전전력량.xlsx', engine='openpyxl')
df.head()
df_ns=df.iloc[[0,5],3:]

df_ns.index=['south','north']

df_ns.columns= df_ns.columns.map(int)

print(df_ns.head())

df_ns.plot()

tdf_ns= df_ns.T

tdf_ns.head()

tdf_ns.plot()

tdf_ns.plot(kind='bar')

tdf_ns.plot(kind='hist')

df=pd.read_csv(file_path,header=None)
df.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

df.plot(x='weight',y='mpg',kind='scatter')

df[['mpg','cylinders']].plot(kind='box')

import matplotlib.pyplot as plt

df= pd.read_excel(dir+'\\part4\\시도별 전출입 인구수.xlsx', engine='openpyxl', header=0)

df.head()

df= df.fillna(method='ffill')

mask=(df['전출지별']=='서울특별시') & (df['전입지별']!='서울특별시')
df_seoul=df[mask]
df_seoul= df_seoul.drop(['전출지별'],axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
df_seoul.head()

sr_one= df_seoul.loc['경기도']
sr_one.head()

plt.plot(sr_one.index, sr_one.values)

plt.plot(sr_one)

plt.plot(sr_one.index, sr_one.values)
plt.title('서울 -> 경기 이동 인구')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.show()
from matplotlib import font_manager, rc
font_path=dir+'\\part4\\malgun.ttf'
font_name=font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.figure(figsize=(14,5))
plt.xticks(rotation='vertical')
plt.style.use('ggplot')
plt.plot(sr_one, marker='o',markersize=10)
plt.title('서울 -> 경기 이동 인구',size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수')
plt.legend(labels=['서울->경기'],loc='best', fontsize=15)


plt.ylim(5000,800000)
plt.annotate('',
xy=(20,620000),
xytext=(2,290000),
xycoords='data',
arrowprops=dict(arrowstyle='->',color='skyblue', lw=5),
)
plt.annotate('',
xy(47,450000),
xytext=(30,580000),
xycoords='data',
arrowprops=dict(arrowstyle='->',color='red', lw=5),
)
plt.annotate('인구 이동 증가(1970-1955)',
xy=(10,550000),
rotation=25,
va='baseline',
ha='center',
fontsize=15,
)
plt.annotate('인구 이동 감소(1955-2017)',
xy=(40,560000),
rotation=-11,
va='baseline',
ha='center',
fontsize=15,
)
plt.show()

plt.ylim(50000, 800000)

# 주석 표시 - 화살표
plt.annotate('',
             xy=(20, 620000),       #화살표의 머리 부분(끝점)
             xytext=(2, 290000),    #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), #화살표 서식
             )

plt.annotate('',
             xy=(47, 450000),       #화살표의 머리 부분(끝점)
             xytext=(30, 580000),   #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),  #화살표 서식
             )

# 주석 표시 - 텍스트
plt.annotate('인구이동 증가(1970-1995)',  #텍스트 입력
             xy=(10, 550000),            #텍스트 위치 기준점
             rotation=25,                #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.annotate('인구이동 감소(1995-2017)',  #텍스트 입력
             xy=(40, 560000),            #텍스트 위치 기준점
             rotation=-11,               #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.show()  # 변경사항 저장하고 그래프 출력


plt.figure(figsize=(14,5))
plt.xticks(rotation='vertical')
plt.style.use('ggplot')
plt.plot(sr_one, marker='+',markersize=10)
plt.title('서울 -> 경기 이동 인구',size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구수')
plt.legend(labels=['서울->경기'],loc='best', fontsize=15)
fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
ax1.plot(sr_one, marker='.', markersize=10)
ax2.plot(sr_one, marker='*', markerfacecolor='green', markersize=10,
color='olive', linewidth=2, label='서울->경기')
ax2.legend(loc='best')

ax1.set_ylim(50000,800000)
ax2.set_ylim(50000,800000)
ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)
plt.show()


plt.style.use('ggplot') 

fig=plt.figure(figsize=(20,5))
ax=fig.add_subplot(1,1,1)
ax.plot(sr_one, marker='.', markerfacecolor='orange', markersize=10,
color='olive', linewidth=2, label='서울->경기')
ax.legend(loc='best')

ax.set_ylim(50000,800000)
ax.set_title('서울 ->  경기 이동 인구', size=20)
ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size=12)

ax.set_xticklabels(sr_one.index, rotation=75)
ax.tic_params(axis='x', labelsize=10)
ax.tic_params(axis='y', labelsize=10)
plt.show()

col_years=list(map(str, range(1970,2018)))
df_3=df_seoul.loc[['충청남도','경상북도','강원도'],col_years]
df_3.head()
plt.style.use('ggplot')
fig= plt.figure(figsize=(20,5))
ax=fig.add_subplot(1,1,1)
ax.plot(col_years, df_3.loc['충청남도',:], marker='.',markerfacecolor='green', markersize=10, color='olive', linewidth=2, label='서울->충남')
ax.plot(col_years, df_3.loc['경상북도',:], marker='.', markerfacecolor='blue', markersize=10, color='skyblue', linewidth=2, label='서울->경북')
ax.plot(col_years, df_3.loc['강원도',:], marker='.', markerfacecolor='red', markersize=10, color='darkmagenta', linewidth=2, label='서울->강원')
ax.legend(loc='best')

ax.set_title('서울-> 충청, 경북, 강원', size=14)
ax.set_xlabel('기간',  size=10)
ax.set_ylabel('이동 인구수', size=10)
ax.set_xticklabels(col_years, rotation=90)
ax.tick_params(axis='x', labelsize=10)
ax.tick_params(axis='y', labelsize=10)
plt.show()

plt.style.use('ggplot') 


fig = plt.figure(figsize=(20, 10))   
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)


ax1.plot(col_years, df_4.loc['충청남도',:], marker='o', markerfacecolor='green', 
        markersize=10, color='olive', linewidth=2, label='서울 -> 충남')
ax2.plot(col_years, df_4.loc['경상북도',:], marker='o', markerfacecolor='blue', 
        markersize=10, color='skyblue', linewidth=2, label='서울 -> 경북')
ax3.plot(col_years, df_4.loc['강원도',:], marker='o', markerfacecolor='red', 
        markersize=10, color='magenta', linewidth=2, label='서울 -> 강원')
ax4.plot(col_years, df_4.loc['전라남도',:], marker='o', markerfacecolor='orange', 
        markersize=10, color='yellow', linewidth=2, label='서울 -> 전남')


ax1.legend(loc='best')
ax2.legend(loc='best')
ax3.legend(loc='best')
ax4.legend(loc='best')


ax1.set_title('서울 -> 충남 인구 이동', size=15)
ax2.set_title('서울 -> 경북 인구 이동', size=15)
ax3.set_title('서울 -> 강원 인구 이동', size=15)
ax4.set_title('서울 -> 전남 인구 이동', size=15)


ax1.set_xticklabels(col_years, rotation=90)
ax2.set_xticklabels(col_years, rotation=90)
ax3.set_xticklabels(col_years, rotation=90)
ax4.set_xticklabels(col_years, rotation=90)

plt.show()
import matplotlib
colors={}
for name, hex in matplotlib.colors.cnames.items():
     colors[name]= hex
print(colors)

df_4= df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years]
df_4=df_4.transpose()
plt.style.use('ggplot')
df_4.index=df_4.index.map(int)
df_4.plot(kind='area',  alpha=0.2, figsize=(20,10))
plt.title('서울->타시도 인구 이동', size=10)
plt.legend(loc='best', fontsize=14)
plt.show()

df_4.plot(kind='barh', figsize=(20,10), width=0.7,
color=['orange','green','skyblue','blue'])
plt.ylim(5000,30000)
plt.show()
df.head()

plt.style.use('classic')   # 스타일 서식 지정

# read_csv() 함수로 df 생성
df = pd.read_csv(dir+'\\part4\\auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']

# 연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist', bins=10, color='coral', figsize=(10, 5))

# 그래프 꾸미기
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()

plt.style.use('default')   
cylinders_size = df.cylinders / df.cylinders.max() * 300
df.plot(kind='scatter', x='weight', y='mpg',  c='coral', s=cylinders_size, figsize=(10, 5))
plt.title('Scatter Plot - mpg vs. weight')
plt.show()

df.plot(kind='scatter', x='weight', y='mpg', marker='+', figsize=(10, 5),
        cmap='viridis', c=cylinders_size, s=50, alpha=0.3)
plt.title('Scatter Plot: mpg-weight-cylinders')
plt.show()


df['count']=1
df_origin= df.groupby('origin').sum()
print(df_origin.head())
df_origin['count'].index=['USA','EU','JPN']

df_origin['count'].plot(kind='pie',
figsize=(7,5),
autopct='%1.1f%%',
startangle=10,
colors=['chocolate','bisque','cadetblue']
)
plt.title('Model Origin', size=20)
plt.axis('equal')
plt.legent(labels=df_origin.index, loc='upper right')

plt.show()


fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# axe 객체에 boxplot 메서드로 그래프 출력
ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN'])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN'],
         vert=False)

ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')

plt.show()

import seaborn as sns

titanic= sns.load_dataset('titanic')

print(titanic.head())

sns.set_style('darkgrid')
fig=plt.figure(figsize=(15,5))
ax1= fig.add_subplot(1,2,1)
ax2= fig.add_subplot(1,2,2)

sns.regplot(x='age',
y='fare',
data=titanic,
ax=ax1)

sns.regplot(x='age', y='fare', data=titanic,
ax=ax2, fit_reg=False, color='r')
plt.show()

fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
 

sns.distplot(titanic['fare'], ax=ax1) 


sns.kdeplot(x='fare', data=titanic, ax=ax2) 


sns.histplot(x='fare', data=titanic,  ax=ax3)        


ax1.set_title('titanic fare - distplot')
ax2.set_title('titanic fare - kedplot')
ax3.set_title('titanic fare - histplot')

plt.show()

table = titanic.pivot_table(index=['sex'], columns=['class'], aggfunc='size')


sns.heatmap(table,                  # 데이터프레임
            annot=True, fmt='d',    # 데이터 값 표시 여부, 정수형 포맷
            cmap='YlGnBu',          # 컬러 맵
            linewidth=.5,           # 구분 선
            cbar=True)             # 컬러 바 표시 여부

plt.show()

sns.set_style('whitegrid')

fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
 
# 이산형 변수의 분포 - 데이터 분산 미고려
sns.stripplot(x="class",      #x축 변수
              y="age",        #y축 변수           
              data=titanic,   #데이터셋 - 데이터프레임
              ax=ax1)         #axe 객체 - 1번째 그래프 

# 이산형 변수의 분포 - 데이터 분산 고려 (중복 X) 
sns.swarmplot(x="class",      #x축 변수
              y="age",        #y축 변수
              data=titanic,
              hue='sex',   #데이터셋 - 데이터프레임
              ax=ax2)         #axe 객체 - 2번째 그래프        

# 차트 제목 표시
ax1.set_title('Strip Plot')
ax2.set_title('Strip Plot')

plt.show()

sns.set_style('whitegrid')

# 그래프 객체 생성 (figure에 3개의 서브 플롯을 생성)
fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
 

sns.barplot(x='sex', y='survived', data=titanic, ax=ax1) 

# x축, y축에 변수 할당하고 hue 옵션 추가 
sns.barplot(x='sex', y='survived', hue='class', data=titanic, ax=ax2) 

# x축, y축에 변수 할당하고 hue 옵션을 추가하여 누적 출력
sns.barplot(x='sex', y='survived', hue='class', dodge=False, data=titanic, ax=ax3)       


ax1.set_title('titanic survived - sex')
ax2.set_title('titanic survived - sex/class')
ax3.set_title('titanic survived - sex/class(stacked)')

plt.show()

fig = plt.figure(figsize=(15, 5))   
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)
 
# 기본값
sns.countplot(x='class', palette='Set1', data=titanic, ax=ax1) 

# hue 옵션에 'who' 추가 
sns.countplot(x='class', hue='who', palette='Set2', data=titanic, ax=ax2) 

# dodge=False 옵션 추가 (축 방향으로 분리하지 않고 누적 그래프 출력)
sns.countplot(x='class', hue='who', palette='Set3', dodge=False, data=titanic, ax=ax3)       

# 차트 제목 표시
ax1.set_title('titanic class')
ax2.set_title('titanic class - who')
ax3.set_title('titanic class - who(stacked)')

plt.show()

fig = plt.figure(figsize=(15, 10))   
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
 
# 박스 그래프 - 기본값
sns.boxplot(x='alive', y='age', data=titanic, ax=ax1) 

# 바이올린 그래프 - hue 변수 추가
sns.boxplot(x='alive', y='age', hue='sex', data=titanic, ax=ax2) 

# 박스 그래프 - 기본값
sns.violinplot(x='alive', y='age', data=titanic, ax=ax3) 

# 바이올린 그래프 - hue 변수 추가
sns.violinplot(x='alive', y='age', hue='sex', data=titanic, ax=ax4) 

plt.show()

j1 = sns.jointplot(x='fare', y='age', data=titanic) 

# 조인트 그래프 - 회귀선
j2 = sns.jointplot(x='fare', y='age', kind='reg', data=titanic) 

# 조인트 그래프 - 육각 그래프
j3 = sns.jointplot(x='fare', y='age', kind='hex', data=titanic) 

# 조인트 그래프 - 커럴 밀집 그래프
j4 = sns.jointplot(x='fare', y='age', kind='kde', data=titanic) 

# 차트 제목 표시
j1.fig.suptitle('titanic fare - scatter', size=15)
j2.fig.suptitle('titanic fare - reg', size=15)
j3.fig.suptitle('titanic fare - hex', size=15)
j4.fig.suptitle('titanic fare - kde', size=15)

plt.show()

# 조건에 따라 그리드 나누기
g = sns.FacetGrid(data=titanic, col='who', row='survived') 

# 그래프 적용하기
g = g.map(plt.hist, 'age')


plt.show()

sns.set_style('whitegrid')

# titanic 데이터셋 중에서 분석 데이터 선택하기
titanic_pair = titanic[['age','pclass', 'fare']]

# 조건에 따라 그리드 나누기
g = sns.pairplot(titanic_pair)
plt.show()

