# Generated by Django 3.2.8 on 2021-11-01 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(choices=[('3', 'bepul'), ('1', 'yangi'), ('2', 'ishlatilgan')], default='1', max_length=10),
        ),
    ]
