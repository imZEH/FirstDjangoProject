import graphene
from graphene_django import DjangoObjectType
from .models import Task, Todo, Person


class TaskType(DjangoObjectType):
    class Meta:
        model = Task


class PersonType(DjangoObjectType):
    class Meta:
        model = Person


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo


class Query(graphene.ObjectType):
    all_task = graphene.List(TaskType)
    all_todo = graphene.List(TodoType)
    all_person = graphene.List(PersonType)

    @staticmethod
    def resolve_all_task(self, info, **kwargs):
        return Task.objects.all()

    @staticmethod
    def resolve_all_todo(self, info, **kwargs):
        return Todo.objects.all()

    @staticmethod
    def resolve_all_person(self, info, **kwargs):
        return Person.objects.all()



