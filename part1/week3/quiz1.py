'''
1. Merging with smaller auxiliary array. Suppose that the subarray
a[0] to a[n - 1] is sorted and the subarray a[n] to a[2*n-1] is sorted. 
How can you merge the two subarrays so that a[0] to a[2*n-1] is sorted 
using an auxiliary array of length n (instead of 2n)?
'''

def merge_two_sub_arrays(arr, n):
    aux = arr[0:n]
    #arr[:n] = ['x'] * n
    #print aux
    #print arr
    #quit()
    arr1_index = 0
    arr2_index = n
    curr_index = 0

    while curr_index < len(arr):
        # if one array is already done, just put the otherone instead
        if arr1_index >= n: # array 1 (aux) is done, put the other array (arr[n:2n]) in
            arr[curr_index] = arr[arr2_index]
            arr2_index += 1
        elif arr2_index >= 2*n: # array 2 is done, put the other array (aux[0:n]) in
            arr[curr_index] = aux[arr1_index]
            arr1_index += 1
        else: # no premature breaking
            if aux[arr1_index] <= arr[arr2_index]:
                arr[curr_index] = aux[arr1_index]
                arr1_index += 1
            else:
                arr[curr_index] = arr[arr2_index]
                arr2_index += 1
        curr_index += 1

arr = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
merge_two_sub_arrays(arr, 5)
print arr
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
merge_two_sub_arrays(arr1, 5)
print arr1
arr2 = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
merge_two_sub_arrays(arr2, 5)
print arr2

# Don't do these tests, b/c problem states that the arrays are of the same size
#arr1 = [1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 8]
#merge_two_sub_arrays(arr1, 3)
#print arr1
#arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3]
#merge_two_sub_arrays(arr2, 8)
#print arr2

'''
2. Counting inversions. An inversion in an array a[] 
is a pair of entries a[i] and a[j] such that i<j but a[i]>a[j]. 
Given an array, design a linearithmic algorithm to count the number of inversions.
'''
def count_inversions_naive(arr):
    # O(n^2), space complexity is also O(n^2) b/c of arr[index1:]
    num_of_inversions = 0
    for index1, val1 in enumerate(arr):
        for index2, val2 in enumerate(arr[index1:]):
            if index2 > index1:
                num_of_inversions += 1
    return num_of_inversions

def count_inversions(arr):
    


    