# Generated by Django 5.1.6 on 2025-02-19 10:10

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('izox', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Karzinka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=100)),
                ('narxi', models.CharField(max_length=50)),
                ('soni', models.IntegerField()),
                ('stol_soni', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=25)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('status_choise', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Savat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=100)),
                ('narxi', models.CharField(max_length=50)),
                ('soni', models.IntegerField()),
                ('stol_soni', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=35)),
                ('familya', models.CharField(max_length=35)),
                ('parol', models.CharField(max_length=50)),
                ('tel', models.PositiveBigIntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('izoh', models.TextField()),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.commentmodel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
                ('narxi', models.BigIntegerField()),
                ('rasmi', models.ImageField(upload_to='products/')),
                ('video', models.FileField(upload_to='products_videos/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mov', 'mkv'])])),
                ('maxsulotlar', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categoryfood')),
            ],
        ),
        migrations.AddField(
            model_name='commentmodel',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.foodpost'),
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('creat_time', models.DateTimeField(auto_now_add=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.foodpost')),
            ],
        ),
        migrations.CreateModel(
            name='TablesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raqam', models.BigIntegerField(unique=True)),
                ('nomi', models.CharField(max_length=25)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status_Choice', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('bandligi', models.BooleanField()),
                ('qr_code', models.ImageField(upload_to='QR_Code/')),
                ('xona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.room')),
            ],
        ),
    ]
