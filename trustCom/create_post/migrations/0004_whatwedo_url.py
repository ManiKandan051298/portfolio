# Generated by Django 3.1.7 on 2021-05-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_post', '0003_auto_20210304_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='whatwedo',
            name='url',
            field=models.CharField(default='hello', max_length=200),
            preserve_default=False,
        ),
    ]