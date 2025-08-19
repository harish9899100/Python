# for i in range(1,11):
#     if i > 5:
#         break
#     print(i)


num=int(input("Enter a number :"))
flag=0
for i in range(2,num):         # if number is only devide 1 and self otherwise not devide any number that number are called prime number 
    if num%i==0:
     flag=1
    break
if flag==0:
   print(num,"is prime number")
else:
   print(num,"is not prime number")