# A class is just a blueprint to create a desirable object.
# in this lesson we will create our own classes(blueprints) to create our own objects.

# to create a class first you need to use the keyword-class followed by the class-name that is PascalCased.
# Quick little knowledge
# PascalCase: every new starting word would be capital, e.g: CarBlueprintDemo
# camelCase: Every new starting word would be capital only except the first word e.g: carBlueprintDemo
# snake_case: Every word is lower case but separated by the underscore_ e.g: car_blueprint_demo


# class-name always start with the capital letter
class User:
    # pass can be used to replace the empty space and to avoid any errors
    pass


user_1 = User()

# Adding an attribute
# id is an attribute
user_1.id = "001"
user_1.username = "angela"

print(user_1.username)
# quick reminder: Attribute is a variable that is associated with the object

# creating a new user
user_2 = User()
user_2.id = "002"
user_2.username = "Jack"
