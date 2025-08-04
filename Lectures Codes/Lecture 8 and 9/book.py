# For exercise 1 - Passed
# Exercise 2 - Passed
class Book(object):
    """
    Object book will have the following attributes:
    String: Title and Author
    Int: Page
    """
    def __init__(self, title='', author='', pages=0):
        self.title = title
        self.author = author
        self.pages = pages

    # Set Methods
    def setTitle(self, newTitle):
        self.title = newTitle

    def setAuthor(self, newAuthor):
        self.author = newAuthor

    def setPage(self, newPage):
        self.pages = newPage
    # Get Methods
    def getTitle(self):
        return self.title
    
    def getAuthor(self):
        return self.author
    
    def getPages(self):
        return self.pages
    
    # Other methods
    def isLong(self): 
        if self.pages > 300:
            return True
        else:
            return False

    def getSummary(self):
        return self.title + ' by ' + self.author + ', ' + str(self.pages) + ' pages.'

# Test Exercise 1 - Passed
book = Book("1984", "George Orwell", 328)
#print(book.getSummary())
assert book.getSummary() == "1984 by George Orwell, 328 pages."

# Test book - Getters
# print(book.getName())
# print(book.getAuthor())
# print(book.getPages())

# Test setters, newBook:
newBook = Book()

newBook.setTitle("Dune")
newBook.setAuthor("Frank Herbert")
newBook.setPage(412)

# Test getters, newBook: 
assert newBook.getTitle() == "Dune"
assert newBook.getAuthor() == "Frank Herbert"
assert newBook.getPages() == 412

# Modify title and page from newBook
newBook.setTitle("Dune Messiah")
newBook.setPage(256)

assert newBook.getTitle() == "Dune Messiah"
assert newBook.getPages() == 256

# Test logic, isLong() method and getSummary
assert not newBook.isLong()
newBook.setPage(500)
assert newBook.isLong()
assert newBook.getSummary() == "Dune Messiah by Frank Herbert, 500 pages."

# print(newBook.getName())
# print(newBook.getAuthor())
# print(newBook.getPages())
# print("is", book.getName(), "a big book? ", book.isLong())
# print("is", newBook.getName(), "a big book? ", newBook.isLong())