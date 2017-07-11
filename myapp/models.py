from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthdate = models.DateField()
    #3c - Comment the 'age' field in Author
    #age = models.IntegerField()
    #3b
    city = models.CharField(max_length=100, blank=True, null=True)
    newField = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        if (self.city != None or self.city == ''):
            return str(self.firstName + ' ' + self.lastName + ' born ' + str(self.birthdate) + ' lives in ' + self.city)
        else:
            return str(self.firstName + ' ' + self.lastName + ' born ' + str(self.birthdate))

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    in_stock = models.BooleanField(default=True)
    #3a
    numpages = models.IntegerField(null=True)
    def __str__(self):
        if (self.in_stock == True):
            return str(self.title + ' by ' + self.author.firstName + ' ' + self.author.lastName + ' ' + str(self.numpages) + ' pages')
        else:
            return str(self.title + ' by ' + self.author.firstName + ' ' + self.author.lastName + ' ' + str(self.numpages) + ' pages ' + 'NOT-IN-STOCK')

class Student(User):
    PROVINCE_CHOICES = (
        ('AB','Alberta'), # First value is stored in db, the second is descriptive
        ('MB', 'Manitoba'),
        ('ON', 'Ontario'),
        ('QC', 'Quebec'),
    )
    address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=20, default='Windsor')
    province=models.CharField(max_length=2, choices=PROVINCE_CHOICES, default='ON')
    age = models.IntegerField()
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Course(models.Model):
    course_no = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    textbook = models.ForeignKey(Book)
    students = models.ManyToManyField(Student, null=True, blank=True)
    def __str__(self):
        return str(str(self.course_no) + " '" + self.title + "' " + " uses " + str(self.textbook.title))

class Topic(models.Model):
    subject = models.CharField(max_length=100, unique=True)
    intro_course = models.BooleanField(default=True)
    NO_PREFERENCE = 0
    MORNING = 1
    AFTERNOON = 2
    EVENING = 3
    TIME_CHOICES = (
        (0, 'No preference'),
        (1, 'Morning'),
        (2, 'Afternoon'),
        (3, 'Evening')
    )
    time = models.IntegerField(default=0, choices=TIME_CHOICES)
    num_responses = models.IntegerField(default=0)
    avg_age =models.IntegerField(default=20)
    def __str__(self):
        return str('Subject: ' + self.subject)