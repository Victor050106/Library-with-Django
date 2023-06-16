# Generated by Django 4.2.2 on 2023-06-16 00:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='name',
            new_name='fname',
        ),
        migrations.RemoveField(
            model_name='book',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='lname',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.author'),
        ),
    ]
