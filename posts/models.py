from django.db import models
from categories.models import Category
from author.models import Author

# Create your models here.
class Post(models.Model) :
    title = models.CharField(max_length = 100)
    content = models.TextField()
    category  = models.ManyToManyField(Category) # many to many relations : ekti post multiple category er hote pare ebong multiple post ekti category er hote pare
    author = models.ForeignKey(Author, on_delete = models.CASCADE)# one to many relations: 1 ti post er 1 jon er author hote pare ebong onak gulo post er ekjon e author thakte pare

    def __str__ (self) :
        return f'{self.title} - ({self.author})'