# Generated by Django 4.0.2 on 2022-02-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0005_op'),
    ]

    operations = [
        migrations.AddField(
            model_name='gab',
            name='defect_code',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gab',
            name='lider_assy',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gab',
            name='lider_sub',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gab',
            name='masa',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
