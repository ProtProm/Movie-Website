#this module provides the Movie() class and imports webbrowser
import media
#this module provides the style and scripting of the page, as well as the mainpage layout, title bar and a movie entry template
#imports webbrowser, os and re
#displays the functions create_movie_titles_content() and open_movies_page()
import fresh_tomatoes

 #this variables are the ones that will be shown in the page as the movies, and all the info that is wanted to be seen
django  = media.Movie("Django Unchained", "With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.", "https://ia.media-imdb.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_SY1000_CR0,0,674,1000_AL_.jpg", "https://www.youtube.com/watch?v=CLofzNkIqAc","2012", "R")

brian = media.Movie("Life of Brian", "Born on the original Christmas in the stable next door to Jesus, Brian of Nazareth spends his life being mistaken for a messiah.", "https://ia.media-imdb.com/images/M/MV5BMzAwNjU1OTktYjY3Mi00NDY5LWFlZWUtZjhjNGE0OTkwZDkwXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,637,1000_AL_.jpg", "https://www.youtube.com/watch?v=TKPmGjVFbrY","1979", "R")

orient = media.Movie("Murder on the Orient Express", "In December 1935, when his train is stopped by deep snow, detective Hercule Poirot is called on to solve a murder that occurred in his car the night before.", "https://ia.media-imdb.com/images/M/MV5BNDlkZjJjYTktZDI4OS00MWFkLTg1MzMtNTY3MmI2OTBkMTU1XkEyXkFqcGdeQXVyMjUzOTY1NTc@._V1_.jpg", "https://www.youtube.com/watch?v=u0ykCP1AYlk","1974", "PG-13")

bruges = media.Movie("In Bruges", "Guilt-stricken after a job gone wrong, hitman Ray and his partner await orders from their ruthless boss in Bruges, Belgium, the last place in the world Ray wants to be.", "https://ia.media-imdb.com/images/M/MV5BMTUwOGFiM2QtOWMxYS00MjU2LThmZDMtZDM2MWMzNzllNjdhXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_.jpg", "https://www.youtube.com/watch?v=p-gG2qo_l_A","2008", "R")

monkeys = media.Movie("Twelve Monkeys","In a future world devastated by disease, a convict is sent back in time to gather information about the man-made virus that wiped out most of the human population on the planet.", "https://ia.media-imdb.com/images/M/MV5BN2Y2OWU4MWMtNmIyMy00YzMyLWI0Y2ItMTcyZDc3MTdmZDU4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,671,1000_AL_.jpg", "https://www.youtube.com/watch?v=15s4Y9ffW_o","1995", "PG-13")

darjeeling = media.Movie("The Darjeeling Limited", "A year after their father's funeral, three brothers travel across India by train in an attempt to bond with each other.", "https://pics.filmaffinity.com/the_darjeeling_limited-866831800-large.jpg","https://www.youtube.com/watch?v=aO1bYukdvLI","2007", "R")

primer = media.Movie("Primer", "Four friends/fledgling entrepreneurs, knowing that there's something bigger and more innovative than the different error-checking devices they've built, wrestle over their new invention.", "https://ia.media-imdb.com/images/M/MV5BNjc3OWVjMTItYjc0Yi00NmFlLTk2YTgtYmU0MzcxMjBkNTYxXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY1000_CR0,0,675,1000_AL_.jpg", "https://www.youtube.com/watch?v=-vD-yj9o664","2004", "PG-13")

smoking = media.Movie("Thank You for Smoking", "Satirical comedy follows the machinations of Big Tobacco's chief spokesman, Nick Naylor, who spins on behalf of cigarettes while trying to remain a role model for his twelve-year-old son.", "https://ia.media-imdb.com/images/M/MV5BMTI2MDk5MjE4NV5BMl5BanBnXkFtZTYwMjkwNTU3._V1_.jpg", "https://www.youtube.com/watch?v=Df32RijORLo","2005", "R")

#list that contains all the movies for the page
movies = [orient, brian, monkeys, primer, smoking, darjeeling, bruges, django]

#as output opens the movie webpage and takes as input movies' list
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
