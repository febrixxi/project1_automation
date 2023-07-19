from modules.library_item import libraryItem

class Magazine(libraryItem):
    def __init__(self,title,subject,upc,volume,issue):
        libraryItem.__init__(self,title,subject,upc)
        self.volume = volume
        self.issue = issue