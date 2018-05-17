#NEW VOCABULARY WORDS:
#Class
#Instance
#Constructor(init)
#Self- is the object being created
#Instance variables
#Instance method

#this module provides a hihg-level interface to allowdisplaying web-based documents
import webbrowser

#this class provides the variables and functions for the object Movie()
class Movie():

    #prints the string
    "movie related info"

    #this function creates a new space and initializes th object
    #takes as input the function itSELF, the movie_title, movie_storyline, poster_image and trailer_youtube
    #has no output, and assigns the inputs to variable names
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, launch_date, VALID_RATINGS):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.launch_date = launch_date
        self.ratings = VALID_RATINGS

    #this function takes as input itself, and opens the trailer of the movie through the webbrowser module
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
