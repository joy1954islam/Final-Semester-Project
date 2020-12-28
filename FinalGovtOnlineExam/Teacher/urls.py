from django.urls import path

from Teacher import views
from CourseMaterial import views as material_views
from UploadLecture import views as lecture_views

urlpatterns = [

    path('TeacherHome/', views.home, name='TeacherHome'),

    path('TeacherProfile/', views.TeacherProfile, name='TeacherProfile'),
    path('change/password/', views.ChangePasswordView.as_view(), name='Teacher_change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='Teacher_change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

    path('quiz/', views.QuizListView.as_view(), name='quiz_change_list'),
    path('quiz/add/', views.QuizCreateView.as_view(), name='quiz_add'),
    path('quiz/<int:pk>/', views.QuizUpdateView.as_view(), name='quiz_change'),
    path('quiz/<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz_delete'),
    path('quiz/<int:pk>/results/', views.QuizResultsView.as_view(), name='quiz_results'),
    path('quiz/<int:pk>/question/add/', views.question_add, name='question_add'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/', views.question_change, name='question_change'),
    path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', views.QuestionDeleteView.as_view(),
         name='question_delete'),
    path('mcq/quiz/<int:pk>/', views.mcq_question_list, name='mcq_question_views'),
    path('mcq/quiz/', views.MCQQuizListView.as_view(), name='mcq_list'),

    path('studentResult/',views.StudentAnswerShit,name='StudentAnswerShit'),


    path('material/', material_views.material_list, name='material_list'),
    path('material/create/', material_views.material_create, name='material_create'),
    path('<int:pk>/material/update/', material_views.material_update, name='material_update'),
    path('<int:pk>/material/delete/', material_views.material_delete, name='material_delete'),

    path('lecture/', lecture_views.lecture_list, name='lecture_list'),
    path('lecture/create/', lecture_views.lecture_create, name='lecture_create'),
    path('<int:pk>/lecture/update/', lecture_views.lecture_update, name='lecture_update'),
    path('<int:pk>/lecture/delete/', lecture_views.lecture_delete, name='lecture_delete'),


]
