import pandas

'''
Series - представляет из себя объект, похожий на одномерный массив, но отличительной его чертой является
наличие ассоциированных меток, т.н. индексов, вдоль каждого элемента из списка.
Такая особенность превращает его в словарь.
'''

my_series = pandas.Series([5, 6, 7, 8, 9, 10])
print(my_series)
print(my_series.index)
print(my_series.values)
print(my_series[4])
my_series2 = pandas.Series([5, 6, 7, 8, 9, 10], index=['a', 'b', 'c', 'd', 'e', 'f'])
print(my_series2['f'])
print(my_series2[['a', 'b', 'f']])
my_series2[['a', 'b', 'f']] = 0
print(my_series2)
print(my_series2[my_series2 > 0] * 2)

my_series3 = pandas.Series({'a': 5, 'b': 6, 'c': 7, 'd': 8})

# У объекта Series и его индекса есть аттрибут name, задающий имя объекту и индексу соотвественно
my_series3.name = 'numbers'
my_series3.index.name = 'letters'

'''
DataFrame лучше всего представить себе в виде обычной таблицы. 
В любой таблице присутствуют столбцы и строки.
Столбцами в DataFrame выстпают объекты Series, строки которых являются их элементами.
'''

# DataFrame проще всего сконструировать на примере питоновского словаря.
df = pandas.DataFrame({
    'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
    'population': [17.04, 143.5, 9.5, 45.5],
    'square': [2724902, 17125191, 207600, 603628]
})

print(df)
print(df['country'])

df.index = ['KZ', 'RU', 'BY', 'UA']
df.index.name = 'Country Code'
print(df)

# Доступ к строкам по индексу возможен несколькими способами:
# .loc - используется для доступа по строковой метке
# .iloc - используется для доступа по числовому значению (начиная с 0)

print(df.loc['KZ'])
print(df.iloc[0])

print(df.loc[['KZ', 'RU'], 'population'])

print(df[df.population > 10][['country', 'square']])

# Сбросить индексы
df.reset_index()

df['density'] = df['population'] / df['square'] * 1000_000
print(df)

df = df.drop(['density'], axis='columns')
df = df.rename(columns={'Country Code': 'country_code'})
print(df.index)