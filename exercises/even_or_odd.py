def even_or_odd():
    inp = input("Insert a number: ")
    number = int(inp)
    module = number % 2
    if module == 0:
        print("The number is event!")
    else:
        print("The number is odd!")


even_or_odd()
