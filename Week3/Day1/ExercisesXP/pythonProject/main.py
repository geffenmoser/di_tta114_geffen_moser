class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    def issue_book(self):
        if self.available = True:
            print(f"You have now checked out {self.title} by {self.author}")
            self.available = False
        else:
            print(f"{self.title} by {self.author} is not available to be loaned out now")

    def return_book(self):
        print(f"{self.title} by {self.author} has been returned, thank you")
        self.available = True

    def __str__(self):
        if self.available = True:
            avail = "Available"
        else:
            avail = "Issued"
        return (f"{self.title}+{self.author}+{self.isbn}+{avail}")


class Library:

    def __init__(self):
        self.inventory = []
    def add_book(self, title, author, isbn)):
        book.__init__(title, author, isbn)
        self.inventory.append(book.__str__())

    def find_by_author(self, author):
        author_list = []
        for books in self.inventory:
            if author == :
                author_list += book.__list__(self)










