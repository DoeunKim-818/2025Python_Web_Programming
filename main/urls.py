from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # ✅ 자기 자신을 include하지 않음
    path('add/', views.add, name='add'),
    path('student/', views.get_student)
]
