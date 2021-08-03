from django.db import models
from django.contrib.auth.models import User


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=100, null=True)
    mark = models.PositiveIntegerField(null=True)
    answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.question_text


class Quizzes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question)

    def __str__(self):
        return self.title


class Attempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.quiz.user.username + ' - ' + self.answer.answer_text
