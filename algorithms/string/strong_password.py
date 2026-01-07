"""
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

Its length is at least .
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character. The special characters are: !@#$%^&*()-+
She typed a random string of length  in the password field but wasn't sure if it was strong. Given the string she typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
Example

password = "2bbbb"
This password is 5 characters long and is missing an uppercase and a special character. The minimum number of characters to add is .

password = "2bb#A"
This password is 5 characters long and has at least one of each character type. The minimum number of characters to add is .

Function Description

Complete the minimumNumber function in the editor below.

minimumNumber has the following parameters:

int n: the length of the password
string password: the password to test
Returns

int: the minimum number of characters to add
Input Format

The first line contains an integer , the length of the password.
The second line contains the password string. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

Constraints
- 1 <= n <= 100
- All characters in  are in [a-z], [A-Z], [0-9], or [!@#$%^&*()-+ ].
"""

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    n_password_requirements = 4
    
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    n_chars = 6
    
    # I could have used regex to check for the presence of each character type
    # but this is more readable
    password_requirement = {numbers, lower_case, upper_case, special_characters}
       
    temp = password_requirement.copy()
    for c in password:
        if n_password_requirements == 0:
            break # All requirement have been met
   
        for requirement in password_requirement:
            if requirement not in temp:
                continue
            if c in requirement:
                n_password_requirements -= 1
                temp.remove(requirement)
                break # Because requirements are unique and are independent
    
    if (n_chars - n) > n_password_requirements:
        return n_chars - n
    return n_password_requirements


if __name__ == "__main__":
    n = int(input("Enter the number of password characters: ").strip())
    password = input("Enter your password: ").strip()

    if n != len(password):
        print("Password length does not match the number of characters entered.")
    else:
        answer = minimumNumber(n, password)
    print(answer)
