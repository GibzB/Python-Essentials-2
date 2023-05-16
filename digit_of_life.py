# A digit evaluated using somebody's birthday

# You just need to sum all the digits of the date. 
# If the result contains more than one digit, you have to repeat the addition until you get exactly one digit.

# For example, if somebody was born on the 5th of March 1998, you have to add digits: 5 + 3 + 1 + 9 + 9 + 8 = 35 and then 3 + 5 = 8.

date = input("Enter your birthday date (in the following format: YYYYMMDD or YYYYDDMM, 8 digits): ")
if len(date) != 8 or not date.isdigit():
    print("Invalid date format.")
else:
    while len(date) > 1:
        the_sum = 0
        for dig in date:
            the_sum += int(dig)
        print(date)
        date = str(the_sum)
    print("Your Digit of Life is: " + date)
