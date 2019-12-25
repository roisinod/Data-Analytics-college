import pandas as pd
import numpy as np
def practicing_series():
    print('practicing pandas')
    obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    print(obj2)
    indexes = obj2.index
    print(obj2.values)
    print(indexes)
    print(obj2.b)
    obj3 = obj2[['d','a']]
    print(obj3)
    print(obj2[obj2<0])
    print(obj2**2)
    print('z' in obj2)
    cat = {'name' : 'Forrest Grump', 'mc' : 'Tom Hanks', 'year' : 1985, 'like' : True}
    cat2 = {'name' :'Joker', 'mc' : 'JP', 'year' : 2019, 'like' : False}
    series1 = pd.Series(cat)
    series2 = pd.Series(cat2)
    print(series1)
    print(series2)
    series3 = series2[['name', 'mc']]
    print(series3)
    print('Joker' in series3)
    sdata ={'texas':10, 'Ohio':20, 'oregon': 15, 'utah': 18}
    states = ['texas','ohio','oregon', 'iowa']
    obj4 = pd.Series(sdata, index=states)
    obj6 = obj4[obj4.isnull()]
    print(obj6)
    sdata2 = {'texas': 20, 'ohio': 20, 'oregon': 15, 'utah': 18}
    states2 = ['texas', 'ohio', 'oregon', 'iowa']
    obj5 = pd.Series(sdata2, index=states2)
    print(obj4 - obj5)
    obj4.name = 'Citizens'
    print(obj4.name)
    obj4.index = ['texas','ohio', 'California', 'utah']
    print(obj4.index)
    film1 = ['Forrest Grump', 'Joke']
    film2 = [True, False]
    film3 = {'name': ['forest ', 'Joke'], 'liked' : [True, False]}
    dfmovies = pd.DataFrame(film3)
    filmcombined = pd.Series(film1, index=film2)
    print(filmcombined)
    print(dfmovies)
    df = pd.read_csv('salaries.csv')
    print(df)
    print(df.head(8))
    print(df.tail(2))
    print(df.dtypes)
    print(df['sex'].dtypes)
    #records
    print(df.shape)
    #elements
    print(df.size)
    #columns
    print(df.columns)
    #summary
    print(df.describe())
    print('------')
    #deviation
    print(df.std())
    print(df.head(50), df.mean())
    print('-----')
    print(df['salary'].std())
    print('-----')
    print(df.salary.describe())
    print('-----')
    print(df.salary.count())
    print('-----')
    print(df.salary.mean())

    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    frame = pd.DataFrame(data)
    pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001:1.7, 2002:3.6}}
    fram_series = pd.DataFrame([pop])
    print(fram_series)
    print(pop)
    print(frame)
    print('------- new topic')
    obj = pd.Series(range(3), index=['a', 'b', 'c'])
    print(obj)
    obj = pd.Series(range(3), index=['a', 'b', 'd'])
    print(obj)
    index = obj.index
    obj.index=['a','d','c']
    print(index)
    print(index[1:])
    fram_series.name = 'students'
    print(fram_series)
    print(fram_series.values)
    print(type(fram_series.values))

    print('-----')
    print(fram_series.values[0][1])
    obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
    print(obj)
    obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e', 'z'], fill_value='0.0')
    print(obj2)
    #create a dataframe - salaries - that has the five first rows for the columns rank and salary
    df = pd.read_csv('salaries.csv')
    data = df.head(5) [['rank', 'salary']]
    dfnew=df.loc[5:11,['rank', 'salary']]
    dfnew=df.iloc[5:11,[0,1]]

    print(dfnew)

    print(data)
def practicing_dataframe():
    #create data dataframe delete ny ohio one four
    data =pd.DataFrame(np.arange(16).reshape(4,4), index=['Ohio', 'Colorado', 'Utah', 'New York'], columns=['one', 'two', 'three', 'four'])
    newcolumns = ['two', 'three']
    data2 =data.reindex(['Colorado', 'Utah'])
    data3= data.reindex(columns = newcolumns)
    data4 =[data2, data3]
    #print(data)
    #data4 = data.update(data2, data3)
    print(data4)
    #print(data2)
    df=pd.read_csv('salaries.csv')
    #print on screen only the staff that earns more than 60,000 euros
    print(df[(df['salary'] > 120000) & (df['sex'] == 'Female')])
    print(df[(df['salary'] > 120000) & (df['sex'] == 'Female')].count())
    print(df[(df['salary'] > 120000) & (df['sex'] == 'Male')].count())
    df_rank = df.groupby('rank')
    print(df_rank.mean())
    #make a group by sex. Compute average salary for female and male
    df_rank = df.groupby('sex')
    print(df_rank.mean())
    #only show salary
    print('salary', df['salary'], df['sex']== 'Female')
    #salaries groupby, sorting and ag
    print('groupby', df.groupby('rank').mean())
    print('sorting', df.sort_values(by = ['salary'], ascending = 'False'))
    print()






if __name__=='__main__':
    practicing_dataframe()
    #practicing_series()


