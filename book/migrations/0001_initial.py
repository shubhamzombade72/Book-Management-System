# Generated by Django 5.1 on 2024-10-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=255)),
                ('b_author', models.CharField(max_length=255)),
                ('b_prize', models.CharField(max_length=255)),
                ('b_category', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Book_table',
            },
        ),
    ]
