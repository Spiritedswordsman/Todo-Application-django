from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ]
    )
    deadline = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
