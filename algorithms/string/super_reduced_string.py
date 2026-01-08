"""
Documentation for superReducedString function.

Reduce a string of lowercase characters in range ascii['a'..'z']by doing a series of operations. In each operation, select a pair of adjacent letters that match, and delete them.
Delete as many characters as possible using this method and return the resulting string. If the final string is empty, return Empty String

Example.

s = "aab"
aab shortens to b in one operation: remove the adjacent a characters.
s = "abba"

Remove the two 'b' characters leaving 'aa'. Remove the two 'a' characters to leave ''. Return 'Empty String'.

Function Description
Complete the superReducedString function in the editor below.

superReducedString has the following parameter(s):
string s: a string to reduce

Returns
- string: the reduced string or Empty String

Input Format
A single string, s.

Constraints

- 1 <= number of string characters <= 100

"""

def superReducedString(s: str):
    def adjacent(s: int, right: bool, left: bool, idx: int):
        print(f"Callback {s=}::{right=}::{left=}::{idx=}")
        n = len(s)
        
        if idx >= n:
            return s if s else "Empty String"

        if right and idx + 1 < n and s[idx] == s[idx+1]:
            print(f"Right check: {s=}, idx: {idx}")
            s = s[:idx] + s[idx+2:]
            print(f"Result of right check: {s=}")
            return adjacent(s, False, True, idx)
        elif left and (idx - 1) >= 0  and idx < n and s[idx-1] == s[idx]:
            print(f"Left check: {s=}, idx: {idx}")
            s = s[:idx-1] + s[idx+1:]
            print(f"Result of left check: {s=}")
            return adjacent(s, False, True, idx-1)
        else:
            print("Move to the next idx: ", idx+1)
            return adjacent(s, True, left, idx+1)
    return adjacent(s, True, False, 0)


if __name__ == "__main__":
    s = input("Enter a string to reduce: ").strip()
    result = superReducedString(s)
    print("Reduced string: ", result)
