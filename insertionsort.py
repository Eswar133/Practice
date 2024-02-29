def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
n=int(input("Enter the no of elements:"))
result=[]
for i in range(n):
    num=int(input(f"enter the  element{i+1}:"))
    result.append(num)
sorted_arr=insertion_sort(result)
print(sorted_arr)
