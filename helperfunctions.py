from bisect import bisect_left, bisect_right

def bin_search_username(arr, x):
    close = bisect_left(arr, x)  # get the supposed location of x in arr
    if close < len(arr) and arr[close] == x:  # check if it is actually at that location
        return close
    else:
        return -1