import random
import sys
import timeit
import datetime

sys.setrecursionlimit(10**6)  # Increase recursion limit for larger datasets

def bubble_sort(myList):  # Bubble Sort Algorithm
    # Traverse the entire list and compare adjacent elements
    for i in range(len(myList) - 1):
        for j in range(len(myList) - i - 1):
            # Swap if the current element is greater than the next element
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList

def merge_sort(m):  # Merge Sort Algorithm (recursive)
    if len(m) <= 1:
        return m  # Base case: single element or empty list is already sorted

    middle = len(m) // 2  # Find the middle index
    left = m[:middle]  # Split the list into left half
    right = m[middle:]  # Split the list into right half

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))  # Merge both halves and return the sorted list

def merge(left, right):  # Merge function for merge sort
    result = []  # This will store the sorted elements
    left_idx, right_idx = 0, 0

    # Compare elements from both lists and merge them into 'result'
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # Append remaining elements from the left and right halves
    if left_idx < len(left):
        result.extend(left[left_idx:])
    if right_idx < len(right):
        result.extend(right[right_idx:])
    return result

def partition(arr, begin, end):  # Partition function for Quick Sort
    pivot_idx = begin  # Choose the first element as pivot
    for i in range(begin + 1, end + 1):
        if arr[i] <= arr[begin]:  # If element is smaller than pivot, move it to the left
            pivot_idx += 1
            arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
    arr[pivot_idx], arr[begin] = arr[begin], arr[pivot_idx]  # Swap pivot to correct position
    return pivot_idx  # Return the index of the pivot

def quick_sort_recursion(array, begin, end):  # Recursive Quick Sort
    if begin >= end:
        return  # Base case: if the subarray is of size 1 or 0, it's already sorted

    pivot_idx = partition(array, begin, end)  # Partition the array around a pivot
    quick_sort_recursion(array, begin, pivot_idx - 1)  # Recursively sort left side of pivot
    quick_sort_recursion(array, pivot_idx + 1, end)  # Recursively sort right side of pivot

def quick_sort(array, begin=0, end=None):  # Quick Sort Wrapper
    if end is None:
        end = len(array) - 1  # Set end to the last index if not provided

    return quick_sort_recursion(array, begin, end)

def countingSort(arr, exp1):  # Counting Sort for Radix Sort (based on digit place 'exp1')
    n = len(arr)
    output = [0] * n  # Output array to store sorted numbers
    count = [0] * 10  # Count array to store count of each digit (0-9)

    # Store count of occurrences of digits
    for i in range(n):
        index = (arr[i] // exp1)
        count[int((index) % 10)] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now contains sorted numbers
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):  # Radix Sort Algorithm
    max1 = max(arr)  # Find the maximum number to know the number of digits
    exp = 1
    # Do counting sort for every digit place (1s, 10s, 100s, etc.)
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10

def generate_test_data(size, case):  # Generates test data for sorting algorithms
    if case == 'sorted':  # Best case: sorted list
        return list(range(size))
    elif case == 'reverse':  # Worst case: reverse sorted list
        return list(range(size, 0, -1))
    else:  # Average case: random list
        return random.sample(range(size), size)

def time_sorting_algorithm(algorithm, arr, case, size):  # Times the sorting algorithms
    arr_copy = arr.copy()  # Create a copy to keep the original array intact
    start_time = timeit.default_timer()  # Start the timer

    # Choose the appropriate sorting algorithm based on the user's choice
    if algorithm == 'bubble_sort':
        sort_func = lambda: bubble_sort(arr)
    elif algorithm == 'merge_sort':
        sort_func = lambda: merge_sort(arr)
    elif algorithm == 'quick_sort':
        sort_func = lambda: quick_sort(arr)
    elif algorithm == 'radix_sort':
        sort_func = lambda: radix_sort(arr)
    else:
        raise ValueError("Invalid algorithm")

    time_taken = timeit.timeit(sort_func, number=1)  # Time the sorting function

    # Record the current timestamp for saving the results
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    end_time = timeit.default_timer()  # Stop the timer

    # Save the results to a text file
    file_name = f"files/{current_time}.txt"
    with open(file_name, 'a') as file:
        file.write(f"Algorithm: {algorithm}\n")
        file.write(f"Case: {case}\n")
        file.write(f"Size: {size}\n")
        file.write(f"Time taken: {end_time - start_time} seconds\n")
        if size <= 100:  # For small arrays, log the before and after arrays
            file.write(f"Array before sorting: {arr_copy}\n")
            file.write(f"Array after sorting: {arr}\n")
        file.write("\n")

    return time_taken

