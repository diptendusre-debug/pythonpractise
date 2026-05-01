arr=[15,10,35,21]
def insertion(arr):
    size=len(arr)
    for i in range (1,size):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j -=1
        arr[j+1]=key
    print(arr)
insertion(arr)
