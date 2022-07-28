from fractions import Fraction as fc
x=int(input())
l=[]
ll=[]
di={}
g=0
for i in range(x):
  y=int(input())
  l=input().split()
  g=0
  ll=[]
  for j in range(y):
    g+=fc(f'1/{l[j]}')
    ll.append(fc(f'1/{l[j]}'))
  di[g]=ll
for i,j in di.items():
   print(*j,sep='+',end="=")
   print(i)