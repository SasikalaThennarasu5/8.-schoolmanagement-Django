from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(blank=True)
    subject = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=150)
    code = models.CharField(max_length=20, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return self.title

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    dob = models.DateField(null=True, blank=True)
    roll_no = models.CharField(max_length=30, unique=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    photo = models.ImageField(upload_to='students/', null=True, blank=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.roll_no})"

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    relation = models.CharField(max_length=50, default='Parent')
    def __str__(self):
        return f"{self.user.username} - {self.student}"

class Exam(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.course}"

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)
    def __str__(self):
        return f"{self.student} | {self.exam} : {self.marks_obtained}/{self.max_marks}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.student} - {self.date} - {'P' if self.present else 'A'}"
