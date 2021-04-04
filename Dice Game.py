from random import randint

number = randint(1,6)
score = 0

while True:
    print("Roll = " + str(number))
    print("Your score so far is: ", score)
    print("What's it to be? Higher or Lower?")
    user = input("Higher (H) or Lower (L) > ")




