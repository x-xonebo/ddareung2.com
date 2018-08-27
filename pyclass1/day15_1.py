import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import platform
from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family=='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(
    fname='c:/Windows/Fonts/malgun.ttf').get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...')


df = pd.read_csv('/data/2016crime.tsv', delimiter='\t', index_col='자치구')


df['살인검거율'] = df['살인(검거)'] / df['살인(발생)'] * 100

df['강도검거율'] = df['강도(검거)'] / df['강도(발생)'] * 100

df['강간검거율'] = df['강간(검거)'] / df['강간(발생)'] * 100

df['절도검거율'] = df['절도(검거)'] / df['절도(발생)'] * 100

df['폭력검거율'] = df['폭력(검거)'] / df['폭력(발생)'] * 100

print(df.head())

del df['살인(검거)']
del df['강도(검거)']
del df['강간강제추행(검거)']
del df['절도(검거)']
del df['폭력(검거)']
del df['합계(검거)']

print(df.shape)
print(df.head(25))
cols = ['살인검거율', '강도검거율', '강간강제추행검거율', '절도검거율', '폭력검거율', '합계검거율']

df.loc[df['살인검거율'] > 100, '살인검거율'] = 100
df.loc[df['살인검거율'] > 100, '살인검거율'] = 100
df.loc[df['살인검거율'] > 100, '살인검거율'] = 100
df.loc[df['살인검거율'] > 100, '살인검거율'] = 100
df.loc[df['살인검거율'] > 100, '살인검거율'] = 100
df.loc[df['살인검거율'] > 100, '살인검거율'] = 100

df.rename(columns={'살인(발생)':'살인','강도(발생)':'강도','강간강제추행(발생)':'강간','절도(발생)':'절도','폭력(발생)':'폭력'}, inplace=True)

del df['합계(발생)']
print(df)

popDF = pd.read_csv('./data/2016_seoul_pop.csv', index_col='자치구')

# df.to_csv('data/crime1.csv', encoding='utf-8')

target_col = ['살인', '강도', '강간', '절도', '폭행']
weight_col = df[target_col].max() 
# print(weight_col)

crime_count_norm = df[target_col] / weight_col
print(crime_count_norm)


sns.heatmap(flights2)
