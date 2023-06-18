# Generated by Django 4.2 on 2023-04-14 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0002_alter_order_is_dusty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.CharField(default='', max_length=255, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=10, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='order',
            name='season_ticket_id',
            field=models.IntegerField(blank=True, verbose_name='Id абонемента'),
        ),
    ]