#Why do you get an error and how would you fix it?

# error in below code
# def foo(a=2, b):
#     return a + b

def foo(a, b=2):
    return a + b

print(foo(3, 4))
