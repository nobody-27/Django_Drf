from django.contrib import admin
from django.urls import path,include
from Json_Web_Token import views
urlpatterns = [
    path('student/',views.Student_class.as_view(),name="student")
]
