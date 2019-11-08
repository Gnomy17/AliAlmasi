from django.contrib.auth.models import User
from django.db import models

# Create your models here.
DAYS_OF_WEEK = (
    (0, 'Saturday'),
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Thursday'),
)


class Course(models.Model):
    department = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    course_number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    exam_date = models.DateField()
    first_day = models.IntegerField(choices=DAYS_OF_WEEK)
    second_day = models.IntegerField(choices=DAYS_OF_WEEK, null=True, blank=True)

class CourseUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)