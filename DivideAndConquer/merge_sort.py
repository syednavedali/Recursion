def merge_sort(arr):
    #base case
    if len(arr) <= 1:
      return arr

    #Divide
    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    #Conquer
    #Combining result
    return merge(left, right)

def merge(left, right):
    result = []
    i=j=0

    #Combine: two sorted arrays
    while i<len(left) and j<len(right):
        if(left[i]<right[j]):
         result.append(left[i])
         i += 1
        else:
         result.append(right[j])
         j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [38,27,43,3,9,82,10]
print(merge_sort(arr))