from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from userDemo import views as v 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userDemo/', v.register, name='register'),
    path('', include('system.urls'))
]


