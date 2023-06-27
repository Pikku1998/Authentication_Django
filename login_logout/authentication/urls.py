from django.urls import path
from . views import register, sign_in, home, sign_out

urlpatterns = [
    path('register', register, name='register'),
    path('', sign_in, name='sign_in'),
    path('home', home, name = 'home'),
    path('signout', sign_out, name='sign_out'),
]