def menu():  # Main menu for selecting sorting algorithm and test cases
    print("Welcome to the test suite of selected sorting algorithms!")
    while True:
        try:
            # Present sorting algorithm choices
            print("Please select the sorting algorithm you want to test:\n\t1. Bubble Sort\n\t2. Merge Sort\n\t3. Quick Sort\n\t4. Radix Sort\n\t5. Quit")
            algorithm_choice = int(input(">> "))  # User inputs their choice
            if algorithm_choice in [1, 2, 3, 4, 5]:
                if algorithm_choice == 5:
                    print("Goodbye!")
                    break  # Exit the program if user selects 'Quit'
                elif algorithm_choice == 1:
                    # Bubble Sort scenario selection loop
                    while True:
                        try:
                            print("Case Scenarios for Bubble Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            case_choice = int(input(">> "))  # Case selection for bubble sort
                            if case_choice in [1, 2, 3, 4]:
                                if case_choice == 4:
                                    break  # Go back to the main menu
                                else:
                                    case = ['sorted', 'average', 'reverse'][case_choice - 1]
                                    for size in [100, 1000, 10000]:  # Test for different sizes
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('bubble_sort', data_set, case, size)
                                        if case == 'sorted':
                                            print(f"In Best Case for N = {size}, it takes '{time_taken}' seconds")
                                        elif case == 'reverse':
                                            print(f"In Worst Case for N = {size}, it takes '{time_taken}' seconds")
                                        else:
                                            print(f"In Average Case for N = {size}, it takes '{time_taken}' seconds")

                                    while True:
                                        # Ask the user if they'd like to input a custom N
                                        print("Would you like to input another N? [Y/N]")
                                        user_input = input(">> ").upper()
                                        if user_input == 'N':
                                            break
                                        elif user_input == 'Y':
                                            print("What is N?")
                                            n = int(input(">> "))
                                            custom_data_set = generate_test_data(n, case)
                                            start_time = timeit.default_timer()
                                            time_taken = time_sorting_algorithm('bubble_sort', custom_data_set, case, n)
                                            end_time = timeit.default_timer()
                                            if case == 'sorted':
                                                print(f"In Best Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            elif case == 'reverse':
                                                print(f"In Worst Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            else:
                                                print(f"In Average Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                        else:
                                            print("Invalid input")
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
                                    case = ['sorted', 'average', 'reverse'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('merge_sort', data_set, case, size)
                                        if case == 'sorted':
                                            print(f"In Best Case for N = {size}, it takes '{time_taken}' seconds")
                                        elif case == 'reverse':
                                            print(f"In Average Case for N = {size}, it takes '{time_taken}' seconds")
                                        else:
                                            print(f"In Worst Case for N = {size}, it takes '{time_taken}' seconds")

                                    while True:
                                        print("Would you like to input another N? [Y/N]")
                                        user_input = input(">> ").upper()
                                        if user_input == 'N':
                                            break
                                        elif user_input == 'Y':
                                            print("What is N?")
                                            n = int(input(">> "))
                                            custom_data_set = generate_test_data(n, case)
                                            start_time = timeit.default_timer()
                                            time_taken = time_sorting_algorithm('merge_sort', custom_data_set, case, n)
                                            end_time = timeit.default_timer()
                                            if case == 'sorted':
                                                print(f"In Best Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            elif case == 'reverse':
                                                print(
                                                    f"In Average Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            else:
                                                print(f"In Worst Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                        else:
                                            print("Invalid input")
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
                                    case = ['sorted', 'average', 'reverse'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('quick_sort', data_set, case, size)
                                        if case == 'sorted':
                                            print(f"In Worst Case for N = {size}, it takes '{time_taken}' seconds")
                                        elif case == 'reverse':
                                            print(f"In Average Case for N = {size}, it takes '{time_taken}' seconds")
                                        else:
                                            print(f"In Best Case for N = {size}, it takes '{time_taken}' seconds")

                                    while True:
                                        print("Would you like to input another N? [Y/N]")
                                        user_input = input(">> ").upper()
                                        if user_input == 'N':
                                            break
                                        elif user_input == 'Y':
                                            print("What is N?")
                                            n = int(input(">> "))
                                            custom_data_set = generate_test_data(n, case)
                                            start_time = timeit.default_timer()
                                            time_taken = time_sorting_algorithm('quick_sort', custom_data_set, case, n)
                                            end_time = timeit.default_timer()
                                            if case == 'sorted':
                                                print(f"In Worst Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            elif case == 'reverse':
                                                print(
                                                    f"In Average Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            else:
                                                print(f"In Best Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                        else:
                                            print("Invalid input")
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
                                    case = ['sorted', 'average', 'reverse'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('radix_sort', data_set, case, size)
                                        if case == 'sorted':
                                            print(f"In Best Case for N = {size}, it takes '{time_taken}' seconds")
                                        elif case == 'reverse':
                                            print(f"In Average Case for N = {size}, it takes '{time_taken}' seconds")
                                        else:
                                            print(f"In Worst Case for N = {size}, it takes '{time_taken}' seconds")

                                    while True:
                                        print("Would you like to input another N? [Y/N]")
                                        user_input = input(">> ").upper()
                                        if user_input == 'N':
                                            break
                                        elif user_input == 'Y':
                                            print("What is N?")
                                            n = int(input(">> "))
                                            custom_data_set = generate_test_data(n, case)
                                            start_time = timeit.default_timer()
                                            time_taken = time_sorting_algorithm('radix_sort', custom_data_set, case, n)
                                            end_time = timeit.default_timer()
                                            if case == 'sorted':
                                                print(f"In Best Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            elif case == 'reverse':
                                                print(
                                                    f"In Average Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                            else:
                                                print(f"In Worst Case for N = {size}, it takes '{end_time - start_time}' seconds")
                                        else:
                                            print("Invalid input")
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