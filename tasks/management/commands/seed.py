# tasks/management/commands/seed.py
from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import timedelta
from django.utils import timezone

from tasks.models import Task, SubTask, Status, Category

class Command(BaseCommand):
    help = "Заполняет базу тестовыми данными (Tasks, SubTasks, Categories) через faker"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # создаём статусы
        statuses = ["To Do", "In Progress", "Done"]
        status_objs = {}
        for name in statuses:
            status, _ = Status.objects.get_or_create(name=name)
            status_objs[name] = status

        # создаём категории
        categories = []
        for _ in range(5):
            cat = Category.objects.create(
                name=fake.word().capitalize(),
            )
            categories.append(cat)

        # создаём задачи
        tasks = []
        for _ in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.text(),
                status=random.choice(list(status_objs.values())),
                deadline=timezone.now() + timedelta(days=random.randint(1, 30)),
                category=random.choice(categories),
            )
            tasks.append(task)

        # создаём подзадачи
        for task in tasks:
            for _ in range(random.randint(2, 5)):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=2),
                    description=fake.text(),
                    status=random.choice(list(status_objs.values())),
                    deadline=timezone.now() + timedelta(days=random.randint(1, 30)),
                    task=task,
                )

        self.stdout.write(self.style.SUCCESS("База успешно заполнена тестовыми данными!"))
