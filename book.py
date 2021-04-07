class Book:
    def __init__(self, title, revison, authors):
        self.title = title
        self.title = revison
        self.authors = authors

    def lend(self, userName):
        print("Book {} lent by {}".format(self.title, userName))
