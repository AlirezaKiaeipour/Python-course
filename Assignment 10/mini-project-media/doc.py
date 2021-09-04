from media import Media

class Doc(Media):
    def __init__(self, group, name, director, imdb, url, duration, cast,type):
        super().__init__(group, name, director, imdb, url, duration, cast)
        self.type = type

    def show_info(self):
        return Media.show_info(self) , print("Type:",self.type)

    def edit_doc(self):
        self.name = input("Please Enter New Name: ")
        self.director = input("Please Enter New Director: ")
        self.imdb = input("Please Enter New IMDB: ")
        self.url = input("Please Enter New Url: ")
        self.duration = input("Please Enter New Duration: ")
        self.cast = input("Please Enter New Actor And split With (/): ")
        self.type = input("Please Enter Newe Type: ")