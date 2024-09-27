#from https://rosettacode.org/wiki/Sorting_algorithms/Merge_sort
#with minor modifications

import random, time

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

def main(k = 100):
    m = []
    for i in range(k):
        m.append(random.randint(1, 2*k))
    t0 = time.perf_counter()
    sortedList = merge_sort(m)
    t = time.perf_counter()
    print('Merge sort', k, 'items costs', t-t0, 'seconds.')

if __name__ == '__main__':
    main(100000)
                 
