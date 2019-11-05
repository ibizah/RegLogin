from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import UserSerializer

# Create your views here.
class UserApi(APIView):
    def get(self,request):
        user= UserModel.objects.all()
        serializer= UserSerializer(user, many=Tue)
        return Response(serializer.data)
