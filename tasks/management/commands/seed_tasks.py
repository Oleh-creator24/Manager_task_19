from django.core.management.base import BaseCommand
from faker import Faker
import random
from tasks.models import Task, SubTask, Status

class Command(BaseCommand):
    help = "Generate fake tasks and subtasks for testing"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # создаём статусы, если их нет
        statuses = ["To Do", "In Progress", "Done"]
        status_objs = {}
        for s in statuses:
            obj, _ = Status.objects.get_or_create(name=s)
            status_objs[s] = obj

        # создаём 20 задач
        for i in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text(),
                status=random.choice(list(status_objs.values())),
                deadline=fake.future_datetime(end_date="+30d"),
            )

            # для каждой задачи создаём 2–5 подзадач
            for j in range(random.randint(2, 5)):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=4),
                    description=fake.text(),
                    status=random.choice(list(status_objs.values())),
                    deadline=fake.future_datetime(end_date="+15d"),
                    task=task,
                )

        self.stdout.write(self.style.SUCCESS("✅ 20 tasks with subtasks created!"))
