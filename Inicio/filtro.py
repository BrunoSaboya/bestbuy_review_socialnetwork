import os
import pandas as pd
import json
from collections import Counter

# Get a list of all files in the directory
files = os.listdir('./jsons')

# Filter the list to only JSON files
json_files = [file for file in files if file.endswith('.json')]

# Initialize an empty DataFrame
df_combined = pd.DataFrame()

# Loop over the JSON files and concatenate them into the DataFrame
for json_file in json_files:
    data = []
    with open(f"jsons/{json_file}", 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    df = pd.DataFrame(data)
    df_combined = pd.concat([df_combined, df], ignore_index=True)
print(len(df_combined))

df_combined.to_excel('output.xlsx', index=False)
i = 0
usuarios = []
for reviews_produto in df_combined['reviews']:
    for review in reviews_produto:
        if 'username' in review.keys():
            usuarios.append(review['username'])
Brands = []
for brand in df_combined['brand']:
    if brand not in Brands:
        Brands.append(brand)
"""df_combined['usernames'] = df_combined['reviews'][0][0].apply(lambda reviews: [review['username'] for review in reviews])

# Display the first 5 rows to check the data
print(df_combined['usernames'].head())
"""
def find_duplicates(lst):
    counter = Counter(lst)
    return [item for item, count in counter.items() if count > 1]

def find_three(lst):
    counter = Counter(lst)
    return [item for item, count in counter.items() if count > 2]

def find_four(lst):
    counter = Counter(lst)
    return [item for item, count in counter.items() if count > 3]
print(len(usuarios))
print(len(find_duplicates(usuarios)))
print(len(find_three(usuarios)))
print(len(find_four(usuarios)))