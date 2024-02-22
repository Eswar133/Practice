#Sorting Algorithm:Bubble sort:
#Bubble sort is a type of technique used to swap adjacent items but comparing in the process of comparing the small items"bubbles" are at the top of the list means start of the list that's why it is called bubble sort.


arr =[5,2,3,9,1,2]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
print(arr)