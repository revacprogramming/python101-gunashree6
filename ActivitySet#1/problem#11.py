# Tuples
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
d=dict()
for line in handle:
    if not line.startswith("From "):
        continue
    l=line.split()
    l=l[5]
    l=l[0:2]
    d[l]=d.get(l,0)+1
tem=sorted([(v,c) for v,c in d.items()])

for v,c in tem:
    print(v,c)
