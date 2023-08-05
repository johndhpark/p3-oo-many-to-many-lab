class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])


class Book:
    all = []

    def __init__(self, title):
        self.title = title 
        Book.all.append(self)

    def books(self):
        return [book for book in Book.all]

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author is not an instance of the Author class")

        self._author = value

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author is not an instance of the Author class")

        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book is not an instance of the Book class")

        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not type(value) == str:
            raise Exception("date is not of a type string")

        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not type(value) == int:
            raise Exception("royalty is ot of a type int")

        self._royalties = value

    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract : contract.date)