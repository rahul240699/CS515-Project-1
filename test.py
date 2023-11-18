import unittest
import os
import subprocess
#print("Hello World!")

#tests with pytest.py

# def inc(x):
#     return x + 1

# def test_answer():
#     assert inc(3) == 4

class TestResult(Exception):
    pass

class OutputMismatch(TestResult):
    pass

class NonZeroExitStatus(TestResult):
    pass

def run_test(program, test_name):
    input_file = f"test/{program}.{test_name}.in"
    expected_output_file = f"test/{program}.{test_name}.out"
    arg_expected_output_file = f"test/{program}.{test_name}.arg.out"
    args_file = f"test/{test_name}.args"

    try:
        
        print("The name of the program:" +program)
        process = subprocess.run(["python3 prog/"+program+".py "+ input_file],capture_output= True, shell= True, text=True)

        output = process.stdout
        print("This is the output:"+output)

        if os.path.exists(expected_output_file):
            with open(expected_output_file, "r") as file:
                expected_output = file.read()
            if output.strip() != expected_output.strip():
                raise OutputMismatch

       
        # if os.path.exists(args_file):
        #     with open(args_file, "r") as file:
        #         args = file.read().split()
        #     process_args = [f"python3 prog/{program}.py"] + args
        #     process = subprocess.run(
        #         stdout = subprocess.PIPE,stderr = subprocess.PIPE,
        #         text=True
        #     )

           
        #     if os.path.exists(arg_expected_output_file):
        #         with open(arg_expected_output_file, "r") as file:
        #             expected_output = file.read()
        #         if process.stdout.strip() != expected_output.strip():
        #             raise OutputMismatch

        
        if process.returncode != 0:
            raise NonZeroExitStatus

        return True

    except OutputMismatch:
        print(f"FAIL: {program} {test_name} failed ({OutputMismatch})")
        print("      expected:")
        print(open(expected_output_file).read())
        print("\n           got:")
        print(process.stdout.strip())
        return False

    except NonZeroExitStatus:
        print(f"FAIL: {program} {test_name} failed ({NonZeroExitStatus})")
        return False

def run_tests(program):
    test_count = 0
    pass_count = 0
    
    for test_file in os.listdir("test"):
        #print(test_file)
        if test_file.endswith(f".in") and program in test_file:
            print(test_file)
            test_name = test_file.replace(f"{program}.", "").replace(".in", "")
            print(test_name)
            test_count += 1
            if run_test(program, test_name):
                pass_count += 1

    print("\nOK:", pass_count)
    print("output mismatch:", test_count - pass_count)
    print("total:", test_count)

if __name__ == "__main__":
    programs = ["wc", "gron"]

    for program in programs:
        print(f"\nRunning tests for {program}...\n")
        run_tests(program)


# def test_wc():
#     input_files = [f for f in files if f.endswith(".in") and "WC" in f]
#     for i in input_files:
#         with open(test_dir+"/"+i, "r") as test:
#             command = test.readline().strip().split(" ")

#         result = subprocess.run(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, text = True) 
#         output = result.stdout
#         error = result.stderr
#         exit_code = result.returncode
        
#         output_file = i[:-2] + "out"
#         if os.path.isfile(test_dir+"/"+output_file):
#             expected_output = ""
#             with open(test_dir+"/"+output_file) as std:
#                 expected_output = std.read()
#             assert expected_output.strip() == output.strip()
        
#         status_file = i[:-2] + "status"
#         if os.path.isfile(test_dir+"/"+status_file):
#             expected_exit_code = ""
#             with open(test_dir+"/"+status_file) as ste:
#                 expected_exit_code = int(ste.read())
#             assert expected_exit_code == exit_code

# def test_gron():
#     input_files = [f for f in files if f.endswith(".in") and "GRON" in f]
#     for i in input_files:
#         with open(test_dir+"/"+i, "r") as test:
#             command = test.readline().strip().split(" ")
#         result = subprocess.run(command, stdout = subprocess.PIPE,stderr = subprocess.PIPE, text = True) 
#         output = result.stdout
#         error = result.stderr
#         exit_code = result.returncode

#         output_file = i[:-2] + "out"
#         if os.path.isfile(test_dir+"/"+output_file):
#             expected_output = ""
#             with open(test_dir+"/"+output_file) as std:
#                 expected_output = std.read()
#             assert expected_output.strip() == output.strip()
        
#         status_file = i[:-2] + "status"
#         if os.path.isfile(test_dir+"/"+status_file):
#             expected_exit_code = ""
#             with open(test_dir+"/"+status_file) as ste:
#                 expected_exit_code = int(ste.read())
#             assert expected_exit_code == exit_code

# def test_CSV():
#     input_files = [f for f in files if f.endswith(".in") and "CSV" in f]
#     for i in input_files:
#         with open(test_dir+"/"+i, "r") as test:
#             command = test.readline().strip().split(" ")
#         result = subprocess.run(command, stdout = subprocess.PIPE,stderr = subprocess.PIPE, text = True) 
#         output = result.stdout
#         error = result.stderr
#         exit_code = result.returncode

#         output_file = i[:-2] + "out"
#         if os.path.isfile(test_dir+"/"+output_file):
#             expected_output = ""
#             with open(test_dir+"/"+output_file) as std:
#                 expected_output = std.read()
#             assert expected_output.strip() == output.strip()
        
#         status_file = i[:-2] + "status"
#         if os.path.isfile(test_dir+"/"+status_file):
#             expected_exit_code = ""
#             with open(test_dir+"/"+status_file) as ste:
#                 expected_exit_code = int(ste.read())
#             assert expected_exit_code == exit_code
