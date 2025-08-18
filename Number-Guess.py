import random
print("Your 'welcome' in number guessing game.")
low=int(input("Number gessing start from :"))
high=int(input("Number guessing to :"))
print(f"you have a 7 chance for guessing number between {low} to {high}")
num=random.randint(low, high)
ch=7
gc=0
while gc<ch:
    gc+=1
    guess=int(input("Enter your aspected number : "))
    if guess == num:
        print(f"You guess number {num} in {gc} atemps")
        break
    elif gc>=ch and guess!=num:
        print(f"Sorry number was :{num} but you can't guess \nBest of luck for next time")
    elif guess > num:
        print("Your aspectation is very high")
    elif guess < num:
        print("Your aspectation is very less")
