# Generated by Django 3.1.1 on 2021-02-23 09:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Category')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='category/%Y/%m/%d/', verbose_name='Category Image')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_file', models.FileField(null=True, upload_to='3D_File/%Y/%m/%d/', verbose_name='Model File')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='product/%Y/%m/%d/', verbose_name='Image')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='model-video/%d/%m/%Y/', verbose_name='Video/Gif')),
                ('video_link', models.URLField(blank=True, null=True, verbose_name='YouTube Video Link')),
                ('caption', models.CharField(blank=True, max_length=300, null=True, verbose_name='Caption')),
                ('name', models.CharField(max_length=300, verbose_name='Name')),
                ('slug', models.SlugField(max_length=320)),
                ('short_info', models.CharField(default='3D model', max_length=500, verbose_name='Short Info')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, default=100, max_digits=10, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)], verbose_name='Price')),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)], verbose_name='Discount')),
                ('paid', models.BooleanField(default=True, verbose_name='Paid')),
                ('free', models.BooleanField(default=False, verbose_name='Free')),
                ('downloaded', models.IntegerField(default=0, verbose_name='Downloaded')),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='product.category', verbose_name='Category')),
            ],
            options={
                'verbose_name': '3D Model',
                'verbose_name_plural': '3D Models',
                'ordering': ['name', 'published_at', 'updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='product-images/%Y/%m/%d/', verbose_name='Image')),
                ('caption', models.CharField(blank=True, max_length=300, null=True, verbose_name='Caption:')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='product.product', verbose_name='3D Model')),
            ],
            options={
                'verbose_name_plural': "Models' Images",
            },
        ),
    ]
