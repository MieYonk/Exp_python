class Book:
    def __init__(self, name, publisher, price, count):
        self.name = name
        self.publisher = publisher
        self.price = price
        self.count = count

def loadBook(booklist):
    with open('books.txt', 'r',encoding="utf8") as file:
        for line in file:
            name, publisher, price, count = line.strip().split(',')
            book = Book(name, publisher, float(price), int(count))
            booklist.append(book)

def sortBook(booklist):
    booklist.sort(key=lambda x: (x.publisher, x.count))

def saveBook(booklist):
    with open('sorted_books.txt', 'w') as file:
        for book in booklist:
            file.write(f"{book.name},{book.publisher},{book.price},{book.count}\n")

def main():
    booklist = []
    loadBook(booklist)
    sortBook(booklist)
    saveBook(booklist)

main()
