a = int(input("enter a lucky number"))
match a:
    case 1:
        print("you won a bike")
    case 5:
        print("you won a car")
    case 7:
        print("you won a bus")
    case _:
        print("better luck next time")