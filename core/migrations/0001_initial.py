# Generated by Django 4.1.3 on 2022-11-11 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=16)),
                ('familiya', models.CharField(max_length=16)),
            ],
        ),
    ]
