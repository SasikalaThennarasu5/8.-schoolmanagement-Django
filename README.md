# School of Bright Futures
A starter Django project for a School/College Management System.

Features:
- Manage Students, Teachers, Courses, Exams.
- Attendance and Marks entry (via admin).
- Parent login to view student performance.

How to run (after extracting):
1. python -m venv venv
2. Activate venv
3. pip install django
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py createsuperuser
7. python manage.py runserver

Admin site is where you can add Teachers, Courses, Students, Exams, Marks, and Attendance.
Create a User and then create a Parent entry linking that User to a Student to enable parent-dashboard access.
