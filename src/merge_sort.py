def merge_sort(arr):
    if len(arr) > 1:
        x = len(arr)//2
        first = merge_sort(arr[:x])
        second = merge_sort(arr[x:])
        merge_list(first, second, arr)
    return arr

def merge_list(first, second, orig):
    total_element = len(orig)
    i, j, k = 0, 0, 0
    while k < len(orig):
        if i < len(first) and j < len(second):
            if(first[i] >= second[j]):
                orig[k] = second[j]
                j+=1
            else:
                orig[k] = first[i]
                i+=1    
        if (j <len(second)):
            orig[k] = second[j]
            j+=1
        elif i < len(first):
            orig[k] = first[i]
            i+=1
        k+=1