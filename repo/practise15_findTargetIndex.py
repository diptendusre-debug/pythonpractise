def rotlst(lst,target):
    size=len(lst)
    newlst=[]
    for i in range (size):
        if lst[i]==target:
            newlst.append(i)
        if target not in lst:
            newlst.append(-1)
            newlst.append(-1)
            break
    return newlst




lst=[1,2,3,4,4,5]
target=3
print(rotlst(lst,target))
