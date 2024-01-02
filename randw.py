
#program that generates random 4 digits number of 0's and 1's
#and convert the generated number to base 10


import random as R

#to generate random binary digits
def generate_random_binary():
    binary_digits = [str(R.randint(0, 1)) for _ in range(4)]
    binary_number = ''.join(binary_digits)
    return binary_number

def binary_to_decimal(binary_number):
    decimal_number = int(binary_number, 2)
    return decimal_number

# random binary number
ran_bin = generate_random_binary()

# Convert the binary number to decimal
decimal = binary_to_decimal(ran_bin)

# binary and its decimal equivalent
print("Generated Binary Number:", ran_bin)
print("Decimal Equivalent:", decimal)
