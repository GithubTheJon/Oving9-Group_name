print("Hello World!")

text = 0
while type(text) != str:
    try:
        text = str(input("Write a string: "))
    except ValueError:
        pass
print(text)
    
