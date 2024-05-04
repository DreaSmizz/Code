class User:

    def __init__(self, user_id, username):
        print("new user being created....")
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    #Method
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "drea")
user_2 = User("002", "jade")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)




# user_1 = User("001", "drea")
# print(user_1.followers)


# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.name = "jade"