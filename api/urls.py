
from django.urls import path
from .views import StudentDetailView, CourseListView, TeacherListView, ClassesListView, ClassPeriodListView


urlpatterns = [

    path('students/<int:id>/', StudentDetailView.as_view(), name='student-detail'),
   
   path('courses/', CourseListView.as_view(), name='course_list_view'),
   path('teachers/', TeacherListView.as_view(), name='teacher_list_view'),
   path('classes/', ClassesListView.as_view(), name='classes_list_view'),
   path('periods/', ClassPeriodListView.as_view(), name='classroomPeriod_list_view'),
]


