import argparse
import subprocess
import os

def word_count_file(filename):
    with open(filename, "r") as file:
        lines = 0
        words = 0
        chars = 0

        for line in file:
            lines += 1
            words += len(line.split(" "))
            chars += len(line)
    return lines, words, chars 



def main():
    parser = argparse.ArgumentParser(prog= "Word Count Functionality", description= "Returns the count of words of the given input.")
    #parser.print_help()

    parser.add_argument("filename", type = str, help = "Enter the name of the file")


    args = parser.parse_args()

    if args.filename != None:
        if not os.path.isfile(args.filename):
            print(args.filename+": No such file or directory")
        else:
            lines, words, chars = word_count_file(filename = args.filename)
            print(f"{lines} {words} {chars} {args.filename}")

if __name__ == "__main__":
    main()