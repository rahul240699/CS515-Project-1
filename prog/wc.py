import argparse
import subprocess
import os
import sys
import io

def word_count_file(file):
    lines = 0
    words = 0
    chars = 0

    for line in file:
        lines += 1
        words += len(line.split(" "))
        chars += len(line)
    return lines, words, chars 



def main():
    parser = argparse.ArgumentParser(prog= "wc", description= "Returns the count of words of the given input.")
    #parser.print_help()

    parser.add_argument("filenames", type = str, nargs = "*", help = "Enter the name of the file")
    parser.add_argument("-l", "--lines", action = "store_true", help = "Count only the total number of lines.")
    parser.add_argument("-w", "--words", action = "store_true", help = "Count only the total number of words.")
    parser.add_argument("-c", "--characters", action = "store_true", help = "Count only the total number of characters.")

    total_lines = 0
    total_words = 0
    total_chars = 0

    file = ""

    args = parser.parse_args()

    
    try:
        if not sys.stdin.isatty():
            lines, words, chars = word_count_file(file = sys.stdin)
            if args.lines and args.words:
                print(f"{lines} {words}")
            elif args.lines and args.characters:
                print(f"{lines} {chars}")
            elif args.characters and args.words:
                print(f"{words} {chars}")
            elif args.lines:
                print(f"{lines}")
            elif args.words:
                print(f"{words}")
            elif args.characters:
                print(f"{chars}")
            else:
                print(f"{lines} {words} {chars}")
            sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error: {e}")
        sys.exit(1)
            
    file = args.filenames

    for filename in file:
        try:
            with open(filename, "r") as file:
                lines, words, chars = word_count_file(file = file)
            
            total_lines += lines
            total_words += words
            total_chars += chars

            if args.lines and args.words:
                print(f"{lines} {words} {filename}")
            elif args.lines and args.characters:
                print(f"{lines} {chars} {filename}")
            elif args.characters and args.words:
                print(f"{words} {chars} {filename}")
            elif args.lines:
                print(f"{lines} {filename}")
            elif args.words:
                print(f"{words} {filename}")
            elif args.characters:
                print(f"{chars} {filename}")
            else:
                print(f"{lines} {words} {chars} {filename}")
        except Exception as e:
            sys.stderr.write(f"Error: {e}")
            sys.exit(1)
    try:
        if len(args.filenames) > 1:
            print(f"{total_lines} {total_words} {total_chars} total")
    except Exception as e:
        sys.stderr.write(f"Error: {e}")
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    main()