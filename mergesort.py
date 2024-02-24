def merge_sort(arr):
    if len (arr)<=1:
        return arr 
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    return merge(left_half,right_half)

def merge(left,right):
    result=[]
    leftindex,rightindex=0,0
    while leftindex<len(left) and rightindex < len(rightindex):
        if left[leftindex]<right[rightindex]:
            result.append(left[leftindex])
            leftindex+=1
        else:
            result.append(right[rightindex])
            rightindex+=1
    while leftindex < len(left):
        result.append(left[leftindex])
        leftindex+=1
    while rightindex < len(right):
        result.append(right[rightindex])
        rightindex+=1
        
    return result
# Example usage:
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
             
    