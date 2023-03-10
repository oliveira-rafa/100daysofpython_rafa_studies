# 🚨 Don't change the code below 👇
from os import major


student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
major_grad = 0

for score in student_scores:
    if score > major_grad:
        major_grad = score
    else:
        pass
print(f'The highest score in the class is: {major_grad}')