# CS 515 Project 1

## Author Information
Rahul Sohandani 
rsohanda@stevens.edu

[Github Repository](https://github.com/rahul240699/CS515-Project-1)

## Estimation of Hours Spent on the project
I spent around 9 hours approximately on the project.

## Testing of the code
1. Initially I started the testing on my PC's terminal.
2. Later on I wrote test cases in the format specified in description, and used the test harness to run the tests and capturing the output, to compare with the expected out in the corresponding .out files for the test.

## Unresolved Bugs or Issues
1. It was working fine earlier, but now I am facing an issue where I am pushing my code on github for the github actions, github is unable to capture output from the subprocess command i.e, the stdout from command line, therefore, however it works fine on my local pc, so I believe, it is an environment related issue.
2. While running test harness to take arguments from the args file the harness is unable to capture the output for the arguments. The program works when you pass arguments on command line itself.



## Examples of difficult bugs resolved
1. I was facing an issue with taking input from stdin initially, however I could resolve that by adding **sys.stdin.isatty()**, which returns true if the input is from command line and false if it from stdin, this allowed me to add separate conditions for both the cases.
2. I was unable to get the execution to stop at one condition and also capture errors, this was resolved by Exception Handling and using **sys.exit()** statements.

## Extensions Implemented
1. **More advanced wc: Multple Files** : I have implemented the extension for wc where one can input multiple files and get the total count of characters, words, and lines. The following example shows the sample input and output for this.

```
$ python3 prog/wc.py file1.txt file2.txt
1       1       6 file1.txt
1       1      16 file2.txt
2       2      22 total
```

2. **More advanced wc: Flags to control output**: I have implemented wc flags **-l**, **-w** and **-c**, to control output. The following example shows sample input and the sample output for this.
```
$ python3 prog/wc.py test/wc.basic.in -l -w
7 412 test/wc.basic.in
$ python3 prog/wc.py test/wc.basic.in -c
2620 test/wc.basic.in
```

3. **Extension: More advanced gron: control the base-object name** : I have implemented the extension to control the main object name for gron. The following shows sample input and the sample output for the same.
```
$ python3 prog/gron.py --obj o gron.basic.in 
o = {};
o.menu = {};
o.menu.id = "file"
o.menu.value = "File"
o.menu.popup = {};
o.menu.popup.menuitem = [];
o.menu.popup.menuitem[0] = {};
o.menu.popup.menuitem[0].value = "New"
o.menu.popup.menuitem[0].onclick = "CreateNewDoc()"
o.menu.popup.menuitem[1] = {};
o.menu.popup.menuitem[1].value = "Open"
o.menu.popup.menuitem[1].onclick = "OpenDoc()"
o.menu.popup.menuitem[2] = {};
o.menu.popup.menuitem[2].value = "Close"
o.menu.popup.menuitem[2].onclick = "CloseDoc()"
```
## Program 3: csvsum
For my Program 3 I have implemented the csvsum functionality, which takes input the name of the columns and returns the sum of the columns. The following example highlights the working of csvsum functionality.
```
$ python3 prog/csvsum.py salary_data.csv YearsExperience, Salary
YearsExperience        159.4
Salary             2280090.0
dtype: float64
```

## Utilities for **csvsum**
I have implemented the following 2 utilities for **csvsum**.
1. **Sum Elements** - If true then returns row-wise sum for all the elements for the specified columns. The following example shows utility.
```
$ python3 prog/csvsum.py salary_data.csv YearsExperience, Salary -s
0      39344.1
1      46206.3
2      37732.5
3      43527.0
4      39893.2
5      56644.9
6      60153.0
7      54448.2
8      64448.2
9      57192.7
10     63221.9
11     55798.0
12     56961.0
13     57085.1
14     61115.5
15     67942.9
16     66034.1
17     83093.3
18     81368.9
19     93946.0
20     91744.8
21     98280.1
22    101309.9
23    113820.2
24    109439.7
25    105591.0
26    116978.5
27    112644.6
28    122401.3
29    121882.5
dtype: float64
```

2. **Column Range** : Allows to specify a range of columns instead of specifying the names of the columns. Look at the following example.
```
$ python3 prog/csvsum.py grades.csv --col_range 3:5                           
Test1    695.0
Test2    497.0
Test3    978.0
dtype: float64
```