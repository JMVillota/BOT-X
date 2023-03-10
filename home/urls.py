from django.urls import path
from .views import   login, logout, menu, terminos
urlpatterns = [
    path('', terminos, name='terminos'),
    path('login/', login, name='login'),
    path('menu/', menu, name='menu'),
    path('logout/', logout, name='logout'),



    #path('', homeIQ, name='homeIQ'),

]
