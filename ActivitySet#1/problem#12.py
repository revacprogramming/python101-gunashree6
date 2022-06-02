# Regular Expressions
# https://www.py4e.com/lessons/regex
import re

x = input("Enter File Name:")

if x !="dataset/regex_sum_42.txt":
    x="dataset/regex_sum_42.txt"
sum=0
f = open(x)
for line in f:
    y=re.findall("[0-9]+", line)
    if y != []:
        for i in y:
            i = int(i)
            sum= sum+i
print(sum)

