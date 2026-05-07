def islstPalin(lst):
    size=len(lst)
    lst1=[]
    first=size-1
    for i in range(first,-1,-1):
        lst1.append(lst[i])
    print(lst1)
    if lst1==lst:
        return True
    else:
        return False



lst=[7,8,9,8,8,7]
print(islstPalin(lst))
