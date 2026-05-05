def isabc(s,t):
    lst1=s.split()
    lst2=t.split()
    size=len(lst2)
    if size>0:
        for i in range (size):
            if lst2[i]  in lst1:
                return True
        return False
    return False
print(isabc("I Love Python","Python Program")
