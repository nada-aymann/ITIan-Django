from rest_framework import serializers
from course.models import Course

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # Update the instance fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance