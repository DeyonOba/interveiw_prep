"""
Problem: Implement a binary search algorithm that returns the index of a target value within a sorted array.
If the target value is not found, return -1.

INPUT: A sorted array of integers and a target integer.
OUTPUT: The index of the target integer in the array, or -1 if not found.

EXAMPLE:
Input: arr = [1, 2, 3, 4, 5], target = 3
Output: 2

EDGE CASES:
- Empty array
- Target value not present in the array
- Target value is the first or last element in the array
- Array with duplicate values, where the target value appears multiple times

Input Covering Edge Cases:
1. arr = [], target = 3 -> Output: -1
2. arr = [1, 2, 4, 5], target = 3 -> Output: -1
3. arr = [1, 2, 3, 4, 5], target = 1 -> Output: 0
4. arr = [1, 2, 3, 4, 5], target = 5 -> Output: 4
5. arr = [1, 2, 2, 2, 3], target = 2 -> Output: 1 (or 2 or 3)

def binary_search_0(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""

def binary_search_0(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_1(arr: list[int], target: int) -> int:
    left, right = 0, len(arr) - 1

    def lowest_target_idx(left: int, right: int) -> int:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] < target:
                return mid
            return lowest_target_idx(left, mid - 1)
        elif arr[mid] < target:
            return lowest_target_idx(mid + 1, right) 
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return lowest_target_idx(left, mid)
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def generate_test_cases(n: int):
    import random
    test_cases = []
    for _ in range(n):
        size = random.randint(0, 20)
        start, end = 0, 10
        arr = sorted(random.choices(range(start, end+1), k=size))
        target = random.randint(start, end)
        target_index = arr.index(target) if target in arr else -1
        test_cases.append((arr, target, target_index))
    return test_cases

def test_binary_search_0():
    test_cases = [
        ([], 3, -1),
        ([1, 2, 4, 5], 3, -1),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 2, 2, 3], 2, 2),
        ([1, 2, 3, 4, 5], 3, 2),
    ]
    
    for arr, target, expected in test_cases:
        assert binary_search_0(arr, target) == expected

def test_binary_search_1():
    test_cases = generate_test_cases(200)
    
    for arr, target, expected in test_cases:
        assert binary_search_1(arr, target) == expected

if __name__ == "__main__":
    test_binary_search_0()
    test_binary_search_1()
    print("All tests passed.")