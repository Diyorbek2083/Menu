from django.db import models

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
