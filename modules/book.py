from modules.library_item import libraryItem

class Book(libraryItem):

    def __init__(self,title,subject,upc,issbn,authors,dds_number):
        libraryItem.__init__(self,title,upc,subject)
        self.issbn = issbn
        self.authors = authors
        self.dds_number = dds_number
