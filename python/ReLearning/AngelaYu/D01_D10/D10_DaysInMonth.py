"""This program is an extention to D03c_leapYear.py using functions"""
from sys import exit
def is_leap(year):
    """
    The function to check if leap year

    Parameters:
        year(int): year in four digit
    
    Returns:
        bool: Returns True if its a leap year and False if its not a leap year
    """
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
    """
    days_in_month 

    :param int year: pass argument as four digit number eg 2022
    :param int month: pass argument as number between 1 and 12 eg 5 or 05
    :return bool: _description_
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ''' Can use assert too for validation, 
    it will raise error it condition is not true 
    usage: assert <TrueContition >, <Error message>'''
    # assert len(str(year)) == 4, ("year should be 4 digit, "
    #     "Terminating Program")
    # assert (month < 12 and month > 1), ("Month should be between 1 and 12, "
    #     "Terminating Program")
    if is_valid(year, month):
        pass
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]

def is_valid(year, month):
    """
    Validates if the given year is four digit and month between 1 an 12

    Args:
        year (int): takes year in four digit 
        month (int): takes month between 1 and 12

    Returns:
        bool: Returns True if its valid and False if not valid Argument passed
    """
    if len(str(year)) != 4:
        return exit("year should be 4 digit, Terminating Program")
    if month > 12 or month < 1:
        return exit("Month should be between 1 and 12, Terminating Program")
    return True

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)