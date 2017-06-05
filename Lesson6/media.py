#this is for class definition

#choose which details should be remembered for each movie
#1. title 2. storyline 3. poster_image 4. youtube_trailer 5. reviews (possibilities)

class Movie():
    #names of classes are generally started with uppercase letters(Google python styleguide)
    def __init__(self,movie_title, movie_storyline, poster_image, trailer_youtube):
        #2underscores => reserved keyword
        #self is init itself, or the instance being created
        #self can be replaced by any regular word, but its used as a convention
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
