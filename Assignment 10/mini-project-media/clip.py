from media import Media

class Clip(Media):
    def __init__(self, group, name, director, imdb, url, duration, cast,about):
        super().__init__(group, name, director, imdb, url, duration, cast)
        self.about = about

    def show_info(self):
        return Media.show_info(self) , print("about:",self.about)

    def edit_clip(self):
        self.name = input("Please Enter New Name: ")
        self.director = input("Please Enter New Director: ")
        self.imdb = input("Please Enter New IMDB: ")
        self.url = input("Please Enter New Url: ")
        self.duration = input("Please Enter New Duration: ")
        self.cast = input("Please Enter New Actor And split With (/): ")
        self.about = input("Please Enter New About: ")