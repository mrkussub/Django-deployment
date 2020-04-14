# Generated by Django 3.0.5 on 2020-04-09 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=264, unique=True)),
                ('Email', models.CharField(max_length=264, unique=True)),
            ],
        ),
    ]
