# Generated by Django 4.1.6 on 2023-02-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_useraccount_name_alter_useraccount_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='username',
            field=models.CharField(db_index=True, max_length=25, unique=True),
        ),
    ]
