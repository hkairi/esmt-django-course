# Generated by Django 2.0.1 on 2018-02-06 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annonce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('description', models.TextField(default='DESC', max_length=200)),
                ('publiee', models.BooleanField(default=False)),
            ],
        ),
    ]
