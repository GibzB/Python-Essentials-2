# Numbers Processor.
# This program reads a set of numbers from a file and accumulates them



line = input("Enter a line of numbers - separate them with spaces: ") # ask the user to enter a line filled with any number of numbers (the numbers can be floats)
strings = line.split() # split the line receiving a list of substrings;
total = 0 # as the string-float conversion may raise an exception, it's best to continue by using the try-except block;
try: # iterate through the list...
    for substr in strings: # ...and try to convert all its elements into float numbers; if it works, increase the sum;
        total += float(substr) # 
    print("The total is:", total)
except: # the program ends here in the case of an error;
    print(substr, "is not a number.") # print a diagnostic message showing the user the reason for the failure.
    
