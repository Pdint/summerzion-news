# Generated by Django 4.2.7 on 2023-12-10 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawledData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
