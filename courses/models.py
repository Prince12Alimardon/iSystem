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
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

