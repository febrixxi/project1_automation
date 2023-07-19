from modules.library_item import libraryItem

class Dvd(libraryItem):
    def __init__(self,title,subject,upc,actors,directors,genre):
        libraryItem.__init__(self, title, subject,upc)
        self.actors = actors
        self.directors = directors
        self.genre = genre