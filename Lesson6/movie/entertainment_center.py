#using the class definition / calling

import media

#toy_story = media.Movie()
#media is the module/file name ||| turtle, Movie is ||| to Turtle (brad=turtle.Turtle)
#media.Movie does similar functionality as calling a __init__ function
#init function is also called a constructor, here creates space for instance

toy_story = media.Movie("Toy Story",
                        "The story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#inputs are added acc to syntax in definition of class.
#"self" is skipped as it is automatically added in python
print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A Marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)
