from django.db import models

# Create your models here.
"""
create table book(
name varchar(20),
price float(4,2)
);

"""


class Book(models.Model):
    name = models.CharField(max_length=24)
    price = models.IntegerField()
    pub_date = models.DateField()
    author = models.CharField(max_length=32, null=False)


class Author(models.Model):
    name = models.CharField(max_length=32)

