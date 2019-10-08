import random, datetime

secret = random.randint(1,100)
answer = 0
tries = 0
answerlist = []
allanswers = ''
mycounter = 0

while answer != secret and tries <= 6: 
    answer = input("What is my magic number? ")
    answerlist.append(answer)
    #tries = tries + 1
    tries += 1

    if(answer.isnumeric()):
        answer = int(answer)
    
        if(answer < secret):
            print("Sorry too low")
        elif(answer > secret):
            print("Sorry too high")
        elif(answer == secret):
            print("Well done that's correct!")
            print("You did this in ",tries," tries.",sep='')
    else:
        print("That's not a sensible answer is it? Try again.")

if(answer != secret):
    print("Sorry, you didn't get it within ",tries," tries. :( Try again.",sep='')

print("You answered ",end='')
for oneanswer in answerlist:
    # What's wrong with the IF statements below... ;)
    if(mycounter == 0 and len(answerlist)>1):
        print(oneanswer,end='',sep='')
    elif(mycounter != 0 and len(answerlist)>1):
        print(",",oneanswer,end='',sep='')
    elif(mycounter == len(answerlist)):
        print(" and finally, ",oneanswer,end='',sep='')
    else:
        print(oneanswer,"!! Boom! Got it in one!",end='',sep='')
    mycounter += 1
print("")


