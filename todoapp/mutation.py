import graphene
from .models import Task, Todo, Person
from .query import TodoType, PersonType


class TaskInput(graphene.InputObjectType):
    id = graphene.Int()


class TodoInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    task = graphene.Field(TaskInput)


class PersonTodoInput(graphene.InputObjectType):
    id = graphene.Int()


class PersonInput(graphene.InputObjectType):
    name = graphene.String()
    todos = graphene.Field(PersonTodoInput)


class CreateTask(graphene.Mutation):
    name = graphene.String()

    class Arguments:
        name = graphene.String()

    @staticmethod
    def mutate(self, info, name):
        task = Task(name=name)
        task.save()

        return CreateTask(
            name=task.name,
        )


class CreateTodo(graphene.Mutation):
    todo = graphene.Field(TodoType)

    class Arguments:
        todo_data = TodoInput(required=True)

    @staticmethod
    def mutate(self, info, todo_data):
        task = Task.objects.get(pk=todo_data.task.id)
        todo_data['task'] = task
        todo = Todo.objects.create(**todo_data)
        return CreateTodo(todo=todo)


class CreatePerson(graphene.Mutation):
    person = graphene.Field(PersonType)

    class Arguments:
        person_data = PersonInput(required=True)

    @staticmethod
    def mutate(self, info, person_data):
        todo = Todo.objects.get(pk=person_data.todos.id)
        person = Person.objects.create(name=person_data.name)
        person.save()
        person.todos.add(todo)
        return CreatePerson(person=person)


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    create_todo = CreateTodo.Field()
    create_person = CreatePerson.Field()
