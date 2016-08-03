import random

print("Welcome to the choosemybeer interactive algorithm which will help you (randomly) pick a beer from the long list of products available on tap.")
print("")

name = input("What's your name? ")
numberofbeersontap = int(input("How many beers are on tap? "))

beernumber = random.randint(1,numberofbeersontap)

print("")
print(name + ", you'll drink beer #{}".format(beernumber) + ". I hope you'll like it. Cheers!")
print("")
