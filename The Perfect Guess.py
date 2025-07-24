import random
n = random.randint(1, 100)
a = -1
guesses = 0
while (a != n):
    guesses += 1
    a = int(input("Guess the number: "))
    if(a > n):
        print("Lowest Number Please!")
    elif(a==n):
        print("You got the Number. Congratulations!")
    else:
        print("Higgest Number Please!")

print(f"You have gussed the number {n} correctly in {guesses} attempts")