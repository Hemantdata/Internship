#!/usr/bin/env python
# coding: utf-8

# In[2]:


def factorial(n):
    
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 


num = int(input("Enter A number"))
print("Factorial of",num,"is",factorial(num))


# In[3]:


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    if n <= 3:
        return True   # 2 and 3 are prime numbers
    if n % 2 == 0 or n % 3 == 0:
        return False  # Multiples of 2 or 3 are not prime numbers
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

def check_number_type(n):
    """Determine if a number is prime or composite."""
    if is_prime(n):
        return "Prime"
    else:
        return "Composite"

# Example usage
try:
    number = int(input("Enter a number: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        result = check_number_type(number)
        print(f"The number {number} is {result}.")
except ValueError:
    print("Invalid input. Please enter an integer.")


# In[4]:


def is_palindrome(s):
    """Check if the given string is a palindrome."""
    # Remove any non-alphanumeric characters and convert to lowercase
    clean_s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return clean_s == clean_s[::-1]

# Example usage
def main():
    user_input = input("Enter a string: ")
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

# Run the main function
if __name__ == "__main__":
    main()


# In[7]:


import math

def find_third_side(side1, side2):
    """Determine the third side of a right-angled triangle."""
    # Determine which side is the hypotenuse
    if side1 > side2:
        hypotenuse = side1
        side = side2
    else:
        hypotenuse = side2
        side = side1

    # Calculate the third side
    if hypotenuse == side1 or hypotenuse == side2:
        # Check if one side is the hypotenuse
        third_side = math.sqrt(hypotenuse**2 - side**2)
    else:
        # Calculate the hypotenuse
        third_side = math.sqrt(side1**2 + side2**2)

    return third_side

# Example usage
def main():
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))

    if side1 <= 0 or side2 <= 0:
        print("Both sides must be positive numbers.")
    else:
        third_side = find_third_side(side1, side2)
        print(f"The third side of the right-angled triangle is: {third_side:.2f}")

# Run the main function
if __name__ == "__main__":
    main()


# In[8]:


def character_frequency(s):
    """Print the frequency of each character in the given string."""
    # Create a dictionary to store character frequencies
    frequency = {}

    # Iterate through each character in the string
    for char in s:
        # Update the frequency count for the character
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Print the frequency of each character
    for char, count in frequency.items():
        print(f"'{char}': {count}")

# Example usage
def main():
    user_input = input("Enter a string: ")
    character_frequency(user_input)

# Run the main function
if __name__ == "__main__":
    main()



# In[ ]:




