"""This program is an extention to D03c_leapYear.py using functions"""
from sys import exit
def is_leap(year):
    """Returns True if its leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # print("Leap year.")
            else:
                return False  # print("Not leap year.")
        else:
            return True  # print("Leap year.")
    else:
        return False  # print("Not leap year.")


def days_in_month(year, month):
    """Returns day of the month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_valid(year, month):
        pass
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

def is_valid(year, month):
    """Validates if year and month is correct"""
    if len(str(year)) !=4:
        return exit("year should be 4 digit, Terminating Program")
    if month > 12 or month < 1:
        return exit("Month should be between 1 and 12, Terminating Program")
    return True

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)