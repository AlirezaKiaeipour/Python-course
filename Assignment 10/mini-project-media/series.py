
from media import Media

class Series(Media):
    def __init__(self, group, name, director, imdb, url, duration, cast,season):
        super().__init__(group, name, director, imdb, url, duration, cast)
        self.season = season

    def show_info(self):
        return Media.show_info(self) , print("Season:",self.season)

    def edit_series(self):
        self.name = input("Please Enter New Name: ")
        self.director = input("Please Enter New Director: ")
        self.imdb = input("Please Enter New IMDB: ")
        self.url = input("Please Enter New Url: ")
        self.duration = input("Please Enter New Duration: ")
        self.cast = input("Please Enter New Actor And split With (/): ")
        self.season = input("Please Enter New Season: ")