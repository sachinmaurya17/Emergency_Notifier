from django.urls import path
from FormInterface import views
urlpatterns = [
    path('signup',views.Signup),
    path('',views.Login)
]