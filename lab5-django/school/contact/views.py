from django.shortcuts import render
from .models import Feedback

# Create your views here.

def contact(request):
    if request.method == "GET":
        return render(request, "contact.html")

    elif request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")
        Feedback.objects.create(email=email, message=message)
        return render(request, "contact.html", {"msg": "Feedback sent successfully!"})
