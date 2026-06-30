#%%
from categories import CATEGORIES
from validation import validation
import random
# %% Randomly generate 3 rows themes and 3 column themes from the 27 categories
'''
Generate 3 row and columns
Iteratively go through options until it works
'''
def generator():
    indices = random.sample(range(len(CATEGORIES)), 6)
    works = []

    for i in range(0,3):
        for j in range(3,6):
            row = CATEGORIES[indices[i]]
            col = CATEGORIES[indices[j]]
            row_and_col_validation = validation(row, col)
            works.append(row_and_col_validation)    

    if (sum(works) != 9):
        print("test: " + str(indices))
        return generator()         
    return(indices)                   
#%% testing
df = pd.read_csv("pokemon_real2.csv")
# %% Test how the nested for loop should work
indices = random.sample(range(len(CATEGORIES)), 6)
works = []
for i in range(0,3):
        for j in range(3,6):
            row = CATEGORIES[indices[i]]
            col = CATEGORIES[indices[j]]
            row_and_col_validation = validation(row, col)
            works.append(row_and_col_validation)    
# %%
test1 = generator()
# %%

# %%
