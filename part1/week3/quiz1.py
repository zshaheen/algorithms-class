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
'''
arr = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]
merge_two_sub_arrays(arr, 5)
print arr
arr1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
merge_two_sub_arrays(arr1, 5)
print arr1
arr2 = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
merge_two_sub_arrays(arr2, 5)
print arr2
'''
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

######################################################
def is_sorted(arr, low, high):
    ''' Checks if arr[low:high+1] is sorted. '''
    for i in range(low, high+1):
        if arr[i - 1] > arr[i]:
            return False
    return True

def merge(arr, aux, low, mid, high):
    ''' arr is the array with two sorted sub arrays, we don't 
    use two separate arrays. Indices are inclusive, so arrays 
    are arr[low:mid+1] and arr[mid+2:high+1]. aux is an 
    auxillary array. '''
    
    if not is_sorted(arr, low, mid) or not is_sorted(arr, mid, high):
        print is_sorted(arr, low, mid)
        print arr[low:mid]

        print is_sorted(arr, mid, high)
        print arr[mid:high]
        raise Exception('Both sub arrays need to be sorted')
    
    inv_count = 0

    # copy arr into aux
    aux[low:high+1] = arr[low:high+1]

    curr_arr1_indx = low    
    curr_arr2_indx = mid+1    
    for i in range(low, high+1):
        # done with arr1, so add in from arr2
        if curr_arr1_indx > mid:
            arr[i] = aux[curr_arr2_indx]
            curr_arr2_indx += 1
        # done with arr2, so add in from arr1
        elif curr_arr2_indx > high:
            arr[i] = aux[curr_arr1_indx]
            curr_arr1_indx += 1
        # next two cases are called the most often
        elif aux[curr_arr2_indx] < aux[curr_arr1_indx]:
            arr[i] = aux[curr_arr2_indx]
            curr_arr2_indx += 1
            # aux[curr_arr2_indx] is smaller than every elt in aux[curr_arr1_indx:mid]
            inv_count += (mid - curr_arr1_indx)
        else:
            arr[i] = aux[curr_arr1_indx]
            curr_arr1_indx += 1

    return inv_count

def sort(arr, aux, low, high):
    if high <= low:
        return
    mid = low + (high - low)/2
    inv1 = sort(arr, aux, low, mid)
    inv2 = sort(arr, aux, mid+1, high)
    inv3 = merge(arr, aux, low, mid, high)
    return inv1 + inv2 + inv3

def count_inversions(arr):
    # This uses a modified merge sort, which is a divide and conquer problem
    # Slide 15: https://www.cs.princeton.edu/~wayne/kleinberg-tardos/pdf/05DivideAndConquerI.pdf
    # Divide: split array
    # Conquer: count inversions in each list
    # Combine: count inversions in newly merged list
    # - since each sub array is sorted, for each elt in second array, 
    # - we can use binary search to find all numbers larger in first array, 
    # Add all three inversion counts to the total count
    aux = []
    return sort(arr, aux, 0, len(arr)-1)

''' 3. Shuffling a linked list. Given a singly-linked list 
containing n items, rearrange the items uniformly at random. 
Your algorithm should consume a logarithmic (or constant) amount 
of extra memory and run in time proportional to nlogn in the worst case.
'''

# Hint: design a linear-time subroutine that can take two uniformly shuffled 
# linked lists of sizes n1 and n2 and combined them into a uniformly shuffled 
# linked lists of size n1+n2.
