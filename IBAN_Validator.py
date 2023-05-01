# IBAN Validator
# implements (in a slightly simplified form) an algorithm used by European banks to specify account numbers


# Importing the necessary modules
import re

# Defining the function
def IBAN_Validator(iban):
    # Removing all spaces from the IBAN
    iban = iban.replace(' ','')
    # Checking if the IBAN is valid
    if re.match(r'^[A-Z]{2}[0-9]{2}[A-Z0-9]{1,30}$',iban):
        # Rearranging the IBAN
        iban = iban[4:] + iban[:4]
        # Converting the letters into numbers
        iban = ''.join(str(ord(c)-55) if c.isalpha() else c for c in iban)
        # Converting the IBAN into an integer
        iban = int(iban)
        # Checking if the IBAN is valid
        if iban % 97 == 1:
            # Returning the IBAN
            return True
        else:
            # Returning the IBAN
            return False
    else:
        # Returning the IBAN
        return False
    

# Testing the function

# Valid IBANs
print(IBAN_Validator('GB82WEST12345698765432'))

# Invalid IBANs
print(IBAN_Validator('GB82WEST1234569876543'))

print(IBAN_Validator('GB82WEST123456987654322'))

print(IBAN_Validator('GB82WEST1234569876543A'))

print(IBAN_Validator('GB82 WEST 1234 5698 7654 32'))

print(IBAN_Validator('GB82WEST12345698765432 '))
