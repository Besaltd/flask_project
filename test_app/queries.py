import os
import django
from datetime import timedelta
from django.utils import timezone

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoproject.settings")
django.setup()


from test_app.models import Task, SubTask



# CREATE
task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status=Task.Status.NEW,
    deadline=timezone.now() + timedelta(days=3)
)

sub1 = SubTask.objects.create(
    task=task,
    title="Gather information",
    description="Find necessary information for the presentation",
    status=SubTask.Status.NEW,
    deadline=timezone.now() + timedelta(days=2)
)

sub2 = SubTask.objects.create(
    task=task,
    title="Create slides",
    description="Create presentation slides",
    status=SubTask.Status.NEW,
    deadline=timezone.now() + timedelta(days=1)
)



# READ
new_tasks = Task.objects.filter(status=Task.Status.NEW)
print("Tasks with NEW status:", list(new_tasks))

expired_done_subtasks = SubTask.objects.filter(
    status=SubTask.Status.DONE,
    deadline__lt=timezone.now()
)
print("Expired DONE subtasks:", list(expired_done_subtasks))



# UPDATE
task.status = Task.Status.IN_PROGRESS
task.save()

sub1.deadline = timezone.now() - timedelta(days=2)
sub1.save()

sub2.description = "Create and format presentation slides"
sub2.save()



# DELETE
task.delete()
print("Task and its subtasks deleted.")






