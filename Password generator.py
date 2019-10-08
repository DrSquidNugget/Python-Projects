import random
print("Welcome to the Password Generator!")

def passwordgenerator():
    mypw = ""
    count = 0
    alphabet_number =    "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    symbols = "!#$"
    running1 = True
    while running1:

        if len(symbols) == 1:

            #  Reset symbols
            symbols = "!#$"

        if len(alphabet_number) == 1:

            #  Reset letters/numbers
            alphabet_number = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        elif count == pw_length:

            if mypw.isupper() or mypw.islower():  # check if there is only upper     or only lower letter and rerun if True
                passwordgenerator()

            else:
                x = mypw
                y = list(x)  # creates a list and put the pw in to shuffle it
                random.shuffle(y)
                mypw = "".join(y)

                print(mypw)
                #input("\nPress <Enter> to close the program")
                running1 = False

        elif count % 4 == 0:

            #  pick a random symbol every 3 loop and add it to the pw
            symbols_index = random.randrange(len(symbols))
            new_symbols = symbols[symbols_index]
            mypw = mypw + new_symbols

            # delete the symbols that is picked so there are no duplicate
            symbols_list_change = symbols.replace(new_symbols, "")
            symbols = symbols_list_change

        else:

            # pick a random number or letter and add it to the pw
            next_index = random.randrange(len(alphabet_number))
            new_alphabetnumber = alphabet_number[next_index]
            mypw = mypw + new_alphabetnumber

            # delete the symbols that is picked so there are no duplicate
            an_list_change = alphabet_number.replace(new_alphabetnumber, "")
            alphabet_number = an_list_change

        count += 1


if __name__ == '__main__':
    print("12 Characters is a recomended minimum for good security")

    print("=" * 55)  # just to make it pretty

    running = True
    while running:
        pw_length = input("How many Characters do you want?\n")
        num_ofpasswords = input("How many passwords do you want?\n")

        if pw_length.isdigit():  # verify if user input a number
            pw_length = int(pw_length)
            num_ofpasswords = int(num_ofpasswords)
            counter = 0
            for counter in range(1,num_ofpasswords+1):
                print("Password number ",counter," is: ",end='')
                passwordgenerator()
                print("")
            
            running = False
        else:
            print("A number is needed")