# In this program we are check year is leap year or not
year = int(input("Enter year : "))
if year%400 == 0 and year%100 == 0:
    print(year, "is centuries leap year")
elif year%4 == 0 and year%100 != 0:
    print(year, "is noncenturies leap year")
else:
    print(year, "is not leap year")