# Python program to print all prime number in an interval
 
 
def prime_number(starting_range, ending_range):
    lst = []
    flag = 0  # Declared the flag variable
    # elements range between starting and ending range
    for i in range(starting_range, ending_range):
        for j in range(2, i):
            if(i % j == 0):  # checking if number is divisible or not
                flag = 1  # if number is divisible, then flag variable will become 1
                break
            else:
                flag = 0
        if(flag == 0):  # if flag variable is 0, then element will append in list
            lst.append(i)
    return lst
 
 
# Driver program
starting_range = 1
ending_range = 250
lst = prime_number(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)