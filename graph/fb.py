class Account:
    def __init__(self,username):
        self.username = username
        self.friends = []

class Facebook:
    def __init__(self):
        self.accounts = {}

    def create_account(self,username):
        if username not in self.accounts:
            account = Account(username)
            self.accounts[username] = account
            print("Account Created")
        else:
            print("user already exists") 

    def add_connection(self, user1, user2):
        if user1 == user2:
            print("same user cannot be connected")
        elif user1 in self.accounts and user2 in self.accounts:
            user1_acc = self.accounts[user1]
            user2_acc = self.accounts[user2]
            user1_acc.friends.append(user2_acc)
            user2_acc.friends.append(user1_acc)  
            print("User connected")
        else:
            print("user doesn't exists")

    def find_friends(self,username):
        if username in self.accounts:
            friends = self.accounts[username].friends
            return [ friend.username for friend in friends]
        else:
            return("user not found")
                    
    def friend_suggestion(self, username):
        if username in self.accounts:
            friends = self.accounts[username].friends
            suggestion = []
            for friend in friends:
                for user in friend.friends:
                    if user not in friends and user.username is not username:
                        suggestion.append(user.username) 
            return suggestion 
        else:
            print("user not exists")             

fb = Facebook()
fb.create_account("aditya")
fb.create_account("anshu")
fb.create_account("aadi")
fb.add_connection("anshu","aditya")
fb.add_connection("anshu","aadi")

# print(fb.accounts["anshu"].friends)
print(fb.find_friends("anshu"))
print(fb.friend_suggestion("aadi"))

        