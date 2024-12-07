import time
import random
def lore():
    print("hello greg")
    time.sleep(2)
    print("you are in a shoe store")
    time.sleep(2)
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
            print("you got one hundred moneys!!")
    if (choice == "die"):
        print("you died")
        raise SystemExit
else:
    print("you can only use rob or die")
    raise SystemExit