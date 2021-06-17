from django.db import models
from datetime import datetime
import random
from django.contrib.auth.models import User

# Create your models here.

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

# Create your models here.
class Category (models.Model):
    title =models.CharField(max_length=100)
    image=models.TextField(null=True)

    def __str__(self):
        return self.title
        
    def get_quiz(self):
        return self.quiz_set


class Quiz(models.Model):
    name = models.CharField(max_length=120, null=True)
    topic = models.CharField(max_length=120, null=True)
    number_of_questions = models.IntegerField(null=True)
    time = models.IntegerField(help_text="duration of the quiz in minutes", null=True)
    required_score_to_pass = models.IntegerField(help_text="required score in %", null=True)
    difficluty = models.CharField(max_length=6, choices=DIFF_CHOICES, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'

class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)

