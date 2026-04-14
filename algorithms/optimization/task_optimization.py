"""
### Task Scheduling: Load Balancing Optimization

The goal is to partition a set of tasks (represented by their completion times) into two groups 
to minimize the total time required for both groups to finish. This is equivalent to 
minimizing the difference between the sum of task times in each group.

#### Problem Description
Given an array of integers representing task durations, distribute the tasks between 
Group A and Group B. Since the groups work in parallel, the total time to finish all tasks 
is determined by the group with the larger workload. By minimizing the difference between 
the two groups, we achieve the most efficient parallel execution.

#### Example
Input: `[100, 3, 5, 6]`

1. **Uneven Distribution**: Focuses only on minimizing the time delta.
   - Group 1: [100], Group 2: [6, 5, 3] -> Delta: |100 - 14| = 86
2. **Even Distribution**: Attempts to balance the workload while keeping the number 
   of tasks per group roughly equal (N/2).

#### Constraints
- Task times are non-negative integers.
- Tasks are independent and cannot be split.
- The input may be an empty list or a non-list type.

#### Returns
- `int`: The absolute difference between the total times of the two groups.
"""



def uneven_task_distribution(array: list) -> int:
    """
    Greedy approximation for the Partition Problem.
    Sorts tasks in descending order and assigns the next largest task to 
    whichever group currently has the smaller total sum.
    """
    if type(array) is not list:
        return 0
    
    if not array:
        return 0
    
    if len(array) == 1:
        return array[0]
    
    array.sort(reverse=True) # Sort array inplace in a descending order

    group_1, group_2 = 0, 0

    for idx, tsk_time in enumerate(array):
        if idx == 0:
            group_1 = tsk_time
        
        elif group_1 > group_2:
            group_2 += tsk_time
        
        else:
            group_1 += tsk_time
    
    return abs(group_1 - group_2)


def even_task_distribution(array: list) -> int:
    """
    Balanced task distribution.
    Similar to the greedy approach, but enforces a constraint that neither 
    group can take more than approximately half of the total number of tasks.
    """
    if type(array) is not list:
        return 0
    
    if not array:
        return 0
    
    if len(array) == 1:
        return array[0]
    
    array.sort(reverse=True)

    mid = len(array) / 2 if len(array) % 2 == 0 else (len(array) + 1) / 2
   
    group_1, group_2 = 0, 0
    group_1_tsk_count, group_2_tsk_count = 0, 0


    for idx, tsk_time in enumerate(array):
        if idx == 0:
            group_1 = tsk_time
            group_1_tsk_count += 1
        
        elif group_1 > group_2 and group_2_tsk_count < mid:
            group_2 += tsk_time
            group_2_tsk_count += 1
        
        else:
            group_1 += tsk_time
            group_1_tsk_count += 1
    
    return abs(group_1 - group_2)


if __name__ == "__main__":
    array = [100, 3, 5, 6]
    print(uneven_task_distribution(array))
    print(even_task_distribution(array))

