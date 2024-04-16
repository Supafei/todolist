from rest_framework import serializers
from tasks.models import Task

class TaskSerializer (serializers.ModelSerializer):
    class Meta:
        model = Task
        fields= ['id', 'title', 'description', 'status']
    def create(self, validated_data):
        """
        Create and return a new `Task` instance, given the validated data.
        """
        return Task.objects.create(**validated_data)
    
    def update (self, instance, validated_data):
        """
        Update and return a new `Snippet` instance, given the validated data.
        """
        instance.title= validated_data.get('title', instance.title)
        instance.description=validated_data.get('description', instance.description)
        instance.status=validated_data.get('status', instance.status)
        instance.save()
        return instance
    

    
