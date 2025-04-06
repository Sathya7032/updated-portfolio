from django.db import models
from django.utils.html import format_html
from ckeditor.fields import RichTextField
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=40)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    discription = models.TextField()
    url = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='category/')
     
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;"/>'.format(self.image))
    
    def __str__(self):
        return self.title
    

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post/')
    content = RichTextField()
    url = models.CharField(max_length=100,unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)  


    class Meta:
        ordering = ['title']     

    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px;height:40px;"/>'.format(self.image))
    
    def __str__(self):
        return self.title    
  


class Projects(models.Model):
    name = models.CharField(max_length = 10000)
    details = RichTextField()
    image = models.ImageField(upload_to='images')
    links = models.URLField()
    