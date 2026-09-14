# we need to create  a data structure which can store alot of records. we should be able to perform insertion sort and more very easily

# input is user profile = email,name,username

## pyhton class 

class User:
    def __init__ (self,username,email,name):
        self.username = username
        self.email = email
        self.name = name
        print ("user created")

    

# init means initailize. self means object being created. pyhton auto sends the object as self (this specific object)
user1 = User(username = "ayushg", email = "ayushg0500@gmail.com", name = "ayush gupta")




#class Node:
    #def __init__ (self,value):
        #self.value = value
        #self.left = None
        #self.right = None


class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        for i in range (0, len(self.users) - 1):
            if self.users[i].username