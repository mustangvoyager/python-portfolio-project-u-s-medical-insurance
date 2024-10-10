import csv
import pandas as pd

with open("insurance.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    med_df = pd.DataFrame([csv_reader], index=None)
    med_df.head()

for val in list(med_df[0]):
    print(val)

# peering at the solution ipynb
# How about lists to accommodate each of the various attributes / columns.
age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []