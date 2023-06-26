from django.urls import path
from . views import sign_in, register

urlpatterns = [
    path('', sign_in, name='sign_in'),
    path('register', register, name='register'),

]
