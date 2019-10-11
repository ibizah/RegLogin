from django.urls import path
from . import views
app_name= 'demoapp'

urlpatterns=[

path('', views.home, name='home'),
path('form/', views.form, name='form'),
path('employee/', views.Empview.as_view()),
path('register/', views.register, name='register'),
path('reg/', views.reg, name= 'reg'),
path('user_login/', views.user_login, name='user_login'),


]
