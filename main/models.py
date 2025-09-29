from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)

    #object-wise function (오브젝트 대상의 함수?)
    def __str__(self):
        return f"{self.name} ({self.student_id})" #문자열 커스터마이징
    #최강타 (2023130)