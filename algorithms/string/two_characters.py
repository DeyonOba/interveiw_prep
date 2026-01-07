"""
Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.

Example
s="abaacdabd"

Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4. Removing either b or d at any point would not result in a valid string. Return .
Given a string , convert it to the longest possible string  made up only of alternating characters. Return the length of string . If no string  can be formed, return .

Function Description
Complete the alternate function in the editor below.

alternate has the following parameter(s):
string s: a string

Returns.
- int: the length of the longest valid string, or  if there are none

Input Format
The first line contains a single integer that denotes the length of .
The second line contains string .

Constraints
- 1 <= length of s <= 1000
- s[i] ∈ {ascii_lowercase}

Sample Input
```
STDIN       Function
-----       --------
10          length of s = 10
beabeefeab  s = 'beabeefeab'
```
"""

def alternate(s):
    # Write your code here
    count = 0
    unique_chars = list(set(s))
    char_combinations = []
    for i in unique_chars:
        for j in unique_chars:
            if i != j:
                char_combinations.append(f"{i}{j}")
    
    for char_combination in char_combinations:
        temp_count = 0
        last_seen = char_combination[1]
        for c in s:
            if last_seen == c:
                temp_count = 0
                break
            elif c in char_combination:
                temp_count += 1
                last_seen = (
                    char_combination[0] 
                    if last_seen == char_combination[1]
                    else char_combination[1]
                )
        count = temp_count if count < temp_count else count
    return count
    
            
if __name__ == "__main__":
    s = input()
    print("Input string:", s)
    result = alternate(s)
    print("Length of longest valid string:", result)

