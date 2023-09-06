# A class is just a blueprint to create a desirable object.
# in this lesson we will create our own classes(blueprints) to create our own objects.

# to create a class first you need to use the keyword-class followed by the class-name that is PascalCased.
# Quick little knowledge
# PascalCase: every new starting word would be capital, e.g: CarBlueprintDemo
# camelCase: Every new starting word would be capital only except the first word e.g: carBlueprintDemo
# snake_case: Every word is lower case but separated by the underscore_ e.g: car_blueprint_demo


# class-name always start with the capital letter
class User:
    # __init__ function is used to initialize the attributes and is a special function
    # this will print whenever new construction will be happening. (New user being created in this case)
    # self is an actual object that is being created.
    # with that you can add as many parameters as you wish
    def __init__(self, user_id, username):
        print(f"new user being created {user_id}")
        self.user_id = user_id
        self.username = username
        # set to a default value, so we don't have to provide it everytime in the parameter
        self.followers = 0



user_1 = User("001", "Angela")

print(user_1.user_id)
print(user_1.username)
# printing the default value
print(f"followers = {user_1.followers}")
# quick reminder: Attribute is a variable that is associated with the object

# creating a new user
user_2 = User("002", "Jack")
print(user_2.user_id)
print(user_2.username)
print(f"followers = {user_2.followers}")

# In python how can we create a constructor?
# A Constructor is nothing but initializer
# Whenever we are creating a new attributes they must provide 2 parameters
