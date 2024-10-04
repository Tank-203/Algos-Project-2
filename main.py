import os
import random, time
import sys
import timeit

sys.setrecursionlimit(10**6)

def bubble_sort(myList): # Bubble Sort Algorithm
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = \
                           myList[j + 1], myList[j]
    return myList

def merge_sort(m):
    if len(m) <= 1:
        return m

    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def partition(arr, begin, end):
    pivot_idx = begin
    for i in range(begin+1, end+1):
        if arr[i] <= arr[begin]:
            pivot_idx += 1
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
    arr[pivot_idx], arr[begin] = arr[begin], arr[pivot_idx]
    return pivot_idx

def quick_sort_recursion(array, begin, end):
    if begin >= end:
        return

    pivot_idx = partition(array, begin, end)
    quick_sort_recursion(array, begin, pivot_idx-1)
    quick_sort_recursion(array, pivot_idx+1, end)

def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    return quick_sort_recursion(array, begin, end)


# A function to do counting sort of arr[] according to
# the digit represented by exp.
def countingSort(arr, exp1):
    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1

    # Change count[i] so that count[i] now contains actual
    #  position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

        # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that instead
    # of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10

# Generate Test Data
def generate_test_data(size, case):
    if case == 'best':
        return list(range(size))  # Already sorted
    elif case == 'worst':
        return list(range(size, 0, -1))  # Reverse sorted
    else:  # 'average'
        return random.sample(range(size), size)  # Random order

# Time Execution
def time_sorting_algorithm(algorithm, arr):
    if algorithm == 'bubble_sort':
        stmt = lambda: bubble_sort(arr)
    elif algorithm == 'merge_sort':
        stmt = lambda: merge_sort(arr)
    elif algorithm == 'quick_sort':
        stmt = lambda: quick_sort(arr)
    elif algorithm == 'radix_sort':
        stmt = lambda: radix_sort(arr)
    else:
        raise ValueError("Invalid algorithm")
    return timeit.timeit(stmt, number=1)

def menu():
    print("Welcome to the test suite of selected sorting algorithms!")
    while True:
        try:
            print("Please select the sorting algorithm you want to test:\n\t1. Bubble Sort\n\t2. Merge Sort\n\t3. Quick Sort\n\t4. Radix Sort\n\t5. Quit")
            algorithm_choice = int(input(">> "))
            if algorithm_choice in [1, 2, 3, 4, 5]:
                if algorithm_choice == 5:
                    print("Goodbye!")
                    break
                elif algorithm_choice == 1:
                    while True:
                        try:
                            print("Case Scenarios for Bubble Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            case_choice = int(input(">> "))
                            if case_choice in [1, 2, 3, 4]:
                                if case_choice == 4:
                                    break
                                else:
                                    case = ['best', 'average', 'worst'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('bubble_sort', data_set)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")
                            else:
                                print("Invalid selection. Please enter a number between 1 and 4.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                elif algorithm_choice == 2:
                    while True:
                        try:
                            print("Case Scenarios for Merge Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            case_choice = int(input(">> "))
                            if case_choice in [1, 2, 3, 4]:
                                if case_choice == 4:
                                    break
                                else:
                                    case = ['best', 'average', 'worst'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('merge_sort', data_set)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")
                            else:
                                print("Invalid selection. Please enter a number between 1 and 4.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                elif algorithm_choice == 3:
                    while True:
                        try:
                            print("Case Scenarios for Quick Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            case_choice = int(input(">> "))
                            if case_choice in [1, 2, 3, 4]:
                                if case_choice == 4:
                                    break
                                else:
                                    case = ['best', 'average', 'worst'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('quick_sort', data_set)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")
                            else:
                                print("Invalid selection. Please enter a number between 1 and 4.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                elif algorithm_choice == 4:
                    while True:
                        try:
                            print("Case Scenarios for Radix Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            case_choice = int(input(">> "))
                            if case_choice in [1, 2, 3, 4]:
                                if case_choice == 4:
                                    break
                                else:
                                    case = ['best', 'average', 'worst'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('radix_sort', data_set)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")
                            else:
                                print("Invalid selection. Please enter a number between 1 and 4.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
            else:
                print("Invalid selection. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    menu()