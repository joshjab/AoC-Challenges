import pandas as pd
import time

# Score multipliers
# Ties are equal to 0 (Multiple 3)
# Wins are equal to -1 or 2 (Multiple 6)
# Losses are equal to 1 or -2 (Multiple 0)
mult_dict = {0:3, -1:6, 2:6, 1:0, -2:0}

# Play dictionaries
opponent_dict = {'A':1, 'B':2, 'C':3}
play_dict = {'X':1,'Y':2,'Z':3}

start_time = time.time()

### Part 1 ###
with open('input.txt') as file:
    lines = file.read().splitlines()

df = pd.DataFrame(lines, columns=['Bets'])
df = df.Bets.str.split(expand=True)
df.columns = ['Opponent', 'Play']

# Make the plays numbers for math
df['Opponent'] = df['Opponent'].apply(lambda x: opponent_dict.get(x))
df['Play'] = df['Play'].apply(lambda x: play_dict.get(x))

# Subtract the Opponent and Play values
df['Result'] = df['Opponent'] - df['Play']


# Get multipliers
df['Multiplier'] = df['Result'].apply(lambda x: mult_dict.get(x))

# Muliply Play by Multipler to get Score for that round
df['Score'] = df['Multiplier'] + df['Play']

# Get the sum of the Scores
print("Total Score:", df['Score'].sum())
print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))

### Part 2 ###
win_dict = {1:2, 2:3, 3:1}
lose_dict = {2:1, 3:2, 1:3}
mult_dict = {3:6, 2:3, 1:0}
# Now we need to calculate what play we need for a certain outcome
# Subtract the Opponent and Play values
start_time = time.time()
df = df[['Opponent', 'Play']]
df.columns = ['Opponent', 'Result']

df.loc[df['Result']==2, 'Play_Tie'] = df['Opponent']
df.loc[df['Result']==3, 'Play_Win'] = df['Opponent'].apply(lambda x: win_dict.get(x))
df.loc[df['Result']==1, 'Play_Lose'] = df['Opponent'].apply(lambda x: lose_dict.get(x))
df.fillna(0.0, inplace=True) # Make NaN 0 for adding
df['Play'] = (df['Play_Tie'] + df['Play_Lose'] + df['Play_Win']).astype(int)
df = df[['Opponent', 'Result', 'Play',]]

# Get multipliers
df['Multiplier'] = df['Result'].apply(lambda x: mult_dict.get(x))

# Muliply Play by Multipler to get Score for that round
df['Score'] = df['Multiplier'] + df['Play']
print(df)
# Get the sum of the Scores
print("Total Score:", df['Score'].sum())
print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))