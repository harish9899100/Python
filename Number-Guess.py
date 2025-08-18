# import random
# print("Your 'welcome' in number guessing game.")
# low=int(input("Number gessing start from :"))
# high=int(input("Number guessing to :"))
# print(f"you have a 7 chance for guessing number between {low} to {high}")
# num=random.randint(low, high)
# ch=7
# gc=0
# while gc<ch:
#     gc+=1
#     guess=int(input("Enter your aspected number : "))
#     if guess == num:
#         print(f"You guess number {num} in {gc} atemps")
#         break
#     elif gc>=ch and guess!=num:
#         print(f"Sorry number was :{num} but you can't guess \nBest of luck for next time")
#     elif guess > num:
#         print("Your aspectation is very high")
#     elif guess < num:
#         print("Your aspectation is very less")






















print("This is a game and game about number guessing ")
import random
low=int(input("Start number guessing from : "))
high=int(input("To :"))
print(f"You have a 7 chance for guess number between {low} to {high}")
num=random.randint(low, high)
ch=7
gc=0
while ch > gc:
    gc+1
    guess=int(input("Enter your aspected number :"))
    if guess == num:
        print(f"Congratulation your apected number {guess} is correct ")
        break
    elif gc>=ch and guess != num:
        print(f"Sorry number was {num} That you can't guess.\nBest of luch for next ettempt")
    elif guess>num:
        print("Your aspect number is very high")
    elif guess<num:
        print("Your guess number is very less")
