# Generated by Django 3.2.4 on 2021-06-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210625_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(db_column='id', primary_key=True, serialize=False),
        ),
    ]
