import pandas as pd
import numpy as np

df = pd.read_csv(filepath_or_buffer=r"..\input\question-1\main.csv")

start_year = df["Year"].iloc[0]
end_year = df["Year"].iloc[-1]

current_decade = start_year
next_decade = start_year + 10

result = []

for _ in range(int((end_year - start_year) / 10) + 1):
    rows = df.index[np.logical_and(df['Year'] < next_decade, df['Year'] >= current_decade)].tolist()

    result_df = df.loc[rows, ['Violent', 'Property', 'Murder', 'Forcible_Rape', 'Robbery', 'Aggravated_assault',
                       'Burglary', 'Larceny_Theft', 'Vehicle_Theft']].sum(axis=0)

    result_df["Population"] = df["Population"].iloc[rows[-1]]
    result_df["Year"] = current_decade

    result.append(list(result_df.values))

    current_decade = next_decade
    next_decade += 10


output_df = pd.DataFrame(result, columns=['Violent', 'Property', 'Murder', 'Forcible_Rape', 'Robbery',
                                          'Aggravated_assault', 'Burglary', 'Larceny_Theft', 'Vehicle_Theft',
                                          'Population', "Year"])

output_df.set_index("Year", inplace=True)

output_df.to_csv(r"..\output\answer-1\output-1.csv")

print("Output CSV Generated Successfully")
