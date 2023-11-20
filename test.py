import sys
import os
import subprocess


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
    args_file = f"test/{program}.{test_name}.args"

    try:
        
        # print("The name of the program:" +program)
        # process = subprocess.check_output(["python3", "prog/"+program+".py", input_file], universal_newlines=True)

        process = subprocess.run(["python3 prog/"+program+".py "+ input_file], capture_output= True, shell= True, text=True)
        
        # process = subprocess.Popen(["python3", "prog/"+program+".py", input_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # process = subprocess.run(["python3", "prog/"+program+".py ",input_file], stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        output = process.stdout
        # print("This is the output:"+output)

        if os.path.exists(expected_output_file):
            with open(expected_output_file, "r") as file:
                expected_output = file.read()
            if output.strip() != expected_output.strip():
                raise OutputMismatch

       
        if os.path.exists(args_file):
            with open(args_file, "r") as file:
                args = file.read().split(" ")
            process_args = ["python3","prog/"+program+".py", input_file] + args
            for i in args:
                process_args[0] += " "+i
            # process = subprocess.check_output(process_args, universal_newlines=True)

            # process = subprocess.run(process_args, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell= True, text=True)
            

            # print("The output:" + process.stdout.strip()+ " The INPUT: "+ str(process_args))
           
            if os.path.exists(arg_expected_output_file):
                with open(arg_expected_output_file, "r") as file:
                    expected_output = file.read()
                if process.stdout.strip() != expected_output.strip():
                    raise OutputMismatch

        
        if process.returncode != 0:
            raise NonZeroExitStatus

        return True

    except OutputMismatch:
        print(f"FAIL: {program} {test_name} failed ({OutputMismatch})")
        print("expected:")
        print(open(expected_output_file).read())
        print("\ngot:")
        print(process.strip())
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
            # print(test_file)
            test_name = test_file.split(".")[1]
            # print(test_name)
            test_count += 1
            if run_test(program, test_name):
                pass_count += 1

    print("\nOK:", pass_count)
    print("Output mismatch:", test_count - pass_count)
    print("total:", test_count)

if __name__ == "__main__":
    programs = ["wc", "gron"]

    for program in programs:
        print(f"\nRunning tests for {program}\n")
        run_tests(program)