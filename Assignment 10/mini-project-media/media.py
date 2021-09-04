
from actor import Actor
from pytube import YouTube
class Media:
    def __init__(self,group,name,director,imdb,url,duration,cast):
        self.group = group
        self.name = name
        self.director = director
        self.imdb = imdb
        self.url = url
        self.duration = duration
        self.cast = cast
        

    def show_info(self):
        print("Group:",self.group,",","Name:",self.name,",","Director:",self.director,","
        ,"IMDB:",self.imdb,",","Url:",self.url,",","Duration:",self.duration,",","Cast:",self.cast,",",end=" ")


    def Download(self):
        YouTube(self.url).streams.get_highest_resolution().download()

    def Cast(self):
        act = self.cast.split("/")
        for i in act:
            Actor(i).show_actor()