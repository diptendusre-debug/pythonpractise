def bin(digits):
    result = []
    size=len(digits)
    for i in range(size):
        for j in range(i, size):
            result.append(digits[i:j+1])
    size1=len(result)
    newsum=[]
    for subarray in result:
        sum=0

        for num in subarray:
            sum=sum+num
        newsum.append(sum)
    size3=len(newsum)
    for i in range (size3):
        for j in range(i,size3):
            if newsum[i]>newsum[j]:
                newsum[i],newsum[j]=newsum[j],newsum[i]
    return newsum[size3-1]





digits=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(bin(digits))


