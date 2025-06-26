from django.contrib import admin
from django.urls import path, include  # <- Asegurate de importar 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),

]


