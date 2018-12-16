import csv
import pygal
data51 = csv.reader(open("2551.txt"))
data52 = csv.reader(open("2552.txt"))
data53 = csv.reader(open("2553.txt"))
data54 = csv.reader(open("2554.txt"))
data55 = csv.reader(open("2555.txt"))

sick51 = []
sick52 = []
sick53 = []
sick54 = []
sick55 = []


givesick1 = []
givesick2 = []
givesick3 = []


for i in data51:
    sick51.append(i)
for i in sick51:
    if i[0] == "โรคภูมิคุ้มกันบกพร่องจากเชื้อไวรัส":
        givesick1.append(int(i[1]))
for i in data52:
    sick52.append(i)
for i in sick52:
    if i[0] == "โรคภูมิคุ้มกันบกพร่องจากเชื้อไวรัส":
        givesick1.append(int(i[1]))
for i in data53:
    sick53.append(i)
for i in sick53:
    if i[0] == "โรคภูมิคุ้มกันบกพร่องจากเชื้อไวรัส":
        givesick1.append(int(i[1]))
for i in data54:
    sick54.append(i)
for i in sick54:
    if i[0] == "โรคภูมิคุ้มกันบกพร่องจากเชื้อไวรัส":
        givesick1.append(int(i[1]))
for i in data55:
    sick55.append(i)
for i in sick55:
    if i[0] == "โรคภูมิคุ้มกันบกพร่องจากเชื้อไวรัส":
        givesick1.append(int(i[1]))

for i in sick51:
    if i[0] == "ไตวายเฉียบพลัน":
        givesick2.append(int(i[1]))
for i in sick52:
    if i[0] == "ไตวายเฉียบพลัน":
        givesick2.append(int(i[1]))
for i in sick53:
    if i[0] == "ไตวายเฉียบพลัน":
        givesick2.append(int(i[1]))
for i in sick54:
    if i[0] == "ไตวายเฉียบพลัน":
        givesick2.append(int(i[1]))
for i in sick55:
    if i[0] == "ไตวายเฉียบพลัน":
        givesick2.append(int(i[1]))

for i in sick51:
    if i[0] == "ไส้เลื่อน":
        givesick3.append(int(i[1]))
for i in sick52:
    if i[0] == "ไส้เลื่อน":
        givesick3.append(int(i[1]))
for i in sick53:
    if i[0] == "ไส้เลื่อน":
        givesick3.append(int(i[1]))
for i in sick54:
    if i[0] == "ไส้เลื่อน":
        givesick3.append(int(i[1]))
for i in sick55:
    if i[0] == "ไส้เลื่อน":
        givesick3.append(int(i[1]))

print(givesick1)
print(givesick2)
print(givesick3)

line = pygal.Bar()
line.title = "เปรียบเทียบอัตราผู้ป่วยจากกลุ่มโรคทั้ง 3 โรค ตลอดระยะเวลา 5 ปี"
line.x_labels = (2551, 2552, 2553, 2554, 2555)
line.add("โรคภูมิคุ้มกันบกพร่องจากเชื้อไวรัส", givesick1)
line.add("ไตวายเฉียบพลัน", givesick2)
line.add("ไส้เลื่อน", givesick3)
line.render_to_file("pair.svg")\