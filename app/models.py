from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
class Room(models.Model):
    nomi = models.CharField(max_length=25)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status_choise = models.BooleanField()
    def __str__(self):
        return self.nomi


class PublishManeger(models.Manager):
    def get_queryset(self):
        return super(PublishManeger, self).get_queryset().filter(status = 'published')



class TablesModel(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    raqam = models.BigIntegerField(unique=True)
    nomi = models.CharField(max_length=25)
    xona = models.ForeignKey(to=Room, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status_Choice = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishManeger()
    bandligi = models.BooleanField()
    qr_code = models.ImageField(upload_to='QR_Code/')
    def __str__(self):
        return self.nomi


class CategoryFood(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=40)
    def __str__(self):
        return self.name

class FoodPost(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.BigIntegerField()
    rasmi = models.ImageField(upload_to='products/')
    video = models.FileField(upload_to='products_videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])
    category = models.ForeignKey(to=CategoryFood, on_delete=models.CASCADE)
    maxsulotlar = models.TextField()
    like = models.ForeignKey(to=User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomi


class CommentModel(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=FoodPost, on_delete=models.CASCADE)
    izox = models.TextField()
    def __str__(self):
        return self.user
class CommentReply(models.Model):
    reply = models.ForeignKey(to=CommentModel, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    izoh = models.TextField()
    def __str__(self):
        return self.user


