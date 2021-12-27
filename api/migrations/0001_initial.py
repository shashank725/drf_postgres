# Generated by Django 4.0 on 2021-12-27 09:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assigment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('descritpion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]