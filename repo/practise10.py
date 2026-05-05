#is Anagram Check
def is_anargam(s,t):
    lst1=list(s)
    lst2=list(t)
    size1=len(lst1)
    size2=len(lst2)
    while size1 >0 and size2>0:
        if size1!=size2:
            return False
        else: 
            for char in s:
                if char not in t:
                    return False
                else : 
                    count=t.count(char)
                    if count>1:
                        return False
                    else: 
                        return True
    return False

print(is_anargam("",""))

             


