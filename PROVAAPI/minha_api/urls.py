from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import GeneroViewSet
from core.views import FilmeViewSet

router = DefaultRouter()
router.register(r'generos', GeneroViewSet, basename='generos')
router.register(r'filmes', FilmeViewSet, basename='filme')

urlpatterns = [
    path('api/', include(router.urls)),
]