import argparse
import subprocess
import os
import sys
import pandas as pd



def sum_csv(filename, columns = "", scr = False, col_range = None):
    try:
        df = pd.read_csv(filename)

        if not (col_range == None):
            start, end = map(str.strip, col_range.split(':'))   
            selected_columns = df.columns[int(start):int(end)+1]
        else:
            selected_columns = columns

        for column in selected_columns:
            if column not in df.columns:
                raise ValueError(f"Column {column} not found in the file.")
        
        if scr:
            res = df[selected_columns].sum(axis = 1)
        else:
            res = df[selected_columns].sum()
        
        print(res)
    except Exception as e:
        print(e)
        sys.exit(1)
    
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(prog= "csvsum", description= "Returns the sum of given columns of a csv file.")

    parser.add_argument("filename", type = str, help="Enter the name of the csv file.")
    parser.add_argument("columns", nargs="*", help="Enter the names of the columns to be summed.")
    parser.add_argument("-s", "--sum_elements", action="store_true", help="Sum Column elemensts row wise.")
    parser.add_argument("--col_range", type=str, nargs="?", help="Sum of specified range of columns, separated by :")

    args = parser.parse_args()

    #print(args.col_range)

    sum_csv(args.filename, args.columns, args.sum_elements, args.col_range)


if __name__ == "__main__":
    main()