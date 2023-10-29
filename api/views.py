from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserDetails
from .serializers import UserDetailsSerializer
from rest_framework_swagger import renderers
from rest_framework.schemas import SchemaGenerator
from rest_framework.permissions import AllowAny

class UserDetailsGetView(APIView):
    serializer_class = UserDetailsSerializer
    def post(self,request):
        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Created Successfully'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        data_obj = UserDetails.objects.all()
        serializer = UserDetailsSerializer(data_obj,many=True)
        json_data = {
            'data':serializer.data,
            'message':'Data Fetched Successfully'
        }
        return Response(json_data,status=status.HTTP_200_OK)

class UserDetailsView(APIView):
    serializer_class = UserDetailsSerializer
    def get(self,request,pk):
        try:
            data_obj = UserDetails.objects.get(id = pk)
        except UserDetails.DoesNotExist:
            return Response({'error': 'UserDetails not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserDetailsSerializer(data_obj)
        json_data = {
            'data':serializer.data,
            'message':'Data Fetched Successfully'
        }
        return Response(json_data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            data_obj = UserDetails.objects.get(id = pk)
        except UserDetails.DoesNotExist:
            return Response({'error': 'UserDetails not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserDetailsSerializer(data_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            json_data = {
                'data':serializer.data,
                'message':'Data Updated Successfully'
            }
            return Response(json_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        try:
            data_obj = UserDetails.objects.get(id = pk)
        except UserDetails.DoesNotExist:
            return Response({'error': 'UserDetails not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserDetailsSerializer(data_obj,data=request.data,partial= True)
        if serializer.is_valid():
            serializer.save()
            json_data = {
                'data':serializer.data,
                'message':'Data Partially Updated Successfully'
            }
            return Response(json_data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            data_obj = UserDetails.objects.get(id=pk)
        except UserDetails.DoesNotExist:
            return Response({'error': 'UserDetails not found'}, status=status.HTTP_404_NOT_FOUND)
        data_obj.delete() 
        return Response({'message': 'User Details Deleted Successfully'})