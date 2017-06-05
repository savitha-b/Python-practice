- Class variables: can be used to define variables that can be shared by different instances of a class. 
so this can be definedd in the class definition itself.

- Pre-defined Class Variables: Python has few.
eg: __doc__
trying it in python shell window,
">>> import turtle"
">>> turtle.Turtle.__doc__"
o/p would be 'RawTurtle auto-creating (scrolled) canvas.\n\n    When a Turtle object is created or a function derived from some\n    Turtle method is called a TurtleScreen object is automatically created.\n 

- Now try to use the same for class Movie.
put required documentation in triple quotes ni class definition.

- Inheritance
common traits/attributes that another class can take from another class
eg:
class Parent
attributes - last name, eye color, height etc

class child
attributes - last name, eye color (these 2 same from above class), number of toys 
=> reusing code.

___________
Try to make movie websote code better by inheritance. 
If we need to add another class such as tv_show, it could inherit details.
attributes: title, season, episode, tv_station another function get_local_listing

We may also have another shared class Video() to display duration of the movie / tv show 
(similar to shared class variables)
i.e. class Movie would inherit from class Video => class Movie(Video) ||| class TvShow

helps inheritance and resue of code also helps to map code easily to human thought process.
____________
defined a new function in class parent. show_info.
this is not explicitly defined / inherited in child class definition but can be used, 
since it is public in class parent and child inherits all attributes of parent class.
_______
Function/ method override: Defining a function with a same name in child class=> this would be used when called from the child class and not the one from teh parent function.

