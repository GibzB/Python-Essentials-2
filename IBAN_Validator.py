# IBAN Validator
# implements (in a slightly simplified form) an algorithm used by European banks to specify account numbers

# An IBAN-compliant account number consists of:

# A two-letter country code taken from the ISO 3166-1 standard (e.g., FR for France, GB for Great Britain, DE for Germany, and so on)
# two check digits used to perform the validity checks – fast and simple, but not fully reliable, tests, showing whether a number is invalid (distorted by a typo) or seems to be good;
# the actual account number (up to 30 alphanumeric characters – the length of that part depends on the country)

# The standard says that validation requires the following steps:

# (step 1) Check that the total IBAN length is correct as per the country (this program won't do that, but you can modify the code to meet this requirement if you wish; note: you have to teach the code all the lengths used in Europe)
# (step 2) Move the four initial characters to the end of the string (i.e., the country code and the check digits)
# (step 3) Replace each letter in the string with two digits, thereby expanding the string, where A = 10, B = 11 ... Z = 35;
# (step 4) Interpret the string as a decimal integer and compute the remainder of that number by modulo-dividing it by 97; If the remainder is 1, the check digit test is passed and the IBAN might be valid.

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

print(IBAN_Validator('DE02100100100152517108')) # German

print(IBAN_Validator('FR76 30003 03620 00020216907 50')) # French

print(IBAN_Validator('GB72 HBZU 7006 7212 1253 00')) # British


 
