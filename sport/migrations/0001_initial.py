# Generated by Django 4.2 on 2023-04-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, verbose_name='Телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('comment', models.CharField(max_length=255, verbose_name='Коментар')),
                ('is_dusty', models.BooleanField(verbose_name='Чи прийнято')),
                ('season_ticket_id', models.IntegerField(verbose_name='Id абонемента')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Час оновлення')),
            ],
            options={
                'verbose_name': 'Замовлення',
                'verbose_name_plural': 'Замовлення',
                'ordering': ['phone', 'email', 'is_dusty', 'time_create', 'time_update'],
            },
        ),
        migrations.CreateModel(
            name='SeasonTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('description', models.TextField(verbose_name='Опис')),
                ('price', models.FloatField(verbose_name='Ціна')),
                ('discount', models.FloatField(verbose_name='Знижка')),
                ('share', models.CharField(blank=True, max_length=255, null=True, verbose_name='Акція')),
                ('is_display', models.BooleanField(verbose_name='Чи показувати')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Час створення')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Час оновлення')),
            ],
            options={
                'verbose_name': 'Абонемент',
                'verbose_name_plural': 'Абонементи',
                'ordering': ['title', 'price', 'discount', 'is_display', 'time_create', 'time_update'],
            },
        ),
    ]