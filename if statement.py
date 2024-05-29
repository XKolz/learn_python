# # if statement
# in python, we use indentation to group our line of code
# we don't use curly braces like in javascript
temperature = 10

if temperature > 30:
    print("it's a rainy day")
    print("please drink water")
elif temperature > 20: #This means the conditions is[ > 20, => 30]
    print("it's a better day")
elif temperature > 10: #This means the conditions is[ > 10, => 20]
    print("it's a nice day")
else:
    print("it's cold")