import pandas as pd

file_name = 'employee.csv'

df = pd.read_csv(file_name)
print(df)
print('-----------------------------------------')
print(df.head(3))
print('-----------------------------------------')
print(df.tail(1))
