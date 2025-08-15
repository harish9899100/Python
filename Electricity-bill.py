unit=int(input("Enter your electricity bill :"))
min=100
bill=0
if unit <= 50:
    bill=min
elif unit>50 and unit<=100:
    bill=min+(unit-50)*2.0
elif unit>100 and unit<=200:
    bill=min+50*2+(unit-100)*3.0
elif unit>200 and unit<=300:
    bill=min+50*2+100*3+(unit-200)*3.5
else:
    bill=min+50*2+100*3+100*3.5+(unit-300)*5
print("Your total unit is :",unit,"And your total electricity bill is :",bill)