import numpy as np
# lst = [1, 2, 3, '5', 'hello']
# arr = np.array(lst)
# r1=np.array([1, 2, 3])

# print(r1, arr, end='\n')
l1=[1, 2, 3]
l2=[4, 5, 6]
np1 = np.array(l1)
np2 = np.array(l2)

print(np1+np2) # array addition
print(l1+l2) # list concatenation
print(np1*np2) # array multiplication
# print(l1*l2) # list multiplication (not element-wise) will raise an error
print(np.arange(2)) # array of 2 elements
print(np.arange(2, 10)) # array of 8 elements starting from 2
print(np.zeros(2)) # array of 5 elements initialized to 0
print(np.zeros((2, 2))) # 2x2 array of zeros
l3=[[1, 2], [3, 4]]
np3=np.array(l3)
print(l3) # 2x2 array
print(np3) # 2x2 array

np4=np.array([[1, 2,3], [4,5, 6], [7, 8, 9]])   
print(np4) # 3x3 array
print(np4.shape) # shape of the array (3, 3)
print("First row:",np4[0]) # first row of the array
print("First row first element:",np4[0][0]) # first element of the first row of the array
print("3R2E:",np4[2, 1]) # second element of the third row of the array
print("1sr2R, 1st2C:",np4[0:2, 0:2]) # first two rows and first two columns of the array
print("2ndR, 2Es:",np4[1:2, :2]) 
print("1ndR, 2Es:",np4[:1, :2]) # first two rows and first two columns of the array

# Generate a 3x3 array of random numbers between 0 and 1
np5 = np.random.randint(100,200,9) # 1D array of random numbers
print(np5) 
np5 = np.random.randint(100,200,9).reshape(3, 3) # convert to 3x3 array from 1D array
print(np5) # 3x3 array of random numbers