from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.http import JsonResponse
from . models import Parent
from myapp.serializers import ParentSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.

class ParentDetail(APIView):
    """
    Post, Retrieve, update or delete a parent instance.
    """
    # def get_object(self, request, format=None):
    #     try:
    #         par = Parent.objects.all()
    #         serializer = ParentSerializer(par, many=True)
    #         return JsonResponse(serializer.data)
    #     except Parent.DoesNotExist:
    #         raise Http404

    # def get_all(request):
    #     par = Parent.objects.all()
    #     serializer = ParentSerializer(par, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    # @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        print("----------------POST START----------------------")
        serializer = ParentSerializer(data=data)
        print("----------------serializer----------------------",serializer)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        try:
            par = Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404
        serializer = ParentSerializer(par)
        return JsonResponse(serializer.data)

    def put(self, request, pk):
        try:
            par = Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404
        serializer = ParentSerializer(par, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            parent = Parent.objects.get(pk=pk)
        except Parent.DoesNotExist:
            raise Http404
        parent.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
