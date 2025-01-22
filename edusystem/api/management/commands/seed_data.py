# api/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from api.models import Institution, Course, Student, Enrollment, Analytic
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with 15 rows of data for each model'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Predefined list of realistic course names
        course_names = [
            "Introduction to Programming",
            "Data Science and Machine Learning",
            "Web Development with Django",
            "Advanced Python Programming",
            "Database Management Systems",
            "Introduction to Artificial Intelligence",
            "Software Engineering Principles",
            "Cybersecurity Fundamentals",
            "Cloud Computing Essentials",
            "Mobile App Development",
            "Computer Networks and Protocols",
            "Digital Marketing Strategies",
            "Project Management for Engineers",
            "Human-Computer Interaction",
            "Game Development with Unity"
        ]

        # Create 15 Institutions
        for i in range(15):
            institution = Institution.objects.create(
                name=fake.company(),
                address=fake.address(),
                domain=fake.domain_name() + str(i),  # Append index to ensure uniqueness
                config={"max_students": random.randint(50, 200)},
            )

            # Create 15 Courses for each Institution with realistic names
            for _ in range(15):
                course_name = random.choice(course_names)  # Select a random course name from the list
                course = Course.objects.create(
                    institution=institution,
                    name=course_name,
                    description=fake.text(),
                    max_students=random.randint(20, 100),
                )

                # Create Analytic only if it doesn't exist
                if not Analytic.objects.filter(course=course).exists():
                    Analytic.objects.create(
                        course=course,
                        total_enrollments=random.randint(10, 50),
                        completed_courses=random.randint(5, 50),
                        average_grade=random.uniform(50.0, 100.0),
                        completion_rate=random.uniform(50.0, 100.0),
                        active_students=random.randint(5, 40),
                    )

            # Create 15 Students
            for _ in range(15):
                student = Student.objects.create(
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                )

                # Create Enrollments for each Student in random Courses
                for course in Course.objects.all():
                    Enrollment.objects.create(
                        student=student,
                        course=course,
                        status=random.choice(['enrolled', 'completed']),
                        active=random.choice([True, False]),
                    )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with 15 rows for each model!'))
