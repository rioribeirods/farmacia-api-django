from django.contrib import admin
from django.urls import path, include
from farmacia.views import ClientesViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'clientes', ClientesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
