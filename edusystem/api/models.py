from django.contrib.auth.models import User
from django.db import models

# Institution Model
class Institution(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    domain = models.CharField(max_length=255, unique=True)  # Added domain
    config = models.JSONField(default=dict)  # Added config (JSON field)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# Course Model
class Course(models.Model):
    institution = models.ForeignKey(Institution, related_name="courses", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    max_students = models.PositiveIntegerField(default=0)  # Added max_students
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

# Student Model
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='students', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Enrollment Model (Many-to-many relationship between students and courses)
class Enrollment(models.Model):
    student = models.ForeignKey(Student, related_name="enrollments", on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('enrolled', 'Enrolled'), ('completed', 'Completed')])  # Added status
    active = models.BooleanField(default=True)  # Optional: track if enrollment is active

    def __str__(self):
        return f"{self.student} - {self.course}"

# Analytics Model (Basic analytics like enrollment count per course)
class Analytics(models.Model):
    course = models.OneToOneField(Course, related_name="analytics", on_delete=models.CASCADE)
    total_enrollments = models.PositiveIntegerField(default=0)  # Ensuring positive numbers
    completed_courses = models.PositiveIntegerField(default=0)  # Ensuring positive numbers
    average_grade = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Added average grade (positive decimal)
    completion_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Added completion rate (percentage)
    active_students = models.PositiveIntegerField(default=0)  # Added active students

    def __str__(self):
        return f"Analytics for {self.course}"
    
    

# Define the roles as a tuple
ROLES = (
    ('admin', 'Admin'),
    ('student', 'Student'),
    ('instructor', 'Instructor'),
)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLES, default='student')

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"    