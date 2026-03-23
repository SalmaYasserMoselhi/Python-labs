from django.shortcuts import redirect, render
from .models import Student

# Create your views here.

def home(request):
    return render(request, "home.html")

def students(request):
    if request.method == "GET":
        students = Student.objects.all()
        return render(request, "students.html", {"students": students})

    elif request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        image = request.FILES.get("image")
        Student.objects.create(name=name, age=age, email=email, image=image)
        students = Student.objects.all()
        return render(request, "students.html", {"students": students, "msg": "Student created successfully!"})

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("students")
