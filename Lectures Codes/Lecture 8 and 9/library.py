class Library:
    def __init__(self):
        self.books = []
        self.members = []

    # Add or remove books or members
    def addBooks(self, book):
        self.books.append(book)

    def removeBooks(self, book):
        self.books.remove(book)

    def registerMember(self, member):
        self.members.append(member)

    # Search library database: members and books
    def searchBooks(self, title):
        for book in self.books:
            if book.title == title:
                return book
        # If book not found, return None
        return None

    def searchMembers(self, name):
        for member in self.members:
            if member.name == name:
                return member
        # If member not found, return None
        return None
    
    # Borrow and return books
    def borrowBook(self, bookTitle, memberName):
        book = self.searchBooks(bookTitle)
        member = self.searchMembers(memberName)

        if book and member and book.isAvailable():
            if member.borrowBook(book):
                return "Book borrowed successfully"
        return False

    def returnBook(self, bookTitle, memberName):
        book = self.searchBooks(bookTitle)
        member = self.searchMembers(memberName)
        if book and member:
            if member.returnBook(book):
                return "Book returned successfully"
        return False

class Book:
    """
    Object book will have the following attributes:
    String: Title and Author
    Int: Page
    """
    def __init__(self, title='', author='', pages=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.borrowed = False

    def isAvailable(self):
        return not self.borrowed
    
    def bookBorrow(self):
        if self.borrowed:
            return False
        # Otherwise flag it as borrowed
        self.borrowed = True

        return True
    
    def bookReturn(self):
        # Flag set as not borrowed
        self.borrowed = False

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
    
class Member:
    def __init__(self, name):
        self.name = name
        # List of all borrowed books
        self.borrowedBooks = []

    def borrowBook(self, book):
        if book.bookBorrow():
            self.borrowedBooks.append(book)
            return True # Book successfully borrowed
        else:
            return False
        
    def returnBook(self, book):
        if book in self.borrowedBooks:
            book.bookReturn()
            self.borrowedBooks.remove(book)
            return True
        
        return False
    
# Test everything:
library = Library()
book1 = Book("1984", "Orwell", 300)
book2 = Book("Brave New World", "Huxley", 288)
member = Member("Alice")

# Add books and register member
library.addBooks(book1)
library.addBooks(book2)
library.registerMember(member)

# Tests
assert library.borrowBook("1984", "Alice") == "Book borrowed successfully"
assert not library.borrowBook("1984", "Alice")  # Book 1984 is already borrowed by Alice
assert library.returnBook("1984", "Alice") == "Book returned successfully"
assert library.borrowBook("1984", "Alice") == "Book borrowed successfully"

# Test result
print("All tests passed!")