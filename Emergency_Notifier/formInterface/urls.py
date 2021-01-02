from django.urls import path
from formInterface import views

urlpatterns = [
    path('',views.Login),
    path('signup',views.Signup)
]