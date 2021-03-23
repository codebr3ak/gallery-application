# Generated by Django 3.1.7 on 2021-03-23 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='image_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.category'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='album.location'),
        ),
    ]
