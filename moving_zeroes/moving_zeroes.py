'''
Input: a List of integers
Returns: a List of integers
'''


# Probably linear?
def moving_zeroes(arr):
    # Your code here
    store = []
    zero_arr = []
    # Append everything but the zeros first
    for i in arr:
        if i > 0:
            store.append(i)
        elif i < 0:
            store.append(i)
        else:
            # Finally append the zeros to the zero_arr
            zero_arr.append(i)
    # Add zero array to the end of store list
    store.extend(zero_arr)
    return store


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
