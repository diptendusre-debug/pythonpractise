arr=[15,13,23,33,45,67]
def search(arr):
    size=len(arr)
    for i in range (0,size-1):
        min=i
        for j in range (i+1,size):
            if arr[min]>arr[j]:
                arr[min],arr[j]=arr[j],arr[min]
    return arr

    print(arr)
def main():
    print(search(arr))
if __name__=="__main__":
    main()
