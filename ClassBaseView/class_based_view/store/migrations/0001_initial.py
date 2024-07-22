# Generated by Django 4.1 on 2024-07-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField()),
                ('update_at', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
