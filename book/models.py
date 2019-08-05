from django.db import models
from django.contrib.auth.models import User

#
# book
#

class Book(models.Model):
    isbn = models.CharField(max_length=20)
    title1 = models.CharField(max_length=250)
    title2 = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=50)
    cover = models.URLField(max_length=50)
    designation = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    publication_year = models.CharField(max_length=20)
    language = models.CharField(max_length=20)
    code_book_id = models.CharField(max_length=20, default='')

class BookCopies(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date_added = models.DateField()


#
# loan
#

class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()