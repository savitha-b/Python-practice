#class definition
class Parent():
    def __init__(self, last_name, eye_color):
        print('Parent Constructor called')
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye Color -"+self.eye_color)

#define class child
class Child(Parent): #syntax to show child can reuse anything publicly available in class parent
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor called")
        Parent.__init__(self, last_name, eye_color) #inherited variables are initialized from parent's init function
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name -"+self.last_name)
        print("Eye Color -"+self.eye_color)
        print("Number of Toys -"+str(self.number_of_toys))
        
#test by creating an instance
billy_cyrus = Parent("Cyrus", "blue")
#print(billy_cyrus.last_name)
#billy_cyrus.show_info()

#instance for class child
miley_cyrus = Child("Cyrus", "blue",5)
#print(miley_cyrus.last_name)
#print(miley_cyrus.number_of_toys)
miley_cyrus.show_info()
