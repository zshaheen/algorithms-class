'''
1. Intersection of two sets. Given two arrays a[] and b[], 
each containing n distinct 2D points in the plane, design a 
subquadratic algorithm to count the number of points that are 
contained both in array b[] and array a[].
'''

def common_points(a, b):
    # an algo is subquadratic if it's complexity is greater than O(n) but less than O(n^2)
    # sort both arrays in-place by the first value in the tuple
    # n log n
    # We need to sort by y values, then x values so in the for loop below, we don't skip any values
    # ex: given two arrays and we don't sort by y first
    # a: (1, 2), (1, 0)
    # b: (1, 0), (1, 2)
    # (1, 2) of a and (1, 0) of b don't match, so increment b. Then they match.
    # (1, 0) of a will not find the (1, 0) of b b/c we skipped over it.

    a.sort(key=lambda x: x[1])
    a.sort(key=lambda x: x[0])
    b.sort(key=lambda x: x[1])
    b.sort(key=lambda x: x[0])

    points_in_common = 0
    b_index = 0
    for elt_a in a:
        elt_b = b[b_index]
        if elt_a == elt_b:
            points_in_common += 1
            b_index += 1
        elif elt_a[0] > elt_b[0]:
            continue
        else:  # elt_a[0] <= elt_b[0] and no match
            b_index += 1

    return points_in_common

'''
2. Permutation. Given two integer arrays of size n, 
design a subquadratic algorithm to determine whether one 
is a permutation of the other. That is, do they contain 
exactly the same entries but, possibly, in a different order.
'''
def is_permutation(a, b):
    # n log n sort
    a.sort()
    b.sort()
    # linear search
    for i, _ in enumerate(a):
        if a[i] != b[i]:
            return False
    return True

'''
Similar to problem 75 on leetcode.
3. Dutch national flag. Given an array of n buckets, 
each containing a red, white, or blue pebble,
sort them by color. The allowed operations are:

swap(i,j): swap the pebble in bucket i with the pebble in bucket j.
color(i): color of pebble in bucket i.
The performance requirements are as follows:

At most n calls to color().
At most n calls to swap().
Constant extra space.

'''
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def color(arr, i):
    return arr[i]

def dnf_naive(arr):
    reds, whites, blues = 0, 0, 0
    for i, _ in enumerate(arr):
        if color(arr, i) == 'r':
            reds += 1
        elif color(arr, i) == 'w':
            whites += 1
        elif color(arr, i) == 'b':
            blues += 1
    
    for i, _ in enumerate(arr):
        if reds > 0:
            arr[i] = 'r'
            reds -= 1
        elif whites > 0:
            arr[i] = 'w'
            whites -= 1
        elif blues > 0:
            arr[i] = 'b'
            blues -= 1

def dnf(arr):
    '''
    Can't use b/c we can't assume that there are equal amounts in the array

    red_index = 0
    white_index = len(arr)/3
    blue_index = len(arr)*(2/3)
    '''
    r_index = 0
    w_index = 0
    b_index = len(arr)-1

    # move all of the red and blue elements in place. white will implicitly remain in place
    while w_index <= b_index:
        # put current elt in red, and increment r_index
        if color(arr, w_index) == 'r':  # arr[w_index] == 'r'
            swap(arr, r_index, w_index)
            r_index += 1
            w_index += 1
        # put current elt in blue, and decrement b_index
        elif color(arr, w_index) == 'b': # arr[w_index] == 'b'
            swap(arr, w_index, b_index)
            b_index -= 1
        # if white, don't move element
        else:
            w_index += 1


