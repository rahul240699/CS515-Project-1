import argparse
import subprocess
import os
import sys
import pandas as pd



def sum_csv(filename, columns):
    try:
        df = pd.read_csv(filename)

        for column in columns:
            if column not in df.columns:
                raise ValueError(f"Column {column} not found in the file.")
            
        res = df[columns].sum()

        print(res)

    except Exception as e:
        print(e)
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(prog= "csvsum", description= "Returns the sum of given columns of a csv file.")

    parser.add_argument("filename", type = str, nargs= "?", help="Enter the name of the csv file.")
    parser.add_argument("columns", nargs="*", help="Enter the names of the columns to be summed.")

    args = parser.parse_args()

    sum_csv(args.filename, args.columns)


if __name__ == "__main__":
    main()