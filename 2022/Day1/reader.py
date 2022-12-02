import pandas as pd
from itertools import groupby
import time

start_time = time.time()
### Part 1 ###
with open('input.txt') as file:
    lines = file.read().splitlines()

# Some nonsense from SO for splitting list on a value
i = (list(g) for _, g in groupby(lines, key=''.__ne__))
res = [a + b for a, b in zip(i, i)]

# Put into dataframe for speed
df = pd.DataFrame(res).fillna(0)
df = df.replace('', 0).astype(int)

#Sum the column
df['Sum'] = df.sum(axis=1)
max_elf = df['Sum'].idxmax()


print("Elf with the most calories: #%d, %d" % (max_elf, df.iloc[max_elf]['Sum']))
#print(df.to_markdown())

### Part 2 ###

print("Calories of top 3 elves: %d" % (df['Sum'].nlargest(3).sum()))
print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))