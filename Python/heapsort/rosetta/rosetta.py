import random

def heapsort(lst):
    ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''

    # in pseudo-code, heapify only called once, so inline it here
    for start in range((len(lst)-2)//2, -1, -1):
        siftdown(lst, start, len(lst)-1)

    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        siftdown(lst, 0, end - 1)
    return lst

def siftdown(lst, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end: break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break

# Generate a list of 1000 random integers between 1 and 1000
lst = [random.randint(1, 1000) for _ in range(1000)]

# Sort the list using heapsort
heapsort(lst)

# The sorted list is now in 'lst', no print statements included
