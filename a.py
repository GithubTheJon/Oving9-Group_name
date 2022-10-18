print("Hello World!")

text = None
while type(text) == str:
    try:
        text = str(input("Write a string: "))
    except ValueError:
        pass
    print(text)
