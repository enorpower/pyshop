import random
print("welcome to pyshop the shop for anything and everything")
iw = input("what would you like to buy")
results = random.randint(1000, 999999999999)
print("i found",results,"results")
def shop ():
   prefix = random.choice(["super","ultimate","ultra","pro","amazing"])
   print(prefix,iw,"is a top result would you like to buy?")
   yn = input("y/n")
   if yn == "y":
      print("thank you for your purchase")
      quit()
   else:
      con = input("would you like to look at other options? y/n")
   if con == "y":
      shop()
shop()
