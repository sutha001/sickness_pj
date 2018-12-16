import csv
import pygal
data55 = csv.reader(open("2555.txt"))
count = 0
top10 = []
for i in data55:
    top10.append(i)
top10_2555 = top10[:10]
disease_name = []
num = []
for i in top10_2555:
    disease_name.append(i[0])
for i in top10_2555:
    num.append(i[1])
print(disease_name)
print(num)

line = pygal.Treemap()
line.title = "จำนวนผู้ป่วยปี2555 Top 10"
line.x_labels = ("")
line.add(disease_name[0], int(num[0]))
line.add(disease_name[1], int(num[1]))
line.add(disease_name[2], int(num[2]))
line.add(disease_name[3], int(num[3]))
line.add(disease_name[4], int(num[4]))
line.add(disease_name[5], int(num[5]))
line.add(disease_name[6], int(num[6]))
line.add(disease_name[7], int(num[7]))
line.add(disease_name[8], int(num[8]))
line.add(disease_name[9], int(num[9]))
line.render_to_file("top10_2555.svg")\