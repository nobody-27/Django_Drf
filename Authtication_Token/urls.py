from django.contrib import admin
from django.urls import path,include
from Authtication_Token import views
from rest_framework.routers import DefaultRouter

#createing Router Object
router = DefaultRouter()

#Register
router.register('token_for_user',views.TokenModelViewSet,basename="token_for_user"),

urlpatterns = [
    path('',include(router.urls)),
    
    
]