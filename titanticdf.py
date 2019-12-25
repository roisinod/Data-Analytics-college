import pandas as pd
df = pd.read_csv('titanic.csv')
print(type(df))
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df[['Age', 'Survived']])
print(df.tail())
print(df.loc[1:20])
df_with_names = pd.read_csv('titanic.csv', index_col = 'Name')
print(df_with_names.head())
df_sel = df_with_names.loc['Master. Gosta Leonard Palsson' : 'Mr. Anders Johan Andersson']
print(df_sel)
df_ages =df_with_names['Age']
print(df_ages.value_counts())
print(df[['Name', 'Age']].head())
df['Age'] +=1
print(df[['Name', 'Age']].head())
df['Name'][1]= 'Mrs. Barry Bradley (Florence Briggs Thayer) Cumings'
print(df[['Name', 'Age']].head())
print(df['Age'].mean())
print(df.columns)
df_with_class = pd.read_csv('titanic.csv', index_col = 'Pclass')
print(df_with_class)
#sex = df(df['Sex'] == 'female')
print(df_with_class.groupby('Sex').mean())
#print(df['Sex'])
print(df[(df['Survived'] == 1) & (df['Sex'] == 'female')].count())
print(df[(df['Survived'] == 0) & (df['Sex'] == 'female')].count())
print(df.groupby('Sex').median())
#number of men v women who survived
print(df.groupby('Sex')[['Survived']].mean())
#the people who paid the highest survived or not

#how many from the class died
print(df.groupby('Pclass')[['Survived']].mean())