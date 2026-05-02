def max_consecutive_difference(lst):
    size=len(lst)
    maxDifferance=0
    for i in range (size):
        for j in range (i+1,size):
            absdifferance=abs(lst[i]-lst[j])
            if absdifferance>maxDifferance:
                maxDifferance=absdifferance
    return maxDifferance
print(max_consecutive_difference([1, 7, 3, 10, 5]))
