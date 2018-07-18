import re

class AuthSystem:
    
    def __init__(self):
        """Define regex"""
        self.username_regex = re.compile(r'[A-Z][a-z0-9]{5,11}')
        #print(type(self.username_regex))
        self.password_regex = re.compile(r'[a-z0-9]{6}')
    
    def _check_username(self, username):
        """Check username is valid or not"""
        if self.username_regex.search(username) is not None and len(username) < 12:
            #print("Correct username")
            return True
        else:
            if(len(username) < 6 or len(username) > 12):
                print("Username length error! Your username length is ",len(username))
            else:
                print("Username format error! Your username is ", username)
            return False
        
    def _check_password(self, password):
        """Check password is valid or not"""
        if self.password_regex.search(password) is not None:
            #print("Correct password")
            return True
        else:
            if(len(password) < 6):
                print("Password length error! Your password length is ",len(password))
            else:
                print("Password format error! Your password is ", password)
            return False
        
    def authenticate(self, username, password):
        """authenticate the user"""
        # print(len(username))
        # print(len(password))
        if not self._check_username(username):
            return
        
        if not self._check_password(password):
            return
        
        print("Welcome,",username,'!',sep='')

    
# Construct a object of type AuthSystem

username1 = input("username1:")
password1 = input("password1:")
username2 = input("username2:")
password2 = input("password2:")
username3 = input("username3:")
password3 = input("password3:")
username4 = input("username4:")
password4 = input("password4:")
#authenticate the user's credentials
auth = AuthSystem()
auth.authenticate(username1, password1)
auth = AuthSystem()
auth.authenticate(username2, password2)
auth = AuthSystem()
auth.authenticate(username3, password3)
auth = AuthSystem()
auth.authenticate(username4, password4)