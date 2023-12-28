from django.db import models
from course.models import Course
from account.models import Account

class Choice(models.Model):
    question = models.ForeignKey('Quiz', on_delete=models.CASCADE, related_name='choices')
    content = models.CharField(max_length=1000, blank=False)
    correct = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.content


class Type(models.Model):
    name = models.CharField(max_length=250, blank=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    created = models.DateTimeField(auto_now=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    quiz = models.ForeignKey('Quiz', on_delete=models.SET_NULL, null=True, related_name='questions')
    #figure = models.ImageField(upload_to='', blank=True, null=True)
    text = models.CharField(max_length=1000, blank=False)

    def __str__(self):
        return self.text[:50]


class Quiz(models.Model):
    name = models.CharField(max_length=250)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now=True)
    time_limit = models.DurationField(null=True, blank=True)
    single_attempt = models.BooleanField(blank=False, default=True)
    pass_mark = models.SmallIntegerField(blank=True, default=50)

    def __str__(self):
        return self.name


class Answer(models.Model):
    created = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Result(models.Model):
    student = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='quiz_results')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.student.username}'s result for {self.quiz.name}"
