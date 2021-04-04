from random import randint


while True:
    number = randint(1,6)
    score = 0


    print("Roll = " + str(number))
    print("Your score so far is: ", score)
    print("What's it to be? Higher or Lower?")
    user = input("Higher (H) or Lower (L) > ")
    print("**********************************************")



