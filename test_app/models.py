from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100) # VarChar(255)
    description = models.TextField()
    price = models.FloatField()

    published_date = models.DateField() # Datetime(%Y%m%d)


"""
CREATE TABLE IF NOT EXISTS 'test_app_book' (
    id ...
    title VarChar(100) NOT NULL
    desctiption TEXT NOT NULL
    published date DATE 
)
"""
