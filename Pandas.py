import pandas as pd
#1. Series Practice

# create series
series_1 = pd.Series([2, 1, 7, 3])
print(series_1)
print("===")
print(series_1[1])
print("===")
print(series_1[0:3])

import pandas as pd
# set index of Series
grades = pd.Series([100, 27, 72, 53, 100], index=['Ting', 'Danny', 'Paul', 'TC', 'Carisa'])
print(grades)
print("===")
print(grades['Ting'])


#2. dataframe
import pandas as pd
# create dataframe
data_1 = {
    'name': ['Ting', 'Danny', 'Paul', 'TC'],
    'email': ['ting@gmail.com', 'hdanny@gmail.com', 'po@gmail.com', 'tyu@gmail.com'],
    'grades': [100, 77, 92, 43]
}
student_df_1 = pd.DataFrame(data_1)
print(student_df_1)

# set index of dataframe
student_df_1 = pd.DataFrame(data, index=['1', '2', '3', '4'])
print(student_df_1)

# description of dataframe
print(student_df_1.info())
print(student_df_1.describe())

# print index/ columns of dataframe
print(student_df_1.index)
print(student_df_1.columns)

# print several records
print(student_df_1.head(1))
print(student_df_1.tail(1))

import pandas as pd
# read_excel
df = pd.read_excel('cleaned_data_2017.xlsx')
df.info()
print("===")
print(df.describe())
print("===")
print(df.head(3))
print("===")
print(df.tail(3))

import pandas as pd
data_2 = {
    'name': ['Ting', 'Danny', 'Paul', 'TC'],
    'email': ['ting@gmail.com', 'hdanny@gmail.com', 'po@gmail.com', 'tyu@gmail.com'],
    'grades': [100, 77, 92, 43]
}

student_df_2 = pd.DataFrame(data_2)
print(student_df_2)

# drop,  axis=1 > columns  axis=0 > rows
student_df_2 = student_df_2.drop(['grades'], axis=1)
print(student_df_2)

#3. missing value
import pandas as pd
import numpy as np

df = pd.DataFrame([[2, np.nan, 2, np.nan, 0],
                   [3, 3, 4, np.nan, 1],
                   [np.nan, np.nan, 4, np.nan, 5],
                   [np.nan, 3, np.nan, 4, np.nan]],
                  columns=list('12345'))
print(df)

# fillna
print(df.fillna(0))

#4. combine rows by concat(), combine columns by merge
import pandas as pd
data_1 = {
    'name': ['Tim', 'JT', 'HM', 'Ted'],
    'email': ['ting@gmail.com', 'hdanny@gmail.com', 'po@gmail.com', 'tyu@gmail.com'],
    'grades': [98, 77, 62, 99]
}

data_2 = {
    'name': ['Ting', 'Danny', 'Paul', 'TC'],
    'email': ['ting@gmail.com', 'hdanny@gmail.com', 'po@gmail.com', 'tyu@gmail.com'],
    'grades': [100, 77, 92, 43]
}

student_df_1 = pd.DataFrame(data_1)
student_df_2 = pd.DataFrame(data_2)

print(student_df_1)
print(student_df_2)

# concat(), sort by index
student_fg_3 = pd.concat([student_df_1, student_df_2], ignore_index=True)
print(student_fg_3)

import pandas as pd
data_3 = {
    'name': ['Ting', 'Danny', 'Paul', 'TC'],
    'email': ['ting@gmail.com', 'hdanny@gmail.com', 'po@gmail.com', 'tyu@gmail.com'],
    'grades': [100, 77, 92, 43]
}
data_4 = {
    'name': ['Ting', 'Danny', 'Paul', 'TC'],
    'age': [24, 28, 26, 26]
}

student_df_5 = pd.DataFrame(data_3)
student_df_6 = pd.DataFrame(data_4)

print(student_df_5)
print(student_df_6)

student_mg_3 = pd.merge(student_df_5, student_df_6)
print(student_mg_3)

# data frame to CSV
print(student_mg_3.to_csv('student_mg_3.csv'))