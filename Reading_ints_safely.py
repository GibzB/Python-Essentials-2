# A function able to input integer values and to check if they are within a specified range.

def readint(prompt, min, max):
    ok = False
    while not ok:
        try:
            value = int(input(prompt))
            ok = True
            if value < min or value > max:
                print("Error: the value is not within permitted range (min..max)")
                ok = False
        except ValueError:
            print("Error: wrong input")
    return value

v = readint("Enter a number from -10 to 10: ", -10, 10)
print(v)

