#1.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง while
row = 1
while row <= 12:  # เเถว
    num = 2  # ( สูตรคูณเเม่ 2 )
    col = 2
    while col <= 12:
        print("%3dx%2d=%3d" % (num, row, num * row), end="")
        num += 1
        col += 1

    print("")
    row += 1

print("")

#2.จงเขียนตารางสูตรคูณให้ผลลัพท์ที่ออกมาเป็นแบบตัวอย่างด้านล่างโดยใช้คำสั่ง for
for number in range(2, 13):
    for i in range(1, 13):
        result = number*i
        print("%d x %d = %d" % (number, i, result))
        print("  ")
    print("-------------------------------------------------------")
