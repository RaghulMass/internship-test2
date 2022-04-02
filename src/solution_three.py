import pandas as pd

df = pd.read_csv(filepath_or_buffer=r'..\input\question-3\main.csv',
                 usecols=["Team", "Yellow Cards", "Red Cards"])

df = df.sort_values(["Red Cards", "Yellow Cards"], ascending=[False, False])

df.to_csv(r'..\output\answer-3\output-3.csv', index=False)

print("Output CSV Generated Successfully")
