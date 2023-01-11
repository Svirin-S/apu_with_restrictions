from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from advertisements.views import AdvModelViewSet

r = DefaultRouter()
r.register('api', AdvModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
] + r.urls
