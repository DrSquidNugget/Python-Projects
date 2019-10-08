import random

secret = random.randint(1,100)
answer = 0
tries = 0
myguess = 0
answerlist = []

while answer != secret and tries <= 6: 
    answer = input("what is my magic number?")
    #tries = tries + 1
    tries += 1
    answerlist.append(answer)

    if(answer.isnumeric()):
        answer = int(answer)
    
        if(answer < secret):
            print("sorry too low")
        elif(answer > secret):
            print("sorry too high")
        elif(answer == secret):
            print("Well done that's correct!")
            print("You did this in ",tries," tries.",sep='')
            print("You guessed ",end='')
            for myguess in answerlist:
                print(myguess," ",end='')

    else:
        print("That's not a sensible answer is it? Try again.")


