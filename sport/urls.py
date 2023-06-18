from django.urls import path
from .views import *

urlpatterns = [
    path('',Index.as_view(),name='home'),
    path('about/',About.as_view(),name='about'),
    path('pricing/',Pricing.as_view(),name='pricing'),

    path('add-order/<int:season_ticket_id>/',add_order,name='form')
]