from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('champions/<str:name>/', views.detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('champions/<str:name>/builds/create/', views.BuildCreate.as_view(), name='build_create'),
]