from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserDetails
from .serializers import UserDetailsSerializer
from rest_framework_swagger import renderers
from rest_framework.schemas import SchemaGenerator
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import NotFound

class UserDetailsGetView(APIView):
    serializer_class = UserDetailsSerializer

    def post(self, request):
        try:
            serializer = UserDetailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Data Created Successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request):
        try:
            data_obj = UserDetails.objects.all()
            serializer = UserDetailsSerializer(data_obj, many=True)
            json_data = {
                'data': serializer.data,
                'message': 'Data Fetched Successfully'
            }
            return Response(json_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserDetailsView(APIView):
    serializer_class = UserDetailsSerializer

    def handle_user_details_not_found(self):
        return Response({'error': 'UserDetails not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        try:
            data_obj = UserDetails.objects.get(id=pk)
            serializer = UserDetailsSerializer(data_obj)
            json_data = {
                'data': serializer.data,
                'message': 'Data Fetched Successfully'
            }
            return Response(json_data, status=status.HTTP_200_OK)
        except UserDetails.DoesNotExist:
            return self.handle_user_details_not_found()

    def put(self, request, pk):
        try:
            data_obj = UserDetails.objects.get(id=pk)
            serializer = UserDetailsSerializer(data_obj, data=request.data)
            if serializer.is_valid():
                serializer.save()
                json_data = {
                    'data': serializer.data,
                    'message': 'Data Updated Successfully'
                }
                return Response(json_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserDetails.DoesNotExist:
            return self.handle_user_details_not_found()

    def patch(self, request, pk):
        try:
            data_obj = UserDetails.objects.get(id=pk)
            serializer = UserDetailsSerializer(data_obj, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                json_data = {
                    'data': serializer.data,
                    'message': 'Data Partially Updated Successfully'
                }
                return Response(json_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserDetails.DoesNotExist:
            return self.handle_user_details_not_found()

    def delete(self, request, pk):
        try:
            data_obj = UserDetails.objects.get(id=pk)
            data_obj.delete()
            return Response({'message': 'User Details Deleted Successfully'})
        except UserDetails.DoesNotExist:
            return self.handle_user_details_not_found()