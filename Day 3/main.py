def hello():
    return 'Hello'

greet = hello
print(hello())
print(greet())

del hello
print(greet())