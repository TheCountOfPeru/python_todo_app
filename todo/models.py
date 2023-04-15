from django.db import models
import datetime
from django.utils import timezone

class Todo(models.Model):
    todo_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    completion_status = models.BooleanField(default = False)
    def __str__(self):
        return self.todo_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
