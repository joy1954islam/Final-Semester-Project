
from django.urls import path

from Student import views

urlpatterns = [
    path('my_courses/', views.my_courses,name='my_course'),
    path('list/', views.QuizListView.as_view(), name='quiz_list'),
    path('interests/', views.StudentInterestsView.as_view(), name='student_interests'),
    path('taken/', views.TakenQuizListView.as_view(), name='taken_quiz_list'),
    path('quiz/<int:pk>/', views.take_quiz, name='take_quiz'),
    # path('Student/Enroll/', views.student_enroll, name='Student_Enroll'),


    path('StudentProfile/', views.profile, name='StudentProfile'),
    path('StudentProfileEdit/', views.StudentProfile, name='StudentProfileEdit'),
    path('change/password/', views.ChangePasswordView.as_view(), name='student_change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='student_change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

]
