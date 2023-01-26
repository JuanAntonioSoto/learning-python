# For print we can use '' or ""
print('Hello world!')
print("Hello world!")

print('test double quotes inside a single quoute "asdas"')
#error -> print('test double quotes inside a single quoute 'asdas'')
#error -> print("test double quotes inside a single quoute "asdas"")

# here we need to use the \ scape char in order to take the double quotes literally
print("test double quotes inside a single quoute \"asdas\"")

print("This is how we can add a new line\n in python with, \\n")

print('Con' + 'cat')