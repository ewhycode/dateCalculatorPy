#

import calendar
from datetime import datetime

def calculate_weeks_from_date():
    #get current date
    current_date = datetime.now()
    
    #ask the user to input a date in YYYY-MM-DD format
    user_input = input("Enter the present date (YYYY-MM-DD): ")
    
    # the input date string into a datetime object
    input_date = datetime.strptime(user_input, "%Y-%m-%d")
    
    # calendar week number for the current date
    current_week = current_date.isocalendar()[1]
    
    #calendar week number for the input date
    input_week = input_date.isocalendar()[1]
    
    #compute the difference in weeks between the input date and the current date
    week_difference = abs(current_week - input_week)
    
    # print the result
    print(f"The number of weeks from the given date to the current date is: {week_difference}")

# run the function
calculate_weeks_from_date()
