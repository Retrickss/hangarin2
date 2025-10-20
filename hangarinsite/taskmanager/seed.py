from faker import Faker
from django.utils import timezone
import random

from taskmanager.models import Category, Priority, Task, SubTask, Note

fake = Faker()

# ✅ Populate Category and Priority (if not already added)
def create_static_data():
    categories = ["Work", "School", "Personal", "Finance", "Projects"]
    priorities = ["High", "Medium", "Low", "Critical", "Optional"]

    for name in categories:
        Category.objects.get_or_create(name=name)

    for name in priorities:
        Priority.objects.get_or_create(name=name)


# ✅ Populate fake Tasks, SubTasks, and Notes
def create_fake_data(num_tasks=10):
    categories = list(Category.objects.all())
    priorities = list(Priority.objects.all())

    for _ in range(num_tasks):
        task = Task.objects.create(
            title=fake.sentence(nb_words=5),
            description=fake.paragraph(nb_sentences=3),
            status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
            category=random.choice(categories),
            priority=random.choice(priorities),
            deadline=timezone.make_aware(fake.date_time_this_month())
        )

        # Add SubTasks
        for _ in range(random.randint(1, 3)):
            SubTask.objects.create(
                title=fake.sentence(nb_words=4),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                parent_task=task
            )

        # Add Notes
        for _ in range(random.randint(1, 2)):
            Note.objects.create(
                task=task,
                content=fake.paragraph(nb_sentences=2)
            )

    print("✅ Fake data successfully added!")


def run():
    create_static_data()
    create_fake_data()
