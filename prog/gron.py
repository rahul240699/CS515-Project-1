import argparse
import json
import os

def gron(data, parent):
    # print(json_file)
    # print(type(json_file))
    # if isinstance()
    # f = open(json_file)
    # data = json.load(f)

    if isinstance(data, dict):
        for k, v in data.items():
            new_parent = f"{parent}.{k}" if parent else k
            gron(v, new_parent)
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_parent = f"{parent}[{i}]"
            gron(item, new_parent)
    else:
        print(f"{parent} = {json.dumps(data)};")



def main():
    parser = argparse.ArgumentParser(prog = "Gron Functionality", description = "Flattens JSON.")

    parser.add_argument("filename", type = str, help = "Enter the name of the file.")

    args = parser.parse_args()
    #data = json.loads(args.filename)

    # print(type(f))
    # print(args.filename)
    f = open(args.filename)
    data = json.load(f)
    gron(data, "")

if __name__ == "__main__":
    main()