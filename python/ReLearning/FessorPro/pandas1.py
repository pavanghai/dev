import numpy as np
import pandas as pd

a1 = np.arange(25).reshape(5, 5)
print(a1)  # 5x5 array of random numbers

df1 = pd.DataFrame(a1)
print(df1)  # DataFrame from 5x5 array
df1 = pd.DataFrame(a1, columns=['A', 'B', 'C', 'D', 'E'], index=['R1', 'R2', 'R3', 'R4', 'R5'])
print(df1)  # DataFrame with custom columns and index
