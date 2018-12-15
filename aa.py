import csv
data51 = csv.reader(open("2551.txt"))
data52 = csv.reader(open("2552.txt"))
data53 = csv.reader(open("2553.txt"))
data54 = csv.reader(open("2554.txt"))
data55 = csv.reader(open("2555.txt"))
top10_2551 = []
top10_2552 = []
top10_2553 = []
top10_2554 = []
top10_2555 = []
for i in data51:
    top10_2551.append(i)
print(2551,top10_2551[:10])

for i in data52:
    top10_2552.append(i)
print(2552,top10_2552[:10])

for i in data53:
    top10_2553.append(i)
print(2553,top10_2553[:10])

for i in data54:
    top10_2554.append(i)
print(2554,top10_2554[:10])

for i in data55:
    top10_2555.append(i)
print(2555,top10_2555[:10])
