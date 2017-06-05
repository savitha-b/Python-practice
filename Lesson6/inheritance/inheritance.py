#class definition
class Parent():
    def __init__(self, last_name, eye_color):
        print('Parent Constructor called')
        self.last_name = last_name
        self.eye_color = eye_color
#test by creating an instance
billy_cyrus = Parent("Cyrus", "blue")
print(billy_cyrus.last_name)
