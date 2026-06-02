from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from django.db.models import Count, Q
from .models import Task
from .serializers import TaskSerializer

def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, Ruslan!')

class TaskCreateView(APIView):
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskListView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

class TaskDetailView(APIView):
    def get(self, request, pk):
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class TaskStatsView(APIView):
    def get(self, request):
        stats = Task.objects.aggregate(
            total=Count('id'),
            new=Count('id', filter=Q(status='new')),
            in_progress=Count('id', filter=Q(status='in_progress')),
            pending=Count('id', filter=Q(status='pending')),
            blocked=Count('id', filter=Q(status='blocked')),
            done=Count('id', filter=Q(status='done')),
            overdue=Count('id', filter=Q(deadline__lt=timezone.now()) & ~Q(status='done')),
        )
        return Response(stats)



