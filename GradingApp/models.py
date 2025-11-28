from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
    
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    subject = models.CharField(max_length=50)
    score = models.IntegerField()  

    def grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        else:
            return 'F'

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.score}"