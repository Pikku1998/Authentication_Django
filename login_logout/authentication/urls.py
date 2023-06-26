from django.urls import path
from . views import register, sign_in, sign_out

urlpatterns = [
    path('register', register, name='register'),
    path('', sign_in, name='sign_in'),
    path('signout', sign_out, name='sign_out'),
]
