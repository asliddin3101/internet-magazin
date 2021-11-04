# Generated by Django 3.2.8 on 2021-11-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_genders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='genders',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=10),
        ),
    ]