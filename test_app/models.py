from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        PENDING = "pending", "Pending"
        BLOCKED = "blocked", "Blocked"
        DONE = "done", "Done"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, related_name="tasks")
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("title", "created_at")

    def __str__(self):
        return self.title


class SubTask(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_PROGRESS = "in_progress", "In progress"
        PENDING = "pending", "Pending"
        BLOCKED = "blocked", "Blocked"
        DONE = "done", "Done"

    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW
    )
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} → {self.title}"
