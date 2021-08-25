# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py --number1 4 --number2 5 --operations add      
# 4
# 5
# add
# 9
# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py --number1 4 --number2 5 --operations multi    
# 4
# 5
# multi
# 20
# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py --number1 4 --number2 5
# 4
# 5
# None
# Goodbye!
# PS D:\Machines\Languages\VSC>

# After applying opertions restrcitions
# PS D:\Machines\Languages\VSC> & C:/Users/Shivam/AppData/Local/Programs/Python/Python38/python.exe d:/Machines/Languages/VSC/tmp.py --number1 4 --number2 5 --operations divide
# usage: tmp.py [-h] [--number1 NUMBER1] [--number2 NUMBER2] [--operations {add,subs,multi}]
# tmp.py: error: argument --operations: invalid choice: 'divide' (choose from 'add', 'subs', 'multi')

import argparse

parser = argparse.ArgumentParser()

# adding -- makes aruguments optional
parser.add_argument("--number1", help="Number 1 Here!")
parser.add_argument("--number2", help="Number 2 Here!")
parser.add_argument("--operations", help="Operations to perform")

# To restrict choices
# parser.add_argument("--operations", help="Operations to perform", \
#      choices=["add", "subs","multi"])

args = parser.parse_args()
# print(args)
print(args.number1)
print(args.number2)
print(args.operations)

# build a normal calc 
a = int(args.number1)
b = int(args.number2)

if args.operations == "add":
    print(a + b)
elif args.operations == "subs":
    print(a - b)
elif args.operations == "multi":
    print(a * b)
else:
    print("Goodbye!")
