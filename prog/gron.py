import argparse
import json
import os

def gron(data, parent = "", open_dict = True, open_list = True, obj = "json"):
    if isinstance(data, dict):
        if not parent:
            print(f"{obj} = {{}};")
        if open_dict and parent:
            print(f"{obj}.{parent} = {{}};")
        for k, v in data.items():
            new_parent = f"{parent}.{k}" if parent else k
            gron(v, new_parent, isinstance(v, dict), isinstance(v,list), obj)
    elif isinstance(data, list):
        if not parent:
            print(f"{obj} = []")
        if open_list:
            print(f"{obj}.{parent} = []")
        for i, item in enumerate(data):
            new_parent = f"{parent}[{i}]"
            gron(item, new_parent, isinstance(item, dict), isinstance(item, list), obj)
    else:
        print(f"{obj}.{parent} = {json.dumps(data)};")



def main():
    parser = argparse.ArgumentParser(prog = "Gron Functionality", description = "Flattens JSON.")

    parser.add_argument("filename", type = str, help = "Enter the name of the file.")
    parser.add_argument("--obj", type= str, default="json", help="Print out a different name of the Object")
    

    args = parser.parse_args()
    # print(args.obj)
    
    f = open(args.filename)
    data = json.load(f)
    gron(data, obj = args.obj)

if __name__ == "__main__":
    main()