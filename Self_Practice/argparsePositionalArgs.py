# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py -h     
# usage: tmp.py [-h] number1 number2 operations

# positional arguments:
#   number1     Number 1 Here!
#   number2     Number 2 Here!
#   operations  Operations to perform

# optional arguments:
#   -h, --help  show this help message and exit

# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py 4 5 add
# 4
# 5
# add
# 9
# PS D:\Machines\Languages\VSC> 

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("number1", help="Number 1 Here!")
parser.add_argument("number2", help="Number 2 Here!")
parser.add_argument("operations", help="Operations to perform")
args = parser.parse_args()
# print(args)
print(args.number1)
print(args.number2)
print(args.operations)
a = int(args.number1)
b = int(args.number2)
print(a + b)
