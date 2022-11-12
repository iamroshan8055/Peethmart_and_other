from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.http import JsonResponse
from myapp.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission, User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

class UserDetail(APIView):
    """
    Post, Retrieve, update or delete a User instance.
    """
    # def get_object(self, request, format=None):
    #     try:
    #         par = User.objects.all()
    #         serializer = UserSerializer(par, many=True)
    #         return JsonResponse(serializer.data)
    #     except User.DoesNotExist:
    #         raise Http404

    # def get_all(request):
    #     par = User.objects.all()
    #     serializer = UserSerializer(par, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    # @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        data["password"] = make_password(data["password"])
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            par = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(par)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        try:
            par = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        serializer = UserSerializer(par, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
        except User.DoesNotExist:
            raise Http404
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginPage(APIView):

    def post(self, request):
        data = JSONParser().parse(request)
        user = User.objects.filter(username=data["username"])
        if user:
            v_pass = check_password(data["password"], user[0].password)
            if v_pass:
                error_msg = {'message':'You are logged in','success':True}
        
                return Response(error_msg,status=status.HTTP_202_ACCEPTED)
            else:
        
                error_msg = {'message':'Invalid Password','success':False}
        
                return Response(error_msg,status=status.HTTP_401_UNAUTHORIZED)

        error_msg = {'message':'Invalid Username','success':False}

        return Response(error_msg,status=status.HTTP_401_UNAUTHORIZED)
