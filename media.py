# Defination for class Video
class Video(object):
    __doc__ = """Provides a way to store Video related information."""
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_info(self):
        print("Title: %s" % self.title)
        print("Duration: %s" % self.duration)

# Defination a sub class of Video i.e TvShow
class TvShow(Video):
    __doc__ = """Provides a way to store TV Show related information."""
    
    def __init__(self, title, duration,
                 season, episode, tv_station):
        super(TvShow, self).__init__(title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station

# Defination a sub class of Video i.e  Movie
class Movie(Video):
    __doc__ = """Provides a way to store Movie related information."""
	
    VALID_RATINGS = []

            
    def __init__(self, title, duration, trailer_youtube_url,
                 poster_image_url, storyline = None,
                 rating =  None, reviews=[]):
        super(Movie, self).__init__(title, duration)
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url
        self.reviews = reviews
        self.storyline = storyline
        
        

