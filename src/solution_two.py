import pandas as pd

df = pd.read_csv(filepath_or_buffer=r'..\input\question-2\main.csv',
                 usecols=["occupation", 'age'])

df = df.groupby('occupation').agg({'age': ['min', 'max']})

df.to_csv(r'..\output\answer-2\output-2.csv')

print("Output CSV Generated Successfully")
