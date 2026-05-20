from rest_framework import viewsets
from .serializers import CourseSerializer
from course.models import Course
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class CourseViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset=Course.objects.all()
        serializer=CourseSerializer(queryset,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self,request,pk):
        queryset=Course.objects.all()
        course=get_object_or_404(queryset,pk=pk)
        serializer=CourseSerializer(course)
        return Response(data=serializer.data,status=status.HTTP_200_OK)
    
    def update(self, request, pk):
        course=get_object_or_404(Course,pk=pk)
        serializer=CourseSerializer(instance=course,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(instance=course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk):
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)