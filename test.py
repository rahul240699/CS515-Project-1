import unittest
import os
import subprocess
#print("Hello World!")

#tests with pytest.py

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4

test_dir = "test"
files = os.listdir(test_dir)


def test_1wc():
    input_files = [f for f in files if f.endswith(".in")]
    for i in input_files:
        result = subprocess.run(["python", "prog/wc.py", test_dir+"/"+i], stdout=subprocess.PIPE, text = True) 
        output = result.stdout
        output_file = i[:-2] + "out"
        if os.path.isfile(test_dir+"/"+output_file):
            expected_output = ""
            with open(test_dir+"/"+output_file) as std:
                expected_output = std.read()
            assert expected_output.strip() == output.strip()