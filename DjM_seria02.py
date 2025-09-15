def prvi(dic):
    
    odnos = 0
    rj = ""

    for podcast in dic:
        total = podcast["br_pozitivni"]+podcast["br_negativni"]
        if total/podcast["br_pozitivni"] > odnos:
            odnos = total/podcast["br_pozitivni"]
            rj = podcast["naziv"]
    

    print(rj)

#drugi
class Book:

    def __init__(self, naslov, autor, godina, brojKopija):
        self.naslov = naslov
        self.autor = autor
        self.godina= godina
        self.brojKopija = brojKopija

    def getNaslov(self):
        return self.naslov    
    def getAutor(self):
        return self.autor    
    def getGodina(self):
        return self.godina   
    def getBrojKopija(self):
        return self.brojKopija
    
    def getBook(self):
        dic = {"naslov": self.naslov, "autor": self.autor}
    
    
    def setNaslov(self, naslov):
        self.naslov = naslov
    def setAutor(self, autor):
        self.autor = autor
    def setGodina(self, godina):
        self.godina = godina
    def setBrojKopija(self, brk):
        self.brojKopija = brk

    
class Library:

    def __init__(self, books):
        self.books = list(books)

    def pregledKnjiga(self):
        for book in self.books:
            print(f'{book.naslov} {book.autor}  {book.godina}')
    def dodavanjeKnjige(self, book):

        self.books.append(book)


    def deleteBook(self,title):

        for b in self.books:
            if b.getNaslov == title:
                self.books.remove(b)


ar = [
        {"naziv":"Español para principiantes", "br_pozitivni":1000,"br_negativni":10},
        {"naziv":"Philophize This!", "br_pozitivni":500,"br_negativni": 30},
        {"naziv": "Science VS." ,"br_pozitivni":600,"br_negativni": 45} 
    ]

#prvi(ar)

book1 = Book("Harry Potter", "a1", 1990, 5)
book2 = Book("b2", "a2", 2020, 3)
book3 = Book("b3", "a3", 2020, 3)



books = []
books.append(book1)
books.append(book2)

bibl = Library(books)


bibl.pregledKnjiga()


print('-------------------------------')

bibl.dodavanjeKnjige(book3)
bibl.pregledKnjiga()

print('-------------------------------')

bibl.deleteBook("b2")
bibl.pregledKnjiga()
