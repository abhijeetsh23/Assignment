def insertion_sort(arr):
    i=1;
    while i < len(arr):
        j=i
        temp = arr[i]
        while j > 0:
            if(arr[j-1] > temp): 
                arr[j] = arr[j-1]
                arr[j-1] =temp
            else:
                break
            j=j-1
            
        i=i+1
