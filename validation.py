#%%
from categories import CATEGORIES
import sqlite3
from itertools import combinations
# %%
# %%
def matching(cat1, cat2, db_path="poke_database.db"):
    cat_union = f"{cat1['condition']} AND {cat2['condition']}"
    matching_pokemon = "SELECT name FROM my_table WHERE " + cat_union
    
    conn = sqlite3.connect("poke_database.db")
    results = conn.execute(matching_pokemon).fetchall()
    conn.close()

    return ([i[0] for i in results])
#%%
def validation_all():
    empty = []
    for cat1, cat2 in combinations(CATEGORIES, 2):
        result = matching(cat1, cat2)
        if len(result) == 0:
            empty.append((cat1["label"], cat2["label"]))
        print(f"Done with {cat1['label']} and {cat2['label']}")
    return empty
#%%
def validation(cat1, cat2):
    result = matching(cat1, cat2)
    if len(result) == 0:
        return 0
    else:
        return 1
# %%
test1 = validation_all()
# %% cool syntax
print([i for i in range(0,10)])
# %% Testing 1
test2 = validation(CATEGORIES[2], CATEGORIES[2])
print(test2)
# %% Testing 2
conn = sqlite3.connect("poke_database.db")
cat1 = CATEGORIES[2]
cat2 = CATEGORIES[6]
testing = f"SELECT name FROM my_table WHERE {cat1['condition']} AND {cat2['condition']}"

# %%
conn = sqlite3.connect("poke_database.db")
results = conn.execute("SELECT * FROM my_table WHERE type_water = 1 AND type_fighting = 1").fetchall()
conn.close()
# %% testing
conn = sqlite3.connect("poke_database.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM my_table LIMIT 5")
print(cursor.fetchall())
conn.close()
# %%
