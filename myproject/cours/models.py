from django.db import models

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    schedule = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class StudentCourse(models.Model):
    student_id = models.IntegerField()  
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')

    def __str__(self):
        return f"Student {self.student_id} in {self.course.name}"