import pandas as pd
import time

def range_to_int_min(range_vals):
    values = range_vals.split('-')
    val1 = int(values[0])
    return val1

def range_to_int_max(range_vals):
    values = range_vals.split('-')
    val2 = int(values[1])
    return val2

def range_to_set(range_vals):
    values = range_vals.split('-')
    val1 = int(values[0])
    val2 = int(values[1])
    if val1==val2:
        return set({val1})
    return set(range(val1, val2+1))

def get_inclusive(min1, max1, min2, max2):
    if ((min1 >= min2) and (max1 <= max2)) or ((min2 >= min1) and (max2 <= max1)):
            return 1
    return 0

def get_any_inclusive(set, set2):
    for val in set:
        if val in set2:
            return 1
    return 0

if __name__ == "__main__":

    start_time = time.time()

    with open('input.txt') as file:
        lines = file.read().splitlines()

    # Add lines to dataframe
    df = pd.DataFrame(lines, columns=['Ranges'])
    # Split into 2 columns on comma
    df[['Elf_1','Elf_2']] = df['Ranges'].str.split(',', 1, expand=True)

    #Convert the columns from ranges to strings
    df['Elf_1_Min'] = df['Elf_1'].apply(lambda x: range_to_int_min(x))
    df['Elf_1_Max'] = df['Elf_1'].apply(lambda x: range_to_int_max(x))
    df['Elf_2_Min'] = df['Elf_2'].apply(lambda x: range_to_int_min(x))
    df['Elf_2_Max'] = df['Elf_2'].apply(lambda x: range_to_int_max(x))
    #print(df)
    #Check if one is string is in the other
    df['Match'] = df.apply(lambda x: get_inclusive(x['Elf_1_Min'], x['Elf_1_Max'], x['Elf_2_Min'], x['Elf_2_Max']), axis=1)
    #with pd.option_context('display.max_rows', None):
    #    print(df)
    #Sum all match columns
    print("Total Matches:", df['Match'].sum())
    print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))

    ## Part 2 ##
    start_time = time.time()

    df['Elf1_Set'] = df['Elf_1'].apply(lambda x: range_to_set(x))
    df['Elf2_Set'] = df['Elf_2'].apply(lambda x: range_to_set(x))
    
    df['Match2'] = df.apply(lambda x: get_any_inclusive(x['Elf1_Set'], x['Elf2_Set']), axis=1)
    print(df)
    print("Total Matches:", df['Match2'].sum())
    print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))