from __future__ import unicode_literals

from django.db import models

# Book and Author have ManyToMany relationship
# So we can define their relationship on either side since they are both on Many side of relationship

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    notes = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Dojo object: First Name: {} \nLast Name: {} \nEmail: {} \nCreated At: {} \nUpdated At: {}>".format(self.first_name, self.last_name, self.email, self.created_at, self.updated_at)
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    authors = models.ManyToManyField(Author, related_name="books")
    def __repr__(self):
        return "<Dojo object: Name: {} \nDescription: {} \nCreated At: {} \nUpdated At: {}>".format(self.name, self.desc, self.created_at, self.updated_at)

# Using the shell...
# Create 5 books with the following names: C sharp, Java, Python, PHP, Ruby
# Book.objects.create(name="C#", desc="about C#")
# Book.objects.create(name="Java", desc="about Java")
# etc.

# Create 5 different authors: Mike, Speros, John, Jadee, Jay
# Author.objects.create(first_name="Mike", last_name="Dunder", email="mikeduner@gmail.com")
# Author.objects.create(first_name="Speros", last_name="Scott", email="sperosscott@gmail.com")
# Author.objects.create(first_name="John", last_name="Weasley", email="johnweasley@gmail.com")
# etc.

# Add a new field in the authors table called 'notes'. Make this a TextField. Successfully create and run the migration files.

# Using the shell...
# Change the name of the 5th book to C#
# >>> b = Book.objects.get(id=5)
# >>> b.name = "C#"
# >>> b.save()

# Change the first_name of the 5th author to Ketul
# >>> b = Author.objects.get(id=5)
# >>> b.first_name = "Ketul"
# >>> b.save()

# Assign the first author to the first 2 books
# >>> this_author = Author.objects.first()
# >>> this_book = Book.objects.get(id=1)
# >>> this_book2 = Book.objects.get(id=2)
# >>> this_author.books.add(this_book, this_book2)

# Assign the second author to the first 3 books
# >>> this_author = Author.objects.get(id=2)
# >>> this_book = Book.objects.get(id=1)
# >>> this_book2 = Book.objects.get(id=2)
# >>> this_book3 = Book.objects.get(id=3)
# >>> this_author.books.add(this_book, this_book2, this_book3)

# For the 3rd book, retrieve all the authors
# >>> Book.objects.get(id=3).authors.all()

# For the 3rd book, remove the first author
# >>> Book.objects.get(id=3).authors.first().delete()

# For the 2nd book, add the 5th author as one of the authors
# >>> Book.objects.get(id=2).add(Author.objects.get(id=5)

# Find all the books that the 3rd author is part of
# >>> Author.objects.get(id=3).books.all()

# Find all the books that the 2nd author is part of
# >>> Author.objects.get(id=2).books.all()
