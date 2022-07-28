def inp():
  return list((map(float,input().split())))
  
def find_area(l):
    a = l[0]*(l[3]-l[4])
    b = l[2]*(l[5]-l[1])
    c = l[4]*(l[1]-l[3])
    return abs(a+b+c)

def output(areas,a):
    for _ in range(0,a):
        for area, ver in areas.items():
            print(f"Area of rectangle with vertices ({ver[0]},{ver[1]}),({ver[2]},{ver[3]}),({ver[4]},{ver[5]}) is {area}" )
def main():
    l = list()
    areas = {}
    a=int(input("enter the number of rectangles:"))
    for i in range(a):
        l.append(inp())
        areas[find_area(l[i])] = l[i]
    output(areas,a)

if __name__ == '_main_':
    main()