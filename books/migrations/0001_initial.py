# Generated by Django 2.2.5 on 2020-12-15 16:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=40)),
                ('year', models.PositiveIntegerField(default=2020, help_text='Use the following format: <YYYY>', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2020)])),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_photos')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='categories.Category')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='people.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
