import pandas as pd
import time

priority_dict = { 'a':1, 'b':2,
                  'c':3, 'd':4,
                  'e':5, 'f':6,
                  'g':7, 'h':8,
                  'i':9, 'j':10,
                  'k':11, 'l':12,
                  'm':13, 'n':14,
                  'o':15, 'p':16,
                  'q':17, 'r':18,
                  's':19, 't':20,
                  'u':21, 'v':22,
                  'w':23, 'x':24,
                  'y':25, 'z':26,
                  'A':27, 'B':28,
                  'C':29, 'D':30,
                  'E':31, 'F':32,
                  'G':33, 'H':34,
                  'I':35, 'J':36,
                  'K':37, 'L':38,
                  'M':39, 'N':40,
                  'O':41, 'P':42,
                  'Q':43, 'R':44,
                  'S':45, 'T':46,
                  'U':47, 'V':48,
                  'W':49, 'X':50,
                  'Y':51, 'Z':52}

def half(str):
    halflen = int(len(str)/2)
    return str[0:halflen], str[halflen:len(str)]

def get_match(str1, str2):
    char = ''
    for char in str1:
        if char in str2:
            return char
    return char

def get_match_3(str1, str2, str3):
    char = ''
    for char in str1:
        if char in str2:
            if char in str3:
                return char
    return char


if __name__ == "__main__":

    start_time = time.time()

    with open('input.txt') as file:
        lines = file.read().splitlines()

    # Each line is a rucksack, divided in half is each compartment
    ruck_df = pd.DataFrame(lines, columns=['Rucksack'])
    ruck_df['Split'] = ruck_df['Rucksack'].apply(lambda x : half(x))
    ruck_df = pd.DataFrame(ruck_df['Split'].to_list(), columns=['Comp1', 'Comp2'])

    # Need to find the item type that appears in both compartments
    ruck_df['Match'] = ruck_df.apply(lambda x: get_match(x['Comp1'], x['Comp2']),axis=1)
    ruck_df['Priority'] = ruck_df['Match'].apply(lambda x: priority_dict.get(x))

    print(ruck_df)
    print("Sum of priorities:", ruck_df['Priority'].sum())
    print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))

    ## Part 2 ##
    start_time = time.time()

    ruck_df = pd.DataFrame(lines, columns=['Rucksack'])
    # Move every 3rd rucksack to it's own column
    ruck_df['Elf_1'] = ruck_df['Rucksack'].iloc[::3]
    ruck_df['Elf_2'] = ruck_df['Rucksack'].iloc[1::3]
    ruck_df['Elf_3'] = ruck_df['Rucksack'].iloc[2::3]
    #This could be sped up with numpy if we cared
    ruck_df = ruck_df[['Elf_1', 'Elf_2', 'Elf_3']]
    ruck_df = ruck_df.apply(lambda x: pd.Series(x.dropna().values))

    ruck_df['Match'] = ruck_df.apply(lambda x: get_match_3(x['Elf_1'], x['Elf_2'], x['Elf_3']),axis=1)
    ruck_df['Priority'] = ruck_df['Match'].apply(lambda x: priority_dict.get(x))

    print("Sum of priorities:", ruck_df['Priority'].sum())
    print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))