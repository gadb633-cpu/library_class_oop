class Book:
    total_books = 0
    def __init__(self,book_name,author,copies):
        self.book_name = book_name
        self.author = author
        self.__copies = copies
        if copies <1:
            raise ValueError("most be above 0!")
        self.__available = copies
        Book.total_books +=1
    def borrow(self):
        if self.__available <1:
            raise ValueError("is not available!")
        self.__available -=1
    def return_book(self):
        if self.__available == self.copies:
            raise ValueError("All the books have already been returned!")  
        self.__available+1
    def is_available(self):
        if self.__available >=1:
            return True
        return False
    def __str__(self):
        return f"book_name:{self.book_name} \nauthor is:{self.author} \navailable:{self.__available}/{self.__copies}"    


