import pandas as pd
import numpy as np
from textwrap import wrap
import re
import time

def parse_move(move):
    values = re.findall(r'\d+', move)
    return values

def parse_box_list(boxes_list):
    boxes_list = boxes_list[:-1]
    row_lists = []
    for row in boxes_list:
        new_val = wrap(row,4,replace_whitespace=False, drop_whitespace=False)
        for i in range(len(new_val)):
            new_val[i] = new_val[i].replace('[','')
            new_val[i] = new_val[i].replace(']','')
            new_val[i] = new_val[i].replace(' ','')
        row_lists.append(new_val)
    column_lists = [''] * 9
    for i in range(len(row_lists)):
        for j in range(0,9):
            column_lists[j]+=row_lists[i][j]
    return column_lists

def get_state_df(boxes_list):
    state_lists = parse_box_list(boxes_list)
    column_names= ['1','2','3','4','5','6','7','8','9']
    df = pd.DataFrame(state_lists).T
    df.columns = column_names
    return df

def perform_move(amount, column1, column2):
    return column1

if __name__ == "__main__":

    start_time = time.time()

    with open('input.txt') as file:
        lines = file.read().splitlines()

    # Get the current box state and store into a dataframe
    boxes_list = lines[:lines.index('')]
    df = get_state_df(boxes_list)
    df['NumberOfBoxes'] = 0
    df['FromColumn'] = 1
    df['ToColumn'] = 2

    moves_list = lines[lines.index('')+1:]
    for move in moves_list:
        values = parse_move(move)
        new_row = {'1': '',
                   '2': '',
                   '3': '',
                   '4': '',
                   '5': '',
                   '6': '',
                   '7': '',
                   '8': '',
                   '9': '',
                   'NumberOfBoxes': values[0],
                   'FromColumn': values[1],
                   'ToColumn': values[2]}
        df = df.append(new_row, ignore_index=True)
        
    print(df)
    print("--- Execution: %.4f ms ---" % (float(time.time() - start_time)*1000))
    #print(moves_list)

