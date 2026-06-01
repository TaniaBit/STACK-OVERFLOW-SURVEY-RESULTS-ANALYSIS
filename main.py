!pip install gdown

import pandas as pd
import gdown
import json
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',None)

file_id = '1sbhGtRxh7h_1tkfBsoqqZbPVP3Ks7RDf'
url = f'https://drive.google.com/uc?id={file_id}'

#pd.set_option('display.max_columns',None)
#df = pd.read_csv(url)
gdown.download(url, 'survey_results_public.csv', quiet=False)

df = pd.read_csv('survey_results_public.csv')

file_id1 = '1lmFk3UrBaCQJblWjphfBWCd9T4girt0v'
url1 = f'https://drive.google.com/uc?id={file_id1}'

pd.set_option('display.max_columns',None)
df1= pd.read_csv(url1)

numberOfRespondents = df.ResponseId.nunique(dropna=True)
print(f'Загальна кількість респондентів: {numberOfRespondents}')

questions = set(df1['qname'].unique()).intersection(set(df.columns))

print(f'Кількість питань для перевірки: {len(questions)}')

respondents_full = df[list(questions)].dropna()

full_answers_count = respondents_full.shape[0]

print(f'Кількість респондентів, які відповіли на всі запитання: {full_answers_count}')

workexp = df['WorkExp'].dropna()

mean_value = workexp.mean()
median_value = workexp.median()
mode_value = workexp.mode()[0]

print('Статистичний аналіз досвіду роботи респондентів:')
print(f'Mean: {round(mean_value, 1)}')
print(f'Median: {median_value}')
print(f'Mode: {mode_value}')

print(df['RemoteWork'].value_counts(dropna=False))

remote_count = df[df['RemoteWork'] == 'Remote'].shape[0]

print(f'Кількість респондентів, які працюють віддалено: {remote_count}')

df['worked_with_python'] = df['LanguageHaveWorkedWith'].str.contains(
    'Python',
    case=False,
    na=False
)

python_users = df['worked_with_python'].sum()

total_respondents = df.shape[0]

python_percent = (python_users / total_respondents) * 100

print(f'Відсоток респондентів, які програмують на Python: {round(python_percent, 1)}%')