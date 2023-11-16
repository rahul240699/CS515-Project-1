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
    input_files = [f for f in files if f.endswith(".in") and "WC" in f]
    for i in input_files:
        with open(test_dir+"/"+i, "r") as test:
            command = test.readline().strip().split(" ")

        result = subprocess.run(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True) 
        output = result.stdout
        error = result.stderr
        exit_code = result.returncode
        
        output_file = i[:-2] + "out"
        if os.path.isfile(test_dir+"/"+output_file):
            expected_output = ""
            with open(test_dir+"/"+output_file) as std:
                expected_output = std.read()
            assert expected_output.strip() == output.strip()
        
        status_file = i[:-2] + "status"
        if os.path.isfile(test_dir+"/"+status_file):
            expected_exit_code = ""
            with open(test_dir+"/"+status_file) as ste:
                expected_exit_code = ste.read()
            assert expected_exit_code.strip() == exit_code.strip()

def test_1gron():
    input_files = [f for f in files if f.endswith(".in") and "GRON" in f]
    for i in input_files:
        result = subprocess.run(["python", "prog/gron.py", test_dir+"/"+i], stdout = subprocess.PIPE, text = True) 
        output = result.stdout
        output_file = i[:-2] + "out"
        if os.path.isfile(test_dir+"/"+output_file):
            expected_output = ""
            with open(test_dir+"/"+output_file) as std:
                expected_output = std.read()
            assert expected_output.strip() == output.strip()
