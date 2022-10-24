#Write your code below this line 👇
# Define a function called paint_calc() so that the code below works.   

from math import ceil
def paint_calc(height, width, cover):
    print(ceil((height * width) / cover))
    return ceil((height * width) / cover)

#Write your code above this line 👆

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_required = paint_calc(height=test_h, width=test_w, cover=coverage)
print(f"you'll need {paint_required} cans of paint.")