import os
import random, time

def bubbleSort(myList): # Bubble Sort Algorithm
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

def quick_sort():
    return


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

def menu():
    while True:
        try:
            print("Welcome to the test suite of selected sorting algorithms!")
            print("Please select the sorting algorithm you want to test:\n\t1. Bubble Sort\n\t2. Merge Sort\n\t3. Quick Sort\n\t4. Radix Sort\n\t5. Quit")
            print(">> ", end="")
            user_type = int(input())
            if user_type in [1, 2, 3, 4, 5]:
                if user_type == 5:
                    print("Goodbye!")
                    break
                elif user_type == 1:
                    while True:
                        try:
                            print("Case Scenarios for Bubble Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            print(">> ", end="")
                            user_choice = int(input())
                            if user_choice in [1, 2, 3, 4]:
                                if user_choice == 1:
                                    print("Enter the message you would like to send:")
                                    print(">> ", end="")
                                    message = input()
                                elif user_choice == 2:
                                    return
                                elif user_choice == 3:
                                    break
                            else:
                                print("Invalid selection. Please enter a number between 1 and 3.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                elif user_type == 2:
                    while True:
                        try:
                            print("Case Scenarios for Merge Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            print(">> ", end="")
                            user_choice = int(input())
                            if user_choice in [1, 2, 3, 4]:
                                if user_choice == 1:
                                    return
                                elif user_choice == 2:
                                    print("Enter a message:")
                                    print(">> ", end="")
                                    message = input()

                                    pass
                                elif user_choice == 3:
                                    # Method call to show keys

                                    pass
                                elif user_choice == 4:
                                    break
                            else:
                                print("Invalid selection. Please enter a number between 1 and 5.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                elif user_type == 3:
                    while True:
                        try:
                            print("Case Scenarios for Quick Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            print(">> ", end="")
                            user_choice = int(input())
                            if user_choice in [1, 2, 3, 4]:
                                if user_choice == 1:
                                    return
                                elif user_choice == 2:
                                    print("Enter a message:")
                                    print(">> ", end="")
                                    message = input()
                                    pass
                                elif user_choice == 3:
                                    # Method call to show keys
                                    pass
                                elif user_choice == 4:
                                    break
                            else:
                                print("Invalid selection. Please enter a number between 1 and 5.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
                elif user_type == 4:
                    while True:
                        try:
                            print("Case Scenarios for Radix Sort")
                            print("\t1. Best Case\n\t2. Average Case\n\t3. Worst Case\n\t4. Back")
                            print(">> ", end="")
                            user_choice = int(input())
                            if user_choice in [1, 2, 3, 4]:
                                if user_choice == 1:
                                    return
                                elif user_choice == 2:
                                    print("Enter a message:")
                                    print(">> ", end="")
                                    message = input()
                                    pass
                                elif user_choice == 3:
                                    # Method call to show keys

                                    pass
                                elif user_choice == 4:
                                    break
                            else:
                                print("Invalid selection. Please enter a number between 1 and 5.")
                        except ValueError:
                            print("Invalid input. Please enter a valid number.")
            else:
                print("Invalid selection. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    menu()