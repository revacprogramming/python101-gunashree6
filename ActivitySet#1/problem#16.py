# Databases
# https://www.py4e.com/lessons/database
import token


m=int(input("enter the max value:"))
evensum=0
oddsum=0
for num in range(1,m+1):
    if(num%2==0):
        evensum=evensum + num
    else:
        oddsum=oddsum+num
print("the sum of even num till",num,"is",evensum )
print("the sum of odd num till",num,"is",oddsum)