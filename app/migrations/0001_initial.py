# Generated by Django 5.1.1 on 2024-09-09 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('mail', models.EmailField(max_length=250)),
                ('password', models.TextField(max_length=200)),
            ],
        ),
    ]
