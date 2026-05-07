from django.contrib import admin
from django.urls import path
from test_app.views import greetings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', greetings)
]
