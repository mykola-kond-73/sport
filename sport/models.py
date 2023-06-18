from django.db import models
from django.urls import reverse

class SeasonTicket(models.Model):
    title=models.CharField(max_length=255,verbose_name="Назва")
    description=models.TextField(verbose_name="Опис")
    price=models.FloatField(verbose_name="Ціна")
    discount=models.FloatField(verbose_name="Знижка")
    share=models.CharField(max_length=255,null=True,blank=True,verbose_name="Акція")
    is_display=models.BooleanField(verbose_name="Чи показувати")

    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')
    time_update=models.DateTimeField(auto_now=True,verbose_name='Час оновлення')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="Абонемент"
        verbose_name_plural="Абонементи"
        ordering=['title','price','discount','is_display','time_create','time_update']

class Order(models.Model):
    phone=models.CharField(max_length=10,verbose_name="Phone")
    email=models.EmailField(verbose_name="E-mail")
    comment=models.CharField(blank=True,default="",max_length=255,verbose_name="Comment")
    is_dusty=models.BooleanField(default=False,verbose_name="Чи прийнято")
    season_ticket_id=models.IntegerField(blank=True,verbose_name='Id абонемента')

    time_create=models.DateTimeField(auto_now_add=True,verbose_name='Час створення')
    time_update=models.DateTimeField(auto_now=True,verbose_name='Час оновлення')

    def __str__(self):
        return self.id
    
    class Meta:
        verbose_name="Замовлення"
        verbose_name_plural="Замовлення"
        ordering=['phone','email','is_dusty','time_create','time_update']