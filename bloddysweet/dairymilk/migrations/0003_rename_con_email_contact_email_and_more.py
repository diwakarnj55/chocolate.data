# Generated by Django 5.0.6 on 2024-06-02 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dairymilk', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='con_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='con_message',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='con_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='con_phone',
            new_name='phone',
        ),
    ]
