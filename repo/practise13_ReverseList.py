def revlst(lst):
    size=len(lst)
    start=size-1
    newlst=[]
    for i in range (start,-1,-1):
        newlst.append(lst[i])
    return newlst




lst=[1,2,3,4,5]
print(revlst(lst))
