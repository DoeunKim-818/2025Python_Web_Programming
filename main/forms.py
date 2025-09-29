from django import forms
from .models import Student #같은 폴더 안에 있는 models 파일을 불러오겠다는 뜻

class StudentForm(forms.ModelForm): #모델 폼 기능 상속
    class Meta: #모델 폼 기능은 Meta class 선언해서 사용
        model=Student
        fields = [
            'name',
            'department',
            'student_id'
        ]

