#!/usr/bin/python3
""" 
User class
"""

class User():
    """ Documentation """
    
    def __init__(self): 
        """ Documentation """
    
    def email(self, value, email):
        """ Documentation """
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.email = email 

    @property
    def email(self):
        """ Documentation """
        return self.email
   
    
if __name__ == "__main__":

    u = User()
  
    print(u)
    



