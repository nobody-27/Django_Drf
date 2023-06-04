from django.urls import path,include
from Nested_Serializer_Exmp.views import ProfileViewset
from rest_framework.routers import DefaultRouter

nested = DefaultRouter()
nested.register('profile',ProfileViewset)

urlpatterns = [
    path('', include(nested.urls)),
]