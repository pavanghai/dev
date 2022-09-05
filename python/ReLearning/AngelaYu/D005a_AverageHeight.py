# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# Important You should not use the sum() or len() functions in your answer. 
# print(round(sum(student_heights)/len(student_heights)))
total_height = 0
student_count = 0
for student in student_heights:
    # total_height += student; student_count += 1 # this works too 😊 
    total_height += student
    student_count += 1

# print(f" total_height: {total_height}, students: {student_count}, \nAge height is {round(total_height/student_count)}")
print(round(total_height/student_count))