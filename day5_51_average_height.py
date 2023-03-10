# 🚨 Don't change the code below 👇
from sys import api_version


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total = 0
for height in student_heights:
    total = height + total

average = round(total/len(student_heights))

print(average)