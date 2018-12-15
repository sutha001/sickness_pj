import csv
file51 = open("2551.txt")
data51 = csv.reader(file51)
lis = []
for i in data51:
    lis.append(i)
print(lis)
