from django.db import models


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tags", blank=True)

    class Meta:
        ordering = ["-completed", "-created_at",]


class Tags(models.Model):
    name = models.CharField(max_length=255)
