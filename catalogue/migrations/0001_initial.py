# Generated by Django 4.2.1 on 2023-05-10 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.CharField(max_length=13)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('size', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('unisex', 'unisex')], max_length=10)),
                ('type', models.CharField(choices=[('EDP', 'EDP'), ('EDT', 'EDT'), ('Cologne', 'Cologne'), ('Perfumes', 'Perfumes')], max_length=20)),
                ('image', models.ImageField(upload_to='catalogue/images/')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.brand')),
            ],
        ),
    ]
