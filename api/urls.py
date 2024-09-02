from django.urls import path
from .views import (
    ClassPeriodListView, 
    CourseListView, 
    StudentDetailView, 

    TeacherListView,
    CourseDetailView
)
from .views import StudentListView

urlpatterns = [
    path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),
    path('students/', StudentListView.as_view(), name='student_list_view'),
    path('classperiod/', ClassPeriodListView.as_view(), name='classperiod_list_view'),
    path('course/', CourseListView.as_view(), name='course_list_view'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail_view'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail_view'),
    path('courses/', CourseListView.as_view(), name='course_list_view'),
]