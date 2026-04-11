from django.urls import path
from . import views

urlpatterns = [
    path( 'universitet/', views.UniversitetAPIView.as_view()),
    path( 'teacher/', views.TeacherAPIView.as_view()),
    path( 'student/', views.StudentAPIView.as_view()),
    path( 'group/', views.GroupAPIView.as_view()),

]
