# Generated by Django 4.0.2 on 2022-02-10 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_per_grup'),
    ]

    operations = [
        migrations.AddField(
            model_name='gab',
            name='grup',
            field=models.CharField(default='0101', max_length=200),
            preserve_default=False,
        ),
    ]
