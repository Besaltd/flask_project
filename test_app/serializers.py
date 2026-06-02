from rest_framework import serializers
from .models import Task, SubTask, Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'deadline')

# Завдання 1
class SubTaskCreateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = SubTask
        fields = ('id', 'title', 'description', 'status', 'deadline', 'task', 'created_at')


# Завдання 2
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self, validated_data):
        if Category.objects.filter(name=validated_data['name']).exists():
            raise serializers.ValidationError({'name': 'Category with this name already exists.'})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if Category.objects.filter(name=validated_data['name']).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError({'name': 'Category with this name already exists.'})
        return super().update(instance, validated_data)


# Завдання 3
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = ('id', 'title', 'description', 'status', 'deadline', 'created_at')


class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'deadline', 'created_at', 'subtasks')


# Завдання 4
class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'status', 'deadline')

    def validate_deadline(self, value):
        if value and value < timezone.now():
            raise serializers.ValidationError('Deadline cannot be in the past.')
        return value