# Generated by Django 2.2.6 on 2020-06-12 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0007_auto_20200612_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='friend',
        ),
        migrations.AddField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Friend'),
        ),
    ]
