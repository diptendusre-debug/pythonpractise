#Linear search to find the target element
arr=[10,20,30,40,50,60,70,80,90,100]
target=int(input("Enter the Target : "))

def linearSearch(arr,target):
    size=len(arr)
    for i in range (size):
        if arr[i]==target:
            return i
    return -1

print(linearSearch(arr,target))
