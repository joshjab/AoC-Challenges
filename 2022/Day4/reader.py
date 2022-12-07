import pandas as pd
import time

def range_to_string(range_vals):
    values = range_vals.split('-')
    val1 = int(values[0])
    val2 = int(values[1])
    range_str = ""
    for i in range(val1,val2+1):
        range_str+=str(i)+','
    return range_str[:-1]

def get_inclusive(str1, str2):
    if (str1 in str2) or (str2 in str1):
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
    df['Elf_1_Str'] = df['Elf_1'].apply(lambda x: range_to_string(x))
    df['Elf_2_Str'] = df['Elf_2'].apply(lambda x: range_to_string(x))
    #Check if one is string is in the other
    df['Match'] = df.apply(lambda x: get_inclusive(x['Elf_1_Str'], x['Elf_2_Str']), axis=1)
    with pd.option_context('display.max_rows', None):
        print(df)
    #Sum all match columns
    print("Total Matches:", df['Match'].sum())
    print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))