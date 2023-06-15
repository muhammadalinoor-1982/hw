
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('detailsProfile/<int:id>/', detailsProfile, name='detailsProfile'),
    path('update/<int:id>/', update, name='update')
]
