from django.db import models
from account.models import Account


class CourseCategories(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('course', 'category')


class Category(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, through=CourseCategories, related_name='course_categories')
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=600, blank=True, null=True)
    prerequisites = models.ManyToManyField('Course', symmetrical=False, blank=True)

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='enrolled_account')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('account', 'course')
