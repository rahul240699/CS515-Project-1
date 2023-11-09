import argparse
import subprocess
import os
import sys

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
    parser.add_argument("-l", "--lines", action = "store_true", help = "Count only the total number of lines.")
    parser.add_argument("-w", "--words", action = "store_true", help = "Count only the total number of words.")
    parser.add_argument("-c", "--characters", action = "store_true", help = "Count only the total number of characters.")


    args = parser.parse_args()

    try:
        # if args.filename is None:
        #     raise ValueError(args.filename+": ")
        # else:
            if not os.path.isfile(args.filename):
                raise ValueError(args.filename+": No such file or directory")
            else:
                lines, words, chars = word_count_file(filename = args.filename)
                if args.lines and args.words:
                    print(f"{lines} {words} {args.filename}")
                elif args.lines and args.characters:
                    print(f"{lines} {chars} {args.filename}")
                elif args.characters and args.words:
                    print(f"{words} {chars} {args.filename}")
                elif args.lines:
                    print(f"{lines} {args.filename}")
                elif args.words:
                    print(f"{words} {args.filename}")
                elif args.characters:
                    print(f"{chars} {args.filename}")
                else:
                    print(f"{lines} {words} {chars} {args.filename}")
    except Exception as e:
        print(e)
        sys.exit(1)
    

if __name__ == "__main__":
    main()