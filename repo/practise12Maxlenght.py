def isabc(s):
    lst1=s.split()
    size=len(lst1)
    maxlen=0
    for i in range (size):
        newlst=list(lst1[i])
        size1=len(newlst)
        if maxlen<size1:
            maxlen=size1
    return maxlen
print(isabc("i love dip"))
