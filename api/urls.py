from django.urls import path
from . import views
app_name= 'api'

urlpatterns=[

path('api/', views.UserApi.as_view(), name='api')

]
