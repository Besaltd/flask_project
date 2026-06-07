from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpRequest, HttpResponse
from django.utils import timezone
from django.db.models import Count, Q
from .models import Task, SubTask
from .serializers import TaskSerializer, SubTaskCreateSerializer

def greetings(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Hello, Ruslan!')

# class TaskCreateView(APIView):
#     def post(self, request):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# class TaskListView(APIView):
#     def get(self, request):
#         tasks = Task.objects.all()
#         day = request.GET.get('day')
#         if day:
#             tasks = Task.objects.filter(deadline__week_day=day)
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

# class TaskDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

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



# class SubTaskListCreateView(APIView):
#     def get(self, request):
#         subtasks = SubTask.objects.all().order_by('-created_at')
#         task_title = request.GET.get('task_title')
#         sub_status = request.GET.get('status')
#         if task_title:
#             subtasks = subtasks.filter(task__title=task_title)
#         if sub_status:
#             subtasks = subtasks.filter(status=sub_status)
#
#         paginator = Paginator(subtasks, 5)
#         page = paginator.get_page(request.GET.get('page', 1))
#         serializer = SubTaskCreateSerializer(page.object_list, many=True)
#
#         return Response({
#             'count': paginator.count,
#             'total_pages': paginator.num_pages,
#             'results': serializer.data
#         })

    # def post(self, request):
    #     serializer = SubTaskCreateSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class SubTaskDetailUpdateDeleteView(APIView):
#     def get_object(self, pk):
#         try:
#             return SubTask.objects.get(pk=pk)
#         except SubTask.DoesNotExist:
#             return None
#
#     def get(self, request, pk):
#         subtask = self.get_object(pk)
#         if not subtask:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = SubTaskCreateSerializer(subtask)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         subtask = self.get_object(pk)
#         if not subtask:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = SubTaskCreateSerializer(subtask, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         subtask = self.get_object(pk)
#         if not subtask:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         subtask.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']


class SubTaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
