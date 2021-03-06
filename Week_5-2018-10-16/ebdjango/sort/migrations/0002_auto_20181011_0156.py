# Generated by Django 2.0 on 2018-10-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sort', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='bookID',
        ),
        migrations.RemoveField(
            model_name='book',
            name='reviewsCount',
        ),
        migrations.AddField(
            model_name='book',
            name='genre_type',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='img_url',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='publish_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.FloatField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ratingsCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
