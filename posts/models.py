from unicodedata import category, name
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    image = models.ImageField(null = False, blank = False)
    imgdesc = models.TextField()
    details = models.TextField()

    def __str__(self):
        return self.title

class Volume(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Journal(models.Model):
    category = models.ForeignKey(Volume, on_delete=models.SET_NULL, null=True, blank=True)
    title =  models.CharField(max_length=200, null=False, blank=False)
    author = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(null=True)
    abstract = models.TextField()
    pdf= models.FileField(upload_to='store/pdfs')
    cover = models.ImageField(upload_to='store/covers')

    def __str__(self):
        return self.title