age = int(input("Enter your age: "))

print("Welcome to the grand line!")

if age >= 18:
    print("you're a pirate")
    gold = int(input("How much gold do you want to steal? "))
    if gold >= 10000:
        print("you are a pirate for sure!")
    else:
        print("you should steal more!")
    ship_name = input("What's the name of your ship? ")
    print(f" Oh the {ship_name}, very nice name!")
    crew_size = int(input("How many in your pirate crew? "))
    if crew_size <= 10:
        print("you need a bigger crew!")
    else:
        print("Fantastic size crew, Yarg!")
else:
    print("maybe next time")
