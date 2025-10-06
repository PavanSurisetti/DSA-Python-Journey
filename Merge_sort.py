# Merge Sort in Python
# Take input from the user and convert it into a list of integers
ar = list(map(int, input('Enter the numbers into the list: ').split()))

# Function to divide the list and sort it recursively
def dividing(ar):
    if len(ar) <= 1:   # Base case: a list with 0 or 1 element is already sorted
        return ar
    # Find the middle index to split the list
    mid = len(ar) // 2
    # Recursively divide and sort the left half
    l = dividing(ar[:mid])
    # Recursively divide and sort the right half
    r = dividing(ar[mid:])
    # Merge the two sorted halves and return the result
    return merge(l, r)
# Function to merge two sorted lists into one sorted list
def merge(l, r):
    res = []   # Resultant list to store merged elements
    i = j = 0  # Pointers for left and right lists
    # Compare elements from left and right lists and add the smaller one
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    # If any elements are left in left or right list, add them
    res.extend(l[i:])
    res.extend(r[j:])
    return res  # Return the merged sorted list
# Print the original list
print(f'Before Sorting: {ar}')
# Print the sorted list after applying merge sort
print(f'After Sorting: {dividing(ar)}')
