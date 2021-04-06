from random import randint

start =  False
name = input("What is your name? > ")

while start == False:
             print(f"Hello", name, """This is the Higher / Lower game. Choose how much of your bank balance to
bet on your next roll. If you roll under 7 you win your stake back +50%, if you
roll a 7 or over you lose your stake! The dice is numbered 1 - 13""")
             number = randint(1,13)
             bank_bal = "£" + str(100)

             print("Balance: ", bank_bal)
             print("How much do you want to bet?")
             print("DICE: = " + str(number))
             user = input("> £")
             print("**********************************************")
             start = True
             if number < 7:
                 print("You win!")
             bank_bal += str(1)
             print("Balance: ", bank_bal)
            
                    


    




                    
