from rest_framework import viewsets
from .serializers import TraineeSerializer
from trainee.models import Trainee
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class TraineeViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Trainee.objects.select_related('course').all()
        serializer=TraineeSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk):
        queryset=Trainee.objects.select_related('course').all()
        trainee=get_object_or_404(queryset,pk=pk)
        serializer=TraineeSerializer(trainee)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        trainee=get_object_or_404(Trainee,pk=pk)
        serializer=TraineeSerializer(instance=trainee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        serializer = TraineeSerializer(instance=trainee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        trainee = get_object_or_404(Trainee, pk=pk)
        trainee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)