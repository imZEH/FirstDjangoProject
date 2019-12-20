from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=50)
    todos = models.ManyToManyField(Todo)

    def __str__(self):
        return self.name