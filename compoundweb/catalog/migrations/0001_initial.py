# Generated by Django 4.0.4 on 2022-05-17 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('smiles', models.CharField(max_length=50)),
                ('inchlkey', models.CharField(max_length=50)),
            ],
        ),
    ]
