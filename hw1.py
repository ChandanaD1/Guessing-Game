#number guessing game
import random

number = random.randint(1,50)
count = 0
print(number)

while count < 3:
    count += 1
    guess = int(input("Guess an integer number between 1 and 50: "))
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('Congratulations, you guessed the number!')
else:
    print('You did not guess the number, the number was ' + str(number))
