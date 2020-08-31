import random

def getGuess():
    rndm = int(random.random()*1000)
    rndmfirst = random.randrange(1,10)
    rndmsecond = random.randrange(1,10)
    x=rndm - rndmfirst
    y=rndm + rndmsecond
    print("The number is between {} and {} ".format(x,y))
    n=int(input("Your guess: "))
    if(n==rndm):
        print("Congrats, Your guess is correct")
        inp = input("Do you want to try again?? (Y/N)")
        if inp in ["YES","yes", "y","Y","Yes"]:
            getGuess()
        elif inp in ["NO","No", "n","N","no"]:
            exit(0)
    else:
        print("OHHHHH, Your guess is incorrect")
        inp = input("Do you want to try again?? (Y/N)")
        if inp in ["YES","yes", "y","Y","Yes"]:
            getGuess()
        elif inp == "n" or inp == "no":
            exit(0)


if __name__ == "__main__":
    getGuess()
