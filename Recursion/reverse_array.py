arr = [1,8,3,5,7,8]


def reverse_array(arr):
    rev_arr = []
    def rev(arr, index):
        if index < 0:
            return
        rev_arr.append(arr[index])
        rev(arr,index-1)
    index = len(arr) - 1
    rev(arr,index)
    return rev_arr

print("Reverse Array: ", reverse_array(arr))    
        
