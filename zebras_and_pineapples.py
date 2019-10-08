print("Pineapples and zebras")

pineapples = input("How many pineapples? ")
zebras = input("How many zebras? ")

if(zebras.isnumeric() == False or pineapples.isnumeric() == False):
    print("One of your values is not a number!")
elif(zebras == pineapples):
    print("Same number of zebras as pineapples")
elif(zebras > pineapples):
    print("More zebras than pineapples")
else:
    print("Less zebras than pineapples")
