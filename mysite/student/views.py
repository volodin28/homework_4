from random import randrange

from django.http import HttpResponse
from faker import Faker

from .models import Student

faker = Faker()


def generate_student(request):
    student = Student.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), age=randrange(100))
    return HttpResponse(f"""
            <p>A new student added: {student.first_name} {student.last_name} {student.age} years old<p>
        """)


def generate_students(request):
    try:
        count = int(request.GET['count'])
        if count > 100:
            return HttpResponse(f"The request is too large")
        elif count <= 0:
            return HttpResponse(f"The request is not correct")
        else:
            for _ in range(int(count)):
                Student.objects.create(first_name=faker.first_name(), last_name=faker.last_name(), age=randrange(100))
            return HttpResponse(f"""
                    <p>{count} new students added. Total number of students = {Student.objects.count()}<p>
            """)
    except ValueError:
        return HttpResponse(f"The request is wrong")
