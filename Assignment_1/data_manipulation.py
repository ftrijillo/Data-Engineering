#!/Users/franktrijillo/opt/anaconda3/bin/python

import pandas as pd

df = pd.read_csv("students.csv")

print(df.to_string())

sf_students = df[df["City"].isin(["San Francisco"])]
print(sf_students.to_string())

avg_age_chicago = df[df["City"].isin(["Chicago"])].groupby("City")
print(avg_age_chicago["Age"].mean())

under_30 = df[df["Age"] >= 30]
print(under_30.to_string())
