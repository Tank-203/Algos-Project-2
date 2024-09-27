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

def radix_sort():
    return

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
                                #eofse
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
                                #Blah
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
                                #Blah
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
                                #Blah
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