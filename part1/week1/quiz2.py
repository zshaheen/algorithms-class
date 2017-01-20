'''
1. 3-SUM in quadratic time. Design an algorithm for the 3-SUM problem that
takes time proportional to n2 in the worst case. You may assume that you can
sort the n integers in time proportional to n2 or better.
'''

def binary_search(arr, query):
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


arr = [-1, 2, -1, 3, 4, 5, 6, -12, -3, -6, 2, 7]
print three_sum(arr)
