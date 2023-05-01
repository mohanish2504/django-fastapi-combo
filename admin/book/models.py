from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name.capitalize()
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title.capitalize() + " by " + str(self.author)