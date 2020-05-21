usernameinput = input("Username : ")
passwordinput = input("Password : ")
if usernameinput == "admin" and passwordinput == "123":
    print("Success")
    print("---------------Welcome to RoMShop------------")
    print("1. Amethyst        1       21,798    Zeny")
    print("2. Punk Card       1       442,757   Zeny")
    print("3. FireAlloy       1       45,450    Zeny")
    print("4. Memento         1       468       Zeny")
    print("5. Magic Plate     1       28,063    Zeny")
    print("6. Sticky Mucus    1       178       Zeny")
    print("7. Gift Box        1       27,444    Zeny")
    print("8. Deje Card       1       9,675,796 Zeny")
    item = int(input("Choose Your Item (Number) : "))
    amount = int(input("How many Item : "))
    amethyst = 21,789
    pkcard = 442757
    firealloy = 45450
    memento = 468
    magicplate = 28063
    stickymacus = 178
    giftbox = 27444
    dejecard = 9675796
    print("--------------------------------------------")
    if item == 1:
        print("Total Zeny : ", amethyst*amount)
    elif item == 2:
        print("Total Zeny : ", pkcard*amount)
    elif item == 3:
        print("Total Zeny : ", firealloy*amount)
    elif item == 4:
        print("Total Zeny : ", memento * amount)
    elif item == 5:
        print("Total Zeny : ", magicplate*amount)
    elif item == 6:
        print("Total Zeny : ", stickymacus*amount)
    elif item == 7:
        print("Total Zeny : ", giftbox*amount)
    elif item == 8:
        print("Total Zeny : ", dejecard*amount)
else:
    print("Error")