# Functions


def computepay(h, r):
    if h<=40:
        pay=h*r
    elif h>40:
        pay=40*r+(h-40)*1.5*r
    return pay


hrs = float(input("Enter hours? "))
rate = float(input("Enter rate per hour? "))

p = computepay(hrs, rate)
print("Pay", p)
