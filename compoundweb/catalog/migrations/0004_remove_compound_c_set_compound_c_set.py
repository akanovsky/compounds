# Generated by Django 4.0.4 on 2022-05-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_library_remove_compound_c_set_compound_c_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compound',
            name='c_set',
        ),
        migrations.AddField(
            model_name='compound',
            name='c_set',
            field=models.CharField(default='N', max_length=30),
        ),
    ]