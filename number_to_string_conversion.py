# It's done by a function named str().

# The function takes one argument (a number or a string) and returns a string presenting the number in a human-readable form.
print("\nInteger to string")
itg = 13
flt = 1.3
si = str(itg)
sf = str(flt)

print(si + ' ' + sf)

# The reverse transformation (string-number) is possible when and only when the string represents a valid number.
# Otherwise, you'll get an error message.( ValueError )

print("\nString to Integer")
si = '13'
sf = '1.3'
itg = int(si)
flt = float(sf)

print(itg + flt)