from modules.library_item import libraryItem

class Cd(libraryItem):
    def __init__(self,title,subject,upc,artist):
        libraryItem.__init__(self, title, subject,upc)
        self.artist = artist
