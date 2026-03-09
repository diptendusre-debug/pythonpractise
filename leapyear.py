year=int(input("Enter the year :"))
if year>=0:
    print("The year is valid")
    if year%4==0:
        print(str(year)+"is a leap year")
    else:
        print(str(year)+"is not a leap year")
else:
    print("The year is invalid")