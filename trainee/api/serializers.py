from rest_framework import serializers
from trainee.models import Trainee
from course.models import Course

class TraineeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100, allow_null=False, allow_blank=False)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=20)
    age = serializers.IntegerField()
    image = serializers.ImageField(allow_null=True, required=False)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    def create(self, validated_data):
        return Trainee.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # Update the instance fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance