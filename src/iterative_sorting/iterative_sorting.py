# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements 
    for cur_index in range(0, len(arr) - 1):
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here

        # loop through all the items
        # range(smallest_index, len(arr)) makes it so we start at a step ahead everytime we iterate through the first loop 
        for item in range(smallest_index, len(arr)):
            # check if the current item is smaller than the current index,
            if arr[item] < arr[smallest_index]:
                # assign that number here
                smallest_index = item
        # TO-DO: swap
        # Your code here

        # at the end of the second loop, swap the curr_index with the final smallest_index number
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here

    # # looping through arr in index form
    # for cur_index in range(len(arr) - 1):
    #     # save the latest index to start from there in second loop
    #     # smallest_index = cur_index
    #     #loop through the item again starting from smallest_index
    #     for item in range(0, len(arr)-cur_index-1):
    #         # compare if first item is bigger than it's neighbor,
    #         if arr[item] > arr[item + 1]:
    #             # if it is smaller, then swap them with each other.
    #             # smallest_index = item
    #             arr[item], arr[item + 1] = arr[item], arr[item + 1]

    for cur_index in range(len(arr) - 1):

        for item in range(len(arr) - cur_index - 1):
            if arr[item] > arr[item + 1]:
                arr[item], arr[item + 1] = arr[item + 1], arr[item]


    # for i in range(len(arr) - 1):
        
    #     for j in range(len(arr)-i-1):
    #         print(j)

    return arr



'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
