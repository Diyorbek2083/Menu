from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
import qrc
from django.core.files.base import ContentFile
from io import BytesIO

class PublishManeger(models.Manager):
    def get_queryset(self):
        return super(PublishManeger, self).get_queryset().filter(status = 'published')

class RoomModels(models.Model):
    nomi = models.CharField(max_length=25)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status_choise = models.BooleanField()
    
    def __str__(self):
        return self.nomi


class TableModels(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    raqam = models.BigIntegerField(unique=True)
    nomi = models.CharField(max_length=30)
    xona = models.ForeignKey(RoomModels, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status_Choice = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    bandligi = models.BooleanField(default=False)
    qr_code = models.ImageField(upload_to='QR_Code/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nomi} ({self.raqam})"
    
    def generate_qr_code(self):
        """Stol uchun QR kod yaratish"""
        data = f"Stol-{self.raqam}"  # QR kodga tushadigan matn
        qr = qrc.make(data)  # QR kod yaratish
        buffer = BytesIO()
        qr.save(buffer, format="PNG")  # PNG formatida saqlash
        return ContentFile(buffer.getvalue(), name=f"stol_{self.raqam}.png")

    def save(self, *args, **kwargs):
        """Saqlashdan oldin avtomatik QR kod yaratish"""
        if not self.qr_code:  # Agar QR kod yo‘q bo‘lsa, yangisini yaratish
            self.qr_code = self.generate_qr_code()
            self.nomi = f"{self.raqam} - stol"
        super().save(*args, **kwargs)  # Asosiy saqlash funksiyasini chaqirish


class ChefModels(models.Model):
    name = models.CharField(max_length=30)
    familya = models.CharField(max_length=30)
    mutaxasislik = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)


class FoodCategoryaModels(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=40)
    def __str__(self):
        return self.name

class FoodsModels(models.Model):
    nomi = models.CharField(max_length=30)
    narxi = models.BigIntegerField()
    rasmi = models.ImageField(upload_to='products/')
    video = models.FileField(upload_to='products_videos/', validators=[FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])
    category = models.ForeignKey(to=FoodCategoryaModels, on_delete=models.CASCADE)
    oshpaz = models.ForeignKey(to=ChefModels, on_delete=models.CASCADE)  # TO‘G‘RI!
    maxsulotlar = models.TextField()
    
    def __str__(self):
        return self.nomi


class CommentModel(models.Model):
    user = models.CharField(max_length=30)
    product = models.ForeignKey(to=FoodsModels, on_delete=models.CASCADE)
    izox = models.TextField()

    def __str__(self):
        return self.user
    

class ReplayCommentModels(models.Model):
    reply = models.ForeignKey(to=CommentModel, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    izoh = models.TextField()

    def __str__(self):
        return self.user
    

class LikeMolels(models.Model):
    food = models.ForeignKey(to=FoodsModels, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    creat_time = models.DateTimeField(auto_now_add=True)


class WaiterModels(models.Model):
    ism = models.CharField(max_length=35)
    familya = models.CharField(max_length=35)
    parol = models.CharField(max_length=50)
    tel = models.PositiveBigIntegerField()
    create_time = models.DateTimeField(auto_now_add=True)
    kun = models.IntegerField()

class UserModels(models.Model):
    name = models.CharField(max_length=25)
    familiya = models.CharField(max_length=25)
    tel = models.IntegerField()
    parol = models.CharField(max_length=30)
    zakaz_soni = models.IntegerField()
    zaqaz_pul = models.BigIntegerField()



class KarzinkaModels(models.Model):
    user = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    narxi = models.CharField(max_length=50)
    soni = models.IntegerField()
    stol_soni = models.IntegerField()
    coment = models.TextField()
    oshpaz = models.ForeignKey(to=ChefModels, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class DoimiyKarzinkaModels(models.Model):
    user = models.CharField(max_length=40)
    name = models.CharField(max_length=100)
    narxi = models.CharField(max_length=50)
    soni = models.IntegerField()
    stol_soni = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)



