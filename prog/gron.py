import argparse
import json
import os

def gron(data, parent = "", open_dict = True):
    if isinstance(data, dict):
        if not parent:
            print(f"json = {{}};")
        if open_dict and parent:
            print(f"json.{parent} = {{}};")
        for k, v in data.items():
            new_parent = f"{parent}.{k}" if parent else k
            gron(v, new_parent, isinstance(v, dict))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_parent = f"{parent}[{i}]"
            gron(item, new_parent, isinstance(item, dict))
    else:
        print(f"json.{parent} = {json.dumps(data)};")



def main():
    parser = argparse.ArgumentParser(prog = "Gron Functionality", description = "Flattens JSON.")

    parser.add_argument("filename", type = str, help = "Enter the name of the file.")

    args = parser.parse_args()
    
    f = open(args.filename)
    data = json.load(f)
    gron(data)

if __name__ == "__main__":
    main()