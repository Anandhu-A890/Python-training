library=[]
def addbook(title,author):
    book={"title":title,"author":author,"issued":False}
    library.append(book)
    print(f"The book titled {title} of author {author} is added to the library")
addbook("Harry Potter","J K Rowling")
addbook("The Hobbit","J. R. R. Tolkien")
addbook("Da Vinci Code","Dan Brown")
addbook("The Days at Morisaki Bookshop","Satoshi Yagisawa")
def issuebook(title):
    for book in library:
        if book["title"].lower()==title.lower():
            if book["issued"]:
                print(f"The book {title} is already issued")
            else:
                book["issued"]=True
                print(f"The book {title} is issued")
            return
    print(f"The book {title} is not available")
issuebook("Harry Potter")

def return_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            if not book["issued"]:
                print(f"'{title}' was not issued.")
            else:
                book["issued"] = False
                print(f"'{title}' has been returned.")
            return
    print(f"'{title}' not found in the library.")
return_book("The Hobbit")

def search_book(title):
    for book in library:
        if book["title"].lower() == title.lower():
            status = "Issued" if book["issued"] else "Available"
            print(f"Found: '{book['title']}' by {book['author']} - {status}")
            return
    print(f"'{title}' not found in the library.")
search_book("Da Vinci Code")


def display_books():
    if not library:
        print("The library is empty.")
        return
    print("\nLibrary Books:")
    for book in library:
        status = "Issued" if book["issued"] else "Available"
        print(f"- {book['title']} by {book['author']} [{status}]")
display_books()