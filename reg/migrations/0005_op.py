# Generated by Django 4.0.2 on 2022-02-14 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0004_gab_grup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Op',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('eq', models.CharField(max_length=4)),
            ],
        ),
    ]
