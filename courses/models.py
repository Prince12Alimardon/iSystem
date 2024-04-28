from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=212)
    course_month = models.IntegerField(default=3)
    course_day = models.IntegerField(default=3)
    price = models.IntegerField(default=0)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    message = models.TextField()
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Isystem_in_numbers(models.Model):
    course_count = models.CharField(max_length=212, default=0)
    teachers_count = models.CharField(max_length=212, default=0)
    projects_count = models.CharField(max_length=212, default=0)

    def __str__(self):
        return self.course_count
