#using the class definition / calling

import media
import fresh_tomatoes

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

#print(toy_story.storyline)
#toy_story.show_trailer()
#toy_story.show_poster()

avatar = media.Movie("Avatar",
                        "A Marine on an alien planet",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print(avatar.storyline)
#avatar.show_trailer()
#avatar.show_poster()

up = media.Movie("Up",
                        "Story of a young wilderness explorer meets an old man",
                        "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                        "https://www.youtube.com/watch?v=pkqzFUhGPJg")
#print(up.storyline)
#up.show_trailer()
#up.show_poster()
ratatouille = media.Movie("Ratatouille",
                        "A rat is a chef in Paris",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=B7X_RXq0Urw")

midnight_in_paris = media.Movie("Midnight in paris",
                        "Going back in time to meet authors",
                        "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=dtiklALGz20")

hunger_games = media.Movie("Hunger Games",
                        "A really real reality game",
                        "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=PbA63a7H0bo")
#use fresh tomatoes code

#define array/list for movie instances to use with open movies function
movies = [toy_story, avatar, up, ratatouille, midnight_in_paris, hunger_games]
#fresh_tomatoes.open_movies_page(movies)

#valid ratings
#print (media.Movie.VALID_RATINGS)
#valid ratings is a list that can be shared among all its instances, eg: toy story, avatar etc. => class variable

print(media.Movie.__doc__)
