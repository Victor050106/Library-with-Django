# Generated by Django 4.2.1 on 2023-06-22 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_author_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(help_text='Enter date of birth of Author'),
        ),
    ]