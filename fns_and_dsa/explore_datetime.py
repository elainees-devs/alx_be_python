from datetime import datetime, timedelta


def display_current_date_time():
    """ 

    Display the current date and time in the format YYYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    print("Current data and time: ", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """

    Promts the user of a number of days and calculates the future date.
    Displays the future date in  the format YYYY-MM-DD.
    """

    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        future_date = datetime.now() + timedelta(days = days_to_add)
        print("Future date: ", future_date.strftime("%Y-%m-%d"))

    except ValueError:
        print("Invalid input. Please enter an integer value. ")


