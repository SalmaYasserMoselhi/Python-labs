from django.urls import path
from .views import home, students, student_delete

urlpatterns = [
    path("", home, name="home"),
    path("students/", students, name="students"),
    path("student_delete/<int:id>/", student_delete, name="student_delete"),
]
