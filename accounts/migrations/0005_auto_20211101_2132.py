# Generated by Django 3.2.8 on 2021-11-01 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_genders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone_number', models.PositiveIntegerField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='genders',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], default='m', max_length=10),
        ),
    ]