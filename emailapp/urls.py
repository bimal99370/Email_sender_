from django.urls import path
from emailapp import views

urlpatterns = [
    path('', views.send_mail, name="contact")
]