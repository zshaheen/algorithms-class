'''
1. 3-SUM in quadratic time. Design an algorithm for the 3-SUM problem that
takes time proportional to n2 in the worst case. You may assume that you can
sort the n integers in time proportional to n2 or better.
'''

def binary_search(arr, query):
    # log n worst case
    if len(arr) <= 1:
        return arr
    l_index = 0
    h_index = len(arr) - 1

    while(l_index < h_index):
        m_index = l_index + (h_index - l_index)/2
        if query > arr[m_index]:
            l_index = m_index + 1
        elif query < arr[m_index]:
            h_index = m_index - 1
        else:
            return m_index

    return -1

def three_sum(arr):
    arr.sort()  # takes at worst N^2, but probably N lg N
    # for each pair of arr[i] and arr[j], binary search for -(arr[i] + arr[j]),
    # because arr[i] + arr[j] -(arr[i] + arr[j]) = 0
    for arr_i in arr:
        for arr_j in arr:
            result = binary_search(arr, -(arr_i + arr_j))
            if result != -1:
                return arr_i, arr_j, arr[result]
    return 'no 3 sum in array.'


#arr = [-1, 2, -1, 3, 4, 5, 6, -12, -3, -6, 2, 7]
#print three_sum(arr)


'''
2. Search in a bitonic array. An array is bitonic if it is comprised of an
increasing sequence of integers followed immediately by a decreasing sequence
of integers. Write a program that, given a bitonic array of n distinct integer
values, determines whether a given integer is in the array.
- Standard version: Use ~3lgn compares in the worst case.
- Signing bonus: Use ~2lgn compares in the worst case (and prove that no
algorithm can guarantee to perform fewer than ~2lgn compares in the worst case).
'''

def find_bitonic_index(arr):
    # O(N)
    if len(arr) == 0:
        return -1
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            return i
    return len(arr) - 1

def binary_search_reversed(arr, query):
    l_index = len(arr) - 1
    h_index = 0
    #h-----l
    while(l_index > h_index):
        #m_index = l_index + (h_index - l_index)/2
        m_index = h_index + (l_index - h_index)/2
        if query > arr[m_index]:
            l_index = m_index# - 1
        elif query < arr[m_index]:
            h_index = m_index# + 1
        else:
            return m_index
    return -1

def biotonic_search(arr, query):
    biotonic_index = find_bitonic_index(arr)
    result = binary_search(arr[0:biotonic_index+1], query)
    if result == -1:
        result = binary_search_reversed(arr[biotonic_index+1:], query)
    return result

arr = [0,2,4,8,10,9,7,5,3,1]
print biotonic_search(arr, 3)

'''
3. Egg drop. Suppose that you have an n-story building (with floors 1 through n)
 and plenty of eggs. An egg breaks if it is dropped from floor T or higher and
 does not break otherwise. Your goal is to devise a strategy to determine the
 value of T given the following limitations on the number of eggs and tosses:

Version 0: 1 egg, ≤T tosses.
Version 1: ∼1lgn eggs and ∼1lgn tosses.
Version 2: ∼lgT eggs and ∼2lgT tosses.
Version 3: 2 eggs and ∼2n‾‾√ tosses.
Version 4: 2 eggs and ≤cT‾‾√ tosses for some fixed constant c.
'''
