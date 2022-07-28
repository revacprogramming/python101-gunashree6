def main():
  n=int(input())
  fdi={}
  for a in range(n):
    x=int(input())
    w=input()
    l=[]
    for i in range(len(w)):
      for j in range(i+3,len(w)+1):
        s=w[i:j]        
        if(s==s[::-1]):  
          l.append((i+1,s))
    fdi[w]=l
  for i,j in fdi.items():
    print(i)
    for k in j:
      print(k[0],end="\t")
      print(k[1])
    print("\n")
main()