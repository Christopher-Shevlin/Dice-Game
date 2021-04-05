from random import randint

start =  False
name = input("What is your name? > ")

while start == False:
             print(f"Hello", name, """This is the Higher / Lower game, simply decide if the next roll will be higher or lower
than the previous. Get it right you get 1 point. Get wrong you lose 2 points! Get to 10 points
to be the winner!""")
             number = randint(1,6)
             score = 0


             print("Roll = " + str(number))
             print("Your score so far is: ", score)
             print("What's it to be? Higher or Lower?")
             user = input("Higher (H) or Lower (L) > ")
             print("**********************************************")
             if user == 'H':
                 start = True
                 if number <7:
                    print("Test")
                    
