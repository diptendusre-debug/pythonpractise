#Binary search to prin the target element

arr=[10,20,30,40,50,60,70,80,90,100]
target=int(input("Enter the Target : "))

def binarySerach(arr,target):
    size=len(arr)
    end=size-1
    start=0 
    while (start<=end):
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        elif arr[mid]<target:
            start=mid+1 
    return -1 
print(binarySerach(arr,target))
