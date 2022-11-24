"""
This script splits student.csv file based on nationality 
new file name: nationality_todaysDate
nationality_todaysDate.csv: gender, age, name, city
"""
import pandas as pd
import os
from datetime import date

date_str = date.today().strftime("%m_%d_%Y")
file_path  = "E:\\Pavan\\dev\\python\\ReLearning\\Other\\"
# data = pd.read_csv(r"E:\Pavan\dev\python\ReLearning\Other\removal.csv", delimiter = ",")
data = pd.read_csv(f"{file_path}student.csv", delimiter = ",")
print(data.head())
nationality_list = data['nationality'].drop_duplicates()
# print(nationality_list)

# exit()

for nationality in nationality_list:
    # user_path = os.path.join(file_path, date_str, nationality)
    user_path = os.path.join(file_path, date_str)
    nationality_data = data[data['nationality'] == nationality] 
    # print(nationality_data.head())
    new_nationality_data = nationality_data[['gender','age','name','city']]
    # print(new_nationality_data.head())

    if not os.path.exists(user_path):
        os.makedirs(user_path)
    output_file = os.path.join(user_path, f'nationality_{nationality}.csv')
    # print(output_file)
    new_nationality_data.to_csv(output_file, index=False, header=False)