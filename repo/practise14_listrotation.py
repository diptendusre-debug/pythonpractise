def rotlst(lst,d):
    size=len(lst)
    newlst=[]
    for i in range (d,size,1):
        newlst.insert(i-d,lst[i])
    for i in range (d):
        newlst.append(lst[i])
    return newlst





lst=[1,2,3,4,5]
d=2
print(rotlst(lst,d))
