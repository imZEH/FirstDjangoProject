from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task, Todo, Person
from .serializers import TaskSerializer, TodoSerializer, PersonSerializer
# Create your views here.

class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TodoView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer