from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('rugby/', views.lista_rugby, name='lista_rugby'),
]

