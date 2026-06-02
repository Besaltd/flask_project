from django.contrib import admin
from .models import Task, SubTask, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1
    fields = ('title', 'status', 'deadline')
    show_change_link = True


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "short_title", "status", "deadline", "created_at")
    list_filter = ("status", "categories")
    search_fields = ("title", "description")
    filter_horizontal = ("categories",)
    inlines = [SubTaskInline]

    def short_title(self, obj):
        return obj.title[:10] + "..." if len(obj.title) > 10 else obj.title
    short_title.short_description = "Title"

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "task", "status", "deadline", "created_at")
    list_filter = ("status", "task")
    search_fields = ("title", "description")

    def mark_done(modeladmin, request, queryset):
        queryset.update(status=SubTask.Status.DONE)

    mark_done.short_description = "Mark selected as Done"

    actions = [mark_done]