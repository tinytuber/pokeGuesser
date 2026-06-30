#%%
import pandas as pd
import matplotlib.pyplot as plt
import requests
import csv
import sqlite3
# %% Testing to see how the API works
response = requests.get("https://pokeapi.co/api/v2/pokemon/1")
print(response.json()["name"])
print(response.json()["types"])
print(response.json()["types"][0])
len(response.json()["types"])
#print(response.json()["types"][0]["type"]["name"])
#%% Function to call a specific pokemon's name based on id
def poke_name(id):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(id))
    return response.json()["name"]

def poke(id):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(id))
    return response.json()

# %% Creating a file with all relevant header values
fieldnames = [
    "id",
    "name",
    "type_normal","type_fire","type_water","type_electric","type_grass","type_ice",
    "type_fighting","type_poison","type_ground","type_flying","type_psychic","type_bug",
    "type_rock","type_ghost","type_dragon",
    "evo_stage",
    "legs",
    "height_ft",
    "weight_lbs"
]
with open('pokemon.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
# %% Start with populating id and name
with open('pokemon.csv', 'a', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    for i in range(1, 152):
        name = poke_name(i)
        writer.writerow({'id': i, 'name': name})  
# %% Populate the types. Use pandas since writer can only append rows
df = pd.read_csv("pokemon.csv")
for i in range(1, 152):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(i))
    poke_types = response.json()["types"]

    for fn in fieldnames:
        if fn.startswith('type_'):
            df.at[i-1,fn] = 0

    for t in poke_types:
        type_name = t['type']['name']
        df.at[i-1, f'type_{type_name}'] = 1
# %%

# %%
try1 = {'id': 1, 'name': "try1"}

# %% This is a way to do it all at once
rows = []
fieldnames = [
    "id",
    "name",
    "type_normal","type_fire","type_water","type_electric","type_grass","type_ice",
    "type_fighting","type_poison","type_ground","type_flying","type_psychic","type_bug",
    "type_rock","type_ghost","type_dragon",
    "evo_stage",
    "legs",
    "height_ft",
    "weight_lbs"
]

for i in range(1,152):

    data = poke(i)
    row = {'id': i, 'name': data['name']}  ##Name and ID

    for fn in fieldnames:
        if fn.startswith('type_'):
            row[fn] = 0
    for t in data['types']:
        row[f"type_{t['type']['name']}"] = 1 ##Type

    #Skip evolution and legs. Will fill out later

    row["height_ft"] = data["height"]
    row["weight_lbs"] = data["weight"]

    rows.append(row)

df = pd.DataFrame(rows, columns=fieldnames)
df.to_csv("pokemon_real.csv")

#%%
# step 1 - get species data
species = requests.get(f'https://pokeapi.co/api/v2/pokemon-species/2').json()

# step 2 - get evolution chain url from species
evo_url = species['evolution_chain']['url']

# step 3 - fetch the evolution chain
evo_chain = requests.get(evo_url).json()
# %% convert the csv to sqlite
df2 = pd.read_csv("pokemon_real2.csv")
df2.head()
# %%
# Connect to SQLite (creates the file if it doesn't exist) 
conn = sqlite3.connect("poke_database.db") 
# Convert dataframe to SQL table 
df2.to_sql("my_table", conn, if_exists="replace", index=False) 
conn.close()

# %%
plt.hist(df2.height_ft)
plt.show()
# %%
