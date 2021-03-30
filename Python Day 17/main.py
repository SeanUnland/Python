# Creating Classes

# class User: 
#     # use "pass" to create blank classes or functions
#     pass
# object.attribute = something

class User: 
    def __init__(self, user_id, username): 
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
    # Methods always need a "self" parameter as the first parameter, methods are functions attached to an object
    def follow(self, user): 
        user.followers += 1
        self.following += 1
            
user_1 = User("001", "Sean")

user_2 = User("002", "Bill")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)