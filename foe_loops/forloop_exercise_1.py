# จงเขียนคำสั่งเพื่อแสดงต้น christmas โดยใช้คำสั่ง for โปรแกรมสามารถกำหนดความสูงของต้น christmas ได้

# input: height = 5
# outpu:
#      *
#     ***
#    *****
#   *******
#  *********

# input: height = 3
# outpu:
#    *
#   ***
#  *****

# input: height = 10
# outpu:
#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#   *****************
#  *******************

for i in range(3):
    height = int(input("Enter your height :"))
    for x in range(height, 0, -1):
        print((x * " " + (height - x) * "*") + "*" + ((height - x) * "*") + (x * " "))
