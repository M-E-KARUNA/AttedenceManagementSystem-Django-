# Generated by Django 4.1.7 on 2023-03-13 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Stat', '0007_thirdcse_delete_cse_delete_ece_delete_eee_delete_fdt_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=10)),
                ('oesubject', models.CharField(max_length=20)),
                ('oeat', models.CharField(max_length=120)),
            ],
        ),
    ]
