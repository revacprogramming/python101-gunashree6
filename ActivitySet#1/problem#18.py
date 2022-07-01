#Lists
#problem 8.5
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
count=0
fh = open(fname)
for line in fh:
    x=line.split()
    if "From" in x:
        
        print(x[1])
        count+=1
    else:
        continue

print("There were", count, "lines in the file with From as the first word")
