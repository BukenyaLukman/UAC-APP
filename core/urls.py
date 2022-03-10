
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterViewSet
router = DefaultRouter()
router.register('register', RegisterViewSet, basename='register')

from .views import (
    home_view,
    register_view,
    login_view,
)

urlpatterns = [
    path('', home_view, name='home'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('api/', include(router.urls)),
]
