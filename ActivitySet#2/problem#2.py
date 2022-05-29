
def add(a, b):
     s=a+b # ...\
     return s

def output(a, b, sum):
    print("{a}+{b}={c}")

def main():
    a, b = map(int(input("input?").spilt()))
    sum = add(a, b)
    output(a, b, sum)


if __name__ == '__main__':
    main()
