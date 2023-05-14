from django.shortcuts import render
from .models import Student
def list_view(request):
  # dictionary for initial data with
  # field names as keys
  context ={}
  # add the dictionary during initialization
  context["dataset"] = Student.objects.all()
  return render(request, "list_view.html", context)