"""  /question_creation/models.py
    Data models for the mathstack app.
"""

from django.conf import settings
from django.db import models
from django.urls import reverse
from mathstack.models import Student

import uuid

class ShortAnswerQuestion(models.Model):
    """ A `ShortAnswerQuestion` is a `Student`-created question with an integer answer.
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=150)
    right_answer = models.IntegerField()

    def __str__(self):
        return "{} created new question: {}".format(self.student.username, self.question)
