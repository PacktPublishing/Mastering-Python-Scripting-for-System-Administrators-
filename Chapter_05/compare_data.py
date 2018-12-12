import pandas as pd

df1 = pd.read_csv("student1.csv")
df2 = pd.read_csv("student2.csv")

s1 = set([ tuple(values) for values in df1.values.tolist()])
s2 = set([ tuple(values) for values in df2.values.tolist()])

s1.symmetric_difference(s2)

print (pd.DataFrame(list(s1.difference(s2))),'\n\n')
print (pd.DataFrame(list(s2.difference(s1))),'\n\n')
