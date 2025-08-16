# In This Program we are check how to calculate electricity bill 
unit = int(input("Enter Your Electricity Units : "))
max=100
bill=0
if unit <= 50:
    bill=max
elif unit > 50 and unit <= 100:
    bill=max + (unit-50)*2.0
elif unit > 100 and unit <= 200:
    bill=max + 50*2 + (unit-100)*3.0
elif unit > 200 and unit <= 300:
    bill= max + 50*2 + 100*3 + (unit-200)*3.5
else:
    bill= max + 50*2 + 100*3 + 100*3.5 + (unit-300)*5
print("Your Electricity Units Is : ",unit,"And Your Electcricity Bill Is : Rs.",bill)