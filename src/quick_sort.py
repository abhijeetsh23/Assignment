def quick_sort(arr):
    return quick_sort_internal(arr, 0, len(arr)-1)

def quick_sort_internal(arr, initial, last):
    if last - initial < 1:
        return arr
    pivot_index = find_pivot(arr, initial, last)
    quick_sort_internal(arr, initial, pivot_index-1)
    quick_sort_internal(arr, pivot_index+1,last)
    return arr

def find_pivot(arr, initial_index, last_index):
    pivot_index = initial_index-1
    pivot_value = arr[last_index]
    current_index= initial_index
    while current_index < last_index:
        if(arr[current_index] < pivot_value):  
            pivot_index+=1
            if(current_index - pivot_index) >=1:
                swap(arr, current_index , pivot_index)    
        current_index+=1
    pivot_index+=1
    swap(arr, current_index, pivot_index) 
    return pivot_index
            
def swap(arr, current_index, pivot_index):
    temp = arr[current_index]
    arr[current_index] = arr[pivot_index]
    arr[pivot_index] = temp


arr1 = quick_sort([1,3,2,9,4,5])
print(arr1)