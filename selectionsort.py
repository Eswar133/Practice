def selection_sort(arr):
    for i in range (len(arr)):
        minimum=i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[minimum]:
                minimum=j
            arr[i],arr[minimum]=arr[minimum],arr[i]
    return arr

#example
n=int(input("Enter the number of elements:"))
result=[]
for i in range(n):
    num=int(input(f"enter the element{i+1}:"))
    result.append(num)
    
sorted_arr=selection_sort(result)
print(sorted_arr)

    