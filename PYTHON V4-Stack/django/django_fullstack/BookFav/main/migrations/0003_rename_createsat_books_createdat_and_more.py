# Generated by Django 4.0.5 on 2022-06-24 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_books_uploaded_by_remove_books_userswholike'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='createsAt',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='createsAt',
            new_name='createdAt',
        ),
    ]
