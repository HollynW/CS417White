# Hollyn White
# CS417: Assignment 2
# Problem 2: 
# Given a month and the day of the week that’s the first of that month entered as arugments on the command
# line, write a program that prints a calendar for the month.

def main():
    month = input("Enter the month: ")
    first_day = input("Enter the first day of the month: ")

    if month == "January":
        days_in_month = 31
    elif month == "February":
        days_in_month = 28
    elif month == "March":
        days_in_month = 31
    elif month == "April":
        days_in_month = 30
    elif month == "May":
        days_in_month = 31
    elif month == "June":
        days_in_month = 30
    elif month == "July":
        days_in_month = 31
    elif month == "August":
        days_in_month = 31
    elif month == "September":
        days_in_month = 30
    elif month == "October":
        days_in_month = 31
    elif month == "November":
        days_in_month = 30
    else:
        days_in_month = 31

    if first_day == "Sunday":
        first_day = 0
    elif first_day == "Monday":
        first_day = 1
    elif first_day == "Tuesday":
        first_day = 2
    elif first_day == "Wednesday":
        first_day = 3
    elif first_day == "Thursday":
        first_day = 4
    elif first_day == "Friday":
        first_day = 5
    else:
        first_day = 6

    print(month)
    print("Su Mo Tu We Th Fr Sa")
    
    i = 0 
    while i < first_day: 
        print("   ", end="") 
        i = i + 1
  
    day = 1
    while day <= days_in_month:
        print(day, end=" ")
        if (day + first_day) % 7 == 0:
            print()
        day = day + 1

if __name__ == "__main__":
    main()
