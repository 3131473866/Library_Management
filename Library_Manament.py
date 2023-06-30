import os, sys

class Book:

    def __init__(self, name, author, status, index, ISBN):
        """This function creates variables defines a book"""
        self.name = name
        self.author = author
        self.status = status
        self.index = index
        self.ISBN = ISBN
    
    def __str__(self):
        """This funciton will check the availability of the book"""
        if self.status >= 1:
            stats = 'Still Available'
        elif self.status == 0:
            stats = 'Currently Not Available'
        else:
            stats = 'Error'
        return 'Booktitle: <%s> Author: <%s> Status: <%s> Position: <%s> ISBN: <%s>' %(self.name, self.author, stats, self.index, self.ISBN)

class Librarian:

    books = [] # Declares the list for the books

    def shelf(self):
        """This shelf contains few books"""
        self.books.append(Book('Fairy Tale', 'Stephen King', 1, 'HV0972', '9781668002179'))
        self.books.append(Book('Harry Potter', 'J.K. Rowling', 1, 'PR7312', '9780590353427'))
        self.books.append(Book('The Great Gatsby', 'F. Scott Fitzgerald', 1, 'PKA5411', '9780743273565'))
        self.books.append(Book('To Kill a Mockingbird','Harper Lee', 1, 'AZ7232', '0446310786'))
        self.books.append(Book('Crazy Rich Asians','Kevin Kwan', 1, 'HU6812', '9780345803788'))

    def Homepage(self):
        """This is a homepage function showing different options"""
        self.shelf()
        while True:
                print('********************************************')
                print('***********Welcome to the Library***********')
                print('********************************************')
                print('********** 1. Display all Books  ***********')
                print('********** 2. Add Books          ***********')
                print('********** 3. Borrow Books       ***********')
                print('********** 4. Return Books       ***********')
                print('********** 5. Exit               ***********')
                print('********************************************')
                print('********************************************')
                print('********************************************')
                
                option = input('Please select a option: ')

                if option == '1':
                    self.all_book() # Display all the books in the shelf
                elif option == '2':
                    self.add_book() # Allow users to add book
                elif option == '3':
                    self.borrow_book() # Allow users to borrow book from shelf
                elif option == '4':
                    self.return_book() # Allows users to return the book
                elif option == '5':
                    print('********************************************')
                    print('Thank you for using, Have a Wonderful Day :)')
                    print('____________________________________________')
                    os._exit(0) # Exit the program.
                else:
                    print('Please choose a option you need: ')
                    continue
    def all_book(self):
        """Using a for loop to iterate over the books contained in the shelf"""
        for book in self.books:
            print(book)

    def add_book(self):
        """This function allow user to add books
            They would need to input details about the book
            Then, it will return the added book
            Store it in the shelf
        """
        name = input('Enter the Booktitle: ')
        author = input('Enter the Author: ')
        self.books.append(Book(name, author, 1, input('Position: '), input('ISBN: ')))
        print('Book <%s> Added Sucess!' % name)
    def check_book(self, name):
        """This function checks the book in the lists
            If the name is still there, it will return
            the all books"""
        for book in self.books:
            if book.name == name:
                return book
        else:
            return None
    def borrow_book(self):
        """This function let the user borrow books from the shelf."""
        name = input('Please enter the book you want to borrow: ')
        borrow = self.check_book(name)
        print(borrow)

        if borrow != None:
            if borrow.status == 0:
                print('Book <%s> is already rented! ' % name)  # If the input booktitle doesnt match the books in the list it means it's already rented.
            else:
                borrow.status = 0
                print('Book <%s> borrowed sucess! ' % name) # If its not rented and user wants to borrow, it will display lend suces
        else:
            print('Book <%s> does not exist! ' % name) # Or else, the input book title doesnt exist in the lists.
    
    def return_book(self):
        """This function let the user to return the book
            The if/else statement checks differnt possibilities
            when returning a book"""
        name = input('Please enter the book you want to return: ')
        borrow = self.check_book(name)

        if borrow != None:
            if borrow.status == 0:
                borrow.status = 1
                print('Book <%s> is returned sucess, thank you! ' % name) # If the booktitle match to the list then it will print return sucess
                print(borrow)
            else:
                print('Book <%s> is not borrowed! ' % name)  # If the book didn't match the list it means user didn't borrow that one
        else:
            print('Book <%s> does not exist! ' % name) # Or else, the book user input it doesn't exist.

library = Librarian()
library.Homepage() # calls the function