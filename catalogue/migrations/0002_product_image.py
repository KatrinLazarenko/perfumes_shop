# Generated by Django 4.2.1 on 2023-05-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='catalogue/images/'),
            preserve_default=False,
        ),
    ]