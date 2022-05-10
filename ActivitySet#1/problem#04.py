# Conditional Execution

hrs = input("Enter hours? ")
h = float(hrs)
rate=input("Enter rate:")
r = float(rate)
if h<=40:
    print(h*r)
elif h>40:
    print(40*r+(h-40)*1.5*r)