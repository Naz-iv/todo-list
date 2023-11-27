
from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from todo.models import Tag, Task


class TestTodoModels(TestCase):
    def test_tag_str_method(self):
        tag = Tag.objects.create(name="Test Tag")
        self.assertEqual(str(tag), "Test Tag")

    def test_task_ordering(self):
        task1 = Task.objects.create(
            content="Test Task 1",
            completed=True,
            created_at=datetime(2020, 1, 1, 22, 10)
        )
        task2 = Task.objects.create(
            content="Test Task 2",
            completed=False,
            created_at=datetime(2020, 1, 1, 22, 10)
        )
        task3 = Task.objects.create(
            content="Test Task 3",
            completed=True,
            created_at=datetime(2022, 1, 1, 22, 10)
        )
        task4 = Task.objects.create(
            content="Test Task 4",
            completed=False,
            created_at=datetime(2022, 1, 1, 22, 10)
        )
        tasks = list(Task.objects.all())
        expected = [task4, task2, task3, task1]
        self.assertEqual(tasks, expected)


class TestTodoViews(TestCase):
    def test_toggle_completed(self):
        task1 = Task.objects.create(
            id=1,
            content="Test Task 1",
            completed=True,
            created_at=datetime.now()
        )
        response = self.client.get(reverse("todo:toggle-complete", kwargs={"pk": task1.id}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Task.objects.get(id=task1.id).completed)
