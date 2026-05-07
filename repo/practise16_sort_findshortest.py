def fle(lst):
    size=len(lst)
    for i in range (size):
        min=i
        for j in range (i+1,size,1):
            if lst[min]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
    return lst[0]





lst=[11, 13, 15, 17] 
print(fle(lst))
