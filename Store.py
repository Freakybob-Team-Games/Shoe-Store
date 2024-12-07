import time
import random
moneys = 50
def lore():
    print("hello greg")
    time.sleep(1)
    print("you have " + str(moneys) + " moneys currently.. thats an issue")
    time.sleep(1)
    print("you are in a shoe store")
    time.sleep(1)
    print("you can rob the place or just die which one")
lore()
choice = input("which one? ")
if (choice == "rob" or choice == "die"):
    if (choice == "rob"):
        rdn = random.randint(1, 2)
        print(rdn)
        if (rdn == 1):
            print("you got shot")
            raise SystemExit
        else:
            moneys = moneys + 100
            print("you got one hundred moneys!! (" + str(moneys) + ")")
    if (choice == "die"):
        print("you died")
        raise SystemExit
else:
    print("you can only use rob or die")
    raise SystemExit