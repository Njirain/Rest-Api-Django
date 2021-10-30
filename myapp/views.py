from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# for requesting objects
from django.shortcuts import get_object_or_404

# for normal views to return Api data
from rest_framework.views import APIView

# get back status
from rest_framework.response import Response

# sending back status
from rest_framework import status

# name of the model
from .models import Employee

# name of the serializer
from .serializers import EmployeeSerializer


# create a class that inherits the APiView
class EmployeeList(APIView):
    def get(self, request):
        # create a variable that stores all objects
        var1 = Employee.objects.all()
        serializer = EmployeeSerializer(var1, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
def functionindex(request):
    return HttpResponse('hello django..')
