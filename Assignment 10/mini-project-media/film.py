from media import Media

class Film(Media):
    def __init__(self, group, name, director, imdb, url, duration, cast,year):
        super().__init__(group, name, director, imdb, url, duration, cast)
        self.year = year

    def show_info(self):
        return Media.show_info(self) , print("Year:",self.year)

    def edit_film(self):
        self.name = input("Please Enter New Name: ")
        self.director = input("Please Enter New Director: ")
        self.imdb = input("Please Enter New IMDB: ")
        self.url = input("Please Enter New Url: ")
        self.duration = input("Please Enter New Duration: ")
        self.cast = input("Please Enter New Actor And split With (/): ")
        self.year = input("Please Enter New Year: ")
        
        