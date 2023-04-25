# isalnum() method
# The isalnum() method returns True if the string consists only of letters and numbers and it returns False otherwise.



# Demonstrating the isalnum() method:
print('DEMO 1:')
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum()) 

# Demo 2
print('\nDEMO 2: ')
t = 'Six lambdas'
print(t.isalnum()) #the cause of the first result is a space – it's neither a digit nor a letter

t = '&Alpha;&beta;&Gamma;&delta;'
print(t.isalnum())

t = '20E1'
print(t.isalnum())