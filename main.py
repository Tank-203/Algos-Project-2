import random
import sys
import timeit
import datetime

sys.setrecursionlimit(10**6)

def bubble_sort(myList): # Bubble Sort Algorithm
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j+1] = myList[j + 1], myList[j]
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

def countingSort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int((index) % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int((index) % 10)] - 1] = arr[i]
        count[int((index) % 10)] -= 1
        i -= 1
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        countingSort(arr, exp)
        exp *= 10

def generate_test_data(size, case):
    if case == 'best': # Creates a sorted list
        return list(range(size))
    elif case == 'worst':
        return list(range(size, 0, -1)) # Creates a reverse sorted list
    else:
        return random.sample(range(size), size) # Creates a random list

def time_sorting_algorithm(algorithm, arr, case, size):
    arr_copy = arr.copy()
    start_time = timeit.default_timer()
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

    time_taken = timeit.timeit(sort_func, number=1)

    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    end_time = timeit.default_timer()
    file_name = f"files/{current_time}.txt"
    with open(file_name, 'a') as file:
        file.write(f"Algorithm: {algorithm}\n")
        file.write(f"Case: {case}\n")
        file.write(f"Size: {size}\n")
        file.write(f"Time taken: {end_time - start_time} seconds\n")
        if size <= 100:
            file.write(f"Array before sorting: {arr_copy}\n")
            file.write(f"Array after sorting: {arr}\n")
        file.write("\n")

    return time_taken

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
                                        time_taken = time_sorting_algorithm('bubble_sort', data_set, case, size)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")

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
                                            time_taken = time_sorting_algorithm('bubble_sort', custom_data_set, case, n)
                                            end_time = timeit.default_timer()
                                            print(f"In {case.capitalize()} Case for N = {n}, it takes '{end_time - start_time}' seconds")
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
                                    case = ['best', 'average', 'worst'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('merge_sort', data_set, case, size)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")

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
                                            print(
                                                f"In {case.capitalize()} Case for N = {n}, it takes '{end_time - start_time}' seconds")
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
                                    case = ['best', 'average', 'worst'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('quick_sort', data_set, case, size)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")

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
                                            print(
                                                f"In {case.capitalize()} Case for N = {n}, it takes '{end_time - start_time}' seconds")
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
                                    case = ['best', 'average', 'worst'][case_choice - 1]
                                    for size in [100, 1000, 10000]:
                                        data_set = generate_test_data(size, case)
                                        time_taken = time_sorting_algorithm('radix_sort', data_set, case, size)
                                        print(f"In {case.capitalize()} Case for N = {size}, it takes '{time_taken}' seconds")

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
                                            print(f"In {case.capitalize()} Case for N = {n}, it takes '{end_time - start_time}' seconds")
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