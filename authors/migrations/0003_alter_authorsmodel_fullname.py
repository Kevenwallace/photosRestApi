# Generated by Django 4.1.5 on 2023-02-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_authorsmodel_fullname_alter_authorsmodel_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authorsmodel',
            name='fullname',
            field=models.CharField(max_length=250),
        ),
    ]
